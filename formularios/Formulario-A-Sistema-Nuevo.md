# Formulario A: Solicitud de Sistema Nuevo

## Información General

| Campo | Tipo | Obligatorio | Descripción |
|-------|------|-------------|-------------|
| ID Solicitud | Texto (Auto) | Sí | Generado automáticamente: SN-YYYY-NNNN (NO visible en formulario, solo al consultar) |
| Fecha de Solicitud | Fecha | Sí | Fecha automática de creación (solo día, sin hora) |
| Nombre(s) | Texto | Sí | Nombre del solicitante |
| Apellido Paterno | Texto | Sí | Apellido paterno del solicitante |
| Apellido Materno | Texto | Sí | Apellido materno del solicitante |
| Cargo/Posición | Texto | Sí | Puesto que ocupa |
| Área/Departamento | Lista desplegable | Sí | RRHH, Finanzas, Operaciones, Ventas, Logística, Otro |
| Email de Contacto | Email | Sí | Correo institucional |
| Tipo de Contacto | Lista | Sí | Teléfono o Celular |
| Número de Contacto | Teléfono | Sí | Número telefónico |
| Extensión | Texto | No | Solo si aplica |

## Descripción del Sistema

| Campo | Tipo | Obligatorio | Descripción |
|-------|------|-------------|-------------|
| Nombre del Sistema | Texto (100 chars) | Sí | Nombre descriptivo y claro |
| Tipo de Sistema Web | Lista | Sí | Aplicación Web Interna, Aplicación Web Pública, Portal Web, Sistema Web de Gestión, API/Servicio Web |
| Descripción General | Textarea | Sí | Qué hace el sistema |
| Problema que Resuelve | Textarea | Sí | Situación actual |

## Justificación y Alcance

| Campo | Tipo | Obligatorio | Descripción |
|-------|------|-------------|-------------|
| Justificación del Negocio | Textarea | Sí | Por qué es necesario |
| Beneficios Esperados | Checkbox múltiple | Sí | Ahorro tiempo, automatización, mejora servicio |
| Usuarios Finales Estimados | Número | Sí | Cantidad aproximada de usuarios |
| Áreas Beneficiadas | Radio + Checkbox | Sí | Solo el área solicitante / Toda la institución / Varias áreas (seleccionar) |
| Prioridad del Negocio | Radio button | Sí | Crítica, Alta, Media, Baja |
| Criticidad | Radio button | Sí | Esencial para operación, Mejora de proceso, Optimización |

## Alcance Preliminar

| Campo | Tipo | Obligatorio | Descripción |
|-------|------|-------------|-------------|
| Funcionalidades Principales | Textarea (1000 chars) | Sí | Lista de funciones clave requeridas |
| Integraciones Necesarias | Textarea | No | Sistemas existentes a conectar |
| Plataforma Preferida | Lista | Sí | Web, Windows, Linux, Android, iOS, Multiplataforma |
| Acceso Esperado | Radio button | Sí | Interno (red local), Externo (internet), Ambos |

## Recursos

| Campo | Tipo | Obligatorio | Descripción |
|-------|------|-------------|-------------|
| Recursos Humanos Disponibles | Textarea | No | Personal disponible |

## Documentación Adicional

| Campo | Tipo | Obligatorio | Descripción |
|-------|------|-------------|-------------|
| Archivos Adjuntos | Upload | No | Diagramas, mockups, documentos de referencia |
| Comentarios Adicionales | Textarea | No | Información complementaria relevante |

## Aprobaciones

| Campo | Tipo | Obligatorio | Descripción |
|-------|------|-------------|-------------|
| Aprobación Jefe de Área | Checkbox | Sí | Certifico que cuento con aprobación del jefe |
| Nombre(s) Jefe de Área | Texto | Condicional | Nombre del jefe autorizado |
| Apellidos Jefe de Área | Texto | Condicional | Apellidos del jefe |
| Email Jefe de Área | Email | Condicional | Email del jefe |

---

## Resumen
- **Total de Campos:** 11
- **Requiere Aprobación:** Sí (Revisión ISSEG)
