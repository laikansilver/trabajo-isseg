# Login

## Elemntos

| **ID** | **Elemento** | **Comportamiento** | **Editable** | **Obligatorio** | **Regla de negocio** |
| --- | --- | --- | --- | --- | --- |
| E001 | Campo correo institucional | Permite ingresar el correo institucional del usuario | Sí | Sí | Debe pertenecer al dominio institucional |
| E002 | Campo contraseña | Permite ingresar la contraseña del usuario | Sí | Sí | Debe coincidir con la contraseña registrada |
| E003 | Checkbox “Recordarme” | Permite mantener la sesión iniciada en el dispositivo | Sí | No | Se activa solo si el usuario lo selecciona |
| E004 | Botón “Acceder al sistema” | Envía las credenciales para su validación | No | Sí | Solo se habilita cuando los campos obligatorios están completos |
| E005 | Enlace “¿Olvidaste tu contraseña?” | Redirige al proceso de recuperación de contraseña | No | No | Depende del sistema institucional |

## Excepciones

| **ID** | **Nombre** | **Acción** |
| --- | --- | --- |
| E0001 | Credenciales inválidas | Mostrar mensaje de error y permanecer en la pantalla de login |
| E0002 | Sesión expirada | Redirigir al usuario nuevamente a la pantalla de inicio de sesión |

## Validaciones

| **ID** | **Descripción** | **Acción** |
| --- | --- | --- |
| V0001 | Correo institucional vacío | Mostrar mensaje M0001 |
| V0002 | Contraseña vacía | Mostrar mensaje M0002 |
| V0003 | Formato de correo inválido | Mostrar mensaje M0003 |
| V0004 | Credenciales incorrectas | Mostrar mensaje M0004 |

## Mensajes 

| **ID** | **Descripción** | **Tipo de mensaje** |
| --- | --- | --- |
| M0001 | Debe ingresar su correo institucional | Advertencia |
| M0002 | Debe ingresar su contraseña | Advertencia |
| M0003 | El formato del correo electrónico no es válido | Advertencia |
| M0004 | Correo o contraseña incorrectos | Error |
| M0005 | Inicio de sesión exitoso | Confirmación |

# Mis solicitudes – usuario

## Elemntos

| **ID** | **Elemento** | **Comportamiento** | **Editable** | **Obligatorio** | **Regla de negocio** |
| --- | --- | --- | --- | --- | --- |
| E101 | Menú lateral | Permite navegar entre las diferentes secciones del sistema | No | No | Las opciones disponibles dependen del rol del usuario |
| E102 | Título "Mis solicitudes" | Indica la sección actual del sistema | No | No | Se muestra en la parte superior de la pantalla |
| E103 | Filtro de estado | Permite filtrar solicitudes por estado | Sí | No | Estados posibles: pendiente, aprobado, en desarrollo, cerrado |
| E104 | Filtro de tipo | Permite filtrar solicitudes por tipo | Sí | No | Tipos posibles: nuevo sistema, modificación, incidencia |
| E105 | Campo de búsqueda | Permite buscar solicitudes por folio o descripción | Sí | No | La búsqueda se realiza sobre los datos registrados |
| E106 | Tarjeta de solicitud | Muestra información resumida de una solicitud | No | No | Cada solicitud se representa como una tarjeta |
| E107 | Botón "Ver detalles" | Permite acceder a la pantalla de detalle de la solicitud | No | Sí | Redirige al detalle de la solicitud seleccionada |
| E108 | Estado de solicitud | Indica el estado actual de la solicitud | No | No | Se muestra con una etiqueta de color según el estado |

## Excepciones

| **ID** | **Nombre** | **Acción** |
| --- | --- | --- |
| E1001 | Sesión expirada | Redirigir al usuario a la pantalla de inicio de sesión |
| E1002 | Error al consultar solicitudes | Mostrar mensaje de error y permitir intentar nuevamente |
| E1003 | Acceso no autorizado | Mostrar mensaje de acceso restringido |

## Validaciones

| **ID** | **Descripción** | **Acción** |
| --- | --- | --- |
| V1001 | Campo de búsqueda vacío | Mostrar todas las solicitudes |
| V1002 | Filtro de estado seleccionado | Mostrar solo solicitudes con el estado seleccionado |
| V1003 | Filtro de tipo seleccionado | Mostrar solo solicitudes del tipo seleccionado |
| V1004 | Texto de búsqueda sin coincidencias | Mostrar mensaje M1002 |

## Mensajes 

| **ID** | **Descripción** | **Tipo de mensaje** |
| --- | --- | --- |
| M1001 | No existen solicitudes registradas | Aviso |
| M1002 | No se encontraron resultados para la búsqueda realizada | Advertencia |
| M1003 | Error al cargar las solicitudes | Error |
| M1004 | Solicitudes cargadas correctamente | Confirmación |

# Mis tareas- Dev

## Elemntos

| **ID** | **Elemento** | **Comportamiento** | **Editable** | **Obligatorio** | **Regla de negocio** |
| --- | --- | --- | --- | --- | --- |
| E062 | Indicador Pendientes | Muestra número de solicitudes pendientes | No | No | Información generada por el sistema |
| E063 | Indicador En Desarrollo | Muestra solicitudes en proceso | No | No | Información del sistema |
| E064 | Indicador Completadas | Muestra solicitudes finalizadas | No | No | Información del sistema |
| E065 | Indicador Urgentes | Muestra solicitudes críticas | No | No | Prioridad alta |
| E066 | Tabla de solicitudes | Muestra listado completo de solicitudes | No | No | Información del sistema |
| E067 | Filtro estado | Permite filtrar solicitudes por estado | Sí | No | Opciones definidas en el sistema |
| E068 | Filtro tipo | Permite filtrar solicitudes por tipo | Sí | No | Opciones del catálogo |
| E069 | Botón ver solicitud | Permite visualizar el detalle de la solicitud | No | No | Disponible para todas las solicitudes |
| E070 | Panel detalle solicitud | Muestra información completa de la solicitud | No | No | Información generada por el sistema |

## Excepciones

| **ID** | **Nombre** | **Acción** |
| --- | --- | --- |
| E0013 | Error al cargar solicitudes | Mostrar mensaje de error y permitir recargar la página |
| E0014 | Solicitud no encontrada | Mostrar mensaje indicando que la solicitud no está disponible |

## Validaciones

| **ID** | **Descripción** | **Acción** |
| --- | --- | --- |
| V0021 | Verificar rol desarrollador | Mostrar esta pantalla solo a usuarios con rol desarrollador |
| V0022 | Verificar existencia de solicitudes | Mostrar tabla o mensaje indicando que no hay registros |
| V0023 | Verificar filtros aplicados | Mostrar resultados correspondientes |

## Mensajes 

| **ID** | **Descripción** | **Tipo** |
| --- | --- | --- |
| M0025 | No hay solicitudes registradas | Aviso |
| M0026 | Error al cargar las solicitudes | Error |
| M0027 | Información actualizada correctamente | Confirmación |

# Documentación dev

## Elemntos

| **ID** | **Elemento** | **Comportamiento** | **Editable** | **Obligatorio** | **Regla de negocio** |
| --- | --- | --- | --- | --- | --- |
| E201 | Menú lateral | Permite navegar entre los módulos del sistema | No | No | Las opciones dependen del rol del usuario |
| E202 | Título "Repositorio de Documentación" | Indica la sección actual del sistema | No | No | Se muestra en la parte superior de la pantalla |
| E203 | Campo de búsqueda | Permite buscar documentos por nombre o tipo | Sí | No | La búsqueda se realiza sobre los documentos registrados |
| E204 | Filtros de tipo de solicitud | Permiten filtrar documentos por categoría | Sí | No | Tipos disponibles: todos, requerimientos, modificaciones, urgentes |
| E205 | Tarjeta Total Documentos | Muestra la cantidad total de documentos registrados | No | No | Se actualiza automáticamente |
| E206 | Tarjeta Solicitudes | Muestra el número de solicitudes asociadas a documentos | No | No | Se calcula automáticamente |
| E207 | Tarjeta Tamaño Total | Muestra el tamaño total ocupado por los documentos | No | No | Se calcula automáticamente |
| E208 | Lista de documentos | Muestra los documentos disponibles en el repositorio | No | No | Cada documento corresponde a una solicitud registrada |

## Excepciones

| **ID** | **Nombre** | **Acción** |
| --- | --- | --- |
| E2001 | Sesión expirada | Redirigir al usuario a la pantalla de inicio de sesión |
| E2002 | Error al cargar documentos | Mostrar mensaje de error e intentar recargar la información |
| E2003 | Acceso no autorizado | Mostrar mensaje indicando acceso restringido |

## Validaciones

| **ID** | **Descripción** | **Acción** |
| --- | --- | --- |
| V2001 | Campo de búsqueda vacío | Mostrar todos los documentos |
| V2002 | Filtro seleccionado | Mostrar únicamente documentos de la categoría seleccionada |
| V2003 | Búsqueda sin resultados | Mostrar mensaje M2002 |

## Mensajes 

| **ID** | **Descripción** | **Tipo de mensaje** |
| --- | --- | --- |
| M2001 | No hay documentos registrados en el repositorio | Aviso |
| M2002 | No se encontraron documentos que coincidan con la búsqueda | Advertencia |
| M2003 | Error al cargar la documentación | Error |
| M2004 | Documentos cargados correctamente | Confirmación |

# H Cliente

## Elemntos

| **ID** | **Elemento** | **Comportamiento** | **Editable** | **Obligatorio** | **Regla de negocio** |
| --- | --- | --- | --- | --- | --- |
| E006 | Indicadores de solicitudes | Muestran el estado de solicitudes registradas | No | No | Información generada por el sistema |
| E007 | Tarjeta Reporte de Falla Urgente | Permite registrar una solicitud urgente | No | No | Se genera formulario de urgencia |
| E008 | Tarjeta Modificación de Sistema | Permite registrar solicitudes de cambio en sistemas existentes | No | No | Debe seleccionar sistema existente |
| E009 | Tarjeta Nuevo Sistema | Permite registrar solicitud de desarrollo de un nuevo sistema | No | No | Inicia proceso de evaluación de viabilidad |
| E010 | Tarjeta Requerimientos Técnicos | Muestra formulario técnico detallado | No | No | Solo disponible después de aprobación del PM |
| E011 | Menú lateral | Permite navegación entre módulos | No | No | Visible según rol |
| E012 | Opción Mis Solicitudes | Redirige a la lista de solicitudes del usuario | No | No | Muestra historial de solicitudes |
| E013 | Menú de usuario | Permite acceder a opciones de perfil o cerrar sesión | No | No | Solo disponible para usuarios autenticados |

## Excepciones

| **ID** | **Nombre** | **Acción** |
| --- | --- | --- |
| E0003 | Acceso a formulario no autorizado | Mostrar mensaje indicando que el formulario requiere aprobación |
| E0004 | Error al cargar información | Mostrar mensaje de error y permitir recargar la página |

## Mensajes 

| **ID** | **Descripción** | **Tipo** |
| --- | --- | --- |
| M0006 | Bienvenido al portal de solicitudes | Aviso |
| M0007 | Este formulario requiere aprobación previa | Advertencia |
| M0008 | Sesión expirada, vuelva a iniciar sesión | Advertencia |
| M0009 | Error al cargar información del sistema | Error |
| M0010 | No tienes notificaciones nuevas | Aviso |

## Validaciones

| **ID** | **Descripción** | **Acción** |
| --- | --- | --- |
| V0005 | Validar sesión activa | Redirigir a pantalla de login si la sesión expiró |
| V0006 | Verificar permisos del usuario | Mostrar opciones de navegación según rol |
| V0007 | Verificar aprobación del proyecto | Habilitar formulario de requerimientos técnicos solo si fue aprobado |
| V0008 | Verificar existencia de notificaciones | Mostrar lista de notificaciones o mensaje de ausencia |

# H dev

## Elemntos

| **ID** | **Elemento** | **Comportamiento** | **Editable** | **Obligatorio** | **Regla de negocio** |
| --- | --- | --- | --- | --- | --- |
| E041 | Indicador Pendientes | Muestra número de solicitudes pendientes | No | No | Información generada por el sistema |
| E042 | Indicador En Desarrollo | Muestra número de solicitudes en proceso | No | No | Información generada por el sistema |
| E043 | Indicador Completadas | Muestra número de solicitudes finalizadas | No | No | Información generada por el sistema |
| E044 | Indicador Urgentes | Muestra solicitudes de alta prioridad | No | No | Prioridad alta |
| E045 | Tablero de tareas | Muestra tareas organizadas por estado | No | No | Información del sistema |
| E046 | Tarjeta de tarea | Representa una tarea específica | No | No | Derivada de una solicitud aprobada |
| E047 | Sección actividad reciente | Muestra eventos recientes del sistema | No | No | Historial de acciones |
| E048 | Métricas personales | Muestra indicadores de desempeño | No | No | Información generada por el sistema |
| E049 | Botón gestionar tareas | Redirige al módulo completo de tareas | No | No | Disponible para desarrolladores |
| E050 | Recursos y herramientas | Acceso a herramientas técnicas | No | No | Acceso a recursos del desarrollo |

## Excepciones

| **ID** | **Nombre** | **Acción** |
| --- | --- | --- |
| E0009 | Error al cargar tareas | Mostrar mensaje de error y permitir recargar la página |
| E0010 | No hay tareas asignadas | Mostrar mensaje indicando que no existen tareas |

## Validaciones

| **ID** | **Descripción** | **Acción** |
| --- | --- | --- |
| V0015 | Verificar rol desarrollador | Mostrar esta pantalla solo a usuarios con rol desarrollador |
| V0016 | Verificar existencia de tareas | Mostrar tablero o mensaje de ausencia |
| V0017 | Verificar sesión activa | Redirigir a login si la sesión expiró |

## Mensajes 

| **ID** | **Descripción** | **Tipo** |
| --- | --- | --- |
| M0018 | No hay tareas asignadas actualmente | Aviso |
| M0019 | Error al cargar las tareas | Error |
| M0020 | Sesión expirada, vuelva a iniciar sesión | Advertencia |

# H Pm

## Elemntos

| **ID** | **Elemento** | **Comportamiento** | **Editable** | **Obligatorio** | **Regla de negocio** |
| --- | --- | --- | --- | --- | --- |
| E027 | Indicador pendientes | Muestra solicitudes pendientes de revisión | No | No | Información del sistema |
| E028 | Indicador aprobadas | Muestra solicitudes aprobadas | No | No | Información del sistema |
| E029 | Indicador rechazadas | Muestra solicitudes rechazadas | No | No | Información del sistema |
| E030 | Indicador total de solicitudes | Muestra total de solicitudes registradas | No | No | Información del sistema |
| E031 | Botón Revisar pendientes | Redirige a solicitudes pendientes | No | No | Solo solicitudes pendientes |
| E032 | Botón Nuevos sistemas | Muestra solicitudes de nuevos proyectos | No | No | Filtrado por tipo |
| E033 | Botón Aprobadas | Muestra historial de solicitudes aprobadas | No | No | Estado aprobado |
| E034 | Botón Todas | Muestra todas las solicitudes | No | No | Sin filtro |
| E035 | Filtro estado | Permite filtrar solicitudes por estado | Sí | No | Opciones predefinidas |
| E036 | Filtro tipo | Permite filtrar solicitudes por tipo | Sí | No | Opciones del catálogo |
| E037 | Tabla solicitudes | Muestra listado de solicitudes registradas | No | No | Información del sistema |
| E038 | Botón Ver Detalles | Permite consultar información completa | No | No | Disponible para todas las solicitudes |
| E039 | Botón Aprobar | Cambia estado de solicitud a aprobada | No | No | Solo solicitudes pendientes |
| E040 | Botón Rechazar | Cambia estado de solicitud a rechazada | No | No | Solo solicitudes pendientes |

## Excepciones

| **ID** | **Nombre** | **Acción** |
| --- | --- | --- |
| E0007 | Error al cargar solicitudes | Mostrar mensaje de error y permitir recargar la página |
| E0008 | Acción no permitida | Mostrar mensaje indicando que la acción no está disponible |

## Validaciones

| **ID** | **Descripción** | **Acción** |
| --- | --- | --- |
| V0012 | Verificar rol Product Manager | Mostrar esta pantalla solo a usuarios con rol PM |
| V0013 | Verificar estado de solicitud | Solo permitir aprobar o rechazar solicitudes pendientes |
| V0014 | Verificar filtros aplicados | Mostrar resultados correspondientes |

## Mensajes 

| **ID** | **Descripción** | **Tipo** |
| --- | --- | --- |
| M0014 | Solicitud aprobada correctamente | Confirmación |
| M0015 | Solicitud rechazada correctamente | Confirmación |
| M0016 | Error al cargar las solicitudes | Error |
| M0017 | No hay solicitudes disponibles | Aviso |

# Perfil de usuario

## Elemntos

| **ID** | **Elemento** | **Comportamiento** | **Editable** | **Obligatorio** | **Regla de negocio** |
| --- | --- | --- | --- | --- | --- |
| E051 | Foto de perfil | Muestra la imagen del usuario | No | No | Imagen asociada al actor |
| E052 | Botón Cambiar Foto | Permite cargar una nueva imagen | Sí | No | Debe ser formato de imagen |
| E053 | Nombre del usuario | Muestra el nombre completo | No | Sí | Información institucional |
| E054 | Correo institucional | Muestra correo del usuario | No | Sí | No editable |
| E055 | Campo teléfono | Permite actualizar número telefónico | Sí | No | Formato numérico |
| E056 | Campo extensión | Permite actualizar extensión | Sí | No | Número interno |
| E057 | Campo departamento | Muestra área del usuario | No | Sí | Información institucional |
| E058 | Botón editar | Habilita edición de campos | No | No | Permite modificar datos |
| E059 | Preferencia notificaciones correo | Activa o desactiva notificaciones por correo | Sí | No | Configuración del actor |
| E060 | Preferencia notificaciones push | Activa o desactiva notificaciones del sistema | Sí | No | Configuración del actor |
| E061 | Preferencia modo oscuro | Cambia apariencia del sistema | Sí | No | Configuración visual |

## Excepciones

| **ID** | **Nombre** | **Acción** |
| --- | --- | --- |
| E0011 | Error al guardar cambios | Mostrar mensaje de error y solicitar reintentar |
| E0012 | Error al cargar imagen | Mostrar mensaje indicando que la imagen no es válida |

## Validaciones

| **ID** | **Descripción** | **Acción** |
| --- | --- | --- |
| V0018 | Verificar formato de teléfono | Mostrar mensaje si el formato es incorrecto |
| V0019 | Verificar formato de imagen | Permitir solo formatos de imagen válidos |
| V0020 | Verificar sesión activa | Redirigir a login si la sesión expiró |

## Mensajes 

| **ID** | **Descripción** | **Tipo** |
| --- | --- | --- |
| M0021 | Información actualizada correctamente | Confirmación |
| M0022 | No fue posible guardar los cambios | Error |
| M0023 | Formato de imagen no válido | Advertencia |
| M0024 | Sesión expirada, vuelva a iniciar sesión | Advertencia |

# Deshboard Pm

## Elemntos

| **ID** | **Elemento** | **Comportamiento** | **Editable** | **Obligatorio** | **Regla de negocio** |
| --- | --- | --- | --- | --- | --- |
| E401 | Menú lateral | Permite navegar entre los módulos del sistema | No | No | Las opciones dependen del rol del usuario |
| E402 | Título "Dashboard Ejecutivo" | Indica la sección actual del sistema | No | No | Visible en la parte superior |
| E403 | Tarjeta Solicitudes Activas | Muestra el número de solicitudes actualmente en proceso | No | No | Se calcula automáticamente |
| E404 | Tarjeta Tiempo de Respuesta | Muestra el tiempo promedio de atención de solicitudes | No | No | Se calcula con base en solicitudes resueltas |
| E405 | Tarjeta Tasa de Aprobación | Indica el porcentaje de solicitudes aprobadas | No | No | Se calcula automáticamente |
| E406 | Tarjeta Tasa de Solicitudes | Muestra el promedio de solicitudes registradas por día | No | No | Se calcula automáticamente |
| E407 | Selector de periodo | Permite cambiar el periodo de visualización | Sí | No | Opciones: día, semana, mes |
| E408 | Opción comparar con periodo anterior | Permite comparar métricas entre periodos | Sí | No | Solo afecta la visualización de gráficos |
| E409 | Gráfica de solicitudes por periodo | Muestra el comportamiento de solicitudes en el tiempo | No | No | Se actualiza según filtros |
| E410 | Gráfica estado de solicitudes | Muestra distribución de estados de solicitudes | No | No | Estados: pendiente, aprobado, rechazado, en desarrollo |
| E411 | Sección equipo activo | Muestra desarrolladores y estado de disponibilidad | No | No | Información actualizada del equipo |
| E412 | Sección actividad reciente | Muestra las últimas acciones registradas en el sistema | No | No | Se actualiza automáticamente |
| E413 | Botón descargar gráficas | Permite exportar datos del dashboard | No | No | Genera archivo de reporte |

## Excepciones

| **ID** | **Nombre** | **Acción** |
| --- | --- | --- |
| E4001 | Error al cargar métricas | Mostrar mensaje de error y permitir recargar la información |
| E4002 | Sesión expirada | Redirigir al usuario a la pantalla de inicio de sesión |
| E4003 | Acceso no autorizado | Mostrar mensaje indicando que el usuario no tiene permisos |

## Validaciones

| **ID** | **Descripción** | **Acción** |
| --- | --- | --- |
| V4001 | Cambio de periodo seleccionado | Actualizar automáticamente los gráficos |
| V4002 | Activación de comparación | Mostrar comparación entre periodos |
| V4003 | Sin datos disponibles | Mostrar mensaje informativo |

## Mensajes 

| **ID** | **Descripción** | **Tipo de mensaje** |
| --- | --- | --- |
| M4001 | No existen datos disponibles para el periodo seleccionado | Aviso |
| M4002 | Error al cargar la información del dashboard | Error |
| M4003 | Reporte generado correctamente | Confirmación |

# Equipo pm

## Elemntos

| **ID** | **Elemento** | **Comportamiento** | **Editable** | **Obligatorio** | **Regla de negocio** |
| --- | --- | --- | --- | --- | --- |
| E501 | Menú lateral | Permite navegar entre los módulos del sistema | No | No | Opciones dependen del rol del usuario |
| E502 | Título "Gestión de Equipo" | Indica la sección actual del sistema | No | No | Visible en la parte superior |
| E503 | Tarjeta Total de miembros | Muestra el número total de integrantes del equipo | No | No | Se calcula automáticamente |
| E504 | Tarjeta Activos ahora | Muestra la cantidad de miembros activos | No | No | Se actualiza automáticamente |
| E505 | Tarjeta Carga promedio | Indica el porcentaje promedio de carga del equipo | No | No | Se calcula automáticamente |
| E506 | Tarjeta Rendimiento promedio | Muestra el rendimiento general del equipo | No | No | Se calcula automáticamente |
| E507 | Filtro estado | Permite filtrar miembros por disponibilidad | Sí | No | Opciones: disponible, ocupado |
| E508 | Filtro especialidad | Permite filtrar desarrolladores por especialidad | Sí | No | Ejemplo: backend, frontend, QA |
| E509 | Filtro carga de trabajo | Permite filtrar desarrolladores por carga actual | Sí | No | Opciones según porcentaje de carga |
| E510 | Tarjeta miembro del equipo | Muestra información de cada desarrollador | No | No | Incluye proyectos, rendimiento y carga |
| E511 | Botón "Ver perfil" | Permite consultar información detallada del desarrollador | No | No | Abre perfil del miembro |
| E512 | Botón "Asignar" | Permite asignar una solicitud al desarrollador | No | Sí | Solo disponible para solicitudes aprobadas |
| E513 | Botón "Agregar miembro" | Permite registrar un nuevo integrante del equipo | No | No | Solo disponible para Product Manager |
| E514 | Calendario de disponibilidad | Muestra eventos de disponibilidad del equipo | No | No | Incluye asignaciones, vacaciones y incidencias |
| E515 | Selector de vista del calendario | Permite cambiar entre vista mensual, semanal o lista | Sí | No | Solo afecta visualización |

## Excepciones

| **ID** | **Nombre** | **Acción** |
| --- | --- | --- |
| E5001 | Error al cargar información del equipo | Mostrar mensaje de error y permitir recargar |
| E5002 | Sesión expirada | Redirigir al usuario al inicio de sesión |
| E5003 | Acceso no autorizado | Mostrar mensaje indicando falta de permisos |

## Validaciones

## Mensajes 

| **ID** | **Descripción** | **Tipo de mensaje** |
| --- | --- | --- |
| M5001 | No existen miembros registrados en el equipo | Aviso |
| M5002 | Desarrollador asignado correctamente | Confirmación |
| M5003 | Error al cargar la información del equipo | Error |
| M5004 | El desarrollador seleccionado no tiene disponibilidad | Advertencia |

# Aprobaciones pm

| **ID** | **Elemento** | **Comportamiento** | **Editable** | **Obligatorio** | **Regla de negocio** |
| --- | --- | --- | --- | --- | --- |
| E301 | Menú lateral | Permite navegar entre los módulos del sistema | No | No | Las opciones dependen del rol del usuario |
| E302 | Título "Gestión de Aprobaciones" | Indica la sección actual | No | No | Visible en la parte superior |
| E303 | Filtro tipo de solicitud | Permite filtrar solicitudes por tipo | Sí | No | Tipos: nuevo sistema, modificación, urgente |
| E304 | Filtro prioridad | Permite filtrar solicitudes por prioridad | Sí | No | Prioridades: alta, media, baja |
| E305 | Filtro área | Permite filtrar solicitudes por área solicitante | Sí | No | Lista de áreas institucionales |
| E306 | Tarjeta de solicitud | Muestra información resumida de una solicitud | No | No | Cada solicitud se muestra como una tarjeta |
| E307 | Botón "Aprobar" | Permite aprobar la solicitud | No | Sí | Cambia estado a aprobado |
| E308 | Botón "Rechazar" | Permite rechazar la solicitud | No | Sí | Requiere confirmar la acción |
| E309 | Botón "Solicitar información" | Permite solicitar aclaraciones al solicitante | No | No | Cambia estado a información requerida |
| E310 | Botón "Ver detalles" | Permite acceder al detalle completo de la solicitud | No | No | Redirige a la pantalla de detalle |

| **ID** | **Nombre** | **Acción** |
| --- | --- | --- |
| E3001 | Sesión expirada | Redirigir al usuario al inicio de sesión |
| E3002 | Error al actualizar estado de solicitud | Mostrar mensaje de error y mantener estado anterior |
| E3003 | Acceso no autorizado | Mostrar mensaje indicando que el usuario no tiene permisos |

| **ID** | **Descripción** | **Acción** |
| --- | --- | --- |
| V3001 | Confirmación de rechazo | Mostrar ventana de confirmación antes de rechazar |
| V3002 | Filtros aplicados | Mostrar solo solicitudes que coincidan con los filtros |
| V3003 | Solicitud sin información suficiente | Mostrar mensaje solicitando información adicional |

| **ID** | **Descripción** | **Tipo de mensaje** |
| --- | --- | --- |
| M3001 | Solicitud aprobada correctamente | Confirmación |
| M3002 | Solicitud rechazada | Aviso |
| M3003 | Se solicitó información adicional al solicitante | Confirmación |
| M3004 | Error al procesar la solicitud | Error |
| M3005 | No existen solicitudes pendientes de aprobación | Aviso |