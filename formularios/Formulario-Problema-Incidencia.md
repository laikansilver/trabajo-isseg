# Formulario Problema: Reporte de Incidencias/Problemas

**Propósito:** Reportar errores, fallos, bugs o problemas en sistemas en producción.

## Identificación del Problema

| Campo | Tipo | Obligatorio | Descripción |
|-------|------|-------------|-------------|
| ID Incidencia | Texto (Auto) | Automático | Generado automáticamente: INC-YYYY-NNNN (NO visible en formulario, solo al consultar) |
| Fecha del Problema | Fecha | Sí | Cuándo se detectó el problema (solo día, sin hora) |
| Nombre(s) del Reportante | Texto | Sí | Nombre de la persona que reporta |
| Apellido Paterno del Reportante | Texto | Sí | Apellido paterno de la persona que reporta |
| Apellido Materno del Reportante | Texto | Sí | Apellido materno de la persona que reporta |
| Área/Departamento | Lista | Sí | Seleccionar de catálogo |
| Email del Reportante | Email | Sí | Para comunicaciones de seguimiento |
| Tipo de Contacto | Lista | No | Teléfono o Celular |
| Número de Contacto | Teléfono | No | Número telefónico |
| Extensión | Texto | No | Solo si aplica |

## Sistema Afectado

| Campo | Tipo | Obligatorio | Descripción |
|-------|------|-------------|-------------|
| Sistema | Lista | Sí | Dropdown con sistemas a los que el área tiene acceso (sin mostrar versiones) |
| Módulo Afectado | Texto | Sí | ¿Qué módulo tiene el problema? |
| URL/Pantalla Afectada | Texto | No | Ruta exacta donde ocurre el problema |

## Descripción del Problema

| Campo | Tipo | Obligatorio | Descripción |
|-------|------|-------------|-------------|
| Título Resumido | Texto | Sí | Resumen breve |
| Descripción Detallada | Textarea | Sí | Qué está pasando |
| Pasos para Reproducir | Textarea | Sí | Pasos para reproducir |
| ¿Se puede reproducir? | Radio | Sí | Siempre / A veces / No se puede reproducir |

## Impacto y Urgencia

| Campo | Tipo | Obligatorio | Descripción |
|-------|------|-------------|-------------|
| Nivel de Urgencia | Radio | Sí | **Crítica** / **Alta** / **Media** / **Baja** |
| Cantidad de Usuarios Afectados | Número | Sí | ¿Cuántos usuarios están impactados? |
| ¿Impacta el Negocio? | Radio | Sí | Sí / No / Parcialmente |
| Frecuencia del Problema | Radio | Sí | Contínuo / Intermitente / Una sola vez |

**Nota sobre Urgencia:** El sistema asignará automáticamente al equipo de soporte según el nivel de urgencia seleccionado.

## Contexto Técnico

| Campo | Tipo | Obligatorio | Descripción |
|-------|------|-------------|-------------|
| Navegador / Dispositivo | Texto | Sí | Ej: Chrome 120.0, Safari, iPad |
| Sistema Operativo | Texto | Sí | Windows 11, macOS 14.2, Ubuntu 22.04, Android |
| Memoria Disponible | Texto | No | Ej: 8GB RAM |
| Conexión a Internet | Texto | No | Wifi / Fibra / Móvil |
| Mensaje de Error | Textarea | No | Error exacto |
| Código de Error | Texto | No | Código de error |
| Comportamiento Esperado | Textarea | Sí | Qué debería pasar |

## Evidencia y Anexos

| Campo | Tipo | Obligatorio | Descripción |
|-------|------|-------------|-------------|
| Archivo Adjunto 1 | Upload (JPG/PNG) | No | Captura de pantalla del error |
| Archivo Adjunto 2 | Upload (JPG/PNG) | No | Captura adicional o video corto |
| Archivo Adjunto 3 | Upload (TXT/LOG) | No | Archivo de log del sistema |
| Información Adicional | Textarea (500 chars) | No | Cualquier contexto extra |

## Confirmación y Autorización

| Campo | Tipo | Obligatorio | Descripción |
|-------|------|-------------|-------------|
| Verifico que la información es precisa | Checkbox | Sí | Confirmar que se revisó y es correcta |
| Autorizo contacto para seguimiento | Checkbox | Sí | Permiso para que ISSEG se comunique |
| Detalles de Contacto Preferido | Texto | No | Email preferido, teléfono, horario |

---

## Resumen
- **Total de Campos:** 14
- **Requiere Aprobación:** No
- **SLA Automático:** Sí (por urgencia)

## Notas
- El ID se genera automáticamente al guardar
- La SLA es visual (color badge) y se comunica automáticamente
- Los campos Urgencia desencadenan el SLA correspondiente
- Los adjuntos se almacenan en carpeta: `/incidencias/YYYY/MM/INC-NNNN/`
