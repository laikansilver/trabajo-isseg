# Formulario B: Solicitud de Modificación

## Identificación

| Campo | Tipo | Obligatorio | Descripción |
|-------|------|-------------|-------------|
| ID Modificación | Texto (Auto) | Sí | Generado: MOD-YYYY-NNNN |
| Fecha de Solicitud | Fecha | Sí | Automática |
| Sistema a Modificar | Lista desplegable | Sí | Sistema de Gestión de Inventario (v1.2), Portal RH (v2.1), Plataforma Ventas (v3.0), Sistema Contabilidad (v1.5), Aplicación Logística (v2.3) |
| Versión Actual | Texto (Auto) | Sí | Se llena automáticamente según sistema |
| Nombre del Solicitante | Texto | Sí | Nombre completo |
| Área/Departamento | Texto | Sí | Tu área |
| Email de Contacto | Email | Sí | Correo institucional |

## Descripción del Cambio

| Campo | Tipo | Obligatorio | Descripción |
|-------|------|-------------|-------------|
| Tipo de Modificación | Radio button | Sí | Nueva funcionalidad, Corrección de error, Mejora de rendimiento, Cambio de interfaz, Integración, Seguridad, Otro |
| Descripción Detallada | Textarea (1000 chars) | Sí | Explicación clara del cambio solicitado |
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
| Fecha Límite | Fecha | No | Cuándo se requiere el cambio |
| Archivos Adjuntos | Upload | No | Screenshots, logs, videos |
| Horario Preferido de Implementación | Texto | No | Para minimizar impacto operativo |

## Soluciones Temporales

| Campo | Tipo | Obligatorio | Descripción |
|-------|------|-------------|-------------|
| ¿Existe solución temporal? | Radio button | Sí | Sí, No |
| Descripción del Workaround | Textarea | Condicional | Si existe, describir la solución temporal |
| Comentarios Adicionales | Textarea | No | Información complementaria |

---

## Resumen
- **Total de Secciones:** 8
- **Total de Campos:** 25+
- **Tiempo estimado:** 12-15 minutos
- **Requiere Aprobación:** Sí (Revisión ISSEG)
- **SLA:** Según urgencia seleccionada
