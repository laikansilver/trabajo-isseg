# Formulario C: Levantamiento de Requerimientos Detallado

**Nota:** Se completa DESPUÉS de la aprobación del Formulario A.

## Información del Proyecto

| Campo | Tipo | Obligatorio | Descripción |
|-------|------|-------------|-------------|
| ID Proyecto | Texto | Sí | Referencia del Formulario A aprobado (SN-2026-XXXX) |
| Nombre del Sistema | Texto | Sí | Desde Formulario A |
| Product Manager Asignado | Texto | Sí | Nombre del PM responsable |
| Desarrollador Líder | Texto | Sí | Nombre del Dev Lead |
| Fecha de Inicio | Fecha | Sí | Fecha de levantamiento |
| Responsable de Requerimientos | Texto | Sí | Usuario de área que define necesidades |

## Objetivos y Alcance Técnico

| Campo | Tipo | Obligatorio | Descripción |
|-------|------|-------------|-------------|
| Objetivo General del Sistema | Textarea (500 chars) | Sí | Meta principal del sistema |
| Objetivos Específicos | Textarea (1000 chars) | Sí | Lista numerada de objetivos concretos |
| Alcance Funcional (Qué SÍ incluye) | Textarea (1000 chars) | Sí | Qué sí incluye el sistema |
| Fuera de Alcance (Qué NO incluye) | Textarea (1000 chars) | Sí | Qué NO incluye el sistema (clarificar límites) |

## Actores y Roles del Sistema

| Campo | Tipo | Obligatorio | Descripción |
|-------|------|-------------|-------------|
| Tabla de Roles | Tabla dinámica | Sí | 4 columnas: Rol, Descripción, Permisos Generales, Cant. Usuarios |

**Estructura de Tabla:**

| Rol | Descripción | Permisos Generales | Cant. Usuarios |
|-----|-------------|-------------------|----------------|
| Administrador | Gestión completa | CRUD completo, configuración | 2-3 |
| Usuario Operativo | Registro diario | Crear, consultar, editar propios | 50+ |
| Supervisor | Revisión y aprobación | Consultar todos, aprobar | 5-10 |
| Consulta | Solo visualización | Lectura de reportes | Variable |

## Módulos Funcionales

| Campo | Tipo | Obligatorio | Descripción |
|-------|------|-------------|-------------|
| Nombre del Módulo | Texto | Sí | Ej: Gestión de Usuarios, Registro de Incidentes |
| Descripción | Textarea | Sí | Funcionalidad general del módulo |
| Prioridad | Radio | Sí | Crítico (MVP), Importante, Deseable |
| Dependencias | Texto | No | Otros módulos de los que depende |

**Ejemplo de Módulos:**

- Gestión de Usuarios - Crítico
- Autenticación y Seguridad - Crítico
- Registro de Datos - Crítico
- Reportes - Importante
- Integración con SAP - Deseable

## Requerimientos Funcionales (RF)

**Mínimo 10 RF obligatorios**

| ID | Descripción | Prioridad | Módulo | Criterio de Aceptación |
|----|-------------|-----------|--------|----------------------|
| RF-001 | El sistema debe permitir registro de usuarios con email único | Crítica | Usuarios | Usuario creado, email confirmado |
| RF-002 | El sistema debe generar reporte PDF de actividades | Alta | Reportes | PDF generado en < 5 seg |
| RF-003 | El sistema debe validar integridad de datos | Crítica | BD | Validaciones ejecutadas correctamente |
| ... | ... | ... | ... | ... |

## Reglas de Negocio

Validaciones, cálculos, restricciones que debe implementar el sistema:

- Solo admin puede crear usuarios
- El precio debe ser mayor a 0
- Máximo 100 registros por lote
- Los cambios deben ser registrados en auditoría
- El acceso se revoca 24 horas después de inactividad
- Los reportes deben incluir timestamp y usuario
- etc.

## Requerimientos No Funcionales (RNF)

| Categoría | Descripción | Métrica |
|-----------|-------------|---------|
| **Rendimiento** | Tiempo de respuesta esperado, usuarios concurrentes | < 2 segundos, 500 usuarios concurrentes |
| **Seguridad** | Encriptación, autenticación, autorización | SSL/TLS, OAuth 2.0, RBAC |
| **Escalabilidad** | Capacidad de crecimiento | Soportar 10x usuarios en 2 años |
| **Disponibilidad/SLA** | Uptime esperado, horarios mantenimiento | 99.9% uptime |
| **Compatibilidad** | Navegadores, sistemas operativos | Chrome, Firefox, Safari, Edge; Windows, macOS, Linux |
| **Usabilidad** | Interfaz intuitiva, accesibilidad | WCAG 2.1 Level AA |
| **Mantenibilidad** | Documentación, soporte técnico | Documentación completa, API documentada |
| **Backup/Recuperación** | Estrategia de datos | Backup diario, RTO < 4h |

---

## Resumen
- **Total de Secciones:** 7
- **Total de Campos:** 50+ (incluye tablas dinámicas)
- **Tiempo estimado:** 30-45 minutos
- **Requiere Aprobación:** No (pero requiere validación con PM)
- **Mínimo Requerido:** 10 Requerimientos Funcionales
