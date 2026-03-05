# Documento de Diseño del Software (SDD)
## Sistema de Gestión de Solicitudes ISSEG

### 1. Historial de Versiones
| Fecha | Versión | Descripción | Autor |
|-------|---------|-------------|-------|
| 05/03/2026 | 1.0 | Versión inicial del diseño detallado | Equipo de Arquitectura |

### 2. Bosquejo de Pantalla (Wireframe Layout)

La interfaz general del sistema sigue un diseño de "Dashboard Administrativo" estándar con los siguientes componentes:

*   **Barra Lateral (Sidebar)**: 
    *   Logo ISSEG.
    *   Menú de Navegación:
        *   Inicio / Dashboard.
        *   Mis Solicitudes (Bandeja de entrada).
        *   Nueva Solicitud (Acceso a Formularios A, B, C).
        *   Reportar Incidencia.
        *   Configuración (Si aplica por rol).
    *   Botón Cerrar Sesión.
*   **Barra Superior (Header)**:
    *   Título de la sección actual (Breadcrumbs).
    *   Información del Usuario (Nombre, Rol, Área).
    *   Notificaciones.
*   **Área de Contenido Principal**: Espacio dinámico donde se cargan los formularios y tablas de datos.
*   **Pie de Página (Footer)**: Información legal y versión del sistema.

### 3. Escenarios

#### Escenario 1: Solicitud de Sistema Nuevo
**Descripción**: Un usuario con rol de "Responsable" desea solicitar la creación de un nuevo software para su departamento.
1.  El usuario inicia sesión y accede al Dashboard.
2.  Hace clic en "Nueva Solicitud" y selecciona "Sistema Nuevo".
3.  El sistema valida permisos; si es correcto, muestra el **Formulario A**.
4.  El usuario completa la información general, justificación y alcance.
5.  El usuario envía el formulario.
6.  El sistema genera el ID `SN-2026-0001` y notifica al área de TI.
7.  **Vía Alterna**: Si el usuario no tiene permisos, el sistema muestra el mensaje de error "E0003" y redirige al inicio.

#### Escenario 2: Reporte de Incidencia Crítica
**Descripción**: Un usuario operativo detecta un fallo que detiene la operación.
1.  El usuario selecciona "Reportar Problema".
2.  El sistemas carga la lista de aplicaciones asignadas a su área.
3.  El usuario selecciona el sistema afectado y llena el formulario de incidencia.
4.  Selecciona Urgencia "Crítica".
5.  Adjunta captura de pantalla del error.
6.  Envía el reporte.
7.  El sistema registra la incidencia, inicia el cronómetro de SLA (1 hora) y alerta a soporte inmediatamente.

### 4. Elementos de Pantalla

A continuación se detallan los elementos principales de los formularios.

#### Formulario A: Solicitud de Sistema Nuevo

| Elemento | Comportamiento | Editable | Obligatorio | Regla de Negocio |
|----------|----------------|----------|-------------|------------------|
| Nombre(s) | Input Texto | No (Prellenado) | Sí | Se obtiene de la sesión del usuario. |
| Área/Departamento | Select/Dropdown | No (Prellenado) | Sí | Muestra el área asignada al usuario. |
| Nombre del Sistema Propuesto | Input Texto | Sí | Sí | Máximo 100 caracteres. Debe ser único. |
| Tipo de Sistema | Select | Sí | Sí | Valores: Web, Escritorio, Móvil, API, Híbrido. |
| Justificación del Negocio | Textarea | Sí | Sí | Mínimo 50 caracteres para asegurar detalle. |
| Prioridad del Negocio | Radio Button | Sí | Sí | Afecta la evaluación inicial de viabilidad. |
| Aprobación Jefe de Área | Checkbox/Firma | Sí | Sí | Requerido para procesar la solicitud. |

#### Formulario B: Modificación de Sistema

| Elemento | Comportamiento | Editable | Obligatorio | Regla de Negocio |
|----------|----------------|----------|-------------|------------------|
| Sistema a Modificar | Select | Sí | Sí | Solo lista sistemas activos del área del usuario. |
| Tipo de Modificación | Radio Button | Sí | Sí | Valores: Nueva funcionalidad, Error, Mejora, etc. |
| Descripción Detallada | Textarea | Sí | Sí | Explicación técnica del cambio. |
| Urgencia | Radio Button | Sí | Sí | Determina la prioridad en la cola de desarrollo. |
| Impacto en Operación | Radio Button | Sí | Sí | Usado para matrices de riesgo. |

#### Formulario de Incidencias

| Elemento | Comportamiento | Editable | Obligatorio | Regla de Negocio |
|----------|----------------|----------|-------------|------------------|
| Sistema Afectado | Select | Sí | Sí | Filtra módulos asociados. |
| Nivel de Urgencia | Radio Button | Sí | Sí | Define el SLA: Crítica(1h), Alta(4h), Media(8h), Baja(24h). |
| Evidencia (Adjuntos) | File Upload | Sí | No | Permite JPG, PNG, LOG. Máx 10MB. |

### 5. Excepciones

| ID | Nombre | Acción |
|----|--------|--------|
| E0001 | Sesión Expirada | Redirigir a login y mostrar mensaje "Su sesión ha terminado". |
| E0002 | Acceso Denegado | Mostrar página 403 con mensaje "No tiene permisos para ver este recurso". |
| E0003 | Permiso Insuficiente | Mostrar alerta "Su rol no permite realizar esta solicitud" y volver al Dashboard. |
| E0004 | Recurso No Encontrado | Mostrar página 404 "El sistema o solicitud buscada no existe". |
| E0005 | Error de Servidor | Mostrar mensaje genérico "Error interno, contacte al administrador" (Loguear detalle técnico). |

### 6. Validaciones

| ID | Descripción | Acción |
|----|-------------|--------|
| V0001 | Campos obligatorios vacíos | Resaltar campo en rojo y mostrar mensaje M0001. Bloquear envío. |
| V0002 | Formato de Email inválido | Validar regex de correo. Mostrar mensaje M0007. |
| V0003 | Fecha anterior a la actual | En campos de fecha de inicio/entrega, no permitir fechas pasadas. |
| V0004 | Archivo adjunto muy pesado | Si el archivo > 10MB, mostrar mensaje "El archivo excede el límite permitido". |
| V0005 | Texto demasiado corto | Si la justificación < 50 caracteres, mostrar "Por favor detalle más la justificación". |
| V0006 | Selección de Sistema | Verificar que el sistema seleccionado pertenezca al área del usuario. |

### 7. Mensajes

| ID | Descripción | Tipo de Mensaje |
|----|-------------|-----------------|
| M0001 | "Este campo es obligatorio para continuar." | Error (Validación) |
| M0002 | "Solicitud enviada exitosamente. Su folio es: {ID}" | Confirmación |
| M0003 | "¿Está seguro que desea cancelar? Se perderán los cambios." | Advertencia |
| M0004 | "No se encontraron sistemas registrados para su área." | Información |
| M0005 | "El registro se actualizó correctamente." | Confirmación |
| M0006 | "La fecha seleccionada no es válida." | Error |
| M0007 | "Por favor ingrese un correo electrónico válido." | Advertencia |

### 8. Diagramas de Flujo
El diseño del sistema se apoya en los siguientes diagramas de flujo detallados (ver anexos de documentación técnica):
1.  **Diagrama de Proceso Principal**: Cubre desde el login hasta la selección del tipo de solicitud.
2.  **Diagrama de Estados del Ticket**: Muestra las transiciones (Pendiente -> Aprobado -> En Desarrollo -> Terminado).
3.  **Diagrama de Filtrado**: Lógica para mostrar solo sistemas autorizados por área.
