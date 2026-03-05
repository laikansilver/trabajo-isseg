# Especificación de Requisitos de Software (ERS)
## Sistema de Gestión de Solicitudes ISSEG

**Versión:** 1.0  
**Fecha:** 5 de marzo de 2026  
**Estándar:** Basado en IEEE 830-1998  

---

### 1. Introducción

#### 1.1 Propósito
El propósito de este documento es definir de manera formal y detallada los requisitos funcionales y no funcionales para el "Sistema de Gestión de Solicitudes ISSEG". Este documento servirá como base contractual y guía técnica para el desarrollo, pruebas y validación del software.

#### 1.2 Alcance
El sistema "Gestión de Solicitudes ISSEG" es una plataforma web que permitirá:
-   Digitalizar el proceso de solicitud de nuevos desarrollos (Formulario A).
-   Gestionar el ciclo de vida de mantenimiento de software (Formulario B).
-   Formalizar el levantamiento de requerimientos técnicos (Formulario C).
-   Monitorear y atender incidencias con niveles de servicio (SLA) definidos.
-   Administrar el inventario de aplicaciones y los permisos de acceso por área.

#### 1.3 Definiciones, Acrónimos y Abreviaturas
| Término | Definición |
|---|---|
| **ISSEG** | Instituto de Seguridad Social del Estado de Guanajuato. |
| **ERS / SRS** | Especificación de Requisitos de Software. |
| **SLA** | Service Level Agreement (Acuerdo de Nivel de Servicio). |
| **Rol** | Conjunto de permisos asignados a un usuario (ej. Solicitante, Revisor). |
| **Stakeholder** | Interesado o parte involucrada en el proyecto. |

#### 1.4 Referencias
-   Propuesta Integrada del Sistema ISSEG (V3.0).
-   Diagramas de Flujo de Procesos (01-diagrama-flujo-tickets.md).
-   Estructura de Base de Datos (11-diagrama-er-tablas.md).

---

### 2. Descripción General

#### 2.1 Perspectiva del Producto
El sistema es una solución independiente que reemplazará la gestión manual (correo/papel). Se integrará coexístentemente con la infraestructura de red del ISSEG y su sistema de autenticación (LDAP/Active Directory si aplica, o gestión local).

#### 2.2 Funciones del Producto (Resumen)
1.  **Módulo de Seguridad:** Login, Logout, Recuperación de contraseña, Control de Sesiones.
2.  **Módulo de Solicitudes:** Creación, edición y visualización de Formularios A, B y C.
3.  **Módulo de Incidencias:** Reporte de fallos, cálculo automático de SLA, asignación de técnicos.
4.  **Módulo de Administración:** Gestión de catálogos (Usuarios, Áreas, Sistemas, Roles).
5.  **Módulo de Reportes:** Dashboards de cumplimiento y métricas de desempeño.

#### 2.3 Características de los Usuarios
| Tipo de Usuario | Nivel Técnico | Responsabilidades |
|---|---|---|
| **Administrador TI** | Alto | Configuración del sistema, gestión de catálogos y usuarios. |
| **Gestor/Revisor** | Medio | Revisión y aprobación de solicitudes. Asignación de recursos. |
| **Solicitante (Área)** | Bajo/Medio | Creación de solicitudes y reporte de incidencias. |
| **Desarrollador** | Alto | Atención de tickets y actualización de estatus técnico. |

#### 2.4 Restricciones generales
-   **Normativa:** Cumplimiento con las políticas de seguridad de la información del ISSEG.
-   **Tecnología:** Backend compatible con servidor institucional (ej. .NET/Java/Python), Base de datos relacional (SQL).
-   **Navegadores:** Soporte para Chrome (v90+), Edge y Firefox.

---

### 3. Requisitos Específicos

#### 3.1 Requisitos de Interfaces Externas

**3.1.1 Interfaces de Usuario**
-   Diseño *Responsive* (adaptable a escritorio y móviles).
-   Uso de paleta de colores institucional.
-   Feedback visual inmediato (mensajes de éxito/error).

**3.1.2 Interfaces de Hardware**
-   No se requiere hardware especial. Funciona en estaciones de trabajo estándar.

**3.1.3 Interfaces de Software**
-   Sistema Operativo Servidor: Windows Server / Linux.
-   Motor de Base de Datos: SQL Server / PostgreSQL / MySQL.

#### 3.2 Requisitos Funcionales

##### 3.2.1 Gestión de Identidad y Acceso
-   **RF-01:** El sistema debe permitir el inicio de sesión mediante correo electrónico y contraseña encriptada.
-   **RF-02:** El sistema debe bloquear la cuenta tras 3 intentos fallidos consecutivos (Seguridad).
-   **RF-03:** El sistema debe permitir cerrar la sesión, invalidando el token de acceso.

##### 3.2.2 Gestión de Solicitudes (Formulario A - Nuevo Sistema)
-   **RF-04:** El sistema debe permitir a usuarios con rol "Responsable de Área" crear una solicitud de "Nuevo Sistema".
-   **RF-05:** El sistema debe validar que la "Justificación" tenga una longitud mínima de 50 caracteres.
-   **RF-06:** El sistema debe generar automáticamente un folio con formato `SN-YYYY-NNNN`.
-   **RF-07:** El sistema debe notificar por correo al Revisor ISSEG cuando se crea una nueva solicitud.

##### 3.2.3 Gestión de Modificaciones (Formulario B - Mantenimiento)
-   **RF-08:** El sistema debe permitir seleccionar únicamente los sistemas asignados al área del usuario solicitante.
-   **RF-09:** El sistema debe registrar la versión actual del sistema antes de aplicar la modificación.
-   **RF-10:** El usuario debe clasificar el impacto de la modificación (Crítico, Alto, Medio, Bajo).

##### 3.2.4 Reporte de Incidencias (Soporte)
-   **RF-11:** El sistema debe permitir reportar incidencias asociadas a un módulo específico.
-   **RF-12:** El sistema debe calcular automáticamente la fecha límite de atención (SLA) basada en la urgencia seleccionada:
    -   Crítica: 1 hora.
    -   Alta: 4 horas.
    -   Media: 8 horas.
    -   Baja: 24 horas.
-   **RF-13:** El sistema debe permitir adjuntar evidencias (imágenes/logs) con un límite de 10MB.

##### 3.2.5 Administración
-   **RF-14:** El sistema debe permitir al Administrador dar de alta nuevas Áreas y asignarles un Responsable.
-   **RF-15:** El sistema debe permitir inhabilitar usuarios sin eliminar su historial de acciones.

#### 3.3 Requisitos No Funcionales (Atributos de Calidad)

##### 3.3.1 Rendimiento
-   **RNF-01:** El tiempo de carga de cualquier formulario no debe exceder los 2 segundos en una conexión de 10Mbps.
-   **RNF-02:** El sistema debe soportar al menos 50 usuarios concurrentes sin degradación del servicio.

##### 3.3.2 Seguridad
-   **RNF-03:** Todas las contraseñas deben almacenarse utilizando algoritmos de hash robustos (ej. bcrypt, Argon2).
-   **RNF-04:** La comunicación debe estar cifrada mediante protocolo HTTPS (TLS 1.2 o superior).
-   **RNF-05:** Se debe mantener un log de auditoría inmutable para todas las operaciones de escritura (Crear, Editar, Borrar).

##### 3.3.3 Disponibilidad
-   **RNF-06:** El sistema debe estar disponible el 99.9% del tiempo en horario laboral (Lunes a Viernes, 8:00 - 18:00).

---

### 4. Apéndices

#### 4.1 Reglas de Negocio
-   **RN-01:** Un sistema no puede pasar a "Producción" sin tener el Formulario C (Requerimientos) aprobado.
-   **RN-02:** Solo el "Responsable de Área" puede autorizar solicitudes de presupuesto (Sistemas Nuevos).

#### 4.2 Matriz de Roles y Permisos
(Referencia al archivo: manual de usuario/matriz de permisos)
