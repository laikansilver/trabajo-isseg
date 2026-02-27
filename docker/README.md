# 📁 Estructura de Carpetas - Docker y Node.js

```
trabajo-isseg/
├── 📂 docker/                    ← NUEVA: Archivos de Docker
│   ├── Dockerfile               ← Configuración de imagen Docker
│   ├── docker-compose.yml        ← Orquestación de contenedores
│   └── README-DOCKER.md          ← (Este archivo)
│
├── 📂 server/                    ← NUEVA: Aplicación Node.js/Express
│   ├── server.js                 ← Servidor Express principal
│   ├── package.json              ← Dependencias y scripts npm
│   └── package-lock.json         ← Lock file de dependencias
│
├── 📂 conbinacion de proyecto/   ← Archivos HTML principales
│   ├── ISSEG-Sistema-Solicitudes-Mejorado.html
│   ├── ISSEG-Sistema-Solicitudes.html
│   └── ...
│
├── 📂 formularios/               ← Formularios individuales
├── 📂 diagramas/                 ← Diagramas Mermaid
├── 📂 docmentacion/              ← Documentación técnica
│
├── .github/
│   └── workflows/
│       └── deploy.yml            ← Workflow para GitHub Pages
│
├── CNAME                         ← Configuración de dominio
├── server.js                     ← ⚠️ (REMOVIDO - ahora en /server)
└── package.json                  ← ⚠️ (REMOVIDO - ahora en /server)
```

---

## 🐳 Ejecutar con Docker

### Opción 1: Docker Compose (Recomendado)
```bash
cd docker
docker-compose up -d
```

### Opción 2: Construcción Manual
```bash
cd docker
docker build -t isseg-sistema .
docker run -p 3000:3000 isseg-sistema
```

---

## 📦 Ejecutar Node.js localmente

```bash
cd server
npm install
npm start
```

Acceso: `http://localhost:3000`

---

## 📋 Archivos Movidos

| Archivo Original | Nueva Ubicación |
|------------------|-----------------|
| `server.js` | `server/server.js` |
| `package.json` | `server/package.json` |
| `package-lock.json` | `server/package-lock.json` |
| `Dockerfile` | `docker/Dockerfile` |
| `docker-compose.yml` | `docker/docker-compose.yml` |

---

## 🔄 Path Updates

El archivo actualizado `/server/server.js` ahora usa:
```javascript
app.use(express.static(path.join(__dirname, '..')));
```

Esto permite servir archivos desde la raíz del proyecto (un nivel arriba de `/server`).
