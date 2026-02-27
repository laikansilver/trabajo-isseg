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

## � Ejecución Local

Si necesitas ejecutar la aplicación Node.js localmente:

```bash
cd server
npm install
npm start
```

Accede a: `http://localhost:3000`

Para más detalles, ver [ESTRUCTURA-CARPETAS.md](ESTRUCTURA-CARPETAS.md)

---

## 📝 Credenciales a Usar

**Dominio:** sgspcsi.isseg.com
**TXT Record Name:** _github-pages-challenge-laikansilver.sgspcsi.isseg.com
**TXT Record Value:** 60ce5201bb00ef7c746d78c2f81b2e
**Repositorio:** laikansilver/trabajo-isseg
**Branch:** main
