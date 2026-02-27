# 📁 Estructura Reorganizada: Docker + Node.js

## ✅ Cambios Realizados

Se ha reorganizado el proyecto en carpetas temáticas para mejor mantenibilidad:

```
trabajo-isseg/
│
├── 📂 docker/                              ← Configuración Docker
│   ├── Dockerfile
│   ├── docker-compose.yml
│   └── README.md
│
├── 📂 server/                              ← Aplicación Node.js
│   ├── server.js
│   ├── package.json
│   └── package-lock.json
│
├── 📂 conbinacion de proyecto/
├── 📂 formularios/
├── 📂 diagramas/
├── 📂 docmentacion/
└── ...
```

---

## 🚀 Cómo Ejecutar

### Opción 1: Docker Compose (Recomendado)

```bash
# Navegar a la carpeta docker
cd docker

# Ejecutar con Docker Compose
docker-compose up -d

# Detener
docker-compose down
```

**URL:** http://localhost:3000

---

### Opción 2: Node.js Local

```bash
# Navegar a la carpeta server
cd server

# Instalar dependencias (si es primera vez)
npm install

# Ejecutar servidor
npm start
```

**URL:** http://localhost:3000

---

### Opción 3: Docker Manual

```bash
# Desde la raíz del proyecto
docker build -f docker/Dockerfile -t isseg-app .

# Ejecutar
docker run -p 3000:3000 isseg-app
```

**URL:** http://localhost:3000

---

## 📝 Scripts NPM

En la carpeta `server/`:

```bash
npm start     # Inicia el servidor Express
npm run dev   # Igual a npm start
npm test      # Tests (no configurados aún)
```

---

## 🔧 Variables de Entorno

Se puede configurar:
- `PORT` - Puerto por defecto es 3000
- `NODE_ENV` - "production" en Docker, configurable localmente

Ejemplo:
```bash
# En Windows PowerShell
$env:PORT = 5000
npm start

# En Linux/Mac
PORT=5000 npm start
```

---

## 📂 Rutas de Archivos

La aplicación Express sirve archivos estáticos desde **la raíz del proyecto** (un nivel arriba de `/server`):

```javascript
app.use(express.static(path.join(__dirname, '..')));
```

Por lo tanto:
- `http://localhost:3000/formularios/...` → `/formularios/`
- `http://localhost:3000/diagramas/...` → `/diagramas/`
- `http://localhost:3000/conbinacion de proyecto/...` → `/conbinacion de proyecto/`

---

## 🐳 Docker: Detalles Técnicos

### Contexto de Build
- **Contexto:** Raíz del proyecto (`..` desde `/docker`)
- **Dockerfile:** `./docker/Dockerfile`
- **Volúmenes Montados:** Carpetas de contenido se actualizan en tiempo real

### Variables de Entorno en Docker
```yaml
NODE_ENV=production
PORT=3000
```

### Working Directory
```
/app/server ← Donde se ejecuta npm start
```

---

## ✅ Checklist de Migraciones

- ✅ Archivos movidos a `/docker`
- ✅ Archivos movidos a `/server`
- ✅ Paths actualizados en Dockerfile
- ✅ Paths actualizados en docker-compose.yml
- ✅ Paths actualizados en server.js
- ✅ Git history limpio (commits con rename)
- ✅ Push a GitHub completado

---

## 🔗 Próximos Pasos

1. Prueba Docker Compose: `cd docker && docker-compose up -d`
2. Verifica que funcione: http://localhost:3000
3. Revisa los logs: `docker-compose logs -f`
4. Para detener: `docker-compose down`

---

## 📞 Solucionar Problemas

### "No such file or directory"
- Verifica que estés en la carpeta correcta (`cd docker` o `cd server`)
- Revisa que el Dockerfile exista en `docker/Dockerfile`

### "Port 3000 already in use"
```bash
# Cambiar puerto
docker-compose --file docker/docker-compose.yml -p 5000:3000 up
```

### "Module not found"
```bash
cd server
npm install
```

---

## 📚 Referencia Rápida

| Comando | Ubicación | Función |
|---------|-----------|---------|
| `docker-compose up` | `/docker` | Ejecutar todo con Docker |
| `npm start` | `/server` | Ejecutar servidor localmente |
| `npm install` | `/server` | Instalar dependencias |
| `docker build` | Raíz + `/docker/Dockerfile` | Construir imagen |
