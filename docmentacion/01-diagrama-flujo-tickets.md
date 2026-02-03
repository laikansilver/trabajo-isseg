# Sistema de Gestión de Tickets de Desarrollo - Diagrama de Flujo

## 1. Diagrama de Autenticación y Control de Acceso

```mermaid
flowchart TD
    Start([Inicio - Usuario Accede al Sistema]) --> Login[Pantalla de Login]
    Login --> Auth{¿Credenciales Válidas?}
    
    Auth -->|No Válidas| AuthFail[Mostrar Error:<br/>Usuario/Contraseña Incorrectos]
    AuthFail --> Login
    
    Auth -->|Válidas| LoadProfile[Cargar Perfil de Usuario:<br/>- Nombre<br/>- Rol<br/>- Área<br/>- Permisos]
    LoadProfile --> CheckRole{¿Usuario<br/>Autorizado<br/>para Solicitar?}
    
    CheckRole -->|No Autorizado| DenyAccess[Mostrar Mensaje:<br/>No tiene permisos<br/>para crear solicitudes]
    DenyAccess --> ViewOnly[Acceso Solo Lectura:<br/>Consultar estado de<br/>solicitudes existentes]
    ViewOnly --> End1([Fin - Sesión Limitada])
    
    CheckRole -->|Autorizado| LoadSystems[Cargar Sistemas Autorizados<br/>según Área del Usuario]
    LoadSystems --> Dashboard[Dashboard Principal]
    Dashboard --> MainMenu{Seleccionar Acción}
    
    MainMenu -->|Ver Solicitudes| ViewTickets[Listar mis solicitudes]
    MainMenu -->|Nueva Solicitud| Choice[¿Tipo de Solicitud?]
    MainMenu -->|Cerrar Sesión| Logout([Fin - Sesión Cerrada])
    
    ViewTickets --> Dashboard
    
```

---

## 2. Diagrama de Validación de Permisos de Área

```mermaid
flowchart TD
    LoadProfile[Usuario Autenticado:<br/>ID_Usuario, Área, Rol] --> QueryPerms[Consultar Tabla:<br/>Usuarios_Autorizados_Área]
    
    QueryPerms --> CheckPerm{¿Usuario está<br/>en lista de<br/>autorizados?}
    
    CheckPerm -->|No| ReturnDeny[Retornar: ACCESO DENEGADO]
    ReturnDeny --> LogEvent1[Registrar Intento<br/>de Acceso No Autorizado]
    LogEvent1 --> NotifyAdmin[Notificar a Admin<br/>intento sospechoso]
    
    CheckPerm -->|Sí| ValidatActive{¿Usuario está<br/>Activo?}
    
    ValidatActive -->|No| ReturnInactive[Retornar: CUENTA INACTIVA]
    ReturnInactive --> LogEvent2[Registrar intento<br/>con cuenta inactiva]
    
    ValidatActive -->|Sí| LoadAuth[Cargar Permisos:<br/>- Crear Solicitud Nueva<br/>- Modificar Existente<br/>- Ver Sistemas]
    LoadAuth --> FilterSystems[Obtener lista de<br/>Sistemas visibles<br/>para su Área]
    FilterSystems --> ReturnGrant[Retornar: ACCESO PERMITIDO<br/>+ Lista de Sistemas]
    
```

---

## 3. Diagrama de Proceso Principal con Control de Acceso

```mermaid
flowchart TD
    Start([Inicio - Usuario Ingresa al Sistema]) --> Login[Login/Autenticación]
    Login --> ValidateAccess{Validar Acceso<br/>y Permisos}
    
    ValidateAccess -->|Acceso Denegado| DenyMsg[Mostrar:<br/>No autorizado para solicitar]
    DenyMsg --> ViewOnly[Modo Consulta<br/>Solo Lectura]
    ViewOnly --> EndDeny([Fin])
    
    ValidateAccess -->|Acceso Permitido| Choice{Seleccionar Tipo<br/>de Solicitud}
    
    Choice -->|Creación de Sistema Nuevo| CheckNewPerm{¿Area permite<br/>sistemas nuevos?}
    CheckNewPerm -->|No| DenyNew[Mostrar:<br/>Su área no puede<br/>crear sistemas nuevos]
    DenyNew --> ViewOnly
    
    CheckNewPerm -->|Sí| FormNew[Llenar Formulario A:<br/>Solicitud de Sistema Nuevo]
    
    Choice -->|Modificación de Sistema Existente| CheckModPerm{¿Area permite<br/>modificaciones?}
    CheckModPerm -->|No| DenyMod[Mostrar:<br/>Su área no puede<br/>solicitar modificaciones]
    DenyMod --> ViewOnly
    
    CheckModPerm -->|Sí| GetSystems[Cargar Sistemas<br/>disponibles para su Área]
    GetSystems --> IdentSys[Seleccionar Sistema<br/>de lista filtrada]
    
    IdentSys --> FormMod[Llenar Formulario B:<br/>Cuestionario de Modificación]
    
    %% Flujo Sistema Nuevo
    FormNew --> ReviewNew{Revisión ISSEG}
    ReviewNew -->|Rechazado| RejectNew[Notificar Rechazo<br/>Registrar Motivo]
    RejectNew --> EndReject([Fin - Solicitud Rechazada])
    
    ReviewNew -->|Aprobado| AssignTeam[Asignar Recursos:<br/>- Desarrollador<br/>- Product Manager]
    AssignTeam --> RequestReq[Solicitar Formulario C:<br/>Requerimientos Detallados]
    RequestReq --> FillReq[Usuario completa<br/>Formulario C]
    FillReq --> ValidateReq{Validar Requerimientos}
    ValidateReq -->|Incompleto/Confuso| ClarifyReq[Solicitar Aclaración]
    ClarifyReq --> FillReq
    ValidateReq -->|Completo| StartDev[Iniciar Desarrollo<br/>Crear Ticket en Sistema]
    StartDev --> RegisterNew[Registrar en BD:<br/>- Proyecto Nuevo<br/>- Equipo Asignado<br/>- Timeline]
    RegisterNew --> EndSuccess([Fin - Proyecto Iniciado])
    
    %% Flujo Modificación
    FormMod --> ReviewMod{Revisión ISSEG}
    ReviewMod -->|Rechazado| RejectMod[Notificar Rechazo<br/>Registrar Motivo]
    RejectMod --> EndRejectMod([Fin - Modificación Rechazada])
    
    ReviewMod -->|Información No Clara| Clarify[Solicitar Aclaración<br/>Adicional]
    Clarify --> FormMod
    
    ReviewMod -->|Aprobado| AssignDev[Asignar al Desarrollador<br/>Encargado del Sistema]
    AssignDev --> CreateModTicket[Crear Ticket de Modificación]
    CreateModTicket --> RegisterMod[Registrar en BD:<br/>- Historial de Cambios<br/>- Impacto Estimado<br/>- Desarrollador Asignado]
    RegisterMod --> EndSuccessMod([Fin - Modificación Iniciada])
    
```

---

## 4. Diagrama de Filtrado de Sistemas por Área

```mermaid
flowchart LR
    subgraph Base["Base de Datos"]
        AllSystems[Todos los Sistemas<br/>en Operación]
        UserAreas[Usuario Autenticado<br/>Área_ID]
    end
    
    subgraph Filter["Proceso de Filtrado"]
        Q1{¿Sistema<br/>en Producción?}
        Q2{¿Area del Usuario<br/>puede modificar<br/>este sistema?}
        Q3{¿Sistema no está<br/>descontinuado?}
    end
    
    subgraph Result["Resultado"]
        Allowed[✓ Sistemas Visibles<br/>para el Usuario]
        Denied[✗ Sistemas Ocultos]
    end
    
    AllSystems --> Q1
    UserAreas --> Q2
    Q1 -->|No| Denied
    Q1 -->|Sí| Q3
    Q3 -->|No| Denied
    Q3 -->|Sí| Q2
    Q2 -->|No| Denied
    Q2 -->|Sí| Allowed
    
```

---

## 5. Diagrama de Estructura de Control de Usuarios

```mermaid
graph TD
    subgraph Usuarios["Tabla: Usuarios"]
        U1["ID_Usuario<br/>Email<br/>Nombre Completo<br/>Contraseña Hash<br/>Estado Activo/Inactivo"]
    end
    
    subgraph UsuariosArea["Tabla: Usuarios_Autorizados_Área"]
        UA1["ID_Autorización<br/>ID_Usuario FK<br/>ID_Área FK<br/>Rol_En_Área<br/>Fecha_Asignación<br/>Puede_Solicitar_Nuevo<br/>Puede_Solicitar_Modificación<br/>Activo"]
    end
    
    subgraph Áreas["Tabla: Áreas"]
        A1["ID_Área<br/>Nombre_Área<br/>Descripción<br/>Responsable<br/>Max_Usuarios_Autorizados"]
    end
    
    subgraph SistemasXÁrea["Tabla: Sistemas_Autorizados_Por_Área"]
        SA1["ID_Asociación<br/>ID_Sistema FK<br/>ID_Área FK<br/>Puede_Solicitar_Modificación<br/>Puede_Crear_Nuevo_Sistema<br/>Fecha_Autorización"]
    end
    
    U1 --> UsuariosArea
    UsuariosArea --> Áreas
    Áreas --> SistemasXÁrea
    
```

---

## 6. Tabla de Permisos por Rol y Área

```mermaid
flowchart TD
    A["Validación de Permisos:<br/>ID_Usuario + ID_Área"]
    
    A --> B["Buscar en Tabla:<br/>Usuarios_Autorizados_Área"]
    
    B --> C{¿Existe Registro?}
    
    C -->|No| D["ACCESO DENEGADO<br/>Usuario no autorizado<br/>en esta área"]
    D --> D1["Registrar Intento<br/>No Autorizado en Log"]
    
    C -->|Sí| E["Verificar Campos<br/>de Permisos"]
    E --> E1{¿Puede_Solicitar<br/>Nuevo?}
    E1 -->|Sí| F1["✓ Permitir Crear<br/>Sistema Nuevo"]
    E1 -->|No| F2["✗ Bloquear Crear<br/>Sistema Nuevo"]
    
    E --> E2{¿Puede_Solicitar<br/>Modificación?}
    E2 -->|Sí| G1["✓ Permitir Solicitar<br/>Modificación"]
    E2 -->|No| G2["✗ Bloquear Solicitar<br/>Modificación"]
    
    F1 --> H["Mostrar UI<br/>según Permisos"]
    F2 --> H
    G1 --> H
    G2 --> H
        
```

---

## Diagrama de Control y Registro en Base de Datos

```mermaid
flowchart LR
    subgraph Sistema["Sistema de Gestión"]
        Tickets[Tickets Activos]
        Projects[Proyectos]
        Teams[Equipos y Roles]
    end
    
    subgraph BD["Base de Datos - Control"]
        Hierarchy[Jerarquías<br/>- Áreas<br/>- Responsables<br/>- Prioridades]
        Collaborators[Colaboradores<br/>- Desarrolladores<br/>- Product Managers<br/>- ISSEG]
        Uptime[Uptime/Disponibilidad<br/>- Tiempo de actividad<br/>- SLA<br/>- Incidentes]
        Changes[Historial de Cambios<br/>- Versiones<br/>- Modificaciones<br/>- Responsables]
        Failures[Registro de Fallas<br/>- Incidentes<br/>- Tiempo de resolución<br/>- Impacto]
        Users[Control de Usuarios<br/>- Áreas Autorizadas<br/>- Permisos<br/>- Sistemas Visibles]
    end
    
    Tickets --> Hierarchy
    Tickets --> Collaborators
    Tickets --> Users
    Projects --> Uptime
    Projects --> Changes
    Projects --> Failures
    Teams --> Collaborators
    Teams --> Users
    
```

---

## Diagrama de Estados del Ticket

```mermaid
stateDiagram-v2
    [*] --> Solicitado: Nueva Solicitud
    Solicitado --> EnRevisión: Formulario Completo
    EnRevisión --> Rechazado: No Aprobado
    EnRevisión --> Aprobado: Aprobado ISSEG
    EnRevisión --> AclaraciónRequerida: Info Incompleta
    
    AclaraciónRequerida --> EnRevisión: Info Actualizada
    
    Aprobado --> AsignaciónPendiente: Asignar Recursos
    AsignaciónPendiente --> Asignado: Equipo Asignado
    Asignado --> EnDesarrollo: Desarrollo Iniciado
    EnDesarrollo --> EnPruebas: Desarrollo Completado
    EnPruebas --> EnDesarrollo: Correcciones Necesarias
    EnPruebas --> Implementado: Pruebas Exitosas
    Implementado --> Cerrado: Despliegue Exitoso
    Implementado --> EnMantenimiento: Sistema en Producción
    EnMantenimiento --> [*]: Sistema Descontinuado
    
    Rechazado --> [*]
    Cerrado --> [*]
```

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

```sql
SELECT 
    u.ID_Usuario,
    u.Nombre,
    ua.ID_Área,
    a.Nombre_Área,
    ua.Puede_Solicitar_Nuevo,
    ua.Puede_Solicitar_Modificación,
    ua.Activo
FROM Usuarios u
JOIN Usuarios_Autorizados_Área ua ON u.ID_Usuario = ua.ID_Usuario
JOIN Áreas a ON ua.ID_Área = a.ID_Área
WHERE u.ID_Usuario = @ID_Usuario AND ua.Activo = 1;
```

### Obtener sistemas visibles para un usuario

```sql
SELECT DISTINCT
    s.ID_Sistema,
    s.Nombre_Sistema,
    s.Tipo_Sistema,
    s.Estado_Actual,
    saa.Puede_Solicitar_Modificación
FROM Sistemas s
JOIN Sistemas_Autorizados_Por_Área saa ON s.ID_Sistema = saa.ID_Sistema
JOIN Usuarios_Autorizados_Área ua ON saa.ID_Área = ua.ID_Área
WHERE ua.ID_Usuario = @ID_Usuario
  AND ua.Activo = 1
  AND saa.Activo = 1
  AND s.Estado_Actual IN ('Producción', 'Mantenimiento')
ORDER BY s.Nombre_Sistema;
```

### Registrar intento de acceso no autorizado

```sql
INSERT INTO Audit_Acceso_No_Autorizado (
    ID_Usuario,
    Timestamp,
    Tipo_Intento,
    IP_Origen,
    Motivo_Denegación,
    Acción_Tomada
)
VALUES (
    @ID_Usuario,
    NOW(),
    'SOLICITUD_FORMULARIO',
    @IP,
    'Usuario no autorizado en área solicitante',
    'ACCESO DENEGADO - REGISTRADO'
);
```
