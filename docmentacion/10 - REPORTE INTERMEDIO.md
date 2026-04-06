![](./10%20-%20REPORTE%20INTERMEDIO_images/image-001.png)

**INSTITUTO TECNOLÓGICO DE MORELIA**

**INGENIERÍA EN SISTEMAS COMPUTACIONALES**

RESIDENCIAS PROFESIONALES

**Reporte Intermedio**

**Semestre Enero-Junio 2026**

PRESENTA:

**Jacqueline Hurtado Hernández**

**Edwin Eduardo Mercado Ruiz**

NÚMERO DE CONTROL:

**14160249**

ASESOR INTERNO:

**I.SC.Alma Lilia Nuñez Gonzalez**

ASESOR EXTERNO:

**MTRA. Karla Teresa Arroyo Calero**

MORELIA, MICHOACÁN **26 DE MARZO DE 2026**

Índice

1.  Justificación del proyecto
2.  Datos de la empresa
    1.  Nombre de la empresa
    2.  Misión y Visión
3.  Caracterización del área en que participó.
4.  Problemas resueltos.
5.  Alcances y limitaciones de las soluciones.
6.  Fundamento teórico.
7.  Procedimientos y descripción de las actividades realizadas.
8.  Resultados (planos, gráficas, prototipos, programas, etc.).
9.  Conclusiones y recomendaciones
10.  Referencias bibliográficas
11.  Cuadro de firmas
12.  Hoja de seguimiento
13.  **Justificación del proyecto**

**1. Por qué vale la pena realizar este estudio:**

El Instituto de Seguridad Social del Estado de Guanajuato (ISSEG) es una institución crucial que administra servicios de seguridad social para miles de afiliados. Actualmente, la Coordinación de Sistemas Institucionales gestiona solicitudes de nuevos sistemas, modificaciones y reportes de incidencias de manera parcialmente manual, lo que genera:

- Falta de visibilidad en tiempo real del estado de los proyectos
- Procesos desorganizados sin control centralizado
- Dificultad en la evaluación de viabilidad técnica
- Ausencia de métricas y reportes estadísticos
- Comunicación ineficiente entre solicitantes, desarrolladores y gerencia

La automatización de este flujo es esencial para mejorar la eficiencia operativa y proporcionar un mejor servicio a los usuarios internos.

**2. Implicaciones de los resultados:**

- **Operacionales:** Reducción de tiempos de respuesta, mayor capacidad de gestión simultánea de solicitudes
- **Administrativas:** Control y trazabilidad completa del ciclo de vida de cada solicitud
- **Tecnológicas:** Establecimiento de procesos estandarizados y escalables
- **Mejora del servicio:** Transparencia en el proceso desde la solicitud hasta la implementación

**3. Quiénes se beneficiarán:**

- **Usuarios solicitantes:** Acceso transparente al estado de sus solicitudes y reducción de tiempos de espera
- **Product Managers:** Herramientas para revisión, aprobación y gestión de prioridades
- **Equipo de desarrollo:** Asignación eficiente de tareas y seguimiento del progreso
- **Ejecutivos del ISSEG:** Reportes de productividad y métricas de desempeño
- **Instituciones internas:** Mejor comunicación y coordinación entre departamentos

1.  **Datos de la empresa**
    1.  Nombre de la empresa: Instituto de Seguridad Social de Estado de Guanajuato (ISSEG)
    2.  Misión y Visión

**Misión**

Garantizar el pago de las jubilaciones, pensiones y seguros, así como el otorgamiento de prestaciones, actuando con transparencia y estricto apego a la Ley de Seguridad Social del Estado de Guanajuato, con el fin de coadyuvar al bienestar de todos nuestros asegurados y sus familias.

**Visión**

Ser una Institución humanista, reconocida a nivel nacional como líder en materia de seguridad social, que cuente con un Fondo de Pensiones perenne, a través de la ejecución de un modelo de administración eficiente que contribuya, de esta forma, al bienestar familiar de nuestros asegurados.

1.  **Caracterización del área en que participó.**

**Entorno Organizacional:**

La Coordinación de Sistemas Institucionales del ISSEG es responsable de:
- Administración de infraestructura tecnológica
- Desarrollo y mantenimiento de sistemas de información
- Soporte a usuarios internos
- Evaluación de viabilidad técnica de nuevos proyectos
- Gestión de recursos y personal de desarrollo

**Estructura del Área:**

Esta coordinación opera con:
- **Product Managers:** Encargados de revisar y validar solicitudes
- **Desarrolladores:** Implementación de soluciones técnicas
- **Support:** Atención a usuarios solicitantes
- **Coordinador:** Supervisión y asignación de recursos

**Actividades realizadas en la residencia:**

- **Análisis de procesos actuales:** Levantamiento de flujos manuales existentes
- **Recopilación de requisitos:** Entrevistas con stakeholders de todos los niveles
- **Diseño de solución:** Creación de mockups y especificación de requisitos
- **Documentación:** Elaboración de especificación técnica y diagramas

1.  **Problemas resueltos.**

**Problemas Identificados:**

1. **Falta de control centralizado en solicitudes:**
   - Las solicitudes se reciben por múltiples canales (email, teléfono, presencial)
   - No hay un punto único de registro y seguimiento
   - Riesgo de pérdida o duplicación de solicitudes

2. **Ausencia de procesos estandarizados:**
   - No existe flujo definido para validación de viabilidad técnica
   - Criterios de aprobación no documentados
   - Asignación de desarrolladores sin criterios claros (disponibilidad, expertise)

3. **Falta de visibilidad en el estado de proyectos:**
   - Solicitantes desconocen el estado de sus peticiones
   - Gerencia carece de métricas sobre productividad
   - Imposibilidad de generar reportes estadísticos

4. **Ineficiencia en la comunicación:**
   - Notificaciones manuales y no confiables
   - Retrasos en la comunicación de rechazos o aprobaciones
   - Falta de historial de cambios y decisiones

5. **Ausencia de documentación técnica integrada:**
   - Documentos dispersos en múltiples ubicaciones
   - Difícil acceso a especificaciones y requerimientos
   - No hay versionado de documentos

1.  **Alcances y limitaciones de las soluciones.**

**ALCANCES:**

El Sistema de Gestión de Solicitudes de Proyectos de la Coordinación de Sistemas Institucionales (SGSPCSI) incluye:

**Funcionalidades Implementadas:**
- Módulo de autenticación institucional con 3 roles definidos
- Portal de solicitudes con 4 tipos de peticiones (Nuevos sistemas, Modificaciones, Urgencias, Requerimientos técnicos)
- Dashboard personalizado para cada rol de usuario
- Módulo de aprobaciones con validaciones de viabilidad técnica
- Gestión de equipo de desarrollo con asignación inteligente de tareas
- Repositorio centralizado de documentación técnica
- Sistema de notificaciones en tiempo real
- Reportes estadísticos y métricas de desempeño
- Historial completo y trazabilidad de solicitudes

**11 Pantallas Diseñadas:**
1. Login (autenticación)
2. Home Usuario Solicitante
3. Mis Solicitudes
4. Home Desarrollador
5. Mis Tareas - Desarrollador
6. Repositorio de Documentación
7. Home Product Manager
8. Dashboard Ejecutivo
9. Gestión de Aprobaciones
10. Gestión de Equipo
11. Perfil de Usuario

**Beneficios Esperados:**
- Reducción de 60-70% en tiempos de procesamiento de solicitudes
- Aumento en la transparencia y confianza de usuarios
- Mejora en la coordinación entre equipos
- Facilidad en la generación de reportes y métricas
- Base sólida para futuras mejoras y escalabilidad

**LIMITACIONES:**

1. **Fase actual (Marzo 2026):** Aún en fase de diseño, implementación pendiente para Abril-Mayo
2. **Integración con sistemas existentes:** Se requiere análisis adicional de APIs y conexiones con sistemas legados del ISSEG
3. **Stack tecnológico:** A confirmarse definitivamente la versión exacta de Angular y .NET
4. **Capacitación de usuarios:** Requerirá plan de formación que no está incluido en el alcance actual
5. **Migración de datos históricos:** Requiere análisis de datos legados y estrategia de importación
6. **Configuración de permisos por área:** Necesita mapeo completo de estructura organizacional del ISSEG

1.  **Fundamento teórico.**

**Metodologías y Estándares Aplicados:**

**1. IEEE 830 (Especificación de Requisitos de Software)**
   - Utilizada para la documentación formal de requisitos
   - Estructura de ERS: descripción general, requisitos especí­ficos, requisitos no funcionales
   - Garantiza claridad y completitud de especificaciones

**2. Notación UML (Unified Modeling Language)**
   - Diagramas de casos de uso
   - Diagramas de clases para el modelo de datos
   - Diagramas de secuencia para flujos de proceso

**3. Prototipado de Interfaz de Usuario (UI/UX)**
   - Diseño centrado en usuario
   - Iteración basada en retroalimentación
   - Validación de usabilidad

**4. Principios de Ingeniería de Software**
   - Separación de responsabilidades (MVC/MVVM)
   - Principios SOLID
   - Arquitectura de capas

**5. Control de Acceso Basado en Roles (RBAC)**
   - Implementación de 3 roles: Usuario solicitante, Desarrollador, Product Manager
   - Permisos granulares por funcionalidad

**6. Patrones de Diseño Utilizados**
   - Patrón Repository para acceso a datos
   - Patrón Singleton para conexiones
   - Patrón Observer para notificaciones

**Stack Tecnológico Propuesto:**
   - **Frontend:** Angular (versión 15+) con TypeScript
   - **Backend:** .NET Core (versión 6 o superior) con C#
   - **Base de Datos:** SQL Server
   - **Autenticación:** basada en directorio institucional
   - **Control de Versiones:** Git

1.  **Procedimientos y descripción de las actividades realizadas.**

**FASE 1: INVESTIGACIÓN (Enero 2026)**

**Actividad 1.1 - Diagnóstico del flujo actual**
- ¿Qué se hizo?: Análisis detallado de cómo se gestionan actualmente las solicitudes en ISSEG
- ¿Cómo se hizo?: Entrevistas con personal de Sistemas, revisión de procesos documentados, observación directa
- Resultado: Identificación de cuellos de botella y áreas de mejora
- Tiempo: Primera semana de enero

**Actividad 1.2 - Análisis de stack tecnológico**
- ¿Qué se hizo?: Evaluación de tecnologías actuales y propuestas para la solución
- ¿Cómo se hizo?: Consulta de documentación técnica, experiencia del equipo, requisitos de ISSEG
- Resultado: Definición de Angular + .NET como stack recomendado
- Tiempo: Segunda semana de enero

---

**FASE 2: ANÁLISIS (Febrero 2026)**

**Actividad 2.1 - Levantamiento de requisitos**
- ¿Qué se hizo?: Recopilación exhaustiva de requisitos funcionales y no funcionales
- ¿Cómo se hizo?: Talleres con stakeholders, análisis de procesos, definición de casos de uso
- Resultado: Documento ERS IEEE 830 completo (50+ requisitos funcionales)
- Tiempo: Primera y segunda semana de febrero

**Actividad 2.2 - Elaboración de diagramas de flujo**
- ¿Qué se hizo?: Creación de diagramas para visualizar los procesos del sistema
- ¿Cómo se hizo?: Análisis de casos de uso, definición de conectores y decisiones
- Resultado: 7 diagramas de flujo detallados (solicitud urgente, nueva solicitud, modificación, aprobación, etc.)
- Tiempo: Tercera semana de febrero

---

**FASE 3: DISEÑO (Marzo 2026)**

**Actividad 3.1 - Diseño de interfaces (Mockups)**
- ¿Qué se hizo?: Creación de bosquejos de todas las pantallas del sistema
- ¿Cómo se hizo?: Diseño iterativo con herramientas de prototipado, validación con usuarios
- Resultado: 11 pantallas completamente documentadas con escenarios y especificaciones de elementos
- Tiempo: Primera y segunda semana de marzo

**Actividad 3.2 - Diseño del modelo de datos**
- ¿Qué se hizo?: Definición de la estructura de base de datos
- ¿Cómo se hizo?: Análisis de entidades, relaciones, y normalización
- Resultado: Diagrama E-R con tablas, relaciones y restricciones
- Tiempo: Tercera semana de marzo

**Actividad 3.3 - Documentación de especificaciones técnicas**
- ¿Qué se hizo?: Consolidación de toda la información en documentos finales
- ¿Cómo se hizo?: Compilación de ERS, mockups, diagramas, validaciones, mensajes y excepciones
- Resultado: Documentación completa lista para fase de desarrollo
- Tiempo: Última semana de marzo

1.  **Resultados (planos, gráficas, prototipos, programas, etc.).**

**RESULTADOS ALCANZADOS AL 26 DE MARZO DE 2026:**

**Resultado 1: Especificación de Requisitos de Software (ERS) IEEE 830 - Completo**
- **Documento:** ERS para SGSPCSI v.2.1
- **Contenido:** 
  - Descripción general del sistema
  - 20+ requisitos funcionales detallados
  - Requisitos no funcionales (seguridad, performance, portabilidad)
  - Interfaces (usuario, software, hardware, comunicación)
  - Diagramas de caso de uso
- **Fecha:** Completado 28 de febrero de 2026
- **Actividades relacionadas:** Levantamiento de requisitos, análisis de procesos

---

**Resultado 2: Mockups y Escenarios de Usuario - 11 Pantallas**
- **Documento:** Documento de Mockups y Escenarios v.5
- **Pantallas diseñadas:**
  1. **Login** - Autenticación institucional con 3 escenarios
  2. **Home Usuario solicitante** - Dashboard con 5 escenarios
  3. **Mis Solicitudes** - Listado con filtros y búsqueda (3 escenarios)
  4. **Home Desarrollador** - Panel de control con métricas (8 escenarios)
  5. **Mis Tareas Desarrollador** - Gestión de tareas (5 escenarios)
  6. **Repositorio Documentación** - Acceso a archivos (3 escenarios)
  7. **Home Product Manager** - Panel de gestión (7 escenarios)
  8. **Dashboard Ejecutivo** - Métricas y reportes (3 escenarios)
  9. **Gestión de Aprobaciones** - Revisión de solicitudes (3 escenarios)
  10. **Gestión de Equipo** - Administración de desarrolladores (4 escenarios)
  11. **Perfil de Usuario** - Configuración personal (4 escenarios)

- **Especificaciones:** Cada pantalla incluye:
  - Bosquejo visual detallado
  - Escenarios principales y alternos
  - Elementos de la pantalla (tablas con ID, comportamiento, edibilidad, reglas de negocio)
  - Validaciones y excepciones
  - Mensajes al usuario

- **Fecha:** Completado 23 de marzo de 2026
- **Actividades relacionadas:** Diseño de interfaces, validaciones con stakeholders

---

**Resultado 3: Diagramas de Flujo de Procesos - 8 Diagramas**
- **Documentos:** Ubicados en carpeta `/diagramas`
- **Diagramas creados:**
  1. Diagrama de autenticación y control de acceso
  2. Diagrama de validación de permisos por área
  3. Diagrama de proceso principal con control de acceso
  4. Diagrama de filtrado de sistemas por área
  5. Diagrama de estructura de control de usuarios
  6. Tabla de permisos por rol y área
  7. Diagrama de control y registro en base de datos
  8. Diagrama de estados del ticket

- **Formato:** Notación de flujo en Mermaid (.mmd)
- **Fecha:** Completado 20 de marzo de 2026

---

**Resultado 4: Modelo de Datos - Diagrama E-R**
- **Contenido:** 
  - Identificación de 15+ entidades principales
  - Relaciones entre tablas
  - Atributos y tipos de datos
  - Claves primarias y foráneas
  - Restricciones de integridad

- **Tablas principales:**
  - Usuarios (con roles y permisos)
  - Solicitudes (con estados y prioridades)
  - Tareas (con asignaciones)
  - Equipos (con disponibilidad)
  - Documentos (con versiones)
  - Auditoría (historial de cambios)

- **Fecha:** Completado 24 de marzo de 2026

---

**Resultado 5: Matriz de Validaciones, Excepciones y Mensajes**
- **Cantidad:** 30+ validaciones, 25+ excepciones, 20+ mensajes
- **Cobertura:** Todas las 11 pantallas
- **Formato:** Tablas detalladas en documento de mockups
- **Fecha:** Completado 26 de marzo de 2026

---

**RESUMEN CUANTITATIVO DE RESULTADOS:**

| Tipo de Resultado | Cantidad | Estado |
|------------------|----------|--------|
| Documentos finales | 3 | ✅ Completo |
| Diagramas | 8 | ✅ Completo |
| Pantallas diseñadas | 11 | ✅ Completo |
| Escenarios de usuario | 50+ | ✅ Completo |
| Requisitos funcionales documentados | 20+ | ✅ Completo |
| Elementos de pantalla especificados | 150+ | ✅ Completo |
| Páginas de documentación | 49 (PDF) | ✅ Completo |

---

**ENTREGABLES DISPONIBLES:**

1. ✅ `Documento de mockups y escenarios v.5.pdf` - Documento oficial con todas las pantallas
2. ✅ `ERS para SGSPCSI v.2.1.docx` - Especificación técnica completa
3. ✅ Carpeta `/diagramas` - Diagramas de flujo en formato Mermaid
4. ✅ Carpeta `/docmentacion` - Documentación complementaria (16 documentos)
5. ✅ Repositorios Git - Acceso a historial de cambios y versiones

1.  **Conclusiones y recomendaciones**

**CONCLUSIONES:**

Hasta la fecha (26 de marzo de 2026), se ha completado exitosamente la primera mitad del proyecto, correspondiente a las fases de Investigación, Análisis y Diseño. Los logros alcanzados son:

1. **Documentación exhaustiva:** Se cuenta con especificaciones técnicas completas en formato IEEE 830, priorizando claridad y completitud para la fase de desarrollo.

2. **Diseño centrado en usuario:** Las 11 pantallas diseñadas reflejan los requisitos de los tres roles de usuario (solicitante, desarrollador, product manager) y contemplan múltiples escenarios de uso.

3. **Procesos claramente definidos:** Los diagramas de flujo documentan los procesos end-to-end, facilitando la comprensión de la lógica del negocio y la implementación técnica.

4. **Fundación sólida para desarrollo:** Con el modelo de datos definido, las validaciones especificadas y las excepciones documentadas, el equipo de desarrollo tiene toda la información necesaria para proceder.

5. **Validación de stakeholders:** El proceso iterativo ha garantizado que las especificaciones reflejen las verdaderas necesidades del ISSEG.

**ESTADO ACTUAL:**
El proyecto está en posición de transitar a la fase de Desarrollo (Abril-Mayo 2026) con confianza, ya que todas las decisiones arquitectónicas y de diseño han sido tomadas y documentadas.

---

**RECOMENDACIONES PARA LAS PRÓXIMAS FASES:**

**1. Confirmación del Stack Tecnológico (Acción Inmediata)**
   - Validar definitivamente versiones de Angular, .NET y SQL Server
   - Confirmar herramientas de desarrollo (IDE, control de versiones, deployment)
   - Establecer estándares de codificación

**2. Preparación para Desarrollo (Antes de Abril)**
   - Configurar repositorio Git con estructura de ramas
   - Preparar ambiente de desarrollo y testing
   - Establecer pipeline de CI/CD

**3. Integración con Sistemas Existentes**
   - Analizar APIs disponibles en ISSEG
   - Documentar requerimientos de autenticación institucional
   - Planificar migración de datos históricos

**4. Gestión del Proyecto**
   - Implementar sistema de seguimiento (JIRA, Azure DevOps)
   - Establecer reuniones de sincronización bi-semanales
   - Definir criterios de aceptación por funcionalidad

**5. Planificación de Testing**
   - Desarrollar plan de pruebas unitarias
   - Definir escenarios para pruebas de integración
   - Establecer protocolo de UAT (User Acceptance Testing)

**6. Capacitación de Usuarios**
   - Comenzar a preparar materiales de capacitación en paralelo al desarrollo
   - Identificar usuarios clave para pruebas beta
   - Planificar rollout post-implementación

**7. Documentación Técnica**
   - Mantener documentación actualizada conforme avanza el desarrollo
   - Crear guías de instalación y configuración
   - Documentar procesos de mantenimiento

**RIESGOS IDENTIFICADOS Y MITIGACIÓN:**

| Riesgo | Probabilidad | Impacto | Mitigación |
|--------|-------------|--------|----------|
| Cambios en requisitos durante desarrollo | Media | Alto | Mantener comunicación constante, controlar cambios con CCP |
| Integración con sistemas legados | Media | Alto | Iniciar análisis técnico inmediatamente |
| Disponibilidad de desarrolladores seniors | Baja | Medio | Asegurar continuidad del equipo |
| Cambios en stack tecnológico | Baja | Alto | Evaluar alternativas ahora, no durante desarrollo |

**CRONOGRAMA ESTIMADO PARA FASES RESTANTES:**

- **Abril 2026:** Integración de propuestas y configuración del entorno (1-2 semanas) → Inicio de desarrollo (2-3 semanas)
- **Mayo 2026:** Continuación del desarrollo y pruebas parciales (4 semanas)
- **Junio 2026:** Pruebas finales, correcciones y despliegue pilot (4 semanas)

**MÉTRICAS DE ÉXITO ESPERADAS:**
- Reducción del 70% en tiempo de procesamiento de solicitudes
- 100% de trazabilidad en todas las solicitudes
- Disponibilidad del sistema ≥ 99.5%
- Satisfacción de usuarios ≥ 85%

1.  **Referencias bibliográficas**

LIBRO:

Se incluyen los siguientes datos:

-   Apellido Paterno, Nombre del autor (Si son varios autores, solo colocar apellido paterno seguido de la inicial del nombre de cada autor)
-   Año de publicación, entre paréntesis.
-   Nombre del libro.
-   Lugar de publicación
-   Formato en que se encuentra el archivo electrónico, encerrado entre corchetes (solo en caso de libro electrónico)
-   DOI, si es que cuenta con el (DOI, Digital Object Identifier. Es un dígito permanente comúnmente utilizado para identificar documentos electrónicos)
-   La leyenda “Disponible en:” seguida de la liga completa donde se encontró el artículo (solo en el caso de libros electrónicos).

Ejemplos:

Jiménez, José A. (2009) Matemáticas para la Computación. México, D.F.

Pressman, Roger. (2002) Ingeniería de Software, Un enfoque práctico. Madrid, España. \[PDF Portable Document Format\]. Disponible en: http://www.scribd.com/doc/7978336/Ingenieria-de-Software-Un-Enfoque-Practico-Pressman-5th-Ed.

ARTÍCULO DE REVISTA IMPRESA:

Se incluyen los siguientes datos:

-   Apellido Paterno, Nombre del autor (Si son varios autores, solo colocar apellido paterno seguido de la inicial del nombre de cada autor.)
-   Año de publicación, entre paréntesis.
-   Nombre del artículo, como aparece en la publicación.
-   Nombre de la revista donde se publicó el artículo.
-   Número de la revista (consecutivo según el año)
-   Rango de páginas en donde está contenido el artículo.

Ejemplos:

Zyda, Michael. (2009) Computer Science in the Conceptual Age. Communications of the ACM, 12, 66 – 72.

Izadi, S., Hodges, S., Butler, A., West, D., Rrustemi, A., Molloy, M., & Buxton, W. (2009). ThinSight: A Thin Form-Factor Interactive Surface Technology. Communications of the ACM, 12, 90 – 98.

ARTÍCULO DE REVISTA ELECTRÓNICA:

Se incluyen los siguientes datos:

-   Apellido Paterno, Nombre del autor (Si son varios autores, solo colocar apellido paterno seguido de la inicial del nombre de cada autor.)
-   Año de publicación, entre paréntesis.
-   Nombre del artículo, como aparece en la publicación.
-   Nombre de la revista donde se publicó el artículo.
-   Número de la revista (si es que lo hay)
-   Rango de páginas en donde está contenido el artículo (si es que la revista o journal incluye varias páginas)
-   DOI, si es que cuenta con el (DOI, Digital Object Identifier. Es un dígito permanente comúnmente utilizado para identificar documentos electrónicos)
-   La leyenda “Disponible en:” seguida de la liga completa donde se encontró el artículo.

Ejemplo:

Pensinger, Doug. (2010) Scientists Decode the Secrets of Olympic Skeleton Sliding. ACM News, Disponible en: http://cacm.acm.org/news/73558-scientists-decode-the-secrets-of-olympic-skeleton-sliding/fulltext.

PÁGINA WEB:

Se incluyen los siguientes datos:

-   Apellido Paterno, nombre del autor. Si no tiene, se omite ésta información.
-   Nombre del artículo, o título de la página web.
-   Año de publicación, entre paréntesis. Si no tiene, se coloca entre paréntesis las letras n.d. (no date).
-   La leyenda “Fecha de Consulta:” seguida de la fecha exacta en la que se consultó la página web.
-   La leyenda “Disponible en:” seguida del link completo en donde se puede consultar la página web.

Ejemplo:

El verbo. (n.d) Fecha de Consulta: 18 de Febrero de 2010. Disponible en: [http://roble.pntic.mec.es/~msanto1/lengua/verbo.htm](http://roble.pntic.mec.es/~msanto1/lengua/verbo.htm)

1.  **Hoja de Visto Bueno por parte de los asesores**

| **\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_**   **Karla Teresa Arroyo Calero**   **Asesor Externo** | **\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_**   **Alma Lilia Nuñez Gonzalez**   **Asesor Interno** |
| --- | --- |
| **\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_**   **Jacqueline Hurtado Hernández**   **Residente** | **\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_**   **Edwin Eduardo Mercado Ruiz**   **Residente** |
| **\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_**   **Vo.Bo. Oficina de Residencias Profesionales** |  |