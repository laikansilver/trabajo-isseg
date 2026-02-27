# 🚀 Guía Completa: Configurar GitHub Pages + Subdominio + Contenedor

## Paso 1: Verificación DNS en GitHub Pages

GitHub Pages requiere verificar que eres el dueño del dominio. Sigue estos pasos:

### 1.1 Acceder a GitHub
1. Ve a tu repositorio: https://github.com/laikansilver/trabajo-isseg
2. Ve a **Settings** → **Pages**
3. Busca la sección "Your GitHub Pages site is currently being built from the `main` branch"

### 1.2 Configurar el Dominio Personalizado
1. En **Custom domain**, escribe: `sgspcsi.isseg.com`
2. GitHub te mostrará instrucciones de verificación DNS

### 1.3 Crear el Registro DNS en tu Proveedor

Necesitas crear UN registro TXT en tu DNS (registradores como GoDaddy, Namecheap, etc.):

**Tipo:** TXT Record (Registro de Texto)
**Nombre (Hostname):** `_github-pages-challenge-laikansilver.sgspcsi.isseg.com`
**Valor:** `60ce5201bb00ef7c746d78c2f81b2e`
**TTL:** 3600 (o dejar por defecto)

⏱️ **Espera 15-30 minutos** para que se propague (puede tomar hasta 24 horas)

---

## Paso 2: Configurar CNAME en Repositorio

✅ **YA HECHO:** Se creó archivo `CNAME` con contenido:
```
sgspcsi.isseg.com
```

Este archivo le indica a GitHub Pages qué dominio usar.

---

## Paso 3: Configurar Registros A/ALIAS en DNS

Después de verificar el TXT record, necesitas crear registros A o ALIAS:

### Opción A: Registros A (IP directas)
Si tu proveedor DNS soporta registros A, crea uno para `sgspcsi.isseg.com`:

```
Type: A
Name: sgspcsi.isseg.com (o solo sgspcsi)
Value: 185.199.108.153
Value: 185.199.109.153
Value: 185.199.110.153
Value: 185.199.111.153
```

### Opción B: ALIAS/ANAME (si tu proveedor lo soporta)
```
Type: ALIAS
Name: sgspcsi.isseg.com
Value: laikansilver.github.io
```

---

## Paso 4: Commit y Push a GitHub

```bash
# Desde tu terminal en el directorio del proyecto
cd "C:\Users\eduar\Documents\trabajo isseg"

git add CNAME .github/workflows/deploy.yml
git commit -m "🚀 Configurar GitHub Pages con subdominio sgspcsi.isseg.com"
git push origin main
```

---

## Paso 5: Verificar Configuración en GitHub

1. Ve a **Settings** → **Pages**
2. Verifica que:
   - Source = `main` branch
   - Custom domain = `sgspcsi.isseg.com`
   - Enforce HTTPS = ✅ (una vez verificado)

---

## Paso 6: Esperar Verificación y Despliegue

GitHub Pages:
1. ✅ Verifica que controles el dominio (basado en el TXT record)
2. ✅ Genera certificado HTTPS automático (Let's Encrypt)
3. ✅ Despliega tu contenido (HTML, CSS, JS estático)
4. ✅ Accede en: `https://sgspcsi.isseg.com`

---

## 🐳 Opción Extra: Contenedor Docker (para Node.js/Express)

Si también quieres ejecutar un **contenedor local o en servidor**, usa Docker:

### Requisitos:
- Docker instalado: https://www.docker.com/products/docker-desktop

### Pasos:

#### 1. Construir imagen
```bash
cd "C:\Users\eduar\Documents\trabajo isseg"
docker build -t isseg-sistema .
```

#### 2. Ejecutar contenedor
```bash
docker run -p 3000:3000 isseg-sistema
```

O con Docker Compose:
```bash
docker-compose up -d
```

Accede a: `http://localhost:3000`

### Parámetros Docker:
- `PORT`: 3000
- `NODE_ENV`: production
- Volúmenes montados para actualización en tiempo real

---

## 📊 Arquitectura de Despliegue

```
┌─────────────────────────────────────────────────────────┐
│                    Tu Dominio ISSEG                      │
│            sgspcsi.isseg.com (subdominio)               │
└────────────────┬────────────────────────────────────────┘
                 │
     ┌───────────┴───────────┐
     │                       │
┌────▼──────┐          ┌─────▼──────┐
│ GitHub    │          │  Servidor  │
│  Pages    │          │  Docker    │
│ (Static)  │          │ (Dinámico) │
└───────────┘          └────────────┘
     ✅                      ✅
   Contenido            Aplicación
   Estático         Node.js/Express
```

---

## 🔐 Conexión DNS

```
Tu Proveedor DNS
     ↓
Registros:
  - TXT: _github-pages-challenge... (para verificación)
  - A o ALIAS: sgspcsi.isseg.com → GitHub Pages
     ↓
GitHub Pages
     ↓
https://sgspcsi.isseg.com ✅
```

---

## ✅ Checklist de Configuración

- [ ] Crear registro TXT en DNS (verificación)
- [ ] Esperar 15-30 minutos de propagación
- [ ] Archivo CNAME creado ✅ (ya listo)
- [ ] Workflow GitHub Actions configurado ✅ (ya listo)
- [ ] Push a main branch
- [ ] Verificar en Settings → Pages
- [ ] Crear registros A/ALIAS en DNS
- [ ] Esperar certificado HTTPS (puede tomar 24h)
- [ ] Acceder a https://sgspcsi.isseg.com 🎉

---

## 📞 Soporte y Troubleshooting

### Si GitHub Pages no despliega:
1. Verifica que el branch `main` existe
2. Comprueba que `CNAME` está en la raíz
3. Revisa el log en Actions → deploy

### Si el dominio no resuelve:
1. Verifica propagación DNS: https://dnschecker.org
2. Busca el dominio: `nslookup sgspcsi.isseg.com`
3. Espera más tiempo (hasta 24h)

### Si HTTPS no funciona:
1. GitHub lo genera automático (5-30 min)
2. Verifica en Settings → Pages → "Enforce HTTPS"

---

## 🔗 Enlaces Útiles

- GitHub Pages Docs: https://docs.github.com/en/pages
- Configurar dominio personalizado: https://docs.github.com/en/pages/configuring-a-custom-domain-for-your-github-pages-site
- Propagación DNS: https://dnschecker.org
- Let's Encrypt HTTPS: https://letsencrypt.org

---

## 📝 Credenciales a Usar

**Dominio:** sgspcsi.isseg.com
**TXT Record Name:** _github-pages-challenge-laikansilver.sgspcsi.isseg.com
**TXT Record Value:** 60ce5201bb00ef7c746d78c2f81b2e
**Repositorio:** laikansilver/trabajo-isseg
**Branch:** main
