# Diagramas Adicionales - Control de Acceso y Validaciones

## 1. Diagrama Detallado de Validación Multi-Nivel

```mermaid
graph TD
    subgraph Step1["PASO 1: Validar Usuario Existe"]
        A[Usuario intenta login] --> B{¿Email existe<br/>en USUARIOS?}
        B -->|No| C1["❌ ACCESO DENEGADO<br/>Usuario no existe"]
        B -->|Sí| D{¿Estado = Activo?}
        D -->|No| C2["❌ ACCESO DENEGADO<br/>Cuenta inactiva/suspendida"]
    end
    
    subgraph Step2["PASO 2: Validar Credenciales"]
        D -->|Sí| E{¿Contraseña<br/>es válida?}
        E -->|No| C3["❌ ACCESO DENEGADO<br/>Contraseña incorrecta<br/>+1 intento fallido"]
        E -->|Sí| F{¿Intentos fallidos<br/>> 5?}
        F -->|Sí| C4["❌ CUENTA BLOQUEADA<br/>Demasiados intentos"]
        F -->|No| G["✅ Credenciales OK<br/>Crear sesión"]
    end
    
    subgraph Step3["PASO 3: Cargar Áreas"]
        G --> H[Buscar en<br/>USUARIOS_AUTORIZADOS_ÁREA]
        H --> I{¿Existen áreas<br/>autorizadas?}
        I -->|No| C5["⚠️ ACCESO LIMITADO<br/>Sin áreas asignadas<br/>Modo consulta"]
        I -->|Sí| J["Cargar:<br/>- Áreas autorizadas<br/>- Roles en cada área<br/>- Permisos"]
    end
    
    subgraph Step4["PASO 4: Validar Permisos Globales"]
        J --> K{¿Area permite<br/>crear sistemas<br/>nuevos?}
        K -->|No| L1["Crear sistema: NO"]
        K -->|Sí| L2["Crear sistema: SÍ"]
        
        J --> M{¿Area permite<br/>solicitar<br/>modificaciones?}
        M -->|No| N1["Modificar: NO"]
        M -->|Sí| N2["Modificar: SÍ"]
    end
    
    subgraph Step5["PASO 5: Cargar Sistemas Autorizados"]
        L2 --> O[Consultar<br/>SISTEMAS_AUTORIZADOS_POR_ÁREA]
        O --> P["Filtrar:<br/>- Estado = Producción<br/>- Activo = 1<br/>- Autorizado para área"]
        P --> Q["Cachear permisos<br/>TTL 30 minutos"]
    end
    
    subgraph Result["RESULTADO FINAL"]
        Q --> R["✅ LOGIN EXITOSO<br/>Token JWT + Refresh Token<br/>Permisos cacheados"]
        C1 --> S["❌ ACCESO DENEGADO"]
        C2 --> S
        C3 --> S
        C4 --> S
        C5 --> T["⚠️ CONSULTA LIMITADA"]
        L1 --> U["Permiso Creación: NO"]
        L2 --> V["Permiso Creación: SÍ"]
        N1 --> W["Permiso Modificación: NO"]
        N2 --> X["Permiso Modificación: SÍ"]
    end
    
    style A fill:#e3f2fd
    style B fill:#fff9c4
    style D fill:#fff9c4
    style E fill:#fff9c4
    style F fill:#fff9c4
    style I fill:#fff9c4
    style K fill:#fff9c4
    style M fill:#fff9c4
    style C1 fill:#ffcdd2
    style C2 fill:#ffcdd2
    style C3 fill:#ffcdd2
    style C4 fill:#ffcdd2
    style C5 fill:#ffe0b2
    style R fill:#c8e6c9
    style S fill:#ffcdd2
    style T fill:#ffe0b2
```

---

## 2. Diagrama: Matriz de Permisos por Rol

```mermaid
graph LR
    subgraph Usuarios["👤 USUARIOS"]
        U1["Usuario Regular<br/>(No en Áreas)"]
        U2["Solicitante<br/>(En Área)"]
        U3["Responsable de Área"]
        U4["Revisor ISSEG"]
        U5["Admin Sistema"]
    end
    
    subgraph Permisos["📋 PERMISOS"]
        P1["Ver Solicitudes Propias"]
        P2["Crear Sistema Nuevo"]
        P3["Solicitar Modificación"]
        P4["Ver Sistemas de Su Área"]
        P5["Revisar Solicitudes"]
        P6["Aprobar/Rechazar"]
        P7["Asignar Desarrolladores"]
        P8["Gestionar Usuarios"]
        P9["Ver Auditoría"]
        P10["Cambiar Permisos"]
    end
    
    U1 --> P1
    
    U2 --> P1
    U2 --> P3
    U2 --> P4
    
    U3 --> P1
    U3 --> P2
    U3 --> P3
    U3 --> P4
    
    U4 --> P1
    U4 --> P5
    U4 --> P6
    U4 --> P7
    U4 --> P9
    
    U5 --> P1
    U5 --> P5
    U5 --> P6
    U5 --> P7
    U5 --> P8
    U5 --> P9
    U5 --> P10
    
    style U1 fill:#e0e0e0
    style U2 fill:#c8e6c9
    style U3 fill:#bbdefb
    style U4 fill:#fff9c4
    style U5 fill:#ffccbc
    style Permisos fill:#f5f5f5
```

---

## 3. Diagrama: Flujo de Validación de Solicitud

```mermaid
flowchart TD
    Start([Usuario Selecciona<br/>Crear Sistema Nuevo]) --> Step1{Frontend:<br/>¿Token válido?}
    
    Step1 -->|No| Redirect["Redirigir a Login"]
    Redirect --> End1(["Fin"])
    
    Step1 -->|Sí| Step2{Frontend:<br/>¿Datos completados?}
    Step2 -->|No| Error1["Mostrar errores de validación"]
    Error1 --> Start
    
    Step2 -->|Sí| Step3["Enviar request<br/>POST /api/solicitudes/crear-sistema<br/>Headers: Authorization: Bearer token"]
    
    Step3 --> Step4["Middleware 1:<br/>Validar JWT"]
    Step4 -->|Inválido| Error2["401 Unauthorized"]
    Error2 --> End2(["Fin"])
    
    Step4 -->|Válido| Step5["Middleware 2:<br/>Cargar usuario<br/>g.usuario_id = payload.user_id"]
    
    Step5 --> Step6["Middleware 3:<br/>Validar permiso<br/>Crear Sistema"]
    Step6 -->|Sin permiso| Query1["Buscar en BD:<br/>USUARIOS_AUTORIZADOS_ÁREA"]
    Query1 --> Check1{¿Puede_Solicitar<br/>Nuevo?}
    Check1 -->|No| Audit1["Registrar intento<br/>no autorizado"]
    Audit1 --> Error3["403 Forbidden<br/>No autorizado"]
    Error3 --> End3(["Fin"])
    
    Check1 -->|Sí| Step7["Validar datos<br/>del formulario"]
    Step7 --> Valid{¿Formulario<br/>válido?}
    
    Valid -->|No| Error4["Retornar errores<br/>por campo"]
    Error4 --> End4(["Fin"])
    
    Valid -->|Sí| Step8["Crear registro<br/>en tabla SOLICITUDES"]
    Step8 --> Step9["Estado: PENDIENTE_REVISIÓN"]
    Step9 --> Step10["Registrar en<br/>AUDIT_CAMBIOS"]
    Step10 --> Step11["Enviar email a ISSEG<br/>Nueva solicitud pendiente"]
    Step11 --> Response["200 OK<br/>Retornar ID_Solicitud<br/>+ Confirmación"]
    Response --> End5(["Fin - Solicitud Creada"])
    
    style Start fill:#e3f2fd,stroke:#1976d2,stroke-width:2px
    style Step1 fill:#fff9c4,stroke:#f57f17,stroke-width:2px
    style Step2 fill:#fff9c4,stroke:#f57f17,stroke-width:2px
    style Step6 fill:#fff9c4,stroke:#f57f17,stroke-width:2px
    style Check1 fill:#fff9c4,stroke:#f57f17,stroke-width:2px
    style Valid fill:#fff9c4,stroke:#f57f17,stroke-width:2px
    style Error2 fill:#ffcdd2,stroke:#d32f2f,stroke-width:2px
    style Error3 fill:#ffcdd2,stroke:#d32f2f,stroke-width:2px
    style Error4 fill:#ffcdd2,stroke:#d32f2f,stroke-width:2px
    style Response fill:#c8e6c9,stroke:#388e3c,stroke-width:2px
    style End5 fill:#a5d6a7,stroke:#2e7d32,stroke-width:2px
```

---

## 4. Diagrama: Estados Posibles de un Usuario

```mermaid
stateDiagram-v2
    [*] --> Creado: Nuevo usuario creado
    
    Creado --> SinAutorización: No asignado a área
    
    SinAutorización --> Activo: Asignado a área
    SinAutorización --> Suspendido: Múltiples intentos fallidos
    
    Activo --> Inactivo: Desasignado de todas áreas
    Activo --> Suspendido: Violación de seguridad
    Activo --> Buscando_2FA: Login con 2FA habilitado
    
    Inactivo --> Activo: Re-asignado a área
    Inactivo --> Eliminado: Solicitud de eliminación
    
    Suspendido --> Activo: Admin levanta suspensión
    Suspendido --> Eliminado: Tras investigación
    
    Buscando_2FA --> Activo: 2FA válido
    Buscando_2FA --> Suspendido: Código 2FA inválido 3+ veces
    
    Eliminado --> [*]
    
    note right of Creado
        Usuario creado pero sin
        área asignada
        Puede solo consultar
    end note
    
    note right of SinAutorización
        Puede ver dashboard
        pero sin acciones
    end note
    
    note right of Activo
        Acceso completo según
        permisos del área
    end note
    
    note right of Suspendido
        Acceso bloqueado
        Requiere intervención
        de admin
    end note
    
    note right of Buscando_2FA
        Esperando validación
        de segundo factor
    end note
```

---

## 5. Diagrama: Ciclo de Vida de Permisos

```mermaid
graph LR
    subgraph Asignación["ASIGNACIÓN"]
        A1["Admin selecciona<br/>usuario + área"]
        A2["Define rol<br/>Solicitante"]
        A3["Asigna permisos:<br/>Nuevo: SÍ<br/>Modificación: NO"]
        A4["Registrar en<br/>AUDIT_CAMBIOS"]
        A1 --> A2 --> A3 --> A4
    end
    
    subgraph Validación["VALIDACIÓN EN TIEMPO REAL"]
        V1["Usuario intenta<br/>crear sistema"]
        V2["Buscar en BD<br/>Usuarios_Autorizados_Área"]
        V3{¿Permiso<br/>coincide?}
        V4["✓ Permitir"]
        V5["✗ Bloquear"]
        V1 --> V2 --> V3
        V3 -->|Sí| V4
        V3 -->|No| V5
    end
    
    subgraph Cache["OPTIMIZACIÓN CON CACHE"]
        C1["Cargar en<br/>Cache_Permisos"]
        C2["TTL 30 minutos"]
        C3["Próximas validaciones<br/>desde cache"]
        C4["Si falla cache,<br/>consultar BD"]
        C1 --> C2 --> C3
        C3 -.-> C4
    end
    
    subgraph Cambio["CAMBIO DE PERMISOS"]
        CH1["Admin modifica<br/>permiso"]
        CH2["Actualizar BD"]
        CH3["Invalidar cache<br/>inmediatamente"]
        CH4["Próximo login<br/>tendrá nuevos permisos"]
        CH1 --> CH2 --> CH3 --> CH4
    end
    
    subgraph Revocación["REVOCACIÓN"]
        R1["Admin desasigna<br/>usuario de área"]
        R2["Marcar como<br/>Activo = FALSE"]
        R3["Invalidar sesiones<br/>activas"]
        R4["Registrar en<br/>AUDIT_CAMBIOS"]
        R5["Notificar usuario"]
        R1 --> R2 --> R3 --> R4 --> R5
    end
    
    A4 --> V1
    V4 --> C1
    V5 --> C4
    CH1 --> V1
    R1 --> V1
    
    style Asignación fill:#c8e6c9
    style Validación fill:#bbdefb
    style Cache fill:#ffe0b2
    style Cambio fill:#f8bbd0
    style Revocación fill:#ffcdd2
```

---

## 6. Diagrama: Flujo de Seguridad en Login

```mermaid
sequenceDiagram
    actor Usuario
    participant Browser as 🌐 Browser
    participant Frontend as ⚛️ Frontend
    participant API as 🔗 API
    participant DB as 🗄️ Base Datos
    participant Cache as ⚡ Cache Redis
    participant Email as 📧 Email
    participant Audit as 📝 Audit Log
    
    Usuario->>Browser: Abre sistema
    Browser->>Frontend: Muestra formulario login
    
    Usuario->>Frontend: Escribe email/password
    Frontend->>Frontend: Validar formato email
    Frontend->>Frontend: Validar longitud password
    Frontend->>Frontend: Generar CAPTCHA token
    
    Frontend->>API: POST /auth/login<br/>(email, password_hash, captcha)
    
    API->>API: Validar CAPTCHA con Google
    alt CAPTCHA inválido
        API->>API: Registrar intento sospechoso
        API->>Audit: Log: CAPTCHA_FAILED
        API-->>Frontend: 400 Bad Request
    end
    
    API->>DB: Buscar usuario por email
    alt Usuario no existe
        API->>Audit: Log: USER_NOT_FOUND
        API-->>Frontend: 401 Unauthorized
    end
    
    DB-->>API: Retorna usuario (ID, password_hash)
    
    API->>API: Verificar contraseña<br/>(argon2.verify)
    alt Contraseña incorrecta
        API->>DB: UPDATE intentos_fallidos++
        alt intentos_fallidos >= 5
            API->>DB: UPDATE estado = BLOQUEADO
            API->>Email: Enviar alerta bloqueo
            API->>Audit: Log: ACCOUNT_LOCKED
        else
            API->>Audit: Log: LOGIN_FAILED
        end
        API-->>Frontend: 401 Unauthorized
    end
    
    API->>DB: Verificar estado usuario
    alt Estado != ACTIVO
        API->>Audit: Log: ACCOUNT_INACTIVE
        API-->>Frontend: 403 Forbidden
    end
    
    API->>DB: Buscar áreas autorizadas<br/>(USUARIOS_AUTORIZADOS_ÁREA)
    DB-->>API: Retorna áreas con permisos
    
    API->>API: Crear JWT Token<br/>(user_id, email, áreas, exp=1h)
    API->>API: Crear Refresh Token<br/>(user_id, exp=7d)
    
    API->>DB: Registrar sesión<br/>(SESIONES_ACTIVAS)
    API->>Cache: Cachear permisos<br/>(TTL=30min)
    
    API->>Audit: Log: LOGIN_SUCCESS
    API->>Email: Enviar confirmación login
    
    API-->>Frontend: 200 OK<br/>(access_token, refresh_token)
    
    Frontend->>Frontend: Guardar tokens en localStorage
    Frontend->>Frontend: Guardar usuario en contexto
    Frontend->>Browser: Redirigir a /dashboard
    Browser->>Frontend: Cargar dashboard
    
    note over API, Audit
        Toda transacción registrada en Audit
        para trazabilidad completa
    end
```

---

## 7. Diagrama: Intento de Acceso No Autorizado

```mermaid
graph TD
    Start([Usuario Intenta<br/>Crear Sistema Nuevo]) --> Check1{¿Token válido?}
    Check1 -->|No| Reject1["❌ Rechazar<br/>401 Unauthorized"]
    Check1 -->|Sí| Check2{¿Usuario existe<br/>en sesión?}
    Check2 -->|No| Reject2["❌ Rechazar<br/>Token expirado"]
    Check2 -->|Sí| Check3{¿Usuario en<br/>USUARIOS_AUTORIZADOS_ÁREA?}
    Check3 -->|No| Audit1["Registrar acceso denegado"]
    Audit1 --> Email1["Notificar a admin"]
    Email1 --> Reject3["❌ Rechazar 403"]
    Check3 -->|Sí| Check4{¿Permiso<br/>Puede_Solicitar_Nuevo<br/>= TRUE?}
    Check4 -->|No| Audit2["Registrar acceso denegado"]
    Audit2 --> Check5{¿Múltiples intentos<br/>en 30 min?}
    Check5 -->|Sí| Alert["⚠️ Alerta CRÍTICA<br/>Posible ataque"]
    Alert --> Block["Bloquear usuario<br/>temporalmente"]
    Block --> Email2["Email + SMS a Admin"]
    Check5 -->|No| Email3["Email a Admin"]
    Email3 --> Reject4["❌ Rechazar 403"]
    Check4 -->|Sí| Approve["✅ Permitir<br/>Cargar formulario"]
    
    style Start fill:#e3f2fd
    style Reject1 fill:#ffcdd2
    style Reject2 fill:#ffcdd2
    style Reject3 fill:#ffcdd2
    style Reject4 fill:#ffcdd2
    style Audit1 fill:#fff9c4
    style Audit2 fill:#fff9c4
    style Alert fill:#ff7043
    style Block fill:#d32f2f
    style Approve fill:#c8e6c9
```

---

## 8. Tabla: Matriz de Decisiones de Filtrado

```mermaid
graph LR
    subgraph Datos["DATOS DEL USUARIO"]
        U["Usuario: Juan Pérez<br/>Área: RRHH (ID=1)<br/>Permiso: Modificación=SÍ"]
    end
    
    subgraph Sistemas["SISTEMAS EN BD"]
        S1["SIS-001: Portal RRHH<br/>Área: RRHH<br/>Estado: Producción<br/>Activo: SÍ"]
        S2["SIS-002: ERP Finanzas<br/>Área: Finanzas<br/>Estado: Producción<br/>Activo: SÍ"]
        S3["SIS-003: Nómina<br/>Área: RRHH<br/>Estado: Descontinuado<br/>Activo: NO"]
        S4["SIS-004: Facturación<br/>Área: Ventas<br/>Estado: Desarrollo<br/>Activo: SÍ"]
    end
    
    subgraph Validación["VALIDACIÓN"]
        Q1["¿Estado = Producción?"]
        Q2["¿Activo = SÍ?"]
        Q3["¿Área = del usuario?"]
        Q4["✓ Mostrar"]
        Q5["✗ Ocultar"]
    end
    
    U --> Q1
    
    S1 --> Q1
    Q1 -->|SÍ| Q2
    Q2 -->|SÍ| Q3
    Q3 -->|SÍ| Q4
    Q4 --> R1["📊 Portal RRHH<br/>VISIBLE"]
    
    S2 --> Q1
    Q1 -->|SÍ| Q3_2["¿Área RRHH?"]
    Q3_2 -->|No| Q5
    Q5 --> R2["Portal Finanzas<br/>OCULTO"]
    
    S3 --> Q1_3["¿Producción?"]
    Q1_3 -->|No| Q5
    Q5 --> R3["Nómina<br/>OCULTO<br/>Descontinuado"]
    
    S4 --> Q1_4["¿Producción?"]
    Q1_4 -->|No| Q5
    Q5 --> R4["Facturación<br/>OCULTO<br/>En desarrollo"]
    
    style U fill:#c8e6c9
    style S1 fill:#e3f2fd
    style S2 fill:#e3f2fd
    style S3 fill:#fff9c4
    style S4 fill:#fff9c4
    style Q1 fill:#fff9c4
    style Q2 fill:#fff9c4
    style Q3 fill:#fff9c4
    style Q4 fill:#c8e6c9
    style Q5 fill:#ffcdd2
    style R1 fill:#a5d6a7
    style R2 fill:#ffcdd2
    style R3 fill:#ffcdd2
    style R4 fill:#ffcdd2
```

---

## 9. Diagrama: Recuperación ante Fallos de Seguridad

```mermaid
graph TD
    Alert["🚨 ALERTA DE SEGURIDAD"] --> Type{¿Tipo de<br/>incidente?}
    
    Type -->|1. Múltiples logins fallidos| Case1["Usuario: X<br/>5+ intentos en 5 min"]
    Case1 --> Action1A["Bloquear temporalmente<br/>por 30 minutos"]
    Action1A --> Action1B["Enviar email a usuario"]
    Action1B --> Action1C["Alerta a admin ISSEG"]
    Action1C --> Resolve1["✓ Desbloqueado después<br/>del tiempo"]
    
    Type -->|2. Acceso denegado múltiple| Case2["Usuario: Y<br/>10+ accesos denegados<br/>en 1 hora"]
    Case2 --> Action2A["Investigar patrón"]
    Action2A --> Decision2{¿Ataque?}
    Decision2 -->|Sí| Action2B["Suspender cuenta"]
    Decision2 -->|No| Action2C["Notificar usuario<br/>Revisar permisos"]
    Action2B --> Resolve2["✓ Admin revisa<br/>y restaura si es needed"]
    Action2C --> Resolve2
    
    Type -->|3. Token forjado/robado| Case3["Token inválido<br/>detectado"]
    Case3 --> Action3A["Invalidar token"]
    Action3A --> Action3B["Revocar todas las sesiones<br/>del usuario"]
    Action3B --> Action3C["Forzar nuevo login"]
    Action3C --> Resolve3["✓ Usuario debe<br/>autenticarse nuevamente"]
    
    Type -->|4. Cambio sospechoso de permisos| Case4["Cambios masivos<br/>de permisos detectados"]
    Case4 --> Action4A["Revertir cambios"]
    Action4A --> Action4B["Auditoría de quién<br/>hizo los cambios"]
    Action4B --> Action4C["Suspender admin<br/>si necesario"]
    Action4C --> Resolve4["✓ Investigación<br/>completada"]
    
    Type -->|5. Base de datos comprometida| Case5["Breach de BD detectado"]
    Case5 --> Action5A["Cambio de contraseña<br/>global obligatorio<br/>todos los usuarios"]
    Action5A --> Action5B["Notificación masiva"]
    Action5B --> Action5C["Auditoría forense"]
    Action5C --> Resolve5["✓ Nuevas contraseñas<br/>distribuidas"]
    
    style Alert fill:#ff7043
    style Type fill:#fff9c4
    style Case1 fill:#ffccbc
    style Case2 fill:#ffccbc
    style Case3 fill:#ffccbc
    style Case4 fill:#ffccbc
    style Case5 fill:#ffccbc
    style Resolve1 fill:#c8e6c9
    style Resolve2 fill:#c8e6c9
    style Resolve3 fill:#c8e6c9
    style Resolve4 fill:#c8e6c9
    style Resolve5 fill:#c8e6c9
```

Todos estos diagramas muestran en detalle:
1. Validaciones multi-nivel de acceso
2. Estados y transiciones de usuarios
3. Flujos de solicitudes con auditoría
4. Matriz de permisos
5. Ciclo de vida de permisos
6. Seguridad en login (secuencia)
7. Intentos de acceso no autorizado
8. Filtrado de sistemas
9. Recuperación ante incidentes

Puedes visualizarlos en VS Code con Ctrl+Shift+V
