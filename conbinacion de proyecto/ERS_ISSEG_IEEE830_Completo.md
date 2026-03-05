# Especificación de Requisitos de Software

**Proyecto:** Sistema de Gestión de Solicitudes ISSEG

**Revisión:** 1.0

**Fecha:** 5 de marzo de 2026

**Autores:**
- Jacqueline Hurtado Hernández
- Edwin Eduardo Mercado Ruiz

---

## Contenido

1. [Introducción](#1-introducción)
   1. [Alcance](#11-alcance)
   2. [Personal involucrado](#12-personal-involucrado)
2. [Descripción general](#2-descripción-general)
   1. [Perspectiva del producto](#21-perspectiva-del-producto)
   2. [Funcionalidad del producto](#22-funcionalidad-del-producto)
   3. [Características de los usuarios](#23-características-de-los-usuarios)
   4. [Restricciones](#24-restricciones)
3. [Requisitos específicos](#3-requisitos-específicos)
   1. [Requisitos comunes de los interfaces](#31-requisitos-comunes-de-los-interfaces)
   2. [Requisitos funcionales](#32-requisitos-funcionales)
   3. [Requisitos no funcionales](#33-requisitos-no-funcionales)
   4. [Otros requisitos](#34-otros-requisitos)
4. [Modelado del Sistema](#4-modelado-del-sistema)

---

# 1. Introducción

La Especificación de Requisitos de Software (ERS) del Sistema de Gestión de Solicitudes ISSEG proporciona una descripción completa, formal y detallada de todos los requisitos funcionales y no funcionales que deberá cumplir el sistema de software a desarrollar para el Instituto de Seguridad Social del Estado de Guanajuato (ISSEG).

Este documento está basado y es conforme con el estándar IEEE Std 830-1998 y servirá como base contractual para el desarrollo, pruebas y validación del sistema.

## 1.1. Alcance

**Identificación del producto:**
Sistema de Gestión de Solicitudes ISSEG (SGS-ISSEG)

**Descripción:**
El Sistema de Gestión de Solicitudes ISSEG es una plataforma web integral diseñada para centralizar, estandarizar y automatizar la gestión completa de solicitudes de desarrollo de software dentro del Instituto de Seguridad Social del Estado de Guanajuato. El sistema abarcará desde la solicitud inicial de nuevos sistemas, pasando por la gestión de modificaciones y mantenimientos, hasta el reporte y seguimiento de incidencias con niveles de servicio (SLA) definidos.

**Entorno afectado:**
- Departamento de Tecnologías de la Información del ISSEG
- Todas las áreas y departamentos del ISSEG que requieran servicios tecnológicos
- Procesos de desarrollo y mantenimiento de software institucional
- Procesos de soporte técnico y atención de incidencias
- Sistemas de auditoría y cumplimiento normativo

**Beneficios esperados:**
- Eliminación de solicitudes ad-hoc por correo electrónico, llamadas telefónicas o comunicaciones informales
- Trazabilidad completa del ciclo de vida de solicitudes y sistemas
- Reducción de tiempos de respuesta mediante SLAs automatizados
- Mejora en la asignación de recursos y priorización de tareas
- Generación automática de métricas e indicadores de desempeño

## 1.2. Personal involucrado

| Nombre | Jacqueline Hurtado Hernández |
|---|---|
| **Rol** | Analista de Sistemas / Co-autor |
| **Categoría profesional** | Ingeniera en Sistemas |
| **Responsabilidades** | Análisis de requisitos, diseño de interfaces, validación de funcionalidades, documentación técnica |
| **Información de contacto** | [Correo institucional del ISSEG] |
| **Aprobación** | _________________ |

| Nombre | Edwin Eduardo Mercado Ruiz |
|---|---|
| **Rol** | Analista de Sistemas / Co-autor |
| **Categoría profesional** | Ingeniero en Sistemas |
| **Responsabilidades** | Análisis de requisitos, diseño de base de datos, modelado de procesos, documentación técnica |
| **Información de contacto** | [Correo institucional del ISSEG] |
| **Aprobación** | _________________ |

| Nombre | [Director de TI - ISSEG] |
|---|---|
| **Rol** | Patrocinador del Proyecto |
| **Categoría profesional** | Director de Tecnologías de la Información |
| **Responsabilidades** | Aprobación de requisitos, validación de alcance, disponibilidad de recursos |
| **Información de contacto** | [Correo institucional] |
| **Aprobación** | _________________ |

---

# 2. Descripción general

## 2.1. Perspectiva del producto

El Sistema de Gestión de Solicitudes ISSEG es un **producto independiente** diseñado específicamente para las necesidades del Instituto de Seguridad Social del Estado de Guanajuato. No forma parte de un sistema mayor existente, sino que constituye una solución nueva que reemplazará los procesos manuales y ad-hoc actualmente utilizados.

El sistema se integrará de manera coexistente con la infraestructura tecnológica institucional del ISSEG, específicamente:
- Sistema de autenticación institucional (LDAP/Active Directory o gestión local)
- Servidor de correo electrónico institucional para notificaciones
- Base de datos corporativa
- Red interna del ISSEG

**Diagrama de contexto:**

```
┌─────────────────────────────────────────────────────────────┐
│          ENTORNO INSTITUCIONAL ISSEG                        │
│                                                              │
│  ┌──────────────┐           ┌────────────────────────┐     │
│  │  Sistema de  │◄─────────►│  SGS-ISSEG             │     │
│  │Autenticación │           │  (Sistema Principal)   │     │
│  └──────────────┘           └────────────────────────┘     │
│                                     ▲                        │
│  ┌──────────────┐                  │                        │
│  │  Servidor    │◄─────────────────┘                        │
│  │  de Correo   │                                           │
│  └──────────────┘                                           │
│                                                              │
│  Usuarios: Solicitantes, Revisores, Administradores         │
└─────────────────────────────────────────────────────────────┘
```

## 2.2. Funcionalidad del producto

El Sistema de Gestión de Solicitudes ISSEG proporcionará las siguientes funcionalidades principales:

**1. Módulo de Autenticación y Control de Acceso**
- Inicio y cierre de sesión seguro
- Gestión de usuarios, roles y permisos granulares por área
- Control de acceso basado en roles (RBAC)
- Auditoría de accesos y actividades

**2. Módulo de Gestión de Solicitudes de Sistemas Nuevos (Formulario A)**
- Captura estructurada de solicitudes de nuevos desarrollos
- Justificación de negocio y análisis de beneficios
- Flujo de aprobación y revisión por ISSEG
- Asignación automática de recursos (PM, Desarrolladores, Arquitectos)
- Generación automática de folio único (SN-YYYY-NNNN)

**3. Módulo de Gestión de Modificaciones (Formulario B)**
- Selección de sistemas existentes autorizados por área
- Clasificación de tipos de cambio (Nueva funcionalidad, Corrección, Mejora, etc.)
- Análisis de impacto y urgencia
- Control de versiones de sistemas
- Seguimiento de historial de cambios

**4. Módulo de Levantamiento de Requerimientos (Formulario C)**
- Captura detallada de objetivos y alcance técnico
- Definición de actores y roles del sistema
- Especificación de módulos funcionales
- Documentación de requisitos funcionales y no funcionales
- Vinculación con solicitud aprobada (Formulario A)

**5. Módulo de Gestión de Incidencias y Problemas**
- Reporte estructurado de fallos y errores
- Clasificación automática de urgencia (Crítica, Alta, Media, Baja)
- Cálculo y seguimiento automático de SLA
- Adjuntos de evidencias (capturas, logs)
- Asignación inteligente de técnicos según urgencia

**6. Módulo de Dashboard y Reportes**
- Visualización en tiempo real del estado de solicitudes
- Métricas de cumplimiento de SLA
- Indicadores de desempeño del área de TI
- Inventario de sistemas por área
- Estadísticas de incidencias y tiempos de resolución

**7. Módulo de Administración**
- Gestión de catálogos (Áreas, Sistemas, Usuarios, Roles)
- Configuración de permisos y accesos
- Definición de SLAs por tipo de urgencia
- Gestión de notificaciones

**Casos de Uso Principales:**
Los casos de uso se encuentran documentados en los archivos complementarios de este proyecto (ver Referencias: 01-diagrama-flujo-tickets.md, 12-flujos-integrados-completos.md).

## 2.3. Características de los usuarios

El sistema será utilizado por cuatro perfiles principales de usuarios:

| **Tipo de usuario** | Administrador de Sistema (TI) |
|---|---|
| **Formación** | Ingeniería en Sistemas, Computación o afín |
| **Habilidades** | Gestión de bases de datos, administración de sistemas, conocimientos avanzados en TI |
| **Actividades** | Configuración del sistema, gestión de catálogos, usuarios y permisos, monitoreo general |

| **Tipo de usuario** | Gestor/Revisor ISSEG |
|---|---|
| **Formación** | Ingeniería o experiencia en gestión de proyectos |
| **Habilidades** | Análisis de viabilidad técnica, gestión de recursos, toma de decisiones |
| **Actividades** | Revisión y aprobación de solicitudes, asignación de equipos de desarrollo, supervisión de SLAs |

| **Tipo de usuario** | Solicitante/Responsable de Área |
|---|---|
| **Formación** | Variable (profesionales de diferentes áreas del ISSEG) |
| **Habilidades** | Conocimientos básicos de informática, uso de navegadores web |
| **Actividades** | Creación de solicitudes (Formularios A y B), reporte de incidencias, seguimiento de estatus |

| **Tipo de usuario** | Desarrollador/Técnico |
|---|---|
| **Formación** | Ingeniería en Sistemas, Computación o afín |
| **Habilidades** | Desarrollo de software, análisis técnico, resolución de problemas |
| **Actividades** | Atención de tickets de desarrollo y modificaciones, resolución de incidencias, actualización de estatus técnicos |

## 2.4. Restricciones

El desarrollo del Sistema de Gestión de Solicitudes ISSEG debe considerar las siguientes restricciones:

**Restricciones Tecnológicas:**
- El sistema debe ser una aplicación web accesible mediante navegadores modernos
- Compatible con navegadores: Google Chrome (v90+), Mozilla Firefox (v88+), Microsoft Edge (v90+)
- Debe funcionar en resoluciones de pantalla: escritorio (1366x768 mínimo) y tabletas (768x1024)
- El backend debe desarrollarse con tecnologías compatibles con la infraestructura del ISSEG (.NET, Java o Python)
- Base de datos relacional: Microsoft SQL Server, PostgreSQL o MySQL
- Servidor: Windows Server o Linux según disponibilidad institucional

**Restricciones de Seguridad:**
- Cumplimiento con la Ley Federal de Protección de Datos Personales en Posesión de Particulares
- Cumplimiento con las políticas de seguridad de la información del ISSEG
- Todas las contraseñas deben almacenarse encriptadas (hash bcrypt o Argon2)
- Comunicaciones cifradas mediante HTTPS (TLS 1.2 o superior)
- Registro de auditoría inmutable de todas las operaciones críticas

**Restricciones Operativas:**
- El sistema debe estar disponible en horario laboral: Lunes a Viernes de 8:00 a 18:00 horas
- Disponibilidad mínima del 99.9% en horario operativo
- Tiempo máximo de respuesta de 2 segundos para operaciones comunes
- Soporte para al menos 50 usuarios concurrentes sin degradación

**Restricciones de Desarrollo:**
- Período de desarrollo: 7 meses (Enero - Julio 2026)
- Metodología de desarrollo: Cascada o Ágil según definición del equipo
- Documentación obligatoria: Manual de usuario, Manual técnico, Plan de pruebas
- Entrega de código fuente documentado y versionado

---

# 3. Requisitos específicos

## 3.1. Requisitos comunes de los interfaces

### 3.1.1. Interfaces de usuario

El sistema contará con una interfaz web responsiva con las siguientes características:

**Diseño Visual:**
- Paleta de colores institucional del ISSEG (colores oficiales de la institución)
- Logotipo del ISSEG visible en todas las pantallas
- Tipografía legible y accesible (tamaño mínimo 14px para texto principal)
- Diseño limpio y minimalista que facilite la navegación

**Estructura de Navegación:**
- Barra lateral (Sidebar) con menú principal: Inicio, Mis Solicitudes, Nueva Solicitud, Reportar Incidencia, Configuración
- Barra superior (Header) con breadcrumbs, información del usuario (nombre, rol, área) y notificaciones
- Área de contenido principal dinámico
- Pie de página con información legal y versión del sistema

**Elementos de Interacción:**
- Formularios con validación en tiempo real
- Mensajes de confirmación para acciones críticas (guardar, eliminar, aprobar)
- Indicadores visuales de campos obligatorios (asterisco rojo)
- Tooltips informativos para campos complejos
- Tablas con funcionalidad de ordenamiento y búsqueda
- Paginación para listados extensos

**Accesibilidad:**
- Navegación mediante teclado (teclas Tab, Enter, Esc)
- Botones y enlaces con áreas de clic mínimas de 44x44 píxeles
- Contraste de color suficiente para usuarios con dificultades visuales
- Mensajes de error claros y descriptivos

### 3.1.2. Interfaces de hardware

**Requisitos del cliente (usuario final):**
- Computadora de escritorio, laptop o tableta
- Procesador: Intel Core i3 o equivalente (mínimo)
- RAM: 4 GB mínimo
- Resolución de pantalla: 1366x768 píxeles mínimo
- Conexión a red: 10 Mbps mínimo

**Requisitos del servidor:**
- Servidor físico o virtual según infraestructura del ISSEG
- Procesador: Intel Xeon o equivalente (según carga esperada)
- RAM: 16 GB mínimo
- Almacenamiento: 500 GB mínimo (escalable según crecimiento de datos)
- Conectividad: Gigabit Ethernet

### 3.1.3. Interfaces de software

**Sistema Operativo Cliente:**
- Windows 10/11, macOS 11+, Linux (distribuciones principales)
- Navegador web actualizado (Chrome, Firefox, Edge)

**Sistema Operativo Servidor:**
- Windows Server 2016/2019/2022 o Linux (Ubuntu Server 20.04+, CentOS 8+)

**Base de Datos:**
- Microsoft SQL Server 2016 o superior
- PostgreSQL 12 o superior
- MySQL 8.0 o superior
- *(A definir según infraestructura disponible en el ISSEG)*

**Integración con otros sistemas:**
- **Sistema de autenticación:** Integración con LDAP/Active Directory del ISSEG para validación de usuarios (opcional, puede ser local)
- **Servidor de correo:** Integración con servidor SMTP institucional para envío de notificaciones
- **Formato de intercambio:** JSON para APIs internas, si aplican

### 3.1.4. Interfaces de comunicación

**Protocolos de red:**
- HTTP/HTTPS para comunicación web (puerto 80/443)
- SMTP para envío de correos electrónicos
- LDAP/LDAPS si se integra con Active Directory

**Formato de datos:**
- HTML5 para presentación web
- JSON para intercambio de datos entre cliente y servidor
- SQL para consultas a base de datos

**Seguridad de comunicación:**
- Todas las comunicaciones entre cliente y servidor deben ser cifradas mediante TLS 1.2 o superior
- Certificado SSL/TLS válido instalado en el servidor web

---

## 3.2. Requisitos funcionales

### 3.2.1. Módulo de Autenticación y Control de Acceso

| **Número de requisito** | RF-01 |
|---|---|
| **Nombre de requisito** | Inicio de sesión de usuario |
| **Tipo** | ☑ Requisito ☐ Restricción |
| **Fuente del requisito** | Necesidad institucional de seguridad / ISSEG |
| **Prioridad del requisito** | ☑ Alta/Esencial ☐ Media/Deseado ☐ Baja/Opcional |

**Descripción:**
El sistema debe permitir a los usuarios iniciar sesión mediante un formulario que solicite correo electrónico institucional y contraseña. El sistema validará las credenciales contra la base de datos de usuarios autorizados y, en caso de éxito, creará una sesión activa asociada a un token JWT. Si las credenciales son incorrectas, se mostrará un mensaje de error genérico ("Usuario o contraseña incorrectos") para evitar revelar información sobre cuentas existentes.

---

| **Número de requisito** | RF-02 |
|---|---|
| **Nombre de requisito** | Bloqueo de cuenta por intentos fallidos |
| **Tipo** | ☑ Requisito ☐ Restricción |
| **Fuente del requisito** | Política de seguridad ISSEG |
| **Prioridad del requisito** | ☑ Alta/Esencial ☐ Media/Deseado ☐ Baja/Opcional |

**Descripción:**
El sistema debe bloquear temporalmente una cuenta de usuario tras 3 intentos fallidos consecutivos de inicio de sesión. El bloqueo tendrá una duración de 15 minutos. Durante el período de bloqueo, el sistema mostrará el mensaje "Cuenta bloqueada temporalmente por seguridad. Intente nuevamente en 15 minutos." Todos los intentos fallidos serán registrados en la tabla de auditoría (AUDIT_LOGIN).

---

| **Número de requisito** | RF-03 |
|---|---|
| **Nombre de requisito** | Cierre de sesión |
| **Tipo** | ☑ Requisito ☐ Restricción |
| **Fuente del requisito** | Necesidad funcional básica |
| **Prioridad del requisito** | ☑ Alta/Esencial ☐ Media/Deseado ☐ Baja/Opcional |

**Descripción:**
El sistema debe proporcionar un botón de "Cerrar Sesión" visible en todas las pantallas. Al hacer clic, el sistema invalidará el token de sesión del usuario, eliminará las cookies de autenticación y redirigirá al usuario a la pantalla de inicio de sesión. La sesión cerrada debe registrarse en la tabla SESIONES_ACTIVAS con estado "Cerrada".

---

| **Número de requisito** | RF-04 |
|---|---|
| **Nombre de requisito** | Control de acceso basado en roles (RBAC) |
| **Tipo** | ☑ Requisito ☐ Restricción |
| **Fuente del requisito** | Análisis de requisitos de seguridad |
| **Prioridad del requisito** | ☑ Alta/Esencial ☐ Media/Deseado ☐ Baja/Opcional |

**Descripción:**
El sistema debe implementar un control de acceso granular donde cada usuario tenga asignado uno o más roles por área. Los permisos verificados antes de mostrar cualquier formulario o realizar cualquier acción son:
- Puede_Crear_Sistema_Nuevo
- Puede_Solicitar_Modificación
- Puede_Reportar_Incidencia
- Puede_Revisar_Solicitudes (rol ISSEG)
- Puede_Administrar_Sistema (rol Admin)

Si el usuario intenta acceder a una función sin permisos, se mostrará la excepción E0003 y se registrará el intento en AUDIT_ACCESO_NO_AUTORIZADO.

---

| **Número de requisito** | RF-05 |
|---|---|
| **Nombre de requisito** | Filtrado de sistemas por área del usuario |
| **Tipo** | ☑ Requisito ☐ Restricción |
| **Fuente del requisito** | Requisito de confidencialidad y segmentación |
| **Prioridad del requisito** | ☑ Alta/Esencial ☐ Media/Deseado ☐ Baja/Opcional |

**Descripción:**
El sistema debe filtrar automáticamente la lista de sistemas disponibles para que cada usuario vea únicamente los sistemas asignados a su área o áreas. Este filtrado se aplicará en:
- Formulario B (selección de sistema a modificar)
- Formulario de Incidencias (selección de sistema con problema)
- Dashboard (visualización de "Mis Sistemas")

El filtrado se realizará mediante la tabla SISTEMAS_AUTORIZADOS_POR_ÁREA.

---

### 3.2.2. Módulo de Solicitud de Sistema Nuevo (Formulario A)

| **Número de requisito** | RF-06 |
|---|---|
| **Nombre de requisito** | Captura de solicitud de sistema nuevo |
| **Tipo** | ☑ Requisito ☐ Restricción |
| **Fuente del requisito** | Proceso de negocio ISSEG |
| **Prioridad del requisito** | ☑ Alta/Esencial ☐ Media/Deseado ☐ Baja/Opcional |

**Descripción:**
El sistema debe proporcionar el Formulario A para capturar solicitudes de sistemas nuevos. Los campos obligatorios son:
- Información General: Nombre(s), Apellidos, Área/Departamento, Cargo, Email, Contacto
- Nombre del Sistema Propuesto (máximo 100 caracteres, único)
- Tipo de Sistema (Web, Escritorio, Móvil, API, Híbrido)
- Descripción General (máximo 500 caracteres)
- Problema que Resuelve (máximo 500 caracteres)
- Justificación del Negocio (mínimo 50 caracteres)
- Beneficios Esperados (checkbox múltiple + texto)
- Usuarios Finales Estimados (numérico)
- Prioridad del Negocio (Crítica/Alta/Media/Baja)
- Funcionalidades Principales (máximo 1000 caracteres)

Al enviar el formulario, se aplicará la validación V0001 (campos vacíos), V0002 (formato email), V0005 (texto corto).

---

| **Número de requisito** | RF-07 |
|---|---|
| **Nombre de requisito** | Generación automática de folio único |
| **Tipo** | ☑ Requisito ☐ Restricción |
| **Fuente del requisito** | Necesidad de trazabilidad |
| **Prioridad del requisito** | ☑ Alta/Esencial ☐ Media/Deseado ☐ Baja/Opcional |

**Descripción:**
Al guardar exitosamente una solicitud de sistema nuevo (Formulario A), el sistema debe generar automáticamente un folio único con el formato:
**SN-YYYY-NNNN**
Donde:
- SN = Sistema Nuevo
- YYYY = Año actual (4 dígitos)
- NNNN = Número secuencial de 4 dígitos (0001, 0002, ..., 9999)

El folio será mostrado al usuario mediante el mensaje M0002: "Solicitud enviada exitosamente. Su folio es: SN-2026-0001".

---

| **Número de requisito** | RF-08 |
|---|---|
| **Nombre de requisito** | Notificación de nueva solicitud a ISSEG |
| **Tipo** | ☑ Requisito ☐ Restricción |
| **Fuente del requisito** | Flujo de aprobación |
| **Prioridad del requisito** | ☑ Alta/Esencial ☐ Media/Deseado ☐ Baja/Opcional |

**Descripción:**
Cuando se crea una nueva solicitud de sistema nuevo, el sistema debe enviar automáticamente una notificación por correo electrónico a los usuarios con rol "Revisor ISSEG". El correo debe contener:
- Folio de la solicitud
- Nombre del solicitante
- Área solicitante
- Nombre del sistema propuesto
- Prioridad
- Enlace directo a la solicitud para revisión

---

| **Número de requisito** | RF-09 |
|---|---|
| **Nombre de requisito** | Revisión y aprobación/rechazo de solicitud nueva |
| **Tipo** | ☑ Requisito ☐ Restricción |
| **Fuente del requisito** | Proceso de aprobación ISSEG |
| **Prioridad del requisito** | ☑ Alta/Esencial ☐ Media/Deseado ☐ Baja/Opcional |

**Descripción:**
Los usuarios con rol "Revisor ISSEG" deben poder visualizar las solicitudes en estado "Pendiente" y cambiar su estatus a:
- **Aprobado:** Se habilitará la asignación de equipo (PM, Desarrollador, Arquitecto) y se solicitará completar el Formulario C
- **Rechazado:** Se debe capturar un motivo de rechazo (campo obligatorio, mínimo 20 caracteres) y se notificará al solicitante
- **Requiere Aclaración:** Se solicitarán datos adicionales al solicitante

Cualquier cambio de estado debe registrarse en la tabla AUDIT_SISTEMAS_NUEVOS.

---

| **Número de requisito** | RF-10 |
|---|---|
| **Nombre de requisito** | Asignación de equipo de desarrollo |
| **Tipo** | ☑ Requisito ☐ Restricción |
| **Fuente del requisito** | Flujo operativo post-aprobación |
| **Prioridad del requisito** | ☑ Alta/Esencial ☐ Media/Deseado ☐ Baja/Opcional |

**Descripción:**
Una vez aprobada una solicitud de sistema nuevo, el Revisor ISSEG debe poder asignar:
- Product Manager (obligatorio)
- Desarrollador Líder (obligatorio)
- Arquitecto (opcional)

Esta asignación quedará registrada en la tabla SISTEMAS y vinculada con la solicitud aprobada. Los usuarios asignados recibirán notificación por correo electrónico.

---

### 3.2.3. Módulo de Solicitud de Modificación (Formulario B)

| **Número de requisito** | RF-11 |
|---|---|
| **Nombre de requisito** | Selección de sistema a modificar |
| **Tipo** | ☑ Requisito ☐ Restricción |
| **Fuente del requisito** | Flujo operativo de modificaciones |
| **Prioridad del requisito** | ☑ Alta/Esencial ☐ Media/Deseado ☐ Baja/Opcional |

**Descripción:**
El Formulario B debe presentar una lista desplegable con los sistemas disponibles para modificación. Esta lista estará filtrada automáticamente según el área del usuario (requisito RF-05). Si no existen sistemas autorizados para el área del usuario, se mostrará el mensaje M0004: "No se encontraron sistemas registrados para su área."

El sistema no debe mostrar las versiones de los sistemas, solo el nombre del sistema.

---

| **Número de requisito** | RF-12 |
|---|---|
| **Nombre de requisito** | Captura de solicitud de modificación |
| **Tipo** | ☑ Requisito ☐ Restricción |
| **Fuente del requisito** | Proceso de gestión de cambios |
| **Prioridad del requisito** | ☑ Alta/Esencial ☐ Media/Deseado ☐ Baja/Opcional |

**Descripción:**
El sistema debe proporcionar el Formulario B con los siguientes campos obligatorios:
- Sistema a Modificar (lista filtrada)
- Información del solicitante (prellenada desde perfil)
- Tipo de Modificación (Nueva funcionalidad, Corrección, Mejora, Cambio interfaz, Integración, Otro)
- Descripción Detallada (máximo 1000 caracteres)
- Razón del Cambio (máximo 500 caracteres)
- Situación Actual (máximo 500 caracteres)
- Situación Deseada (máximo 500 caracteres)
- Urgencia (Inmediata, Alta, Media, Baja)
- Impacto en Operación (Crítico, Alto, Medio, Bajo)
- Usuarios Afectados (numérico)

Al enviar, el sistema generará un folio con formato **MOD-YYYY-NNNN**.

---

| **Número de requisito** | RF-13 |
|---|---|
| **Nombre de requisito** | Registro de versión de sistema en modificaciones |
| **Tipo** | ☑ Requisito ☐ Restricción |
| **Fuente del requisito** | Trazabilidad de cambios |
| **Prioridad del requisito** | ☑ Alta/Esencial ☐ Media/Deseado ☐ Baja/Opcional |

**Descripción:**
Cuando se aprueba una solicitud de modificación (Formulario B), el sistema debe:
1. Consultar la versión actual del sistema en la tabla SISTEMAS
2. Incrementar el número de versión (+0.1 para cambios menores, +1.0 para cambios mayores según clasificación)
3. Registrar el cambio en la tabla HISTORIAL_CAMBIOS con la nueva versión
4. Actualizar el campo Versión_Actual en la tabla SISTEMAS

Ejemplo: Sistema en versión 1.2 → Cambio menor aprobado → Nueva versión 1.3

---

| **Número de requisito** | RF-14 |
|---|---|
| **Nombre de requisito** | Revisión de solicitud de modificación |
| **Tipo** | ☑ Requisito ☐ Restricción |
| **Fuente del requisito** | Flujo de aprobación de cambios |
| **Prioridad del requisito** | ☑ Alta/Esencial ☐ Media/Deseado ☐ Baja/Opcional |

**Descripción:**
El usuario con rol "Revisor ISSEG" debe poder evaluar solicitudes de modificación y cambiar su estado a:
- **Aprobada:** Se asignará un desarrollador y se creará ticket en la cola de desarrollo
- **Rechazada:** Se capturará motivo de rechazo (obligatorio)
- **Requiere Aclaración:** Se solicitará información adicional

El Revisor debe poder agregar un campo "Observaciones ISSEG" y "Estimación de Esfuerzo (horas)".

---

### 3.2.4. Módulo de Levantamiento de Requerimientos (Formulario C)

| **Número de requisito** | RF-15 |
|---|---|
| **Nombre de requisito** | Vinculación con solicitud aprobada |
| **Tipo** | ☑ Requisito ☐ Restricción |
| **Fuente del requisito** | Flujo de desarrollo post-aprobación |
| **Prioridad del requisito** | ☑ Alta/Esencial ☐ Media/Deseado ☐ Baja/Opcional |

**Descripción:**
El Formulario C (Levantamiento de Requerimientos) solo debe poder ser accedido si existe una solicitud de sistema nuevo (Formulario A) en estado "Aprobado". Al abrir el Formulario C, el sistema debe precargar automáticamente:
- ID del Proyecto (referencia al Formulario A)
- Nombre del Sistema (desde Formulario A)
- Product Manager asignado (desde asignación ISSEG)
- Desarrollador Líder asignado

---

| **Número de requisito** | RF-16 |
|---|---|
| **Nombre de requisito** | Captura de requerimientos técnicos detallados |
| **Tipo** | ☑ Requisito ☐ Restricción |
| **Fuente del requisito** | Necesidad de documentación técnica formal |
| **Prioridad del requisito** | ☑ Alta/Esencial ☐ Media/Deseado ☐ Baja/Opcional |

**Descripción:**
El Formulario C debe permitir capturar:
- Objetivo General del Sistema (máximo 500 caracteres)
- Objetivos Específicos (lista numerada)
- Alcance Funcional (qué incluye)
- Fuera de Alcance (qué NO incluye)
- Tabla de Roles y Actores (tabla dinámica con campos: Rol, Descripción, Permisos, Cantidad Usuarios)
- Módulos Funcionales (tabla repetible con prioridad MVP/Importante/Deseable)
- Requisitos Funcionales (formato IEEE: RF-NN con descripción)
- Requisitos No Funcionales (RNF-NN)

---

| **Número de requisito** | RF-17 |
|---|---|
| **Nombre de requisito** | Validación de completitud de requerimientos |
| **Tipo** | ☑ Requisito ☐ Restricción |
| **Fuente del requisito** | Control de calidad de documentación |
| **Prioridad del requisito** | ☐ Alta/Esencial ☑ Media/Deseado ☐ Baja/Opcional |

**Descripción:**
El sistema debe validar que el Formulario C tenga completos al menos:
- Objetivo General (obligatorio)
- Mínimo 3 Objetivos Específicos
- Alcance Funcional definido
- Al menos 2 Roles de usuario
- Mínimo 5 Requisitos Funcionales

Si no cumple con lo mínimo, se mostrará advertencia M0003 antes de permitir enviar.

---

### 3.2.5. Módulo de Gestión de Incidencias y Problemas

| **Número de requisito** | RF-18 |
|---|---|
| **Nombre de requisito** | Reporte de incidencia |
| **Tipo** | ☑ Requisito ☐ Restricción |
| **Fuente del requisito** | Necesidad de soporte y atención de fallos |
| **Prioridad del requisito** | ☑ Alta/Esencial ☐ Media/Deseado ☐ Baja/Opcional |

**Descripción:**
El sistema debe proporcionar un formulario de reporte de incidencias con los siguientes campos obligatorios:
- Información del reportante (prellenada)
- Sistema Afectado (lista filtrada por área)
- Módulo Afectado (texto)
- Título Resumido (máximo 100 caracteres)
- Descripción Detallada (máximo 1000 caracteres)
- Pasos para Reproducir (máximo 500 caracteres)
- Nivel de Urgencia (Crítica, Alta, Media, Baja) ← **Campo clave para SLA**
- Cantidad de Usuarios Afectados (numérico)
- Navegador/Dispositivo (texto)
- Sistema Operativo (texto)
- Comportamiento Esperado (máximo 300 caracteres)

Al enviar, el sistema generará folio **INC-YYYY-NNNN**.

---

| **Número de requisito** | RF-19 |
|---|---|
| **Nombre de requisito** | Cálculo automático de SLA |
| **Tipo** | ☑ Requisito ☐ Restricción |
| **Fuente del requisito** | Compromiso de niveles de servicio |
| **Prioridad del requisito** | ☑ Alta/Esencial ☐ Media/Deseado ☐ Baja/Opcional |

**Descripción:**
El sistema debe calcular automáticamente la fecha y hora límite de atención según el nivel de urgencia seleccionado en el reporte de incidencia:
- **Crítica:** 1 hora desde el reporte
- **Alta:** 4 horas desde el reporte
- **Media:** 8 horas desde el reporte
- **Baja:** 24 horas desde el reporte

Este cálculo debe considerar solo horario laboral (Lunes a Viernes, 8:00-18:00). Si el límite cae fuera de horario, se recorre al siguiente día hábil.

El SLA calculado se registrará en la tabla CONTROL_INCIDENCIAS y se mostrará en el Dashboard con códigos de color:
- Verde: Dentro de tiempo
- Amarillo: 80% del tiempo transcurrido
- Rojo: SLA excedido

---

| **Número de requisito** | RF-20 |
|---|---|
| **Nombre de requisito** | Adjuntar evidencias en incidencias |
| **Tipo** | ☑ Requisito ☐ Restricción |
| **Fuente del requisito** | Necesidad de análisis técnico |
| **Prioridad del requisito** | ☐ Alta/Esencial ☑ Media/Deseado ☐ Baja/Opcional |

**Descripción:**
El formulario de incidencias debe permitir adjuntar hasta 3 archivos como evidencia:
- Formatos permitidos: JPG, PNG, TXT, LOG
- Tamaño máximo por archivo: 10 MB
- Tamaño total máximo: 25 MB

Si se intenta subir un archivo de mayor tamaño, se aplicará la validación V0004 y se mostrará mensaje de error.

Los archivos se almacenarán en el servidor con la ruta: `/incidencias/YYYY/MM/INC-NNNN/archivo_original.ext`

---

| **Número de requisito** | RF-21 |
|---|---|
| **Nombre de requisito** | Asignación automática de responsable según urgencia |
| **Tipo** | ☑ Requisito ☐ Restricción |
| **Fuente del requisito** | Optimización de tiempos de respuesta |
| **Prioridad del requisito** | ☐ Alta/Esencial ☑ Media/Deseado ☐ Baja/Opcional |

**Descripción:**
El sistema debe asignar automáticamente un técnico de soporte a cada incidencia según reglas predefinidas:
- **Crítica:** Notificar a todos los técnicos disponibles + Líder de Soporte
- **Alta:** Asignar al técnico con menor carga actual de incidencias abiertas
- **Media/Baja:** Asignar en modo round-robin (turno rotativo)

El técnico asignado recibirá notificación inmediata por correo con los detalles de la incidencia.

---

### 3.2.6. Módulo de Dashboard y Reportes

| **Número de requisito** | RF-22 |
|---|---|
| **Nombre de requisito** | Dashboard del usuario |
| **Tipo** | ☑ Requisito ☐ Restricción |
| **Fuente del requisito** | Necesidad de visibilidad de solicitudes |
| **Prioridad del requisito** | ☑ Alta/Esencial ☐ Media/Deseado ☐ Baja/Opcional |

**Descripción:**
Al iniciar sesión, cada usuario debe visualizar un Dashboard personalizado que muestre:
- **Mis Solicitudes Activas:** Tabla con folios, tipo (SN/MOD/INC), fecha, estado actual
- **Mis Sistemas:** Lista de sistemas autorizados para su área
- **Incidencias Abiertas:** Incidencias reportadas por el usuario o su área que están pendientes
- **Notificaciones:** Mensajes del sistema (aprobaciones, rechazos, solicitudes de aclaración)

El Dashboard debe permitir hacer clic sobre cualquier folio para ver el detalle completo de la solicitud.

---

| **Número de requisito** | RF-23 |
|---|---|
| **Nombre de requisito** | Dashboard de métricas para administradores |
| **Tipo** | ☑ Requisito ☐ Restricción |
| **Fuente del requisito** | Necesidad de indicadores de gestión |
| **Prioridad del requisito** | ☐ Alta/Esencial ☑ Media/Deseado ☐ Baja/Opcional |

**Descripción:**
Los usuarios con rol "Administrador" o "Revisor ISSEG" deben tener acceso a un Dashboard de métricas globales:
- **Total de solicitudes por estado** (Pendiente, Aprobado, Rechazado, En Desarrollo, Terminado)
- **Gráfico de solicitudes por mes** (últimos 12 meses)
- **Cumplimiento de SLA** (porcentaje de incidencias resueltas dentro del tiempo)
- **Sistemas más problemáticos** (Top 5 con más incidencias)
- **Áreas con mayor actividad** (Top 5 con más solicitudes)
- **Tiempo promedio de resolución** (en horas)

Las métricas deben poder filtrarse por rango de fechas.

---

| **Número de requisito** | RF-24 |
|---|---|
| **Nombre de requisito** | Exportación de reportes |
| **Tipo** | ☑ Requisito ☐ Restricción |
| **Fuente del requisito** | Necesidad de reportes ejecutivos |
| **Prioridad del requisito** | ☐ Alta/Esencial ☐ Media/Deseado ☑ Baja/Opcional |

**Descripción:**
El sistema debe permitir exportar los reportes del Dashboard de métricas en los siguientes formatos:
- **PDF:** Para presentaciones ejecutivas
- **Excel (XLSX):** Para análisis de datos
- **CSV:** Para integración con otras herramientas

La exportación debe incluir los filtros aplicados y la fecha de generación del reporte.

---

### 3.2.7. Módulo de Administración

| **Número de requisito** | RF-25 |
|---|---|
| **Nombre de requisito** | Gestión de catálogo de usuarios |
| **Tipo** | ☑ Requisito ☐ Restricción |
| **Fuente del requisito** | Administración del sistema |
| **Prioridad del requisito** | ☑ Alta/Esencial ☐ Media/Deseado ☐ Baja/Opcional |

**Descripción:**
El Administrador debe poder realizar las siguientes operaciones sobre usuarios:
- **Crear:** Dar de alta nuevos usuarios con email, nombre, área y rol inicial
- **Editar:** Modificar datos del usuario, cambiar área, actualizar permisos
- **Inhabilitar:** Desactivar usuario sin eliminar su historial (Estado = Inactivo)
- **Reactivar:** Volver a activar un usuario inactivo
- **Resetear Contraseña:** Generar nueva contraseña temporal y enviarla por correo

Nunca se debe permitir eliminar usuarios que tengan solicitudes o incidencias asociadas.

---

| **Número de requisito** | RF-26 |
|---|---|
| **Nombre de requisito** | Gestión de catálogo de áreas |
| **Tipo** | ☑ Requisito ☐ Restricción |
| **Fuente del requisito** | Estructura organizacional |
| **Prioridad del requisito** | ☑ Alta/Esencial ☐ Media/Deseado ☐ Baja/Opcional |

**Descripción:**
El Administrador debe poder gestionar el catálogo de Áreas/Departamentos del ISSEG:
- Crear nuevas áreas (campos: Nombre_Área, Responsable, Puede_Crear_Sistemas_Nuevos)
- Editar áreas existentes
- Asignar o cambiar responsable de área
- Desactivar áreas (Estado = Inactiva) sin eliminarlas

Cada Área debe poder tener configurado si tiene permiso para crear Sistemas Nuevos (campo booleano).

---

| **Número de requisito** | RF-27 |
|---|---|
| **Nombre de requisito** | Gestión de catálogo de sistemas |
| **Tipo** | ☑ Requisito ☐ Restricción |
| **Fuente del requisito** | Inventario de aplicaciones |
| **Prioridad del requisito** | ☑ Alta/Esencial ☐ Media/Deseado ☐ Baja/Opcional |

**Descripción:**
El Administrador debe poder visualizar y editar el inventario de sistemas existentes:
- Ver listado completo de sistemas con su estado, versión, área responsable
- Editar información de sistemas (nombre, descripción, área responsable)
- Cambiar estado de sistema (Planeación, Desarrollo, Producción, Mantenimiento, Descontinuado)
- Asignar o reasignar áreas autorizadas para acceder al sistema (tabla SISTEMAS_AUTORIZADOS_POR_ÁREA)

---

| **Número de requisito** | RF-28 |
|---|---|
| **Nombre de requisito** | Configuración de SLAs |
| **Tipo** | ☑ Requisito ☐ Restricción |
| **Fuente del requisito** | Flexibilidad operativa |
| **Prioridad del requisito** | ☐ Alta/Esencial ☐ Media/Deseado ☑ Baja/Opcional |

**Descripción:**
El Administrador debe poder configurar los tiempos de SLA para cada nivel de urgencia en la tabla SLA_DEFINICIONES:
- Crítica: [configurar minutos]
- Alta: [configurar minutos]
- Media: [configurar minutos]
- Baja: [configurar minutos]

Esta configuración afectará todos los nuevos reportes de incidencia creados posteriores al cambio.

---

## 3.3. Requisitos no funcionales

### 3.3.1. Requisitos de rendimiento

| **Número de requisito** | RNF-01 |
|---|---|
| **Nombre de requisito** | Tiempo de respuesta del sistema |
| **Tipo** | ☑ Requisito ☐ Restricción |
| **Fuente del requisito** | Experiencia de usuario |
| **Prioridad del requisito** | ☑ Alta/Esencial ☐ Media/Deseado ☐ Baja/Opcional |

**Descripción:**
El tiempo de carga de cualquier pantalla o formulario del sistema no debe exceder los 2 segundos en condiciones normales de red (10 Mbps o superior). Para operaciones complejas como generación de reportes o consultas con grandes volúmenes de datos, el tiempo máximo permitido es de 5 segundos. Si una operación tarda más de 5 segundos, se debe mostrar un indicador de progreso visual.

---

| **Número de requisito** | RNF-02 |
|---|---|
| **Nombre de requisito** | Capacidad de usuarios concurrentes |
| **Tipo** | ☑ Requisito ☐ Restricción |
| **Fuente del requisito** | Dimensionamiento del sistema |
| **Prioridad del requisito** | ☑ Alta/Esencial ☐ Media/Deseado ☐ Baja/Opcional |

**Descripción:**
El sistema debe soportar al menos 50 usuarios concurrentes sin degradación perceptible del servicio. Se considera "degradación perceptible" cuando el tiempo de respuesta aumenta en más del 50% respecto al uso de un solo usuario. El sistema debe estar dimensionado para escalar hasta 100 usuarios concurrentes mediante ajustes de hardware o escalamiento horizontal.

---

| **Número de requisito** | RNF-03 |
|---|---|
| **Nombre de requisito** | Tamaño máximo de base de datos |
| **Tipo** | ☐ Requisito ☑ Restricción |
| **Fuente del requisito** | Planificación de almacenamiento |
| **Prioridad del requisito** | ☐ Alta/Esencial ☑ Media/Deseado ☐ Baja/Opcional |

**Descripción:**
La base de datos debe estar dimensionada para almacenar al menos:
- 10,000 solicitudes (Formularios A, B, C combinados)
- 50,000 incidencias
- 1,000 usuarios
- 500 sistemas
- 3 años de información histórica sin afectar el rendimiento

Se estima un crecimiento aproximado de 200 solicitudes/mes y 500 incidencias/mes.

---

### 3.3.2. Seguridad

| **Número de requisito** | RNF-04 |
|---|---|
| **Nombre de requisito** | Cifrado de contraseñas |
| **Tipo** | ☑ Requisito ☐ Restricción |
| **Fuente del requisito** | Seguridad de credenciales |
| **Prioridad del requisito** | ☑ Alta/Esencial ☐ Media/Deseado ☐ Baja/Opcional |

**Descripción:**
Todas las contraseñas de usuario deben almacenarse en la base de datos utilizando algoritmos de hash robustos y seguros. Los algoritmos aceptados son:
- bcrypt (factor de costo mínimo: 12)
- Argon2 (configuración recomendada)
- PBKDF2 con SHA-256 (mínimo 100,000 iteraciones)

**NUNCA** se deben almacenar contraseñas en texto plano ni utilizar algoritmos débiles como MD5 o SHA-1 sin salt.

---

| **Número de requisito** | RNF-05 |
|---|---|
| **Nombre de requisito** | Comunicación cifrada (HTTPS) |
| **Tipo** | ☑ Requisito ☐ Restricción |
| **Fuente del requisito** | Protección de datos en tránsito |
| **Prioridad del requisito** | ☑ Alta/Esencial ☐ Media/Deseado ☐ Baja/Opcional |

**Descripción:**
Toda la comunicación entre el navegador del usuario y el servidor web debe estar cifrada mediante protocolo HTTPS utilizando TLS versión 1.2 o superior. El servidor debe tener instalado un certificado SSL/TLS válido (puede ser emitido por una CA reconocida o ser un certificado institucional). El sistema debe redirigir automáticamente cualquier intento de conexión HTTP (puerto 80) a HTTPS (puerto 443).

---

| **Número de requisito** | RNF-06 |
|---|---|
| **Nombre de requisito** | Auditoría de operaciones críticas |
| **Tipo** | ☑ Requisito ☐ Restricción |
| **Fuente del requisito** | Cumplimiento y trazabilidad |
| **Prioridad del requisito** | ☑ Alta/Esencial ☐ Media/Deseado ☐ Baja/Opcional |

**Descripción:**
El sistema debe mantener un registro de auditoría inmutable de todas las operaciones de escritura realizadas sobre datos críticos. Las tablas de auditoría deben registrar:
- **Qué:** Acción realizada (Crear, Editar, Eliminar, Aprobar, Rechazar)
- **Quién:** Usuario que realizó la acción (ID_Usuario)
- **Cuándo:** Fecha y hora exacta (timestamp con milisegundos)
- **Dónde:** Módulo o tabla afectada
- **Detalle:** Valores antiguos y nuevos (para operaciones de actualización)

Las tablas de auditoría especificadas son:
- AUDIT_LOGIN
- AUDIT_ACCESO_NO_AUTORIZADO
- AUDIT_SISTEMAS_NUEVOS
- AUDIT_MODIFICACIONES

Los registros de auditoría no pueden ser modificados ni eliminados, ni siquiera por el Administrador.

---

| **Número de requisito** | RNF-07 |
|---|---|
| **Nombre de requisito** | Timeout de sesión por inactividad |
| **Tipo** | ☑ Requisito ☐ Restricción |
| **Fuente del requisito** | Seguridad de sesiones |
| **Prioridad del requisito** | ☑ Alta/Esencial ☐ Media/Deseado ☐ Baja/Opcional |

**Descripción:**
Las sesiones de usuario deben expirar automáticamente tras 30 minutos de inactividad. Se considera "inactividad" cuando no se realizan peticiones al servidor. Al detectar una sesión expirada, el sistema debe:
1. Invalidar el token de sesión
2. Mostrar el mensaje de la excepción E0001: "Su sesión ha terminado"
3. Redirigir al usuario a la pantalla de login
4. Registrar el evento en la tabla SESIONES_ACTIVAS

---

### 3.3.3. Fiabilidad

| **Número de requisito** | RNF-08 |
|---|---|
| **Nombre de requisito** | Tiempo medio entre fallos (MTBF) |
| **Tipo** | ☑ Requisito ☐ Restricción |
| **Fuente del requisito** | Confiabilidad operativa |
| **Prioridad del requisito** | ☐ Alta/Esencial ☑ Media/Deseado ☐ Baja/Opcional |

**Descripción:**
El sistema debe tener un Tiempo Medio Entre Fallos (MTBF) de al menos 720 horas (30 días). Se considera "fallo" cuando el sistema queda completamente inoperante y no puede recuperarse automáticamente. Fallos parciales (un módulo afectado pero el resto funcional) no cuentan para este indicador.

---

| **Número de requisito** | RNF-09 |
|---|---|
| **Nombre de requisito** | Recuperación ante errores |
| **Tipo** | ☑ Requisito ☐ Restricción |
| **Fuente del requisito** | Continuidad operativa |
| **Prioridad del requisito** | ☐ Alta/Esencial ☑ Media/Deseado ☐ Baja/Opcional |

**Descripción:**
En caso de error durante el envío de un formulario (por pérdida de conexión, timeout o error del servidor), el sistema debe:
- Retener la información capturada durante al menos 15 minutos
- Mostrar un mensaje de error descriptivo al usuario
- Permitir reintentar el envío sin pérdida de datos
- Ofrecer la opción de "Guardar borrador" para continuar después

No se considera válido mostrar solo "Error 500" o mensajes técnicos incomprensibles para el usuario.

---

### 3.3.4. Disponibilidad

| **Número de requisito** | RNF-10 |
|---|---|
| **Nombre de requisito** | Disponibilidad del sistema |
| **Tipo** | ☑ Requisito ☐ Restricción |
| **Fuente del requisito** | Acuerdo de nivel de servicio |
| **Prioridad del requisito** | ☑ Alta/Esencial ☐ Media/Deseado ☐ Baja/Opcional |

**Descripción:**
El sistema debe estar disponible el 99.9% del tiempo durante el horario laboral institucional:
- **Horario operativo:** Lunes a Viernes, 8:00 - 18:00 horas (10 horas/día)
- **Tiempo de inactividad permitido:** Máximo 5 minutos por mes en horario operativo
- **Mantenimientos programados:** Deben realizarse fuera del horario operativo (después de las 18:00 o fines de semana) y notificarse con al menos 48 horas de anticipación a todos los usuarios

El incumplimiento de este requisito debe ser reportado al patrocinador del proyecto.

---

### 3.3.5. Mantenibilidad

| **Número de requisito** | RNF-11 |
|---|---|
| **Nombre de requisito** | Código documentado |
| **Tipo** | ☑ Requisito ☐ Restricción |
| **Fuente del requisito** | Facilidad de mantenimiento |
| **Prioridad del requisito** | ☐ Alta/Esencial ☑ Media/Deseado ☐ Baja/Opcional |

**Descripción:**
El código fuente del sistema debe estar documentado siguiendo buenas prácticas:
- Comentarios en funciones complejas explicando su propósito
- Nomenclatura clara y descriptiva para variables, funciones y clases
- Uso de estándares de codificación del lenguaje utilizado (ej. PEP 8 para Python, PSR para PHP, etc.)
- Documentación de APIs internas (si existen)
- README con instrucciones de instalación y configuración

---

| **Número de requisito** | RNF-12 |
|---|---|
| **Nombre de requisito** | Control de versiones |
| **Tipo** | ☑ Requisito ☐ Restricción |
| **Fuente del requisito** | Trazabilidad del desarrollo |
| **Prioridad del requisito** | ☑ Alta/Esencial ☐ Media/Deseado ☐ Baja/Opcional |

**Descripción:**
El código fuente del sistema debe mantenerse bajo un sistema de control de versiones (Git, SVN, etc.). Se debe hacer commit frecuentemente con mensajes descriptivos que expliquen los cambios realizados. Al finalizar el proyecto, se debe entregar:
- Repositorio completo con historial de cambios
- Documentación de estructura de carpetas
- Instrucciones de despliegue

---

| **Número de requisito** | RNF-13 |
|---|---|
| **Nombre de requisito** | Modularidad del sistema |
| **Tipo** | ☑ Requisito ☐ Restricción |
| **Fuente del requisito** | Facilidad de evolución |
| **Prioridad del requisito** | ☐ Alta/Esencial ☑ Media/Deseado ☐ Baja/Opcional |

**Descripción:**
El sistema debe diseñarse con arquitectura modular para facilitar futuras actualizaciones. Los módulos principales (Autenticación, Formularios, Incidencias, Reportes) deben estar claramente separados y con bajo acoplamiento. Esto permitirá agregar nuevos tipos de formularios o modificar uno existente sin afectar a los demás.

---

### 3.3.6. Portabilidad

| **Número de requisito** | RNF-14 |
|---|---|
| **Nombre de requisito** | Compatibilidad de navegadores |
| **Tipo** | ☑ Requisito ☐ Restricción |
| **Fuente del requisito** | Accesibilidad multiplataforma |
| **Prioridad del requisito** | ☑ Alta/Esencial ☐ Media/Deseado ☐ Baja/Opcional |

**Descripción:**
El sistema debe funcionar correctamente en los siguientes navegadores web:
- Google Chrome versión 90 o superior
- Mozilla Firefox versión 88 o superior
- Microsoft Edge versión 90 o superior
- Safari versión 14 o superior (opcional)

No se requiere compatibilidad con Internet Explorer. El sistema debe detectar navegadores obsoletos y mostrar mensaje de advertencia al usuario.

---

| **Número de requisito** | RNF-15 |
|---|---|
| **Nombre de requisito** | Independencia de plataforma del servidor |
| **Tipo** | ☐ Requisito ☑ Restricción |
| **Fuente del requisito** | Flexibilidad de infraestructura |
| **Prioridad del requisito** | ☐ Alta/Esencial ☑ Media/Deseado ☐ Baja/Opcional |

**Descripción:**
El sistema debe poder desplegarse tanto en servidores Windows Server como en servidores Linux sin requerir cambios significativos en el código. Se recomienda el uso de tecnologías multiplataforma (ej. .NET Core, Java, Python/Django, Node.js) y evitar dependencias específicas de sistema operativo.

---

| **Número de requisito** | RNF-16 |
|---|---|
| **Nombre de requisito** | Diseño responsivo |
| **Tipo** | ☑ Requisito ☐ Restricción |
| **Fuente del requisito** | Accesibilidad desde dispositivos móviles |
| **Prioridad del requisito** | ☐ Alta/Esencial ☑ Media/Deseado ☐ Baja/Opcional |

**Descripción:**
La interfaz del sistema debe adaptarse automáticamente al tamaño de pantalla del dispositivo (responsive design). Debe ser funcional en:
- Escritorio: Resolución mínima 1366x768
- Tabletas: Resolución típica 768x1024 (iPad, Android tablets)
- Móviles: Visualización aceptable (no necesariamente toda la funcionalidad)

Se priorizará la experiencia en escritorio, pero el Dashboard y visualización de solicitudes debe verse bien en tabletas.

---

## 3.4. Otros requisitos

### 3.4.1. Requisitos Legales y Normativos

| **Número de requisito** | RO-01 |
|---|---|
| **Nombre de requisito** | Cumplimiento con Ley de Protección de Datos |
| **Tipo** | ☑ Requisito ☐ Restricción |
| **Fuente del requisito** | Marco legal mexicano |
| **Prioridad del requisito** | ☑ Alta/Esencial ☐ Media/Deseado ☐ Baja/Opcional |

**Descripción:**
El sistema debe cumplir con la Ley Federal de Protección de Datos Personales en Posesión de Particulares (LFPDPPP). Específicamente:
- Los datos personales solo deben ser accesibles por personal autorizado
- No se deben compartir datos personales con terceros sin consentimiento
- Los usuarios deben poder solicitar la corrección de sus datos personales
- El sistema debe contar con aviso de privacidad

---

| **Número de requisito** | RO-02 |
|---|---|
| **Nombre de requisito** | Retención de información histórica |
| **Tipo** | ☑ Requisito ☐ Restricción |
| **Fuente del requisito** | Políticas de auditoría institucional |
| **Prioridad del requisito** | ☐ Alta/Esencial ☑ Media/Deseado ☐ Baja/Opcional |

**Descripción:**
El sistema debe mantener toda la información histórica (solicitudes, incidencias, auditorías) durante un período mínimo de 2 años. Después de este período, podrá implementarse un proceso de archivado o purga de datos obsoletos, previa aprobación del área de TI y cumpliendo con las normativas institucionales.

---

### 3.4.2. Requisitos de Documentación

| **Número de requisito** | RO-03 |
|---|---|
| **Nombre de requisito** | Manual de usuario |
| **Tipo** | ☑ Requisito ☐ Restricción |
| **Fuente del requisito** | Necesidad de capacitación |
| **Prioridad del requisito** | ☑ Alta/Esencial ☐ Media/Deseado ☐ Baja/Opcional |

**Descripción:**
Se debe elaborar un Manual de Usuario en formato PDF que explique:
- Cómo iniciar sesión
- Cómo crear cada tipo de solicitud (Formularios A, B, C)
- Cómo reportar incidencias
- Cómo consultar el estado de solicitudes
- Preguntas frecuentes (FAQ)
- Capturas de pantalla ilustrativas

El manual debe estar escrito en español claro y accesible para usuarios no técnicos.

---

| **Número de requisito** | RO-04 |
|---|---|
| **Nombre de requisito** | Manual técnico |
| **Tipo** | ☑ Requisito ☐ Restricción |
| **Fuente del requisito** | Necesidad de transferencia de conocimiento |
| **Prioridad del requisito** | ☑ Alta/Esencial ☐ Media/Deseado ☐ Baja/Opcional |

**Descripción:**
Se debe elaborar un Manual Técnico que incluya:
- Arquitectura del sistema (diagrama de componentes)
- Modelo de base de datos (diagrama ER completo)
- Descripción de tablas y campos principales
- Flujo de datos entre módulos
- Configuración del servidor (requisitos, instalación)
- Procedimientos de respaldo y recuperación
- Troubleshooting de problemas comunes

---

### 3.4.3. Requisitos de Capacitación

| **Número de requisito** | RO-05 |
|---|---|
| **Nombre de requisito** | Capacitación de usuarios finales |
| **Tipo** | ☑ Requisito ☐ Restricción |
| **Fuente del requisito** | Adopción del sistema |
| **Prioridad del requisito** | ☐ Alta/Esencial ☑ Media/Deseado ☐ Baja/Opcional |

**Descripción:**
Antes del lanzamiento oficial del sistema, se debe proporcionar al menos una sesión de capacitación para:
- Usuarios solicitantes (responsables de área): 2 horas
- Revisores ISSEG: 2 horas
- Administradores del sistema: 4 horas

La capacitación debe ser presencial o mediante videoconferencia e incluir ejercicios prácticos.

---

# 4. Modelado del Sistema

## 4.1. Diagrama de Casos de Uso Principal

```
┌───────────────────────────────────────────────────────────────────┐
│                     SISTEMA GESTIÓN SOLICITUDES ISSEG              │
├───────────────────────────────────────────────────────────────────┤
│                                                                     │
│   ┌─────────────┐                                                 │
│   │ Solicitante │────►(Iniciar Sesión)                            │
│   └─────────────┘         │                                        │
│                           ├───►(Crear Solicitud Sistema Nuevo)    │
│                           ├───►(Solicitar Modificación)            │
│                           └───►(Reportar Incidencia)               │
│                           └───►(Consultar Mis Solicitudes)         │
│                                                                     │
│   ┌─────────────┐                                                 │
│   │Revisor ISSEG│────►(Revisar Solicitudes)                       │
│   └─────────────┘     ├───►(Aprobar/Rechazar)                     │
│                       └───►(Asignar Equipo)                        │
│                                                                     │
│   ┌──────────────┐                                                │
│   │Administrador │────►(Gestionar Usuarios)                       │
│   └──────────────┘    ├───►(Gestionar Catálogos)                  │
│                       └───►(Ver Dashboard Métricas)                │
│                                                                     │
└───────────────────────────────────────────────────────────────────┘
```

## 4.2. Diagrama de Flujo General del Sistema

Los diagramas de flujo detallados se encuentran en los archivos complementarios:
- `01-diagrama-flujo-tickets.md`: Diagrama completo desde autenticación hasta registro en BD
- `12-flujos-integrados-completos.md`: Visualización de los 3 flujos principales integrados

## 4.3. Modelo Entidad-Relación (ER)

El modelo de base de datos detallado con todas las tablas, relaciones y campos se encuentra en:
- `11-diagrama-er-tablas.md`: Diagrama ER completo con 15+ tablas

**Tablas Principales:**
- USUARIOS
- ÁREAS
- USUARIOS_AUTORIZADOS_ÁREA
- SISTEMAS
- SISTEMAS_AUTORIZADOS_POR_ÁREA
- HISTORIAL_CAMBIOS
- PROBLEMAS_REPORTADOS
- CONTROL_INCIDENCIAS
- SESIONES_ACTIVAS
- AUDIT_LOGIN
- AUDIT_ACCESO_NO_AUTORIZADO
- AUDIT_SISTEMAS_NUEVOS
- AUDIT_MODIFICACIONES
- SLA_DEFINICIONES
- UPTIME_SISTEMA

## 4.4. Arquitectura del Sistema

```
┌─────────────────────────────────────────────────────────────┐
│                      CAPA DE PRESENTACIÓN                    │
│   (Navegador Web - HTML5, CSS3, JavaScript)                 │
└───────────────┬─────────────────────────────────────────────┘
                │ HTTPS (TLS 1.2+)
                ▼
┌─────────────────────────────────────────────────────────────┐
│                      CAPA DE APLICACIÓN                      │
│   (Servidor Web - Backend: .NET/Java/Python)                │
│   - Controladores de Formularios                            │
│   - Módulo de Autenticación                                 │
│   - Lógica de Negocio                                       │
│   - Generación de Reportes                                  │
└───────────────┬─────────────────────────────────────────────┘
                │ SQL / ORM
                ▼
┌─────────────────────────────────────────────────────────────┐
│                      CAPA DE DATOS                           │
│   (Base de Datos Relacional - SQL Server/PostgreSQL/MySQL)  │
│   - Tablas de Negocio                                       │
│   - Tablas de Auditoría                                     │
└─────────────────────────────────────────────────────────────┘
```

---

## Referencias

- IEEE Std 830-1998: Prácticas Recomendadas para Especificaciones de Requisitos de Software
- Propuesta Integrada del Sistema ISSEG (SISTEMA-ISSEG-PROPUESTA-INTEGRADA.md)
- Documentación Complementaria en carpeta `/docmentacion`:
  - 01-diagrama-flujo-tickets.md
  - 02-formularios-estructurados.md
  - 11-diagrama-er-tablas.md
  - 12-flujos-integrados-completos.md

---

**FIN DEL DOCUMENTO**

**Firmas de Aprobación:**

| Rol | Nombre | Firma | Fecha |
|---|---|---|---|
| Analista/Co-autor | Jacqueline Hurtado Hernández | _____________ | ___/___/___ |
| Analista/Co-autor | Edwin Eduardo Mercado Ruiz | _____________ | ___/___/___ |
| Patrocinador | [Director TI ISSEG] | _____________ | ___/___/___ |
