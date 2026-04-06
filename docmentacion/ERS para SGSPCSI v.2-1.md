|  |
| --- |

Especificación de requisitos de software

Proyecto: Desarrollo del Sistema de Gestión de Solicitudes de Proyectos de la Coordinación de Sistemas Institucionales (SGSPCSI)

Revisión

| ![](./ERS%20para%20SGSPCSI%20v.2-1_images/image-001.png) |  | Marzo/2026 |
| --- | --- | --- |

Contenido

Contenido 2

1 Historial de versiones 4

2 Introducción 4

2.1 Alcance 4

2.2 Definiciones, acrónimos y abreviaturas: 5

2.3 Resumen del documento: 5

2.4 Personal involucrado 5

3 Descripción general 6

3.1 Perspectiva del producto 6

3.2 Funcionalidad del producto 7

3.3 Características de los usuarios 7

3.4 Restricciones 7

4 Requisitos específicos 8

4.1 Requisitos comunes de los interfaces 8

4.1.1 Interfaces de usuario 9

4.1.2 Interfaces de hardware 9

4.1.3 Interfaces de software 9

4.1.4 Interfaces de comunicación 10

4.2 Requisitos funcionales 11

4.2.1 Requisito funcional 1 11

4.2.2 Requisito funcional 2 11

4.2.3 Requisito funcional 3 11

4.2.4 Requisito funcional 4 12

4.2.5 Requisito funcional 5 12

4.2.6 Requisito funcional 6 12

4.2.7 Requisito funcional 7 12

4.2.8 Requisito funcional 8 12

4.2.9 Requisito funcional 9 13

4.2.10 Requisito funcional 10 13

4.2.11 Requisito funcional 11 13

4.2.12 Requisito funcional 12 13

4.2.13 Requisito funcional 13 13

4.2.14 Requisito funcional 14 14

4.2.15 Requisito funcional 15 14

4.2.16 Requisito funcional 16 14

4.2.17 Requisito funcional 17 14

4.2.18 Requisito funcional 18 14

4.2.19 Requisito funcional 19 15

4.2.20 Requisito funcional 20 15

4.3 Requisitos no funcionales 15

4.3.1 Requisito de rendimiento 1 15

4.3.2 Requisito de rendimiento 2 15

4.3.3 Requisito de rendimiento 3 16

4.3.4 Requisito de rendimiento 4 16

4.3.5 Requisito de Seguridad 1 16

4.3.6 Requisito de Seguridad 2 16

4.3.7 Requisito de Seguridad 3 17

4.3.8 Requisito de Seguridad 4 17

4.3.9 Requisito de Fiabilidad 1 17

4.3.10 Requisito de Fiabilidad 2 17

4.3.11 Requisito de disponibilidad 1 18

4.3.12 Requisito de disponibilidad 2 18

4.3.13 Requisito de mantenibilidad 1 18

4.3.14 Requisito de mantenibilidad 2 18

4.3.15 Requisito de portabilidad 1 19

4.3.16 Requisito de portabilidad 2 19

4.4 Otros requisitos 19

5 Modelado del Sistema 20

# Historial de versiones

| **Versión** | **Fecha** | **Autor** | **Descripción** |
| --- | --- | --- | --- |
| 1.0 | 03/03/2026 | Edwin Eduardo Mercado Ruíz | Creación inicial del documento |
| 1.1 | 03/03/2026 | Jacqueline Hurtado Hernández | Definición y modificación del formato ERS simplificado. |
| 1.2 | 03/03/2026 | Jacqueline Hurtado Hernández y Edwin Eduardo Mercado Ruíz | Análisis de la información obtenida hasta el momento e implementación de la introducción, alcance y definiciones. |
| 1.3 | 04/03/2026 | Edwin Eduardo Mercado Ruíz | Desarrollo de descripción general y perspectiva del producto |
| 1.4 | 04/03/2026 | Jacqueline Hurtado Hernández | Definición de interfaces de usuario, hardware y software |
| 1.5 | 04/03/2026 | Jacqueline Hurtado Hernández y Edwin Eduardo Mercado Ruíz | Elaboración de requisitos funcionales del sistema |
| 1.6 | 05/03/2026 | Jacqueline Hurtado Hernández y Edwin Eduardo Mercado Ruíz | Definición y clasificación de requisitos no funcionales del sistema |
| 1.7 | 05/03/2026 | Edwin Eduardo Mercado Ruíz | Revisión de los requisitos obtenidos y creación de otros requisitos |
| 1.8 | 05/03/2026 | Jacqueline Hurtado Hernández | Revisión del diagrama de flujo para la sección de modelado del sistema |
| 1.9 | 06/03/2026 | Jacqueline Hurtado Hernández y Edwin Eduardo Mercado Ruíz | Revisión general y modificación de algunas faltas ortográficas y redundancias dentro del documento. |
| 2.0 | 06/03/2026 | Jacqueline Hurtado Hernández y Edwin Eduardo Mercado Ruíz | Entrega del producto obtenido para su revisión y mejoras |
| 2.1 | 23/03/2026 | Jacqueline Hurtado Hernández y Edwin Eduardo Mercado Ruíz | Inicio de cambios mencionados en el correo |
| 2.2 | 24/03/2026 | Jacqueline Hurtado Hernández y Edwin Eduardo Mercado Ruíz | Cambio de estructura y redacción de los requisitos y diagrama de flujo |

# Introducción

El propósito de este documento es proporcionar una especificación completa de los requisitos del Sistema de Gestión de Solicitudes de Proyectos de la Coordinación de Sistemas Institucionales (SGSPCSI) del Instituto de Seguridad Social del Estado de Guanajuato (ISSEG).

Actualmente, la Coordinación de Sistemas Institucionales gestiona las solicitudes de desarrollo de nuevos sistemas, mantenimiento correctivo y modificaciones mediante procesos manuales que involucran correos electrónicos, documentos físicos y comunicación verbal. Esto provoca pérdida de trazabilidad, retrasos en la asignación de tareas y dificultad para medir el esfuerzo del equipo de desarrollo.

El sistema SGSPCSI busca proporcionar una plataforma digital centralizada que permita registrar, evaluar, asignar y dar seguimiento a las solicitudes de desarrollo de software dentro del Instituto.

Este documento describe las funcionalidades, restricciones, requisitos funcionales y no funcionales del sistema, sirviendo como referencia para el diseño, desarrollo e implementación del sistema.

## Alcance

El sistema SGSPCSI está diseñado para apoyar al área de desarrollo de la Coordinación de Sistemas Institucionales (CSI) de la Dirección de Tecnologías de Información (DTI) del Instituto de Seguridad Social del Estado de Guanajuato.

El sistema permitirá gestionar de manera centralizada las solicitudes relacionadas con:

-   Desarrollo de nuevos sistemas  
    
-   Modificación o mejora de sistemas existentes  
    
-   Corrección de errores en sistemas institucionales  
    
-   Registro y seguimiento de incidencias urgentes  
    

El sistema proporcionará una plataforma web que permitirá a los usuarios registrar solicitudes, al Product Manager evaluar la viabilidad de los proyectos y asignarlos a desarrolladores, así como llevar un registro del tiempo invertido y el seguimiento del desarrollo.

El objetivo principal es mejorar la trazabilidad de las solicitudes, optimizar la asignación de recursos del área de desarrollo y generar métricas que permitan tomar decisiones estratégicas basadas en datos.

## Definiciones, acrónimos y abreviaturas:

| **Término** | **Definición** |
| --- | --- |
| SGSPCSI | Sistema de Gestión de Solicitudes de Proyectos de la Coordinación de Sistemas Institucionales |
| ISSEG | Instituto de Seguridad Social del Estado de Guanajuato |
| CSI | Coordinación de Sistemas Institucionales |
| DTI | Dirección de Tecnologías de Información |
| PM | Product Manager encargado de evaluar las solicitudes |
| API | Interfaz de programación de aplicaciones |
| Front-end | Parte visual del sistema con la que interactúa el usuario |
| Back-end | Lógica del sistema que procesa la información |
| Bitácora | Registro de actividades realizadas por los desarrolladores |

## Resumen del documento:

El presente documento tiene como finalidad describir la Especificación de Requisitos de Software del Sistema de Gestión de Solicitudes de Proyectos de la Coordinación de Sistemas Institucionales (SGSPCSI) del Instituto de Seguridad Social del Estado de Guanajuato (ISSEG). Este sistema surge como una iniciativa para fortalecer la gestión y control de las solicitudes relacionadas con el desarrollo, mantenimiento y mejora de los sistemas institucionales, mediante la implementación de una plataforma que permita registrar, evaluar, priorizar, asignar y dar seguimiento a dichas solicitudes de manera estructurada y trazable. En este documento se establecen los elementos necesarios para definir el comportamiento esperado del sistema, incluyendo su contexto operativo, alcance, actores involucrados, restricciones tecnológicas y organizacionales, así como los requisitos funcionales y no funcionales que deberán cumplirse para garantizar su adecuado funcionamiento. Asimismo, se describen las interfaces de interacción del sistema y los lineamientos generales que servirán como base para las etapas posteriores de diseño, desarrollo, implementación y mantenimiento de la solución tecnológica, contribuyendo a mejorar la eficiencia operativa y la gestión de los proyectos de desarrollo dentro de la Coordinación de Sistemas Institucionales.

## Personal involucrado

| Nombre | Jacqueline Hurtado Hernández |
| --- | --- |
| Rol | Residente desarrollador y analista |
| Categoría profesional | Estudiante ISC |
| Responsabilidades | Análisis de requisitos, documentación y desarrollo del sistema |
| Información de contacto | [jacqueline161718@gmail.com](mailto:jacqueline161718@gmail.com) |
| Aprobación |  |

| Nombre | Edwin Eduardo Mercado Ruíz |
| --- | --- |
| Rol | Residente desarrollador y analista |
| Categoría profesional | Estudiante ISC |
| Responsabilidades | Análisis de requisitos, documentación y desarrollo del sistema |
| Información de contacto | [eduardo0520mr@gmail.com](mailto:eduardo0520mr@gmail.com) |
| Aprobación |  |

| Nombre | Karla Teresa Arroyo Calero |
| --- | --- |
| Rol | Asesora externa |
| Categoría profesional | Jefa del área de Desarrollo de Software |
| Responsabilidades | Supervisión técnica del proyecto |
| Información de contacto | [karroyoca@isseg.gob.mx](mailto:karroyoca@isseg.gob.mx) |
| Aprobación |  |

| Nombre | Alma Lilia Núñez González |
| --- | --- |
| Rol | Asesora Interna |
| Categoría profesional | Profesora del área de Ingeniería de Software |
| Responsabilidades | Supervisión y apoyo con dudas técnicas del proyecto |
| Información de contacto | [alma.ng@morelia.tecnm.mx](mailto:alma.ng@morelia.tecnm.mx) |
| Aprobación |  |

# Descripción general

Actualmente, la Coordinación de Sistemas Institucionales de la Dirección de Tecnologías de Información del ISSEG recibe múltiples solicitudes relacionadas con el desarrollo de software, mantenimiento de sistemas y resolución de incidencias.

Estas solicitudes se gestionan mediante correos electrónicos, documentos físicos o comunicación directa, lo que provoca dificultades para llevar un seguimiento adecuado de cada requerimiento, pérdida de información y falta de métricas que permitan evaluar el desempeño del área de desarrollo.

El sistema SGSPCSI busca resolver estos problemas mediante la implementación de una plataforma digital que permita centralizar la recepción, evaluación, asignación y seguimiento de solicitudes de desarrollo.

Esto permitirá mejorar la eficiencia operativa del área, garantizar la trazabilidad de las solicitudes y facilitar la generación de reportes y métricas sobre el trabajo realizado.

## Perspectiva del producto

El SGSPCSI es una plataforma web institucional diseñada para gestionar de forma centralizada las solicitudes relacionadas con el desarrollo, mantenimiento y mejora de los sistemas informáticos utilizados por el ISSEG.

El sistema formará parte del ecosistema tecnológico de la DTI y se integrará con la infraestructura tecnológica existente del instituto, respetando los estándares de seguridad y desarrollo establecidos por la CSI.

El sistema será desarrollado utilizando las siguientes tecnologías:

-   Front-end: Angular
-   Back-end: API en C# .NET
-   Base de datos: SQL Server

## Funcionalidad del producto

El sistema SGSPCSI proporcionará las siguientes funcionalidades principales:

-   **Gestión de solicitudes de desarrollo**

El sistema permitirá registrar solicitudes para el desarrollo de nuevos sistemas o modificaciones de sistemas existentes.

-   **Evaluación de solicitudes**

El PM podrá evaluar la viabilidad técnica y operativa de las solicitudes registradas.

-   **Gestión de incidencias urgentes**

El sistema permitirá registrar incidencias críticas que requieran atención inmediata por parte del área de desarrollo.

-   **Asignación de desarrolladores**

Las solicitudes aprobadas podrán ser asignadas a desarrolladores responsables para su implementación.

-   **Seguimiento del desarrollo**

El sistema permitirá registrar el avance del desarrollo y consultar el estado de cada solicitud.

-   **Registro de esfuerzo técnico**

Los desarrolladores podrán registrar las actividades realizadas y el tiempo invertido en cada solicitud.

-   **Generación de reportes**

El sistema generará reportes y métricas que permitan analizar la carga de trabajo y el rendimiento del área de desarrollo.

## Características de los usuarios

| Tipo de usuario | Usuario solicitante |
| --- | --- |
| Formación | Personal administrativo o técnico |
| Habilidades | Conocimiento básico de sistemas informáticos |
| Actividades | Registrar solicitudes de desarrollo, consultar el estado de sus solicitudes y revisar el seguimiento del requerimiento. |

| Tipo de usuario | Product Manager |
| --- | --- |
| Formación | Profesional del área de desarrollo |
| Habilidades | Gestión de proyectos, análisis de requerimientos y toma de decisiones técnicas |
| Actividades | Evaluar solicitudes registradas, aprobar o rechazar requerimientos, asignar desarrolladores responsables y consultar métricas del sistema para supervisar el trabajo del área de desarrollo. |

| Tipo de usuario | Desarrollador |
| --- | --- |
| Formación | Ingeniero de software o desarrollador de sistemas |
| Habilidades | Programación, mantenimiento de software y análisis técnico |
| Actividades | Desarrollar o modificar sistemas según las solicitudes asignadas, registrar actividades realizadas y reportar el tiempo invertido en cada solicitud. |

## Restricciones

El desarrollo del sistema SGSPCSI estará sujeto a las siguientes restricciones:

-   El sistema deberá desarrollarse utilizando **Angular para el Front-end**.  
    
-   El back-end deberá implementarse mediante **API en C# .NET**.  
    
-   La base de datos deberá utilizar **SQL Server**.  
    
-   El sistema deberá operar dentro de la infraestructura tecnológica del ISSEG.  
    
-   El acceso al sistema estará restringido a usuarios autorizados dentro de la red institucional.

# Requisitos específicos

Esta sección describe de manera detallada las entradas, salidas e interfaces del sistema SGSPCSI, así como los requisitos específicos que deberá cumplir para operar dentro de la infraestructura tecnológica de la DTI del ISSEG. El nivel de detalle de esta sección permitirá que el equipo de desarrollo diseñe e implemente el sistema, y que el equipo de pruebas determine si se satisfacen los requisitos establecidos.

## Requisitos comunes de los interfaces

**Entradas del sistema**

**1) Entradas de usuario (interacción por interfaz web):**

-   Los usuarios interactuarán con el sistema mediante una interfaz gráfica web (GUI) accesible desde navegadores. Las entradas incluirán:
-   Formularios de captura para registrar solicitudes (nuevo sistema, modificación/mejora o incidencia urgente).
-   Campos de texto para descripción del requerimiento, contexto, justificación y/o detalles técnicos.
-   Selección de catálogo para elegir un sistema institucional existente (cuando aplique).
-   Botones y acciones para enviar, guardar borradores, cancelar, actualizar estatus o cerrar folios.
-   Carga de evidencia (por ejemplo: capturas de pantalla, documentos de apoyo) según políticas internas.

**2) Entradas de otros componentes del sistema:**

-   Solicitudes de autenticación/autorización (módulo institucional o mecanismo definido por la CSI).
-   Consultas y transacciones a la base de datos SQL Server para guardar/actualizar solicitudes, bitácoras, catálogos y estados.
-   Notificaciones internas del sistema (por ejemplo: avisos al PM o al desarrollador asignado).

**Salidas del sistema**

**1) Salidas hacia el usuario (presentación en GUI):**

-   Confirmaciones de registro de solicitud (folio generado).
-   Visualización de estatus y seguimiento (pendiente, en evaluación, aprobado, rechazado, asignado, en desarrollo, cerrado).
-   Detalle de solicitudes y bitácoras asociadas.
-   Panel de métricas y reportes (según rol).
-   Descarga de solicitud.

**2) Salidas hacia otros componentes:**

-   Registros de auditoría/bitácora de acciones.
-   Notificaciones a PM y desarrolladores (según configuración institucional).
-   Reportes exportables (si se define como funcionalidad).

### Interfaces de usuario

El sistema contará con una interfaz web accesible mediante la red institucional. La interfaz deberá mantener consistencia visual en todos los módulos y utilizar formularios estructurados para el registro y gestión de solicitudes.

Las principales pantallas del sistema serán:

-   Inicio de sesión
-   Registro de solicitud
-   Bandeja de solicitudes
-   Evaluación de solicitudes
-   Asignación de desarrollador
-   Seguimiento y bitácora
-   Reportes y métricas

La interfaz deberá ser intuitiva, permitiendo que usuarios con conocimientos básicos de sistemas puedan interactuar con el sistema sin necesidad de capacitación especializada.

### Interfaces de hardware

El sistema SGSPCSI estará alojado en infraestructura de la DTI del ISSEG (servidores de desarrollo/calidad/producción según el ambiente), y será consumido desde equipos de cómputo del personal institucional.

Hardware requerido (referencial, sujeto a lo que determine DTI):

-   Servidor(es) para hospedar la aplicación (API .NET y Front-end Angular desplegado).
-   Servidor de base de datos SQL Server (o instancia institucional existente).
-   Equipos cliente (PC/laptop) para usuarios solicitantes, PM y desarrolladores

| Número de requisito | RH1 |  |  |
| --- | --- | --- | --- |
| Nombre de requisito | Acceso desde equipos institucionales |  |  |
| Tipo | ☒ Requisito | ☐ Restricción |  |
| Fuente del requisito | Usuario |  |  |
| Descripción | Como usuario, se requiere el acceso al sistema desde equipos de cómputo institucionales conectados a la red del ISSEG para su uso en horario laboral. |  |  |
| Prioridad del requisito | ☒ Alta/Esencial | ☐ Media/Deseado | ☐ Baja/ Opcional |

| Número de requisito | RH2 |  |  |
| --- | --- | --- | --- |
| Nombre de requisito | Infraestructura para ambientes de prueba |  |  |
| Tipo | ☒ Requisito | ☐ Restricción |  |
| Fuente del requisito | CSI |  |  |
| Descripción | Como CSI, se requiere contar con ambientes de desarrollo y pruebas para validar el sistema antes de su liberación a producción y evitar afectaciones operativas. |  |  |
| Prioridad del requisito | ☐ Alta/Esencial | ☒ Media/Deseado | ☐ Baja/ Opcional |

### Interfaces de software

El sistema SGSPCSI interactuará con componentes de software internos, incluyendo:

-   **Base de datos SQL Server** para persistencia de solicitudes, catálogos, bitácoras, usuarios/roles (según el modelo definido).
-   **API Back-end en C# .NET** para exponer endpoints de registro, consulta, validación, asignación, bitácora y reportes.
-   **Front-end Angular** para la interfaz de usuario.
-   **Servicio/mecanismo de autenticación institucional** (según lo definido por DTI).
-   (Opcional) Servicio de notificaciones por correo institucional si se integra.

| Número de requisito | RSF1 |  |  |
| --- | --- | --- | --- |
| Nombre de requisito | Persistencia en SQL Server |  |  |
| Tipo | ☒ Requisito | ☐ Restricción |  |
| Fuente del requisito | Sistema |  |  |
| Descripción | Como sistema, se requiere el almacenamiento de información de solicitudes, estados, catálogos y bitácoras en una base de datos SQL Server para asegurar trazabilidad y consulta histórica |  |  |
| Prioridad del requisito | ☒ Alta/Esencial | ☐ Media/Deseado | ☐ Baja/ Opcional |

| Número de requisito | RSF2 |  |  |
| --- | --- | --- | --- |
| Nombre de requisito | API central de operación |  |  |
| Tipo | ☒ Requisito | ☐ Restricción |  |
| Fuente del requisito | Sistema |  |  |
| Descripción | Como sistema, se requiere la operación mediante una API en C# .NET para centralizar la lógica de negocio, aplicar reglas de seguridad y permitir mantenimiento controlado. |  |  |
| Prioridad del requisito | ☒ Alta/Esencial | ☐ Media/Deseado | ☐ Baja/ Opcional |

| Número de requisito | RSF3 |  |  |
| --- | --- | --- | --- |
| Nombre de requisito | Cliente web angular |  |  |
| Tipo | ☒ Requisito | ☐ Restricción |  |
| Fuente del requisito | Usuario |  |  |
| Descripción | Como usuario, se requiere que la interfaz esté desarrollada en Angular para ofrecer una experiencia de uso fluida y formularios dinámicos sin recargas constantes. |  |  |
| Prioridad del requisito | ☐ Alta/Esencial | ☒ Media/Deseado | ☐ Baja/ Opcional |

| Número de requisito | RSF4 |  |  |
| --- | --- | --- | --- |
| Nombre de requisito | Autenticación por usuario de dominio |  |  |
| Tipo | ☒ Requisito | ☐ Restricción |  |
| Fuente del requisito | Seguridad/DTI |  |  |
| Descripción | Como institución, se requiere la autenticación de usuarios mediante el usuario de dominio institucional para asegurar que solo personal autorizado de la red interna tenga acceso. |  |  |
| Prioridad del requisito | ☒ Alta/Esencial | ☐ Media/Deseado | ☐ Baja/ Opcional |

### Interfaces de comunicación

El sistema se comunicará bajo arquitectura cliente-servidor:

● Cliente (navegador) ↔ Front-end Angular ↔ API .NET ↔ SQL Server

● Comunicación sobre HTTP.

| Número de requisito | RC1 |  |  |
| --- | --- | --- | --- |
| Nombre de requisito | Comunicación cliente-servidor |  |  |
| Tipo | ☒ Requisito | ☐ Restricción |  |
| Fuente del requisito | Sistema |  |  |
| Descripción | Como sistema, se requiere que la comunicación entre el cliente web y la API se realice mediante servicios HTTP para permitir el consumo estandarizado de funcionalidades dentro de la red interna. |  |  |
| Prioridad del requisito | ☒ Alta/Esencial | ☐ Media/Deseado | ☐ Baja/ Opcional |

| Número de requisito | RC2 |  |  |
| --- | --- | --- | --- |
| Nombre de requisito | Comunicación segura en red institucional |  |  |
| Tipo | ☒ Requisito | ☐ Restricción |  |
| Fuente del requisito | Seguridad/DTI |  |  |
| Descripción | Como institución, se requiere que las comunicaciones del sistema se realicen bajo los protocolos definidos por la DTI para proteger la integridad de la información transmitida. |  |  |
| Prioridad del requisito | ☒ Alta/Esencial | ☐ Media/Deseado | ☐ Baja/ Opcional |

## Requisitos funcionales

### Requisito funcional 1

| Número de requisito | RF1 |  |  |
| --- | --- | --- | --- |
| Nombre de requisito | Registro de solicitudes |  |  |
| Tipo | ☒ Requisito | ☐ Restricción |  |
| Fuente del requisito | Usuario solicitante |  |  |
| Descripción | Como usuario, se requiere el registro de solicitudes de desarrollo o mantenimiento mediante un formulario digital para su evaluación. |  |  |
| Prioridad del requisito | ☒ Alta/Esencial | ☐ Media/Deseado | ☐ Baja/ Opcional |

### Requisito funcional 2

| Número de requisito | RF2 |  |  |
| --- | --- | --- | --- |
| Nombre de requisito | Clasificación de solicitudes |  |  |
| Tipo | ☒ Requisito | ☐ Restricción |  |
| Fuente del requisito | Sistema |  |  |
| Descripción | Como sistema, se requiere la clasificación automática de solicitudes por tipo (nuevo sistema, modificación o incidencia) para facilitar su gestión. |  |  |
| Prioridad del requisito | ☒ Alta/Esencial | ☐ Media/Deseado | ☐ Baja/ Opcional |

### Requisito funcional 3

| Número de requisito | RF3 |  |  |
| --- | --- | --- | --- |
| Nombre de requisito | Generación de folio |  |  |
| Tipo | ☒ Requisito | ☐ Restricción |  |
| Fuente del requisito | Sistema |  |  |
| Descripción | Como sistema, se requiere la generación de un folio único por solicitud para permitir su identificación y seguimiento. |  |  |
| Prioridad del requisito | ☒ Alta/Esencial | ☐ Media/Deseado | ☐ Baja/ Opcional |

### Requisito funcional 4

| Número de requisito | RF4 |  |  |
| --- | --- | --- | --- |
| Nombre de requisito | Registro de solicitudes urgentes |  |  |
| Tipo | ☒ Requisito | ☐ Restricción |  |
| Fuente del requisito | Usuario solicitante |  |  |
| Descripción | Como usuario, se requiere el registro de solicitudes urgentes por fallas críticas para su atención prioritaria. |  |  |
| Prioridad del requisito | ☒ Alta/Esencial | ☐ Media/Deseado | ☐ Baja/ Opcional |

### Requisito funcional 5

| Número de requisito | RF5 |  |  |
| --- | --- | --- | --- |
| Nombre de requisito | Evaluación de solicitudes |  |  |
| Tipo | ☒ Requisito | ☐ Restricción |  |
| Fuente del requisito | Product Manager |  |  |
| Descripción | Como Product Manager, se requiere la evaluación de viabilidad técnica y operativa de las solicitudes registradas antes de su aprobación. |  |  |
| Prioridad del requisito | ☒ Alta/Esencial | ☐ Media/Deseado | ☐ Baja/ Opcional |

### Requisito funcional 6

| Número de requisito | RF6 |  |  |
| --- | --- | --- | --- |
| Nombre de requisito | Aprobación o rechazo de solicitudes |  |  |
| Tipo | ☒ Requisito | ☐ Restricción |  |
| Fuente del requisito | Product Manager |  |  |
| Descripción | Como Product Manager, se requiere la aprobación o rechazo de solicitudes para decidir los requerimientos que serán atendidos. |  |  |
| Prioridad del requisito | ☒ Alta/Esencial | ☐ Media/Deseado | ☐ Baja/ Opcional |

### Requisito funcional 7

| Número de requisito | RF7 |  |  |
| --- | --- | --- | --- |
| Nombre de requisito | Notificación de resultado de evaluación |  |  |
| Tipo | ☒ Requisito | ☐ Restricción |  |
| Fuente del requisito | Sistema |  |  |
| Descripción | Como sistema, se requiere la notificación al usuario solicitante sobre el resultado (aprobación/rechazo) de su requerimiento. |  |  |
| Prioridad del requisito | ☒ Alta/Esencial | ☐ Media/Deseado | ☐ Baja/ Opcional |

### Requisito funcional 8

| Número de requisito | RF8 |  |  |
| --- | --- | --- | --- |
| Nombre de requisito | Asignación de desarrollador |  |  |
| Tipo | ☒ Requisito | ☐ Restricción |  |
| Fuente del requisito | Product Manager |  |  |
| Descripción | Como Product Manager, se requiere la asignación de solicitudes aprobadas a un desarrollador responsable para iniciar el proceso de atención. |  |  |
| Prioridad del requisito | ☒ Alta/Esencial | ☐ Media/Deseado | ☐ Baja/ Opcional |

### Requisito funcional 9

| Número de requisito | RF9 |  |  |
| --- | --- | --- | --- |
| Nombre de requisito | Registro de requerimientos técnicos |  |  |
| Tipo | ☒ Requisito | ☐ Restricción |  |
| Fuente del requisito | Desarrollador |  |  |
| Descripción | Como desarrollador, se requiere el registro de los requerimientos técnicos detallados para documentar la información necesaria para el desarrollo. |  |  |
| Prioridad del requisito | ☒ Alta/Esencial | ☐ Media/Deseado | ☐ Baja/ Opcional |

### Requisito funcional 10

| Número de requisito | RF10 |  |  |
| --- | --- | --- | --- |
| Nombre de requisito | Seguimiento de solicitudes |  |  |
| Tipo | ☒ Requisito | ☐ Restricción |  |
| Fuente del requisito | Usuario |  |  |
| Descripción | Como usuario, se requiere la consulta del estado de las solicitudes registradas para conocer el avance del proceso. |  |  |
| Prioridad del requisito | ☐ Alta/Esencial | ☒ Media/Deseado | ☐ Baja/ Opcional |

### Requisito funcional 11

| Número de requisito | RF11 |  |  |
| --- | --- | --- | --- |
| Nombre de requisito | Actualización de estado de solicitudes |  |  |
| Tipo | ☒ Requisito | ☐ Restricción |  |
| Fuente del requisito | Sistema |  |  |
| Descripción | Como sistema, se requiere la actualización del estado de la solicitud durante su ciclo de vida para reflejar su progreso. |  |  |
| Prioridad del requisito | ☒ Alta/Esencial | ☐ Media/Deseado | ☐ Baja/ Opcional |

### Requisito funcional 12

| Número de requisito | RF12 |  |  |
| --- | --- | --- | --- |
| Nombre de requisito | Registro de actividades del desarrollador |  |  |
| Tipo | ☒ Requisito | ☐ Restricción |  |
| Fuente del requisito | Desarrollador |  |  |
| Descripción | Como desarrollador, se requiere el registro de las actividades realizadas en cada solicitud para documentar el trabajo técnico. |  |  |
| Prioridad del requisito | ☒ Alta/Esencial | ☐ Media/Deseado | ☐ Baja/ Opcional |

### Requisito funcional 13

| Número de requisito | RF13 |  |  |
| --- | --- | --- | --- |
| Nombre de requisito | Registro de tiempo invertido |  |  |
| Tipo | ☒ Requisito | ☐ Restricción |  |
| Fuente del requisito | Desarrollador |  |  |
| Descripción | Como desarrollador, se requiere el registro del tiempo invertido en cada actividad para justificar el esfuerzo técnico dedicado. |  |  |
| Prioridad del requisito | ☒ Alta/Esencial | ☐ Media/Deseado | ☐ Baja/ Opcional |

### Requisito funcional 14

| Número de requisito | RF14 |  |  |
| --- | --- | --- | --- |
| Nombre de requisito | Gestión de bitácora |  |  |
| Tipo | ☒ Requisito | ☐ Restricción |  |
| Fuente del requisito | Sistema |  |  |
| Descripción | Como sistema, se requiere el registro de una bitácora de actividades y cambios para mantener un historial completo del proceso. |  |  |
| Prioridad del requisito | ☒ Alta/Esencial | ☐ Media/Deseado | ☐ Baja/ Opcional |

### Requisito funcional 15

| Número de requisito | RF15 |  |  |
| --- | --- | --- | --- |
| Nombre de requisito | Cierre de solicitud |  |  |
| Tipo | ☒ Requisito | ☐ Restricción |  |
| Fuente del requisito | Desarrollador |  |  |
| Descripción | Como desarrollador, se requiere el cierre de la solicitud una vez finalizado el desarrollo para indicar que el requerimiento fue atendido. |  |  |
| Prioridad del requisito | ☒ Alta/Esencial | ☐ Media/Deseado | ☐ Baja/ Opcional |

### Requisito funcional 16

| Número de requisito | RF16 |  |  |
| --- | --- | --- | --- |
| Nombre de requisito | Registro de esfuerzo final |  |  |
| Tipo | ☒ Requisito | ☐ Restricción |  |
| Fuente del requisito | Sistema |  |  |
| Descripción | Como sistema, se requiere el registro del esfuerzo total invertido por solicitud para generar métricas de rendimiento. |  |  |
| Prioridad del requisito | ☒ Alta/Esencial | ☐ Media/Deseado | ☐ Baja/ Opcional |

### Requisito funcional 17

| Número de requisito | RF17 |  |  |
| --- | --- | --- | --- |
| Nombre de requisito | Generación de reportes |  |  |
| Tipo | ☒ Requisito | ☐ Restricción |  |
| Fuente del requisito | Product Manager |  |  |
| Descripción | Como Product Manager, se requiere la generación de reportes de atención, tiempos y carga de trabajo para analizar el desempeño del área. |  |  |
| Prioridad del requisito | ☒ Alta/Esencial | ☐ Media/Deseado | ☐ Baja/ Opcional |

### Requisito funcional 18

| Número de requisito | RF18 |  |  |
| --- | --- | --- | --- |
| Nombre de requisito | Consulta de métricas |  |  |
| Tipo | ☒ Requisito | ☐ Restricción |  |
| Fuente del requisito | Product Manager |  |  |
| Descripción | Como Product Manager, se requiere la consulta de métricas del sistema para identificar tendencias en la demanda de desarrollo. |  |  |
| Prioridad del requisito | ☒ Alta/Esencial | ☐ Media/Deseado | ☐ Baja/ Opcional |

### Requisito funcional 19

| Número de requisito | RF19 |  |  |
| --- | --- | --- | --- |
| Nombre de requisito | Gestión de catálogo de sistemas |  |  |
| Tipo | ☒ Requisito | ☐ Restricción |  |
| Fuente del requisito | Product Manager |  |  |
| Descripción | Como Product Manager, se requiere la gestión del catálogo de sistemas institucionales para la correcta selección del sistema al registrar una solicitud. |  |  |
| Prioridad del requisito | ☒ Alta/Esencial | ☐ Media/Deseado | ☐ Baja/ Opcional |

### Requisito funcional 20

| Número de requisito | RF20 |  |  |
| --- | --- | --- | --- |
| Nombre de requisito | Búsqueda de solicitudes |  |  |
| Tipo | ☒ Requisito | ☐ Restricción |  |
| Fuente del requisito | Usuario |  |  |
| Descripción | Como usuario, se requiere la búsqueda de solicitudes mediante filtros (folio, tipo, estado) para localizar información rápidamente. |  |  |
| Prioridad del requisito | ☒ Alta/Esencial | ☐ Media/Deseado | ☐ Baja/ Opcional |

## Requisitos no funcionales

### Requisito de rendimiento 1

| Número de requisito | RR1 |  |  |
| --- | --- | --- | --- |
| Nombre de requisito | Tiempo de respuesta del sistema |  |  |
| Tipo | ☒ Requisito | ☐ Restricción |  |
| Fuente del requisito | Usuario |  |  |
| Descripción | Como usuario, se requiere que el sistema procese las operaciones en menos de 3 segundos para garantizar la eficiencia. |  |  |
| Prioridad del requisito | ☒ Alta/Esencial | ☐ Media/Deseado | ☐ Baja/ Opcional |

### Requisito de rendimiento 2

| Número de requisito | RR2 |  |  |
| --- | --- | --- | --- |
| Nombre de requisito | Soporte de usuarios concurrentes |  |  |
| Tipo | ☒ Requisito | ☐ Restricción |  |
| Fuente del requisito | Sistema |  |  |
| Descripción | Como sistema, Se requiere el soporte de al menos 50 usuarios concurrentes para permitir el uso simultáneo de la plataforma sin afectar el rendimiento. |  |  |
| Prioridad del requisito | ☒ Alta/Esencial | ☐ Media/Deseado | ☐ Baja/ Opcional |

### Requisito de rendimiento 3

| Número de requisito | RR3 |  |  |
| --- | --- | --- | --- |
| Nombre de requisito | Tiempo de carga de información |  |  |
| Tipo | ☒ Requisito | ☐ Restricción |  |
| Fuente del requisito | Usuario |  |  |
| Descripción | Como usuario, se requiere q ue los listados de solicitudes se carguen en un tiempo menor a 5 segundos para agilizar la consulta de información. |  |  |
| Prioridad del requisito | ☐ Alta/Esencial | ☒ Media/Deseado | ☐ Baja/ Opcional |

### Requisito de rendimiento 4

| Número de requisito | RR4 |  |  |
| --- | --- | --- | --- |
| Nombre de requisito | Procesamiento de reportes |  |  |
| Tipo | ☒ Requisito | ☐ Restricción |  |
| Fuente del requisito | Product Manager |  |  |
| Descripción | Como Product Manager, se requiere que la generación de reportes se realice en un tiempo máximo de 10 segundos para el análisis eficiente de la información. |  |  |
| Prioridad del requisito | ☒ Alta/Esencial | ☐ Media/Deseado | ☐ Baja/ Opcional |

### Requisito de Seguridad 1

| Número de requisito | RS1 |  |  |
| --- | --- | --- | --- |
| Nombre de requisito | Autenticación segura |  |  |
| Tipo | ☒ Requisito | ☐ Restricción |  |
| Fuente del requisito | Institución |  |  |
| Descripción | Como institución, se requiere el uso de mecanismos de autenticación segura para proteger el acceso a la información institucional. |  |  |
| Prioridad del requisito | ☒ Alta/Esencial | ☐ Media/Deseado | ☐ Baja/ Opcional |

### Requisito de Seguridad 2

| Número de requisito | RS2 |  |  |
| --- | --- | --- | --- |
| Nombre de requisito | Control de acceso por roles |  |  |
| Tipo | ☒ Requisito | ☐ Restricción |  |
| Fuente del requisito | Sistema |  |  |
| Descripción | Como sistema, la restricción de acceso a las funcionalidades del sistema según el rol asignado al usuario. |  |  |
| Prioridad del requisito | ☒ Alta/Esencial | ☐ Media/Deseado | ☐ Baja/ Opcional |

### Requisito de Seguridad 3

| Número de requisito | RS3 |  |  |
| --- | --- | --- | --- |
| Nombre de requisito | Protección de datos |  |  |
| Tipo | ☒ Requisito | ☐ Restricción |  |
| Fuente del requisito | Institución |  |  |
| Descripción | Como institución se requiere la protección de la información registrada mediante controles de seguridad y validación de acceso. |  |  |
| Prioridad del requisito | ☒ Alta/Esencial | ☐ Media/Deseado | ☐ Baja/ Opcional |

### Requisito de Seguridad 4

| Número de requisito | RS4 |  |  |
| --- | --- | --- | --- |
| Nombre de requisito | Registro de auditoría |  |  |
| Tipo | ☒ Requisito | ☐ Restricción |  |
| Fuente del requisito | Sistema |  |  |
| Descripción | Como sistema, se requiere el registro de las acciones realizadas por los usuarios para mantener la trazabilidad de las operaciones. |  |  |
| Prioridad del requisito | ☒ Alta/Esencial | ☐ Media/Deseado | ☐ Baja/ Opcional |

### Requisito de Fiabilidad 1

| Número de requisito | RFI1 |  |  |
| --- | --- | --- | --- |
| Nombre de requisito | Tolerancia a fallos |  |  |
| Tipo | ☒ Requisito | ☐ Restricción |  |
| Fuente del requisito | Sistema |  |  |
| Descripción | Como sistema, se requiere que el sistema mantenga su operación ante fallos menores para evitar interrupciones en el servicio. |  |  |
| Prioridad del requisito | ☒ Alta/Esencial | ☐ Media/Deseado | ☐ Baja/ Opcional |

### Requisito de Fiabilidad 2

| Número de requisito | RFI2 |  |  |
| --- | --- | --- | --- |
| Nombre de requisito | Registro de errores |  |  |
| Tipo | ☒ Requisito | ☐ Restricción |  |
| Fuente del requisito | Sistema |  |  |
| Descripción | Como sistema, se requiere el registro de los errores ocurridos para facilitar su diagnóstico y posterior corrección. |  |  |
| Prioridad del requisito | ☒ Alta/Esencial | ☐ Media/Deseado | ☐ Baja/ Opcional |

### Requisito de disponibilidad 1

| Número de requisito | RD1 |  |  |
| --- | --- | --- | --- |
| Nombre de requisito | Disponibilidad del sistema |  |  |
| Tipo | ☒ Requisito | ☐ Restricción |  |
| Fuente del requisito | Usuario |  |  |
| Descripción | Como usuario, se requiere que el sistema esté disponible al menos el 95% del tiempo para garantizar el acceso cuando sea necesario. |  |  |
| Prioridad del requisito | ☒ Alta/Esencial | ☐ Media/Deseado | ☐ Baja/ Opcional |

### Requisito de disponibilidad 2

| Número de requisito | RD2 |  |  |
| --- | --- | --- | --- |
| Nombre de requisito | Acceso continuo al sistema |  |  |
| Tipo | ☒ Requisito | ☐ Restricción |  |
| Fuente del requisito | Usuario |  |  |
| Descripción | Como usuario, se requiere el acceso al sistema durante la totalidad del horario laboral institucional. |  |  |
| Prioridad del requisito | ☒ Alta/Esencial | ☐ Media/Deseado | ☐ Baja/ Opcional |

### Requisito de mantenibilidad 1

| Número de requisito | RM1 |  |  |
| --- | --- | --- | --- |
| Nombre de requisito | Arquitectura modular |  |  |
| Tipo | ☒ Requisito | ☐ Restricción |  |
| Fuente del requisito | Equipo de desarrollo |  |  |
| Descripción | Como desarrollador, se requiere la construcción del sistema bajo una arquitectura modular para facilitar su mantenimiento. |  |  |
| Prioridad del requisito | ☒ Alta/Esencial | ☐ Media/Deseado | ☐ Baja/ Opcional |

### Requisito de mantenibilidad 2

| Número de requisito | RM2 |  |  |
| --- | --- | --- | --- |
| Nombre de requisito | Documentación técnica |  |  |
| Tipo | ☒ Requisito | ☐ Restricción |  |
| Fuente del requisito | Equipo de desarrollo |  |  |
| Descripción | Como desarrollador, se requiere contar con documentación técnica actualizada para facilitar futuras modificaciones al sistema. |  |  |
| Prioridad del requisito | ☒ Alta/Esencial | ☐ Media/Deseado | ☐ Baja/ Opcional |

### Requisito de portabilidad 1

| Número de requisito | RP1 |  |  |
| --- | --- | --- | --- |
| Nombre de requisito | Compatibilidad con navegadores |  |  |
| Tipo | ☒ Requisito | ☐ Restricción |  |
| Fuente del requisito | Usuario |  |  |
| Descripción | Como usuario, se requiere el acceso al sistema desde diferentes navegadores web para garantizar su uso sin restricciones técnicas. |  |  |
| Prioridad del requisito | ☒ Alta/Esencial | ☐ Media/Deseado | ☐ Baja/ Opcional |

### Requisito de portabilidad 2

| Número de requisito | RP2 |  |  |
| --- | --- | --- | --- |
| Nombre de requisito | Independencia del sistema operativo |  |  |
| Tipo | ☒ Requisito | ☐ Restricción |  |
| Fuente del requisito | Sistema |  |  |
| Descripción | Como sistema, se requiere la ejecución del sistema en diferentes sistemas operativos mediante el uso de un navegador web. |  |  |
| Prioridad del requisito | ☒ Alta/Esencial | ☐ Media/Deseado | ☐ Baja/ Opcional |

## Otros requisitos

Esta sección describe requisitos adicionales que no se clasifican dentro de las categorías anteriores, pero que deben considerarse para el correcto funcionamiento del sistema dentro del contexto institucional del ISSEG.

| Número de requisito | OR1 |  |  |
| --- | --- | --- | --- |
| Nombre de requisito | Respaldo de información |  |  |
| Tipo | Requisito | Restricción |  |
| Fuente del requisito | Institución |  |  |
| Descripción | Como institución, se requiere la realización de respaldos periódicos de la base de datos para prevenir la pérdida de información. |  |  |
| Prioridad del requisito | Alta/Esencial | Media/Deseado | Baja/ Opcional |

| Número de requisito | OR2 |  |  |
| --- | --- | --- | --- |
| Nombre de requisito | Conservación histórica de información |  |  |
| Tipo | Requisito | Restricción |  |
| Fuente del requisito | Coordinación de Sistemas Institucionales |  |  |
| Descripción | Como área de desarrollo, se requiere la conservación del historial completo de solicitudes, cambios de estado y actividades para análisis de métricas. |  |  |
| Prioridad del requisito | Alta/Esencial | Media/Deseado | Baja/ Opcional |

| Número de requisito | OR3 |  |  |
| --- | --- | --- | --- |
| Nombre de requisito | Restricción de acceso por ubicación |  |  |
| Tipo | Requisito | Restricción |  |
| Fuente del requisito | Product Manager |  |  |
| Descripción | Como Product Manager, se requiere que el acceso al sistema esté limitado a dispositivos conectados a la red institucional del ISSEG. |  |  |
| Prioridad del requisito | Alta/Esencial | Media/Deseado | Baja/ Opcional |

# Modelado del Sistema

La presente sección muestra el modelado general del funcionamiento del SGSPCSI, representando el flujo principal de registro, evaluación, asignación, atención y cierre de solicitudes. Este modelado permite visualizar la interacción entre los actores del sistema y la secuencia operativa base que seguirá cada requerimiento dentro de la plataforma.

![](./ERS%20para%20SGSPCSI%20v.2-1_images/image-002.png)![](./ERS%20para%20SGSPCSI%20v.2-1_images/image-003.png)![](./ERS%20para%20SGSPCSI%20v.2-1_images/image-004.png) ![](./ERS%20para%20SGSPCSI%20v.2-1_images/image-005.png)