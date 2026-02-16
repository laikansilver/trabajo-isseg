# Sistema de Gestión de Tickets de Desarrollo - Diagrama de Flujo

## 0. Mapa Único Integral (Inicio Sesión → Autenticación → Área → Permisos → Sistemas → 3 Tipos Solicitudes → Registros)

```mermaid
flowchart TD
    Start([INICIO SISTEMA]) --> Login[Pantalla de Inicio de Sesión]
    Login --> Auth{¿Credenciales válidas?}
    Auth -->|No| AuthFail[Error: Usuario/Contraseña inválidos<br/>Registrar intento fallido]
    AuthFail --> Login
    Auth -->|Sí| LoadUser[Cargar Usuario:<br/>ID, Nombre, Email, Rol, Área]

    LoadUser --> CheckArea{¿Usuario activo en el área?}
    CheckArea -->|No| DenyArea[Acceso solo lectura<br/>Registrar intento no autorizado]
    DenyArea --> ViewReadOnly[Modo Consulta:<br/>Ver solicitudes existentes]
    ViewReadOnly --> EndReadOnly([Fin - Sesión limitada])

    CheckArea -->|Sí| LoadPerms[Cargar Permisos del Área:<br/>Crear Sistema Nuevo?<br/>Solicitar Modificación?<br/>Reportar Problema?]
    LoadPerms --> FilterSystems[Filtrar Sistemas Autorizados<br/>para esta Área]
    FilterSystems --> Dashboard[Dashboard Principal<br/>- Mis Solicitudes<br/>- Mis Sistemas<br/>- Incidencias Abiertas]

    Dashboard --> Action{¿Seleccionar Acción?}
    
    %% OPCIÓN 1: Crear Sistema Nuevo
    Action -->|Crear Sistema Nuevo| CheckNewPerm{¿Permiso de crear<br/>sistema nuevo?}
    CheckNewPerm -->|No| DenyNew[No autorizado para crear<br/>sistemas nuevos]
    DenyNew --> Dashboard
    CheckNewPerm -->|Sí| FormNewSys[Llenar Formulario A:<br/>- Nombre Sistema<br/>- Justificación<br/>- Alcance<br/>- Beneficios<br/>- Área responsable]
    FormNewSys --> ReviewNewSys{Revisión ISSEG}
    ReviewNewSys -->|Rechazado| RejectNew[Notificar rechazo<br/>Guardar motivo]
    RejectNew --> Dashboard
    ReviewNewSys -->|Aprobado| AssignNewTeam[Asignar Recursos:<br/>- Desarrollador<br/>- Product Manager<br/>- Arquitecto]
    AssignNewTeam --> RequestReq[Solicitar Formulario C:<br/>Requerimientos Detallados]
    RequestReq --> FormReq[Usuario completa<br/>Requerimientos técnicos]
    FormReq --> ValidateReq{Requerimientos<br/>completos?}
    ValidateReq -->|No| ClarifyReq[Solicitar aclaración]
    ClarifyReq --> FormReq
    ValidateReq -->|Sí| CreateNewSys[Crear Sistema en BD<br/>Estado: Planeación]
    CreateNewSys --> RegisterNewSys[REGISTRAR en Base de Datos:<br/>Tabla: Sistemas<br/>- ID_Sistema<br/>- Nombre<br/>- Área_Responsable<br/>- Estado = Planeación<br/>- Fecha_Creación<br/>- Versión = 1.0<br/>- Tiempo_Actividad = 0]
    RegisterNewSys --> RegisterNewSysAudit[REGISTRAR AUDITORÍA:<br/>Tabla: Audit_Sistemas_Nuevos<br/>- Usuario_Solicitante<br/>- Fecha_Solicitud<br/>- Equipo_Asignado<br/>- Timeline_Estimado]
    RegisterNewSysAudit --> EndNewSys([Fin - Sistema Nuevo Creado])

    %% OPCIÓN 2: Solicitar Modificación
    Action -->|Modificar Sistema Existente| CheckModPerm{¿Permiso de<br/>modificación?}
    CheckModPerm -->|No| DenyMod[No autorizado para<br/>solicitar modificaciones]
    DenyMod --> Dashboard
    CheckModPerm -->|Sí| GetSystems[Cargar Sistemas Autorizados<br/>para área del usuario]
    GetSystems --> SelSys[Seleccionar Sistema<br/>de lista filtrada]
    SelSys --> FormMod[Llenar Formulario B:<br/>- Sistema a modificar<br/>- Tipo cambio<br/>- Descripción cambio<br/>- Razón<br/>- Impacto estimado]
    FormMod --> ReviewMod{Revisión ISSEG}
    ReviewMod -->|Rechazado| RejectMod[Notificar rechazo]
    RejectMod --> Dashboard
    ReviewMod -->|No clara| ClarifyMod[Solicitar aclaración]
    ClarifyMod --> FormMod
    ReviewMod -->|Aprobado| AssignModDev[Asignar Desarrollador<br/>Encargado del Sistema]
    AssignModDev --> CreateModTicket[Crear Ticket de Modificación]
    CreateModTicket --> RegisterMod[REGISTRAR MODIFICACIÓN en BD:<br/>Tabla: Historial_Cambios<br/>- ID_Sistema<br/>- Número_Versión++<br/>- Descripción_Cambio<br/>- Usuario_Responsable<br/>- Fecha_Cambio<br/>- Estado = En Desarrollo<br/>- Tiempo_Inicio]
    RegisterMod --> RegisterModAudit[REGISTRAR AUDITORÍA:<br/>Tabla: Audit_Modificaciones<br/>- Qué cambió<br/>- Quién lo cambió<br/>- Cuándo<br/>- Impacto real vs estimado]
    RegisterModAudit --> EndMod([Fin - Modificación Iniciada])

    %% OPCIÓN 3: Reportar Problema / Incidencia
    Action -->|Reportar Problema| CheckIssuePerm{¿Permiso de<br/>reportar problema?}
    CheckIssuePerm -->|No| DenyIssue[No autorizado para<br/>reportar problemas]
    DenyIssue --> Dashboard
    CheckIssuePerm -->|Sí| GetSysIssue[Cargar Sistemas Autorizados<br/>para área del usuario]
    GetSysIssue --> SelSysIssue[Seleccionar Sistema<br/>con problema]
    SelSysIssue --> FormIssue[Llenar Formulario Problema:<br/>- Sistema afectado<br/>- Descripción problema<br/>- Urgencia: Crítica/Alta/Media/Baja<br/>- Módulo afectado<br/>- Usuarios impactados<br/>- Pasos para reproducir]
    FormIssue --> DefSLA[Definir SLA según Urgencia:<br/>Crítica: 1 hora<br/>Alta: 4 horas<br/>Media: 8 horas<br/>Baja: 24 horas]
    DefSLA --> ReviewIssue{Revisión ISSEG}
    ReviewIssue -->|Rechazado| RejectIssue[Notificar rechazo<br/>Guardar motivo]
    RejectIssue --> Dashboard
    ReviewIssue -->|Aprobado| AssignIssue[Asignar Responsable<br/>según urgencia]
    AssignIssue --> StartSLA[Iniciar Reloj de SLA]
    StartSLA --> RegisterIssue[REGISTRAR INCIDENCIA en BD:<br/>Tabla: Problemas_Reportados<br/>- ID_Incidencia<br/>- ID_Sistema<br/>- Usuario_Reportante<br/>- Urgencia<br/>- Descripción<br/>- Estado = Abierto<br/>- Fecha_Reporte<br/>- Tiempo_Respuesta_SLA<br/>- Responsable_Asignado]
    RegisterIssue --> RegisterIssueTiempo[REGISTRAR TIEMPO:<br/>Tabla: Control_Incidencias<br/>- Fecha_Inicio<br/>- Tiempo_Respuesta: 0<br/>- Tiempo_Resolución: 0<br/>- Estado_Actual = Abierto]
    RegisterIssueTiempo --> EndIssue([Fin - Problema Registrado])

    %% OPCIÓN 4: Ver Solicitudes
    Action -->|Ver Mis Solicitudes| ViewTickets[Dashboard Detallado:<br/>- Nuevos Sistemas (estado)<br/>- Modificaciones (versión actual)<br/>- Problemas (tiempo transcurrido)]
    ViewTickets --> Dashboard

    %% OPCIÓN 5: Cerrar Sesión
    Action -->|Cerrar Sesión| SaveSession[Guardar estado sesión]
    SaveSession --> Logout([Fin - Sesión Cerrada])

    style Start fill:#90EE90,stroke:#228B22,stroke-width:3px
    style EndNewSys fill:#87CEEB,stroke:#00008B,stroke-width:2px
    style EndMod fill:#87CEEB,stroke:#00008B,stroke-width:2px
    style EndIssue fill:#87CEEB,stroke:#00008B,stroke-width:2px
    style RegisterNewSys fill:#FFB6C1,stroke:#8B008B,stroke-width:2px
    style RegisterMod fill:#FFB6C1,stroke:#8B008B,stroke-width:2px
    style RegisterIssue fill:#FFB6C1,stroke:#8B008B,stroke-width:2px
    style Dashboard fill:#FFFFE0,stroke:#DAA520,stroke-width:2px
```

---

## Diagramas Complementarios

### Nota Importante
El **Mapa Único Integral (Sección 0)** es el diagrama principal que contiene el flujo completo desde el login hasta todas las acciones. Las siguientes secciones son diagramas complementarios que detallan partes específicas del flujo.

## Leyenda y Descripción de Procesos

### Componentes del Sistema de Control de Acceso

#### 1. Autenticación y Autorización
- **Login**: Validación de credenciales de usuario
- **Control de Área**: Verificación de permisos según área asignada
- **Validación de Rol**: Confirmación de permisos específicos (crear nuevo/modificar)

#### 2. Estructura de Control de Usuarios
```
USUARIOS (Tabla Base)
    ↓
USUARIOS_AUTORIZADOS_ÁREA (Asignación por Área)
    ↓
PERMISOS (Crear Sistema Nuevo / Modificar Existente)
    ↓
SISTEMAS_AUTORIZADOS_POR_ÁREA (Sistemas Visibles)
```

#### 3. Filtrado de Sistemas
Cada usuario ve **solo** los sistemas para los cuales su área tiene autorización:
- Usuario de Área RRHH → Ve solo sistemas de RRHH
- Usuario de Área Finanzas → Ve solo sistemas de Finanzas
- Usuario de Área TI → Acceso a múltiples sistemas (si está autorizado)

#### 4. Niveles de Permisos
| Permiso | Descripción | Control |
|---------|-------------|---------|
| **Crear Sistema Nuevo** | Permite solicitar creación de nuevo sistema | Campo: `Puede_Solicitar_Nuevo` |
| **Solicitar Modificación** | Permite pedir cambios en sistemas existentes | Campo: `Puede_Solicitar_Modificación` |
| **Ver Sistema** | Acceso a información y estado del sistema | Tabla: `Sistemas_Autorizados_Por_Área` |
| **Consulta Solo Lectura** | Usuario bloqueado puede ver pero no actuar | Acceso limitado a dashboards |

---

### Tipos de Formularios
- **Formulario A**: Solicitud de Sistema Nuevo (justificación, alcance, beneficios)
- **Formulario B**: Cuestionario de Modificación (cambios requeridos, impacto, urgencia)
- **Formulario C**: Requerimientos Detallados (especificaciones técnicas completas)

### Roles del Sistema
- **ISSEG**: Revisa, aprueba/rechaza solicitudes, asigna prioridades
- **Desarrollador**: Ejecuta desarrollo y mantenimiento
- **Product Manager**: Coordina requerimientos y seguimiento de proyecto
- **Usuario de Área**: Solicita nuevos sistemas o modificaciones (con permisos)

### Puntos de Control Críticos
1. **Autenticación**: Login con validación de credenciales
2. **Autorización de Área**: Verificación de usuario en tabla `Usuarios_Autorizados_Área`
3. **Validación de Permisos**: Confirmar `Puede_Solicitar_Nuevo` o `Puede_Solicitar_Modificación`
4. **Filtrado de Sistemas**: Mostrar solo sistemas autorizados para el área
5. **Revisión ISSEG**: Aprobación/rechazo de solicitudes
6. **Asignación de Recursos**: Designación de equipo de desarrollo
7. **Registro en BD**: Trazabilidad completa de cambios

---

## Queries SQL para Control de Acceso

### Validar si usuario puede solicitar

### Obtener sistemas visibles para un usuario

### Registrar intento de acceso no autorizado

Se registra el intento de acceso no autorizado con:
- ID de usuario
- Timestamp
- Tipo de intento
- IP de origen
- Motivo de denegación
- Acción tomada (ACCESO DENEGADO - REGISTRADO)
```
