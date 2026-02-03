# Módulo de Autenticación y Control de Acceso - Especificaciones Técnicas

## 1. Arquitectura del Sistema de Autenticación

### 1.1 Componentes Principales

```
┌─────────────────────────────────────────────────────────────────┐
│                    APLICACIÓN WEB / FRONTEND                     │
├─────────────────────────────────────────────────────────────────┤
│  Login Form │ Dashboard │ Formularios │ Gestión de Permisos      │
└────────────────────────────┬──────────────────────────────────────┘
                             │
              ┌──────────────┴──────────────┐
              │    Validación en Cliente    │
              │   (Email format, etc)       │
              └──────────────┬──────────────┘
                             │
┌─────────────────────────────┴──────────────────────────────────────┐
│                        API REST / GraphQL                          │
├─────────────────────────────────────────────────────────────────────┤
│  POST /auth/login        │ GET /auth/validate       │ POST /auth/logout  │
│  POST /auth/refresh      │ GET /auth/permissions    │ POST /auth/2fa     │
└─────────────┬─────────────────────────────┬─────────────────────────┘
              │                             │
    ┌─────────┴──────────┐        ┌────────┴──────────┐
    │  Auth Service      │        │ Permission Service│
    │  - Hash validation │        │ - Nivel usuario   │
    │  - JWT generation  │        │ - Nivel área      │
    │  - Session mgmt    │        │ - Caching         │
    └─────────┬──────────┘        └────────┬──────────┘
              │                             │
┌─────────────┴─────────────────────────────┴──────────────────────┐
│                        DATABASE LAYER                            │
├────────────────────────────────────────────────────────────────┤
│  Usuarios │ Usuarios_Autorizados_Área │ Sistemas_Autorizados  │
│  Sesiones_Activas │ Cache_Permisos │ Audit_Login             │
└────────────────────────────────────────────────────────────────┘
```

---

## 2. Flujo Detallado de Login

### 2.1 POST /auth/login (Request/Response)

**Request (Body):**
```json
{
  "email": "usuario@institución.com",
  "password": "contraseña_hasheada_en_cliente_opcional",
  "remember_me": false,
  "captcha_token": "token_recaptcha_v3"
}
```

**Process:**
```
1. Validar formato de email
2. Verificar CAPTCHA (prevenir bots)
3. Buscar usuario en tabla Usuarios
   - Si no existe → Error 401 + Registrar intento fallido
   - Si existe → Continuar
4. Verificar contraseña con bcrypt.compare()
   - Si no coincide → Error 401 + Incrementar intentos_fallidos
   - Si coincide → Continuar
5. Validar estado del usuario
   - Si Suspendido → Error 403 + Notificar admin
   - Si Inactivo → Error 403
   - Si Activo → Continuar
6. Crear sesión:
   - Generar ID_Sesión (UUID)
   - Generar JWT Token
   - Registrar en Sesiones_Activas
   - Registrar en Audit_Login (exitoso)
7. Retornar tokens al cliente
```

**Response (Success - 200):**
```json
{
  "success": true,
  "token": {
    "access_token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...",
    "token_type": "Bearer",
    "expires_in": 3600,
    "refresh_token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9..."
  },
  "user": {
    "id": 42,
    "email": "usuario@institución.com",
    "nombre": "Juan Pérez",
    "areas": [
      { "id": 1, "nombre": "RRHH" },
      { "id": 3, "nombre": "Finanzas" }
    ],
    "permisos_globales": {
      "puede_crear_sistemas": true,
      "puede_modificar_sistemas": true
    }
  },
  "requiere_2fa": false
}
```

**Response (Error - 401):**
```json
{
  "success": false,
  "error": "Credenciales inválidas",
  "error_code": "INVALID_CREDENTIALS",
  "intentos_restantes": 4,
  "mensaje_usuario": "Email o contraseña incorrectos. Le quedan 4 intentos"
}
```

---

### 2.2 POST /auth/validate (Validar Token Activo)

**Request (Header):**
```
Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...
```

**Response (Success - 200):**
```json
{
  "valid": true,
  "user_id": 42,
  "email": "usuario@institución.com",
  "sesión_id": "uuid-12345-67890",
  "expira_en": 1800,
  "permisos_cache": {
    "timestamp": "2026-02-03T10:30:00Z",
    "puede_solicitar_nuevo": true,
    "puede_solicitar_modificación": true,
    "sistemas_visibles": 12
  }
}
```

**Response (Error - 401):**
```json
{
  "valid": false,
  "error": "Token expirado o inválido",
  "error_code": "INVALID_TOKEN",
  "acción_recomendada": "refresh_token"
}
```

---

## 3. Validación de Permisos (Middleware)

### 3.1 Middleware de Autenticación

```python
# Pseudocódigo - Python/Flask

@app.before_request
def validar_autenticación():
    """Middleware que valida el token JWT en cada request"""
    
    # Obtener token del header Authorization
    token = request.headers.get('Authorization', '').replace('Bearer ', '')
    
    if not token:
        return {'error': 'Token requerido'}, 401
    
    try:
        # Decodificar JWT
        payload = jwt.decode(token, SECRET_KEY, algorithms=['HS256'])
        user_id = payload['user_id']
        
        # Validar sesión activa en BD
        sesión = db.query(Sesiones_Activas).filter(
            Sesiones_Activas.ID_Usuario == user_id,
            Sesiones_Activas.Estado == 'Activa',
            Sesiones_Activas.Expiración > datetime.now()
        ).first()
        
        if not sesión:
            return {'error': 'Sesión expirada'}, 401
        
        # Cargar usuario y permisos en contexto
        g.usuario = db.query(Usuarios).get(user_id)
        g.usuario_id = user_id
        g.sesión_id = sesión.ID_Sesión
        
        # Actualizar última actividad
        sesión.Última_Actividad = datetime.now()
        db.commit()
        
    except jwt.ExpiredSignatureError:
        return {'error': 'Token expirado'}, 401
    except jwt.InvalidTokenError:
        return {'error': 'Token inválido'}, 401
```

---

### 3.2 Middleware de Validación de Permisos

```python
def validar_permiso_crear_sistema():
    """Decorador para validar que usuario puede crear sistemas"""
    def decorator(f):
        @wraps(f)
        def decorated_function(*args, **kwargs):
            user_id = g.usuario_id
            
            # Usar cache si es válido
            cache = db.query(Cache_Permisos_Usuario).filter(
                Cache_Permisos_Usuario.ID_Usuario == user_id,
                Cache_Permisos_Usuario.Válido_Hasta > datetime.now()
            ).first()
            
            if cache and cache.Permisos_JSON.get('puede_solicitar_nuevo'):
                return f(*args, **kwargs)
            
            # Si cache no válido, consultar BD
            permisos = db.execute("""
                SELECT MAX(ua.Puede_Solicitar_Nuevo) as puede_nuevo,
                       MAX(a.Puede_Crear_Sistemas_Nuevos) as area_permite
                FROM Usuarios_Autorizados_Área ua
                JOIN Áreas a ON ua.ID_Área = a.ID_Área
                WHERE ua.ID_Usuario = ? AND ua.Activo = 1
            """, [user_id]).fetchone()
            
            if not (permisos and permisos['puede_nuevo'] and permisos['area_permite']):
                # Registrar intento no autorizado
                db.insert_into('Audit_Acceso_No_Autorizado').values(
                    ID_Usuario=user_id,
                    Tipo_Intento='CREAR_SISTEMA',
                    Motivo_Denegación='Usuario no autorizado para crear sistemas',
                    Acción_Tomada='ACCESO_DENEGADO'
                ).execute()
                return {'error': 'No autorizado'}, 403
            
            # Invalidar y reconstruir cache si fue usado anterior
            if cache:
                cache.Válido_Hasta = datetime.now()
                db.commit()
            
            return f(*args, **kwargs)
        return decorated_function
    return decorator

# Uso:
@app.route('/api/solicitudes/crear-sistema', methods=['POST'])
@validar_permiso_crear_sistema()
def crear_sistema():
    # Lógica de creación...
    pass
```

---

## 4. Endpoints de API

### 4.1 Gestión de Autenticación

| Método | Endpoint | Descripción | Requiere Auth |
|--------|----------|-------------|---------------|
| POST | `/auth/login` | Login con email/password | No |
| POST | `/auth/login/2fa` | Validar código 2FA | No (después de primer login) |
| POST | `/auth/refresh` | Renovar access token | Sí (usa refresh token) |
| POST | `/auth/logout` | Cerrar sesión | Sí |
| GET | `/auth/validate` | Validar token actual | Sí |
| POST | `/auth/change-password` | Cambiar contraseña | Sí |
| POST | `/auth/forgot-password` | Recuperar contraseña | No |
| GET | `/auth/sessions` | Listar sesiones activas | Sí |
| DELETE | `/auth/sessions/{id}` | Cerrar sesión específica | Sí |

---

### 4.2 Gestión de Permisos

| Método | Endpoint | Descripción | Requiere Auth |
|--------|----------|-------------|---------------|
| GET | `/api/permisos/mios` | Obtener mis permisos | Sí |
| GET | `/api/sistemas` | Listar sistemas visibles | Sí |
| GET | `/api/areas` | Listar mis áreas | Sí |
| GET | `/api/solicitudes` | Mis solicitudes | Sí |
| POST | `/api/solicitudes` | Crear solicitud nueva | Sí (con validación) |

---

### 4.3 Gestión Administrativa (ISSEG)

| Método | Endpoint | Descripción | Requiere Auth |
|--------|----------|-------------|---------------|
| GET | `/admin/usuarios` | Listar todos usuarios | Sí (ISSEG) |
| POST | `/admin/usuarios` | Crear usuario | Sí (ISSEG) |
| PUT | `/admin/usuarios/{id}` | Editar usuario | Sí (ISSEG) |
| DELETE | `/admin/usuarios/{id}` | Inactivar usuario | Sí (ISSEG) |
| POST | `/admin/usuarios/{id}/permisos` | Asignar permisos | Sí (ISSEG) |
| GET | `/admin/audit/login` | Historial de logins | Sí (ISSEG) |
| GET | `/admin/audit/acceso-denegado` | Intentos de acceso no autorizado | Sí (ISSEG) |

---

## 5. Seguridad en Detalle

### 5.1 Hash de Contraseñas (Backend)

```python
from argon2 import PasswordHasher
from argon2.exceptions import VerifyMismatchError

ph = PasswordHasher()

# Al crear usuario
hashed_password = ph.hash(password_input)
usuario.Contraseña_Hash = hashed_password
db.save()

# Al validar login
try:
    ph.verify(usuario.Contraseña_Hash, password_input)
    # Contraseña correcta
except VerifyMismatchError:
    # Contraseña incorrecta
    incrementar_intentos_fallidos()
```

---

### 5.2 JWT Token Structure

```python
import jwt
from datetime import datetime, timedelta

payload = {
    'user_id': 42,
    'email': 'usuario@institución.com',
    'area_primaria': 1,
    'roles': ['solicitante', 'revisor'],
    'iat': datetime.utcnow(),
    'exp': datetime.utcnow() + timedelta(hours=1),
    'session_id': 'uuid-sesión'
}

access_token = jwt.encode(payload, SECRET_KEY, algorithm='HS256')
```

---

### 5.3 Rate Limiting

```python
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address

limiter = Limiter(
    app=app,
    key_func=get_remote_address,
    default_limits=["200 per day", "50 per hour"]
)

@app.route('/auth/login', methods=['POST'])
@limiter.limit("5 per minute")  # 5 intentos por minuto
def login():
    """Máximo 5 intentos de login por minuto por IP"""
    # Lógica de login...
    pass

@app.route('/auth/login', methods=['POST'])
@limiter.limit("10 per hour")  # Límite global adicional
def login():
    """Máximo 10 intentos de login por hora por usuario"""
    # Lógica de login...
    pass
```

---

### 5.4 Protección CSRF

```html
<!-- En formularios HTML -->
<form method="POST" action="/auth/login">
    <input type="hidden" name="csrf_token" value="{{ csrf_token() }}"/>
    <input type="email" name="email" required/>
    <input type="password" name="password" required/>
    <button type="submit">Login</button>
</form>

<!-- En API requests (headers) -->
X-CSRFToken: token_valor_aquí
```

---

### 5.5 Validación de CAPTCHA

```python
from requests import post as requests_post

def validar_captcha(captcha_token):
    """Validar token de reCAPTCHA v3 con Google"""
    response = requests_post(
        'https://www.google.com/recaptcha/api/siteverify',
        data={
            'secret': RECAPTCHA_SECRET_KEY,
            'response': captcha_token
        }
    )
    
    data = response.json()
    
    # Verificar score (0.0 a 1.0)
    if data.get('score', 0) < 0.5:  # Si parece bot
        return False
    
    return data.get('success', False)
```

---

## 6. Ejemplo de Implementación Frontend (JavaScript/React)

### 6.1 Componente Login

```jsx
import React, { useState } from 'react';
import ReCAPTCHA from "react-google-recaptcha";

function LoginForm() {
    const [email, setEmail] = useState('');
    const [password, setPassword] = useState('');
    const [captchaToken, setCaptchaToken] = useState(null);
    const [error, setError] = useState('');
    const [loading, setLoading] = useState(false);

    const handleSubmit = async (e) => {
        e.preventDefault();
        setLoading(true);
        setError('');

        try {
            const response = await fetch('/auth/login', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                    'X-Requested-With': 'XMLHttpRequest'
                },
                credentials: 'include', // Incluir cookies
                body: JSON.stringify({
                    email,
                    password: hashPassword(password), // Hash en cliente opcional
                    captcha_token: captchaToken
                })
            });

            const data = await response.json();

            if (!response.ok) {
                setError(data.mensaje_usuario || 'Error en login');
                return;
            }

            if (data.requiere_2fa) {
                // Mostrar pantalla de 2FA
                localStorage.setItem('temp_token', data.temp_token);
                window.location.href = '/auth/2fa';
            } else {
                // Guardar tokens
                localStorage.setItem('access_token', data.token.access_token);
                localStorage.setItem('refresh_token', data.token.refresh_token);
                
                // Redirigir al dashboard
                window.location.href = '/dashboard';
            }
        } catch (err) {
            setError('Error de conexión: ' + err.message);
        } finally {
            setLoading(false);
        }
    };

    return (
        <form onSubmit={handleSubmit} className="login-form">
            <h1>Sistema de Gestión de Tickets</h1>
            
            {error && <div className="error-message">{error}</div>}
            
            <input
                type="email"
                placeholder="Email institucional"
                value={email}
                onChange={(e) => setEmail(e.target.value)}
                required
            />
            
            <input
                type="password"
                placeholder="Contraseña"
                value={password}
                onChange={(e) => setPassword(e.target.value)}
                required
            />
            
            <ReCAPTCHA
                sitekey="YOUR_RECAPTCHA_SITE_KEY"
                onChange={setCaptchaToken}
            />
            
            <button type="submit" disabled={loading || !captchaToken}>
                {loading ? 'Iniciando sesión...' : 'Ingresar'}
            </button>
            
            <a href="/auth/forgot-password">¿Olvidó su contraseña?</a>
        </form>
    );
}

export default LoginForm;
```

---

### 6.2 Axios Interceptor para Refresh Token

```javascript
import axios from 'axios';

const axiosInstance = axios.create({
    baseURL: process.env.REACT_APP_API_URL
});

// Interceptor de request
axiosInstance.interceptors.request.use(
    config => {
        const token = localStorage.getItem('access_token');
        if (token) {
            config.headers.Authorization = `Bearer ${token}`;
        }
        return config;
    },
    error => Promise.reject(error)
);

// Interceptor de response
axiosInstance.interceptors.response.use(
    response => response,
    async error => {
        const originalRequest = error.config;

        // Si el error es 401 y no es un retry
        if (error.response.status === 401 && !originalRequest._retry) {
            originalRequest._retry = true;

            try {
                const refreshToken = localStorage.getItem('refresh_token');
                const response = await axios.post('/auth/refresh', {
                    refresh_token: refreshToken
                });

                const { access_token } = response.data.token;
                localStorage.setItem('access_token', access_token);

                // Reintentar request original
                originalRequest.headers.Authorization = `Bearer ${access_token}`;
                return axiosInstance(originalRequest);
            } catch (refreshError) {
                // Refresh fallido, redirigir a login
                localStorage.clear();
                window.location.href = '/login';
                return Promise.reject(refreshError);
            }
        }

        return Promise.reject(error);
    }
);

export default axiosInstance;
```

---

## 7. Testing

### 7.1 Test de Login Exitoso

```python
# Usando pytest
def test_login_exitoso(client, db):
    """Test: Usuario válido inicia sesión correctamente"""
    
    # Arrange
    usuario = Usuario(
        Email='usuario@test.com',
        Nombre_Completo='Juan Test',
        Contraseña_Hash=hash_password('Password123'),
        Estado='Activo'
    )
    db.add(usuario)
    db.commit()
    
    # Act
    response = client.post('/auth/login', json={
        'email': 'usuario@test.com',
        'password': 'Password123',
        'captcha_token': 'test_token'
    })
    
    # Assert
    assert response.status_code == 200
    data = response.get_json()
    assert data['success'] == True
    assert 'access_token' in data['token']
    assert 'refresh_token' in data['token']
    assert data['user']['email'] == 'usuario@test.com'
```

---

### 7.2 Test de Credenciales Inválidas

```python
def test_login_credenciales_invalidas(client):
    """Test: Credenciales inválidas rechazadas"""
    
    response = client.post('/auth/login', json={
        'email': 'usuario@test.com',
        'password': 'PasswordIncorrecto',
        'captcha_token': 'test_token'
    })
    
    assert response.status_code == 401
    data = response.get_json()
    assert data['success'] == False
    assert 'Credenciales inválidas' in data['error']
```

---

### 7.3 Test de Permiso No Autorizado

```python
def test_crear_sistema_sin_permiso(client, usuario_sin_permiso, auth_token):
    """Test: Usuario sin permiso no puede crear sistema"""
    
    response = client.post(
        '/api/solicitudes/crear-sistema',
        json={'nombre': 'Nuevo Sistema', 'descripcion': 'Test'},
        headers={'Authorization': f'Bearer {auth_token}'}
    )
    
    assert response.status_code == 403
    data = response.get_json()
    assert 'No autorizado' in data['error']
```

---

## 8. Monitoreo y Alertas

### 8.1 Métricas a Monitorear

```
- Intentos de login fallidos por IP
- Intentos de acceso denegado por usuario
- Sesiones activas por usuario
- Tiempo promedio de login
- Tokens expirados vs refresh exitosos
- Usuarios sin autorización que intentan acceder
- Cambios en permisos (quién cambió qué)
```

### 8.2 Alertas Recomendadas

```
CRÍTICA:
- 10+ intentos fallidos por IP en 5 minutos → Bloquear IP temporalmente
- Usuario inactivo 2+ años → Deshabilitar cuenta
- Cambio de rol sin auditoría → Notificar admin

ALTA:
- Usuario sin área asignada intenta crear solicitud
- 5+ intentos de acceso denegado en 15 min
- Token invalidado antes de expiración

MEDIA:
- Sesión inactiva > 30 min (cerrar automáticamente)
- Usuario intenta acceder a sistema no autorizado
```

---

## 9. Checklist de Implementación

```
□ Tabla Usuarios con validación de email único
□ Tabla Usuarios_Autorizados_Área con índices
□ Tabla Sistemas_Autorizados_Por_Área
□ Tabla Sesiones_Activas
□ Tabla Cache_Permisos_Usuario
□ Tabla Audit_Login
□ Tabla Audit_Acceso_No_Autorizado
□ Tabla Audit_Cambios_Permisos
□ Procedimientos almacenados de permisos
□ Vistas de consulta de permisos
□ Endpoint POST /auth/login con validación
□ Endpoint GET /auth/validate
□ Endpoint POST /auth/refresh
□ Endpoint POST /auth/logout
□ Endpoint GET /api/permisos/mios
□ Endpoint GET /api/sistemas (filtrado)
□ Middleware de validación de token
□ Middleware de validación de permisos
□ Hash de contraseñas con Argon2
□ JWT con expiración y refresh
□ Rate limiting en endpoints de login
□ CAPTCHA en formulario de login
□ CSRF protection
□ 2FA con TOTP (opcional)
□ Tests unitarios
□ Tests de integración
□ Monitoreo y alertas
□ Documentación de API
□ Capacitación a administradores
```
