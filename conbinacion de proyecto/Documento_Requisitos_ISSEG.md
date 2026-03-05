# Documento de Requisitos del Software (SRS)
## Sistema de Gestión de Solicitudes ISSEG

### 1. Historial de Versiones
| Fecha | Versión | Descripción | Autor |
|-------|---------|-------------|-------|
| 05/03/2026 | 1.0 | Versión inicial del documento base | Equipo de Desarrollo |

### 2. Introducción

#### 2.1 Propósito
El propósito de este documento es definir los requisitos funcionales y no funcionales para el "Sistema de Gestión de Solicitudes ISSEG". Este sistema tiene como objetivo centralizar, estandarizar y automatizar la gestión de solicitudes de desarrollo de software, modificaciones a sistemas existentes y reporte de incidencias dentro del Instituto de Seguridad Social del Estado de Guanajuato (ISSEG).

#### 2.2 Alcance
El sistema abarcará los procesos de:
*   Solicitud de nuevos sistemas de información (Formulario A).
*   Solicitud de modificaciones a sistemas existentes (Formulario B).
*   Levantamiento detallado de requerimientos técnicos (Formulario C).
*   Reporte y seguimiento de problemas e incidencias.
*   Gestión de usuarios, roles y permisos por área.
*   Tableros de control (Dashboards) para seguimiento de estatus y SLAs.

#### 2.3 Definiciones, Acrónimos y Abreviaturas
*   **ISSEG**: Instituto de Seguridad Social del Estado de Guanajuato.
*   **SLA**: Service Level Agreement (Acuerdo de Nivel de Servicio).
*   **RBAC**: Role-Based Access Control (Control de Acceso Basado en Roles).
*   **PM**: Product Manager.
*   **Formulario A**: Solicitud de Sistema Nuevo.
*   **Formulario B**: Solicitud de Modificación.
*   **Formulario C**: Requerimientos Técnicos.

#### 2.4 Resumen del Documento
Este documento describe las características generales del sistema, los requisitos específicos de las interfaces, las funciones del producto, las restricciones de diseño y los atributos de calidad.

### 3. Descripción General

#### 3.1 Funcionalidad del Producto
El sistema funciona como una plataforma web centralizada donde los usuarios de diferentes áreas del ISSEG pueden gestionar el ciclo de vida de sus necesidades tecnológicas.
*   **Gestión de Identidad**: Autenticación segura y control de acceso granular.
*   **Gestión de Solicitudes**: Flujos de trabajo automatizados para aprobación y seguimiento.
*   **Inventario de Sistemas**: Catálogo de sistemas permitidos por área.
*   **Auditoría**: Registro detallado de todas las acciones realizadas.

#### 3.2 Restricciones y Suposiciones
*   El sistema debe ser accesible vía navegador web moderno.
*   La autenticación debe integrarse con los protocolos de seguridad de la institución.
*   Los usuarios solo pueden ver información pertinente a su área asignada.

### 4. Requisitos Específicos

#### 4.1 Requisitos de Interfaces
*   **Interfaz de Usuario (UI)**: Diseño limpio, intuitivo y responsivo (adaptable a diferentes tamaños de pantalla). Uso de colores institucionales.
*   **Interfaz de Hardware**: No requiere hardware específico del lado del cliente más allá de una estación de trabajo o dispositivo móvil con navegador.
*   **Interfaz de Comunicación**: Uso de protocolo HTTPS para todas las comunicaciones.

#### 4.2 Requisitos Funcionales

**RF-01: Gestión de Usuarios y Acceso**
*   El sistema debe permitir el inicio de sesión mediante credenciales (Email/Password).
*   El sistema debe asignar permisos basados en el rol del usuario y su área.
*   El sistema debe bloquear el acceso tras múltiples intentos fallidos.

**RF-02: Solicitud de Sistema Nuevo (Formulario A)**
*   Permitir a usuarios autorizados ("Responsables") solicitar un nuevo sistema.
*   Capturar justificación, alcance preliminar y beneficios esperados.
*   Generar un ID único (SN-YYYY-NNNN) automático.

**RF-03: Solicitud de Modificaciones (Formulario B)**
*   Permitir seleccionar un sistema existente del inventario del área.
*   Capturar detalle del cambio, justificación e impacto.
*   Generar un ID único (MOD-YYYY-NNNN).

**RF-04: Levantamiento de Requerimientos (Formulario C)**
*   Habilitado tras la aprobación de un sistema nuevo.
*   Permitir detallar objetivos, actores, casos de uso y requerimientos técnicos.

**RF-05: Gestión de Incidencias**
*   Permitir reportar fallos en sistemas productivos.
*   Clasificar urgencia (Crítica, Alta, Media, Baja) y asignar SLA automáticamente.
*   Permitir adjuntar evidencia (capturas, logs).

**RF-06: Dashboard y Seguimiento**
*   Mostrar al usuario el estado de sus solicitudes en tiempo real.
*   Permitir a los administradores visualizar métricas globales.

#### 4.3 Requisitos No Funcionales

##### 4.3.1 Seguridad
*   Las contraseñas deben almacenarse en formato hash.
*   Todas las sesiones deben expirar tras un periodo de inactividad.
*   Se debe mantener un log de auditoría inmutable de todas las transacciones críticas.

##### 4.3.2 Disponibilidad
*   El sistema debe estar disponible 99.9% del tiempo operativo.
*   Debe soportar concurrencia de usuarios sin degradación perceptible del servicio.

##### 4.3.3 Mantenibilidad
*   Arquitectura modular para facilitar actualizaciones futuras.
*   Código documentado y versionado.

##### 4.3.4 Portabilidad
*   Compatible con los navegadores más utilizados: Chrome, Firefox, Edge, Safari.
*   Diseño adaptable a resoluciones de escritorio y tabletas.
