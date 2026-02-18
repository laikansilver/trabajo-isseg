# 🌐 Guía de Configuración del Servicio Web

## Cómo Activar la Visualización Web del Repositorio

Este repositorio está configurado para ser visualizado como un sitio web usando **GitHub Pages**. Sigue estos pasos para activarlo:

### Pasos para Activar GitHub Pages

1. **Ve a la configuración del repositorio**
   - Abre el repositorio en GitHub
   - Haz clic en "Settings" (⚙️ Configuración)

2. **Navega a la sección Pages**
   - En el menú lateral izquierdo, busca "Pages" en la sección "Code and automation"
   - Haz clic en "Pages"

3. **Configura la fuente de publicación**
   - En "Source" (Fuente), selecciona: **Deploy from a branch**
   - En "Branch" (Rama), selecciona: **main** (o la rama principal de tu repositorio)
   - En la carpeta, selecciona: **/ (root)**
   - Haz clic en "Save" (Guardar)

4. **Espera unos minutos**
   - GitHub Pages tardará entre 1-5 minutos en construir y publicar tu sitio
   - Verás un mensaje indicando que tu sitio está listo

5. **Accede a tu sitio web**
   - Tu sitio estará disponible en: `https://<tu-usuario>.github.io/trabajo-isseg/`
   - Por ejemplo: `https://laikansilver.github.io/trabajo-isseg/`

### Estructura del Sitio Web

Una vez activado, podrás acceder a:

- **Página Principal:** `https://<tu-usuario>.github.io/trabajo-isseg/`
  - Punto de entrada con navegación a todas las secciones

- **Visualización de Flujos:** `https://<tu-usuario>.github.io/trabajo-isseg/Visualizacion-Formularios-Flujos.html`
  - Diagramas interactivos del sistema

- **Centro de Formularios:** `https://<tu-usuario>.github.io/trabajo-isseg/formularios/INDEX.html`
  - Acceso a los 4 formularios del sistema

- **Documentación:** Todos los archivos markdown serán renderizados automáticamente por GitHub Pages

### Características del Sitio Web

✅ **Página principal moderna** con navegación intuitiva  
✅ **Responsive design** - funciona en móviles, tablets y escritorio  
✅ **Diagramas interactivos** usando Mermaid.js  
✅ **Formularios visuales** con diseño profesional  
✅ **Sin necesidad de servidor** - completamente estático  
✅ **HTTPS automático** - seguro por defecto  
✅ **Actualizaciones automáticas** - se actualiza con cada commit a la rama principal

### Uso Alternativo: Servicio Web Local

Si prefieres ejecutar el sitio localmente en tu máquina:

#### Opción 1: Servidor HTTP Simple de Python

```bash
# En la raíz del repositorio
cd /ruta/a/trabajo-isseg

# Python 3
python -m http.server 8000

# Python 2
python -m SimpleHTTPServer 8000
```

Luego abre tu navegador en: `http://localhost:8000`

#### Opción 2: Servidor HTTP Simple de Node.js

```bash
# Instalar http-server globalmente
npm install -g http-server

# En la raíz del repositorio
cd /ruta/a/trabajo-isseg
http-server -p 8000
```

Luego abre tu navegador en: `http://localhost:8000`

#### Opción 3: Live Server (VS Code)

1. Instala la extensión "Live Server" en VS Code
2. Abre el archivo `index.html`
3. Haz clic derecho y selecciona "Open with Live Server"

### Actualizar el Sitio

El sitio web se actualiza automáticamente cuando:
- Haces commit de cambios en los archivos HTML, CSS o Markdown
- Los cambios se pushean a la rama configurada (main)
- GitHub Pages reconstruye el sitio (1-5 minutos)

### Compartir el Sitio

Una vez activado GitHub Pages, puedes compartir la URL con:
- Equipos de desarrollo
- Stakeholders del proyecto
- Usuarios finales para que vean los formularios
- Cualquier persona que necesite consultar la documentación

### Troubleshooting

**¿El sitio no se muestra?**
- Verifica que GitHub Pages esté activado en Settings → Pages
- Asegúrate de que la rama configurada sea la correcta
- Espera unos minutos para que se complete el build
- Verifica que el archivo `index.html` esté en la raíz del repositorio

**¿Los enlaces no funcionan?**
- Los enlaces relativos deberían funcionar automáticamente
- Si usas enlaces absolutos, actualízalos para que sean relativos

**¿Los archivos Markdown no se renderizan bien?**
- GitHub Pages usa Jekyll por defecto
- El archivo `_config.yml` ya está configurado
- Los archivos `.md` se convierten automáticamente a HTML

### Seguridad y Privacidad

⚠️ **Importante:** GitHub Pages hace que tu sitio sea **público**, incluso si el repositorio es privado.

Si el repositorio contiene información sensible:
- Considera usar un repositorio privado sin GitHub Pages
- O usa solo el servidor local para visualización interna
- O filtra el contenido sensible antes de publicar

### Soporte

Para más información sobre GitHub Pages:
- Documentación oficial: https://docs.github.com/en/pages
- Limitaciones: https://docs.github.com/en/pages/getting-started-with-github-pages/about-github-pages#usage-limits

---

**¡Listo!** Tu repositorio ahora puede ser visualizado en la web. 🎉
