# Formulario C: Levantamiento de Requerimientos Detallado

**Nota:** Se completa DESPUÉS de la aprobación del Formulario A.

## Información del Proyecto

| Campo | Tipo | Obligatorio | Descripción |
|-------|------|-------------|-------------|
| ID Proyecto | Texto | Sí | Referencia del Formulario A aprobado (SN-2026-XXXX) - NO visible en formulario, solo al consultar |
| Nombre del Sistema | Texto | Sí | Desde Formulario A |
| Nombre(s) del Product Manager | Texto | Sí | Nombre del PM responsable |
| Apellido Paterno del Product Manager | Texto | Sí | Apellido paterno del PM |
| Apellido Materno del Product Manager | Texto | Sí | Apellido materno del PM |
| Nombre(s) del Desarrollador Líder | Texto | Sí | Nombre del Dev Lead |
| Apellido Paterno del Desarrollador Líder | Texto | Sí | Apellido paterno del Dev Lead |
| Apellido Materno del Desarrollador Líder | Texto | Sí | Apellido materno del Dev Lead |
| Fecha de Inicio | Fecha | Sí | Fecha de levantamiento (solo día) |
| Nombre(s) del Responsable | Texto | Sí | Usuario de área que define necesidades |
| Apellido Paterno del Responsable | Texto | Sí | Apellido paterno del responsable |
| Apellido Materno del Responsable | Texto | Sí | Apellido materno del responsable |

## Objetivos y Alcance Técnico

| Campo | Tipo | Obligatorio | Descripción |
|-------|------|-------------|-------------|
| Objetivo General del Sistema | Textarea | Sí | Meta principal |
| Objetivos Específicos | Textarea | Sí | Objetivos concretos |
| Alcance Funcional (Qué SÍ incluye) | Textarea | Sí | Qué incluye |
| Fuera de Alcance (Qué NO incluye) | Textarea | Sí | Qué NO incluye |

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

**Nota:** Los IDs se asignan automáticamente y NO se muestran en el formulario. Solo son visibles al consultar.

| ID | Descripción | Prioridad | Módulo |
|----|-------------|-----------|--------|
| RF-001 (auto) | El sistema debe permitir registro de usuarios con email único | Crítica | Usuarios |
| RF-002 (auto) | El sistema debe generar reporte PDF de actividades | Alta | Reportes |
| RF-003 (auto) | El sistema debe validar integridad de datos | Crítica | BD |
| ... | ... | ... | ... |

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
| **Rendimiento** | Tiempo de respuesta | < 2 segundos |
| **Seguridad** | Encriptación, autenticación | SSL/TLS, OAuth 2.0 |
| **Disponibilidad** | Uptime esperado | 99.9% uptime |

---

## Resumen
- **Total de Campos:** 11
- **Requiere Aprobación:** PM
- **Mínimo:** 10 Requerimientos Funcionales
