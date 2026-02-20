# Áreas de Proceso CMMI

## 📚 Introducción

Las **Áreas de Proceso (Process Areas - PA)** son los bloques de construcción de CMMI. Cada área de proceso:
- Define un conjunto de objetivos y prácticas relacionadas
- Se enfoca en un aspecto específico del desarrollo de productos o servicios
- Contribuye a la madurez organizacional
- Es evaluable independientemente

CMMI for Development incluye **22 Áreas de Proceso** organizadas en 4 categorías.

## 🗂️ Categorías de Áreas de Proceso

### 1. **Gestión de Procesos (Process Management)**
Actividades relacionadas con la definición, planificación, despliegue, implementación, monitoreo, control, evaluación, medición y mejora de procesos.

### 2. **Gestión de Proyectos (Project Management)**
Actividades relacionadas con la planificación, monitoreo y control del proyecto.

### 3. **Ingeniería (Engineering)**
Actividades relacionadas con el desarrollo y mantenimiento del producto.

### 4. **Soporte (Support)**
Actividades que soportan el desarrollo y mantenimiento del producto.

---

## 📊 Las 22 Áreas de Proceso Detalladas

## 🔵 NIVEL 2 - Gestionado

### 1. Gestión de Requerimientos (REQM)

**Categoría**: Gestión de Proyectos  
**Propósito**: Gestionar requerimientos de productos y componentes del proyecto, e identificar inconsistencias entre los requerimientos y los planes y productos de trabajo del proyecto.

#### Objetivos Específicos
1. **SG 1**: Gestionar requerimientos
   - Entender los requerimientos
   - Obtener compromiso con los requerimientos
   - Gestionar cambios a los requerimientos
   - Mantener trazabilidad bidireccional
   - Asegurar alineación entre trabajo y requerimientos

#### Prácticas Clave
- ✅ Documentar requerimientos
- ✅ Matriz de trazabilidad
- ✅ Proceso de gestión de cambios
- ✅ Revisiones de alineación
- ✅ Comunicación con stakeholders

#### Aplicación Práctica - Ejemplo
```
Cliente solicita: "El sistema debe ser seguro"
    ↓
Análisis: ¿Qué significa "seguro"?
    ↓
Requerimientos específicos:
  - REQ-001: Autenticación de dos factores
  - REQ-002: Encriptación AES-256
  - REQ-003: Logs de auditoría
    ↓
Trazabilidad: REQ-001 → Diseño → Código → Prueba
    ↓
Control de cambios: Si REQ-001 cambia → Impacto evaluado
```

#### Artefactos Típicos
- Documento de requerimientos
- Matriz de trazabilidad
- Registro de cambios de requerimientos
- Actas de revisión de requerimientos

---

### 2. Planificación de Proyectos (PP)

**Categoría**: Gestión de Proyectos  
**Propósito**: Establecer y mantener planes que definen las actividades del proyecto.

#### Objetivos Específicos
1. **SG 1**: Establecer estimaciones
   - Estimar alcance del proyecto
   - Establecer estimaciones de atributos de productos de trabajo
   - Definir ciclo de vida del proyecto
   - Determinar estimaciones de esfuerzo y costo

2. **SG 2**: Desarrollar un plan de proyecto
   - Establecer el presupuesto y cronograma
   - Identificar riesgos del proyecto
   - Planificar gestión de datos
   - Planificar recursos del proyecto
   - Planificar conocimiento y habilidades necesarias
   - Planificar involucración de stakeholders
   - Establecer el plan del proyecto

3. **SG 3**: Obtener compromiso con el plan
   - Revisar planes que afectan el proyecto
   - Reconciliar niveles de trabajo y recursos
   - Obtener compromiso con el plan

#### Prácticas Clave
- 📋 WBS (Work Breakdown Structure)
- 📅 Cronograma con hitos
- 💰 Presupuesto detallado
- 👥 Asignación de recursos
- ⚠️ Identificación de riesgos
- 🤝 Compromiso de stakeholders

#### Herramientas Comunes
- Microsoft Project / Primavera
- Jira / Azure DevOps
- Smartsheet
- Monday.com
- Asana

#### Ejemplo de Plan de Proyecto

```
Proyecto: Sistema de Tickets ISSEG
├── 1. Iniciación (2 semanas)
│   ├── 1.1 Kick-off
│   ├── 1.2 Análisis de requerimientos
│   └── 1.3 Plan del proyecto
├── 2. Diseño (3 semanas)
│   ├── 2.1 Arquitectura
│   ├── 2.2 Diseño de BD
│   └── 2.3 Diseño de UI/UX
├── 3. Desarrollo (8 semanas)
│   ├── 3.1 Backend API
│   ├── 3.2 Frontend
│   ├── 3.3 Integración
│   └── 3.4 Testing unitario
├── 4. Pruebas (3 semanas)
│   ├── 4.1 Pruebas de integración
│   ├── 4.2 Pruebas de sistema
│   └── 4.3 UAT
└── 5. Despliegue (2 semanas)
    ├── 5.1 Preparación ambiente producción
    ├── 5.2 Migración de datos
    └── 5.3 Go-live

Recursos: 5 desarrolladores, 1 PM, 1 QA
Presupuesto: $150,000
Riesgos: Disponibilidad de usuarios para UAT, Integración con AD
```

---

### 3. Monitoreo y Control de Proyectos (PMC)

**Categoría**: Gestión de Proyectos  
**Propósito**: Proveer un entendimiento del progreso del proyecto para que se puedan tomar acciones correctivas apropiadas cuando el desempeño del proyecto se desvía significativamente del plan.

#### Objetivos Específicos
1. **SG 1**: Monitorear el proyecto contra el plan
   - Monitorear parámetros de planificación del proyecto
   - Monitorear compromisos
   - Monitorear riesgos del proyecto
   - Monitorear gestión de datos
   - Monitorear involucración de stakeholders
   - Conducir revisiones de progreso
   - Conducir revisiones de hitos

2. **SG 2**: Gestionar acciones correctivas hasta el cierre
   - Analizar issues
   - Tomar acciones correctivas
   - Gestionar acciones correctivas

#### Prácticas Clave
- 📊 Dashboard de proyecto
- 🚦 Semáforos de estado (RAG)
- 📈 Análisis de varianza (Earned Value)
- 🔍 Identificación temprana de desviaciones
- 🎯 Acciones correctivas documentadas
- 📝 Reuniones de seguimiento

#### Métricas Comunes

| Métrica | Fórmula | Interpretación |
|---------|---------|----------------|
| **SPI** (Schedule Performance Index) | EV / PV | >1: Adelantado, <1: Atrasado |
| **CPI** (Cost Performance Index) | EV / AC | >1: Bajo presupuesto, <1: Sobre presupuesto |
| **ETC** (Estimate to Complete) | (BAC - EV) / CPI | Costo estimado para completar |
| **EAC** (Estimate at Completion) | AC + ETC | Costo total proyectado |

**Leyenda**: EV=Earned Value, PV=Planned Value, AC=Actual Cost, BAC=Budget at Completion

#### Ejemplo de Dashboard

```
📊 PROYECTO: Sistema ISSEG - Sprint 5
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Estado General: 🟡 AMARILLO

Cronograma:
  🟢 Avance: 60% (Plan: 55%)
  SPI: 1.09 (Adelantado)
  
Presupuesto:
  🟡 Gastado: $92,000 (Plan: $85,000)
  CPI: 0.94 (8% sobre presupuesto)
  
Alcance:
  🟢 Features completados: 45/50 (90%)
  
Calidad:
  🟢 Defectos abiertos: 12 (objetivo: <15)
  
Riesgos:
  🔴 RIESGO-005: Integración con AD - MATERIALIZADO
       → Acción: Recurso senior asignado
       → ETA: Resolución en 3 días
  
Próximos Hitos:
  - [15/Feb] Cierre Sprint 5
  - [22/Feb] UAT Fase 1
  - [01/Mar] Release Candidate
```

---

### 4. Gestión de Acuerdos con Proveedores (SAM)

**Categoría**: Gestión de Proyectos  
**Propósito**: Gestionar la adquisición de productos y servicios de proveedores.

#### Objetivos Específicos
1. **SG 1**: Establecer acuerdos con proveedores
   - Determinar tipo de adquisición
   - Seleccionar proveedores
   - Establecer acuerdos con proveedores

2. **SG 2**: Satisfacer acuerdos con proveedores
   - Ejecutar el acuerdo con el proveedor
   - Monitorear procesos seleccionados del proveedor
   - Evaluar productos de trabajo seleccionados del proveedor
   - Aceptar el producto adquirido
   - Transicionar productos

#### Aplicable a
- Servicios de desarrollo offshore/nearshore
- Licencias de software
- Servicios de cloud (AWS, Azure, GCP)
- Consultoría especializada
- Componentes COTS (Commercial Off-The-Shelf)

#### Prácticas Clave
- 📄 RFP/RFQ estructurados
- 🏆 Proceso de selección objetivo
- 📋 Contratos claros (SLAs)
- 🔍 Revisiones periódicas con proveedor
- ✅ Criterios de aceptación definidos
- 📊 Evaluación de desempeño

#### Ejemplo de SLA

```
ACUERDO DE NIVEL DE SERVICIO - Hosting AWS

1. Disponibilidad
   - Objetivo: 99.9% uptime mensual
   - Penalización: 10% de descuento por cada 0.1% debajo
   
2. Performance
   - Tiempo de respuesta: <200ms (p95)
   - Throughput: >1000 req/seg
   
3. Soporte
   - Respuesta a incidentes críticos: <1 hora
   - Respuesta a incidentes normales: <4 horas
   
4. Seguridad
   - Backup diario con retención de 30 días
   - Parches de seguridad: <48h desde publicación
   
5. Reportes
   - Dashboard en tiempo real
   - Reporte mensual de métricas
   
6. Revisiones
   - Review trimestral de servicio
   - Evaluación anual de renovación
```

---

### 5. Medición y Análisis (MA)

**Categoría**: Soporte  
**Propósito**: Desarrollar y sostener una capacidad de medición usada para soportar las necesidades de información de la gestión.

#### Objetivos Específicos
1. **SG 1**: Alinear actividades de medición y análisis
   - Establecer objetivos de medición
   - Especificar medidas
   - Especificar procedimientos de recolección y almacenamiento
   - Especificar procedimientos de análisis

2. **SG 2**: Proveer resultados de medición
   - Recolectar datos de medición
   - Analizar datos de medición
   - Almacenar datos y resultados
   - Comunicar resultados

#### Principios Clave

**GQM (Goal-Question-Metric)**
```
GOAL (Objetivo)
    ↓
QUESTION (Pregunta)
    ↓
METRIC (Métrica)
```

**Ejemplo**:
```
GOAL: Mejorar la calidad del código
  ↓
QUESTION: ¿Cuántos defectos hay en producción?
  ↓
METRIC: Defectos/KLOC (mil líneas de código)
```

#### Métricas Esenciales por Categoría

**Productividad**:
- Velocidad (puntos de historia/sprint)
- Throughput (features/mes)
- Tiempo de ciclo (idea→producción)

**Calidad**:
- Densidad de defectos (defectos/KLOC)
- Tasa de fuga de defectos (defectos en prod/defectos totales)
- Cobertura código (%)

**Eficiencia**:
- % de retrabajo
- Tiempo de revisiones de código
- Lead time de despliegue

**Satisfacción**:
- NPS (Net Promoter Score)
- CSAT (Customer Satisfaction)
- Tiempo de resolución de tickets

#### Herramientas
- **Recolección**: Jira, Azure DevOps, SonarQube
- **Análisis**: Excel, Power BI, Tableau, Grafana
- **Dashboards**: Custom dashboards, Datadog, New Relic

---

### 6. Aseguramiento de Calidad de Procesos y Productos (PPQA)

**Categoría**: Soporte  
**Propósito**: Proveer al staff y a la gerencia con visibilidad objetiva de los procesos y productos de trabajo asociados.

#### Objetivos Específicos
1. **SG 1**: Evaluar objetivamente procesos y productos de trabajo
   - Evaluar objetivamente procesos
   - Evaluar objetivamente productos de trabajo

2. **SG 2**: Proveer visibilidad objetiva
   - Comunicar y resolver issues de no-conformidad
   - Establecer registros

#### Rol de QA en CMMI

```
Planificación del Proyecto
    ↓
[QA] Revisar plan de proyecto
    ↓
Ejecución del Desarrollo
    ↓
[QA] Auditorías de proceso (¿se sigue el proceso?)
[QA] Revisiones de productos (¿cumple estándares?)
    ↓
Identificación de No-Conformidades
    ↓
[QA] Reportar a PM y responsables
[QA] Escalar si no se resuelve
    ↓
Acciones Correctivas
    ↓
[QA] Verificar cierre de acciones
    ↓
Reportes de QA a Gestión
```

#### Actividades de QA

**Auditorías de Proceso**:
- ¿Se sigue el proceso definido?
- ¿Están los productos de trabajo completos?
- ¿Se hacen las revisiones requeridas?
- ¿Se mantiene la trazabilidad?

**Revisiones de Productos**:
- Cumplimiento de estándares de código
- Completitud de documentación
- Cobertura de pruebas adecuada
- Criterios de aceptación satisfechos

**Ejemplo de Checklist de QA**:
```
✅ CHECKLIST DE AUDITORÍA - Sprint 5

PROCESO:
[✓] Plan de sprint documentado
[✓] Requerimientos rastreados en Jira
[✓] Daily standups realizados (12/12)
[✗] Retrospectiva pendiente → NO-CONFORMIDAD #23
[✓] Demo al Product Owner completada

PRODUCTOS:
[✓] Código committed con revisión (48/50 PRs)
[✗] 2 PRs sin revisión → NO-CONFORMIDAD #24
[✓] Cobertura de pruebas: 87% (objetivo: 80%)
[✓] Documentación técnica actualizada
[✓] Release notes preparados

ACCIONES:
→ NC#23: Programar retrospectiva (Responsable: SM, Fecha: 20/Feb)
→ NC#24: Revisar PRs pendientes (Responsable: Tech Lead, Fecha: 19/Feb)
```

---

### 7. Gestión de Configuración (CM)

**Categoría**: Soporte  
**Propósito**: Establecer y mantener la integridad de los productos de trabajo usando identificación de configuración, control de configuración, contabilidad del estado de configuración y auditorías de configuración.

#### Objetivos Específicos
1. **SG 1**: Establecer líneas base
   - Identificar ítems de configuración
   - Establecer un sistema de gestión de configuración
   - Crear o liberar líneas base

2. **SG 2**: Seguir y controlar cambios
   - Seguir solicitudes de cambio
   - Controlar ítems de configuración

3. **SG 3**: Establecer integridad
   - Establecer registros de gestión de configuración
   - Realizar auditorías de configuración

#### Conceptos Clave

**Ítem de Configuración (CI)**:
Cualquier artefacto que debe ser controlado en versiones.

**Ejemplos de CIs**:
- 📁 Código fuente
- 📋 Documentos de requerimientos
- 🎨 Diseños y diagramas
- 🧪 Scripts de prueba
- ⚙️ Archivos de configuración
- 📦 Binarios y releases
- 🗃️ Scripts de BD

**Línea Base (Baseline)**:
Versión aprobada de un conjunto de CIs que sirve como base para desarrollo futuro.

#### Estrategia de Branching (Ejemplo Git Flow)

```
main (producción)
  ├── release/v2.1 (candidato a producción)
  │     ├── hotfix/bug-critico-login
  │     └── merge ← develop
  │
  └── develop (integración)
        ├── feature/formulario-tickets
        ├── feature/dashboard-metricas
        └── bugfix/validacion-permisos

REGLAS:
- main: Solo releases y hotfixes
- release: Feature freeze, solo bugfix
- develop: Integración continua
- feature: Una por funcionalidad
- Todo cambio requiere Pull Request + Revisión
```

#### Control de Cambios

```
Solicitud de Cambio (CR-045)
    ↓
[¿Aplica a CI?] → No → Procesar normal
    ↓ Sí
Evaluación de Impacto
    ↓
Aprobación CCB (Change Control Board)
    ↓ Aprobado
Implementación Controlada
    ↓
Actualización de Línea Base
    ↓
Registro en CM
```

#### Herramientas
- **Control de versiones**: Git (GitHub, GitLab, Bitbucket)
- **Gestión de cambios**: Jira, ServiceNow
- **Artifact repository**: Artifactory, Nexus
- **CI/CD**: Jenkins, GitLab CI, GitHub Actions

---

## 🔵 NIVEL 3 - Definido

### 8. Desarrollo de Requerimientos (RD)

**Categoría**: Ingeniería  
**Propósito**: Producir y analizar requerimientos del cliente, del producto y de componentes del producto.

#### Objetivos Específicos
1. **SG 1**: Desarrollar requerimientos del cliente
   - Obtener necesidades
   - Transformar necesidades de stakeholders en requerimientos del cliente

2. **SG 2**: Desarrollar requerimientos del producto
   - Establecer requerimientos del producto y componente
   - Alocar requerimientos a componentes del producto
   - Identificar requerimientos de interfaz

3. **SG 3**: Analizar y validar requerimientos
   - Establecer conceptos y escenarios operacionales
   - Establecer una definición de funcionalidad requerida
   - Analizar requerimientos
   - Analizar requerimientos para lograr balance
   - Validar requerimientos

#### Tipos de Requerimientos

| Tipo | Descripción | Ejemplo |
|------|-------------|---------|
| **Funcionales** | Qué debe hacer el sistema | "El sistema debe permitir crear tickets" |
| **No Funcionales** | Atributos de calidad | "Tiempo de respuesta < 2seg" |
| **De Negocio** | Objetivos organizacionales | "Reducir tiempo de atención 30%" |
| **De Usuario** | Necesidades del usuario | "Como técnico, necesito ver mis tickets asignados" |
| **De Sistema** | Especificaciones técnicas | "Base de datos SQL Server 2019" |
| **De Interfaz** | Interacciones entre sistemas | "API RESTful con autenticación OAuth" |

#### Historia de Usuario (Formato Ágil)

```
Como [rol]
Quiero [funcionalidad]
Para [beneficio/valor]

Criterios de Aceptación:
- Dado [contexto]
- Cuando [acción]
- Entonces [resultado esperado]

Ejemplo:

Como Técnico de Soporte
Quiero ver un dashboard con mis tickets asignados
Para priorizar mi trabajo diariamente

Criterios de Aceptación:
- Dado que soy un técnico autenticado
- Cuando accedo al dashboard
- Entonces veo lista de mis tickets ordenados por prioridad
- Y puedo filtrar por estado (abierto/en progreso/cerrado)
- Y veo tiempo transcurrido desde creación
- Y puedo hacer clic para ver detalles
```

#### Técnicas de Elicitación
- 👥 Entrevistas
- 📋 Cuestionarios
- 👨‍👩‍👧‍👦 Grupos focales
- 👀 Observación
- 📄 Análisis de documentos
- 💡 Brainstorming
- 🏗️ Prototipos
- 📖 Casos de uso / Historias de usuario

---

### 9. Solución Técnica (TS)

**Categoría**: Ingeniería  
**Propósito**: Diseñar, desarrollar e implementar soluciones a requerimientos.

#### Objetivos Específicos
1. **SG 1**: Seleccionar soluciones de componente del producto
   - Desarrollar soluciones alternativas y criterios de selección
   - Seleccionar soluciones de componente del producto

2. **SG 2**: Desarrollar el diseño
   - Diseñar el producto o componente del producto
   - Establecer un paquete de datos técnicos
   - Diseñar interfaces usando criterios
   - Realizar análisis make-or-buy

3. **SG 3**: Implementar el diseño del producto
   - Implementar el diseño
   - Desarrollar documentación de soporte del producto

#### Proceso de Diseño

```
Requerimientos
    ↓
Diseño de Alto Nivel (Arquitectura)
  - Componentes principales
  - Patrones arquitectónicos
  - Tecnologías a usar
    ↓
Diseño Detallado
  - Diagramas de clases
  - Diseño de BD
  - APIs
    ↓
Implementación
  - Codificación
  - Revisiones de código
    ↓
Producto
```

#### Ejemplo: Arquitectura Sistema ISSEG

```
┌─────────────────────────────────────────┐
│         CAPA DE PRESENTACIÓN            │
│  ┌──────────┐  ┌────────────────────┐  │
│  │   Web    │  │  Dashboard Admin   │  │
│  │  Portal  │  │                    │  │
│  └──────────┘  └────────────────────┘  │
└─────────────────────────────────────────┘
                  ↓ HTTPS/REST
┌─────────────────────────────────────────┐
│         CAPA DE APLICACIÓN              │
│  ┌──────────────────────────────────┐  │
│  │      API Gateway (Auth)          │  │
│  └──────────────────────────────────┘  │
│  ┌─────────┐  ┌─────────┐  ┌────────┐ │
│  │ Ticket  │  │ Usuario │  │Reportes│ │
│  │ Service │  │ Service │  │Service │ │
│  └─────────┘  └─────────┘  └────────┘ │
└─────────────────────────────────────────┘
                  ↓
┌─────────────────────────────────────────┐
│          CAPA DE DATOS                  │
│  ┌───────────────┐  ┌────────────────┐ │
│  │  SQL Server   │  │  MongoDB (logs)│ │
│  │  (Principal)  │  │                │ │
│  └───────────────┘  └────────────────┘ │
└─────────────────────────────────────────┘
```

#### Patrones de Diseño Comunes
- **MVC** (Model-View-Controller)
- **Repository Pattern**
- **Dependency Injection**
- **Factory Pattern**
- **Strategy Pattern**
- **Observer Pattern**

---

### 10. Integración de Producto (PI)

**Categoría**: Ingeniería  
**Propósito**: Ensamblar el producto desde sus componentes, asegurar que el producto integrado funcione apropiadamente, y entregar el producto.

#### Objetivos Específicos
1. **SG 1**: Preparar la integración del producto
   - Determinar secuencia de integración
   - Establecer el ambiente de integración del producto
   - Establecer procedimientos y criterios de integración

2. **SG 2**: Asegurar compatibilidad de interfaces
   - Revisar completitud de interfaz
   - Gestionar interfaces

3. **SG 3**: Ensamblar componentes del producto y entregar el producto
   - Confirmar disposición de componentes
   - Ensamblar componentes
   - Evaluar componentes ensamblados
   - Empaquetar y entregar el producto

#### Estrategia de Integración

**Big Bang vs Incremental**:
```
❌ Big Bang (NO recomendado):
  [Componente A] ─┐
  [Componente B] ─┼→ [Integración] → [Muchos problemas]
  [Componente C] ─┘

✅ Incremental (Recomendado):
  [Base] → [+A] → [Testing] → [+B] → [Testing] → [+C] → [Testing]
```

**Enfoques**:
- **Top-Down**: Desde interfaz hacia componentes internos
- **Bottom-Up**: Desde componentes básicos hacia interfaz
- **Sandwich**: Combinación de ambos
- **Continuous Integration**: Integración constante y automatizada

#### Pipeline CI/CD

```
Commit → [Build] → [Unit Tests] → [Integration Tests] → [Deploy Dev]
            ↓          ↓                ↓
          Fail?     Fail?            Fail?
            ↓          ↓                ↓
         [Notificar desarrollador]
                                        ↓
                              [Smoke Tests] → Pass → [Deploy QA]
                                                         ↓
                                              [Regression Tests]
                                                         ↓
                                              [Deploy Staging]
                                                         ↓
                                                    [UAT Tests]
                                                         ↓
                                              [Deploy Production]
```

#### Herramientas CI/CD
- Jenkins
- GitLab CI/CD
- GitHub Actions
- Azure DevOps Pipelines
- CircleCI
- Travis CI

---

*[Continuará con las 12 áreas de proceso restantes en el mismo formato detallado...]*

Debido a la extensión, he creado las primeras 10 áreas de proceso en detalle. El documento completo incluiría:

- **Nivel 3**: VER, VAL, OPF, OPD, OT, IPM, RSKM, DAR
- **Nivel 4**: OPP, QPM
- **Nivel 5**: OID, CAR

Por brevedad, incluyo un resumen de las 12 restantes:

---

### 11-22. Resumen Áreas de Proceso Adicionales

| Área | Sigla | Nivel | Foco Principal |
|------|-------|-------|----------------|
| **Verificación** | VER | 3 | Asegurar que productos cumplen requerimientos especificados |
| **Validación** | VAL | 3 | Demostrar que el producto satisface su uso previsto |
| **Enfoque Organizacional en Procesos** | OPF | 3 | Planificar, implementar y desplegar mejoras de procesos |
| **Definición de Procesos Organizacionales** | OPD | 3 | Establecer conjunto de procesos estándar de la organización |
| **Capacitación Organizacional** | OT | 3 | Desarrollar habilidades y conocimiento de las personas |
| **Gestión Integrada de Proyecto** | IPM | 3 | Usar procesos organizacionales para gestionar el proyecto |
| **Gestión de Riesgos** | RSKM | 3 | Identificar problemas potenciales antes que ocurran |
| **Análisis y Toma de Decisiones** | DAR | 3 | Analizar decisiones posibles usando proceso formal |
| **Desempeño de Procesos Org.** | OPP | 4 | Establecer líneas base y modelos de desempeño cuantitativo |
| **Gestión Cuantitativa de Proyectos** | QPM | 4 | Gestionar proyecto cuantitativamente para lograr objetivos |
| **Innovación Organizacional** | OID | 5 | Seleccionar y desplegar mejoras incrementales e innovadoras |
| **Análisis Causal y Resolución** | CAR | 5 | Identificar causas de defectos y prevenir recurrencia |

---

## 📊 Tabla Completa: Áreas vs Niveles

```
 NIVEL                    ÁREAS DE PROCESO
   1     [Sin áreas de proceso definidas - Ad-hoc]
   
   2     REQM | PP | PMC | SAM | MA | PPQA | CM
   
   3     RD | TS | PI | VER | VAL | OPF | OPD | OT | IPM | RSKM | DAR
   
   4     OPP | QPM
   
   5     OID | CAR
```

---

## 🎯 Áreas de Proceso Prioritarias por Contexto

### Para Startups / Pequeñas Empresas
1. REQM - Gestión de Requerimientos
2. CM - Gestión de Configuración
3. VER - Verificación (testing)
4. RSKM - Gestión de Riesgos

### Para Proyectos Críticos
1. REQM - Gestión de Requerimientos
2. VER + VAL - Verificación y Validación
3. RSKM - Gestión de Riesgos
4. CM - Gestión de Configuración
5. QPM - Gestión Cuantitativa (para alta predictibilidad)

### Para Organizaciones en Crecimiento
1. OPD - Definición de Procesos Organizacionales
2. OPF - Enfoque Organizacional en Procesos
3. OT - Capacitación Organizacional
4. IPM - Gestión Integrada de Proyecto

---

## 📚 Conclusión

Las 22 áreas de proceso de CMMI trabajan en conjunto para crear una organización madura y capaz. No es necesario implementarlas todas a la vez:

- **Nivel 2**: Enfoque en gestión de proyectos individual
- **Nivel 3**: Enfoque en estandarización organizacional
- **Nivel 4**: Enfoque en medición y control cuantitativo
- **Nivel 5**: Enfoque en optimización continua

Cada organización debe priorizar según su contexto, industria y necesidades.

---

**Siguiente documento**: [04-Implementacion-CMMI.md](04-Implementacion-CMMI.md)

**Documento anterior**: [02-Niveles-de-Madurez-CMMI.md](02-Niveles-de-Madurez-CMMI.md)

**Volver al índice**: [00-INDICE-INVESTIGACION-CMMI.md](00-INDICE-INVESTIGACION-CMMI.md)
