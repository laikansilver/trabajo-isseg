# 📁 Estructura del Proyecto

## ✅ Organización de Carpetas

El proyecto está organizado en carpetas temáticas para mejor mantenibilidad:

```
trabajo-isseg/
│
├── 📂 server/                              ← Aplicación Node.js/Express
│   ├── server.js                           (servidor principal)
│   ├── package.json                        (dependencias)
│   └── package-lock.json                   (lock file)
│
├── 📂 conbinacion de proyecto/             ← Aplicación principal HTML
│   ├── ISSEG-Sistema-Solicitudes-Mejorado.html
│   ├── ISSEG-Sistema-Solicitudes.html
│   └── ...
│
├── 📂 formularios/                         ← Formularios individuales
├── 📂 diagramas/                           ← Diagramas Mermaid
├── 📂 docmentacion/                        ← Documentación técnica
├── 📂 .github/workflows/                   ← GitHub Actions (GitHub Pages)
│
├── CNAME                                   ← Configuración de dominio personalizado
├── ESTRUCTURA-CARPETAS.md                  ← Este archivo
├── GITHUB-PAGES-SETUP.md                   ← Configuración GitHub Pages
└── ...
```

---

## 🚀 Cómo Ejecutar

### Ejecutar Servidor Node.js Localmente

```bash
# Navegar a la carpeta server
cd server

# Instalar dependencias (solo primera vez)
npm install

# Ejecutar servidor
npm start
```

**URL:** http://localhost:3000

---

## 📝 Scripts NPM

En la carpeta `server/`:

```bash
npm start     # Inicia el servidor Express
npm test      # Tests (no configurados aún)
```

---

## 🔧 Variables de Entorno

Se puede configurar el puerto:
- `PORT` - Puerto por defecto es 3000

Ejemplos:
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

## 🌐 Despliegue a GitHub Pages

El proyecto está configurado para desplegarse automáticamente en GitHub Pages:

- **Dominio:** `sgspcsi.isseg.com`
- **Branch:** `main`
- **Workflow:** `.github/workflows/deploy.yml`

Ver [GITHUB-PAGES-SETUP.md](GITHUB-PAGES-SETUP.md) para detalles de configuración DNS.

---

## 📋 Resumen de Carpetas

| Carpeta | Contenido | Propósito |
|---------|-----------|----------|
| `/server` | Servidor Node.js | Servir aplicación localmente |
| `/conbinacion de proyecto` | HTML principal | Aplicación web principal |
| `/formularios` | Formularios HTML | Formularios individuales |
| `/diagramas` | Diagramas Mermaid | Diagramas de flujo y proceso |
| `/docmentacion` | Documentación técnica | Guías y especificaciones |
| `/.github/workflows` | GitHub Actions | Despliegue automatizado |

---

## 🔗 Próximos Pasos

1. Ejecutar localmente: `cd server && npm install && npm start`
2. Acceder a: http://localhost:3000
3. Para despliegue en línea: Seguir pasos en [GITHUB-PAGES-SETUP.md](GITHUB-PAGES-SETUP.md)
