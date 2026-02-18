# Formulario B: Solicitud de Modificación

## Identificación

| Campo | Tipo | Obligatorio | Descripción |
|-------|------|-------------|-------------|
| ID Modificación | Texto (Auto) | Sí | Generado: MOD-YYYY-NNNN (NO visible en formulario, solo al consultar) |
| Fecha de Solicitud | Fecha | Sí | Automática (solo día, sin hora) |
| Sistema a Modificar | Lista desplegable | Sí | Solo muestra sistemas a los que el área tiene acceso (sin mostrar versión) |
| Nombre(s) del Solicitante | Texto | Sí | Nombre del solicitante |
| Apellido Paterno | Texto | Sí | Apellido paterno del solicitante |
| Apellido Materno | Texto | Sí | Apellido materno del solicitante |
| Área/Departamento | Texto | Sí | Tu área |
| Email de Contacto | Email | Sí | Correo institucional |
| Tipo de Contacto | Lista | Sí | Teléfono o Celular |
| Número de Contacto | Teléfono | Sí | Número telefónico |
| Extensión | Texto | No | Solo si aplica |

## Descripción del Cambio

| Campo | Tipo | Obligatorio | Descripción |
|-------|------|-------------|-------------|
| Tipo de Modificación | Radio button | Sí | Nueva funcionalidad, Corrección, Mejora, Integración |
| Descripción Detallada | Textarea | Sí | Detalle del cambio |
| Módulos Afectados | Checkbox múltiple | Sí | Frontend, Backend, Base de Datos, Reportes, Integraciones, Seguridad |

## Análisis de Necesidad

| Campo | Tipo | Obligatorio | Descripción |
|-------|------|-------------|-------------|
| Razón del Cambio | Textarea (500 chars) | Sí | Por qué es necesaria esta modificación |
| Situación Actual | Textarea (500 chars) | Sí | Cómo funciona ahora |
| Situación Deseada | Textarea (500 chars) | Sí | Cómo debería funcionar |
| Frecuencia de Uso | Radio button | Sí | Diaria, Semanal, Mensual, Ocasional |

## Análisis de Impacto

| Campo | Tipo | Obligatorio | Descripción |
|-------|------|-------------|-------------|
| Urgencia | Radio button | Sí | Inmediata, Alta, Media, Baja |
| Impacto en Operación | Radio button | Sí | Crítico (bloquea operación), Alto, Medio, Bajo |
| Usuarios Afectados | Número | Sí | Cantidad de usuarios impactados |
| ¿Afecta Otros Sistemas? | Radio button | Sí | Sí (especificar abajo), No |
| Sistemas Afectados | Textarea | Condicional | Enumera sistemas impactados si aplica |
| ¿Requiere Migración de Datos? | Radio button | Sí | No, Parcial, Completa |
| ¿Requiere Capacitación? | Radio button | Sí | No, Capacitación Básica, Capacitación Completa |

## Detalles Técnicos

| Campo | Tipo | Obligatorio | Descripción |
|-------|------|-------------|-------------|
| Especificación Técnica | Textarea (1000 chars) | Sí | Detalles técnicos del requerimiento |
| Campos/Datos Involucrados | Textarea | No | Especificar qué datos se modifican |
| Validaciones/Reglas Requeridas | Textarea | No | Reglas de negocio a implementar |

## Contexto y Referencias

| Campo | Tipo | Obligatorio | Descripción |
|-------|------|-------------|-------------|
| Ticket de Error Relacionado | Texto | No | Si es corrección, número de ticket |
| Archivos Adjuntos | Upload | No | Screenshots, logs, videos |
| Horario Preferido de Implementación | Texto | No | Para minimizar impacto operativo |

## Soluciones Temporales

| Campo | Tipo | Obligatorio | Descripción |
|-------|------|-------------|-------------|
| ¿Existe solución temporal? | Radio button | Sí | Sí, No |
| Descripción de la Solución Temporal | Textarea | Condicional | Si existe, describir cuál es la solución temporal |
| ¿Cómo se utiliza? | Textarea | Condicional | Indicar los pasos o instrucciones para utilizar la solución temporal (ayuda a optimizar la modificación) |
| Comentarios Adicionales | Textarea | No | Información complementaria |

---

## Resumen
- **Total de Campos:** 13
- **Requiere Aprobación:** Sí (Revisión ISSEG)
- **SLA:** Según urgencia
