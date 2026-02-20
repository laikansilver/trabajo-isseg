# Herramientas y Recursos para CMMI

## 🛠️ Herramientas por Área de Proceso

### Gestión de Requerimientos (REQM)

#### Herramientas Principales

| Herramienta | Tipo | Mejor Para | Precio | Rating |
|-------------|------|------------|--------|--------|
| **Jira** | Issue Tracking | Equipos ágiles medianos-grandes | $7-14/usuario/mes | ⭐⭐⭐⭐⭐ |
| **Azure DevOps** | ALM completo | Ecosistema Microsoft | $6/usuario/mes | ⭐⭐⭐⭐⭐ |
| **IBM DOORS** | Gestión de req | Proyectos críticos/complejos | $$$$ Enterprise | ⭐⭐⭐⭐ |
| **Jama Connect** | Gestión de req | Industrias reguladas | $$$ | ⭐⭐⭐⭐ |
| **ReqView** | Gestión de req | Equipos pequeños | €8/usuario/mes | ⭐⭐⭐⭐ |
| **Trello** | Kanban básico | Startups, equipos pequeños | Gratis-$12.50/usuario/mes | ⭐⭐⭐ |

#### Características Clave a Buscar
- ✅ Trazabilidad bidireccional
- ✅ Gestión de cambios con aprobaciones
- ✅ Versionamiento de requerimientos
- ✅ Matriz de trazabilidad automatizada
- ✅ Integración con herramientas de desarrollo
- ✅ Custom fields para atributos específicos
- ✅ Reportes y dashboards

#### Configuración Recomendada en Jira

```yaml
# Campos Custom para Requerimientos en Jira

Tipo de Requerimiento:
  - Funcional
  - No Funcional
  - Interfaz
  - Datos

Estado de Requerimiento:
  - Propuesto
  - En Análisis
  - Aprobado
  - En Desarrollo
  - En Pruebas
  - Implementado
  - Verificado

Criticidad:
  - Crítico (Must Have)
  - Alto (Should Have)
  - Medio (Could Have)
  - Bajo (Won't Have)

Trazabilidad:
  - Diseño Relacionado (Link)
  - PRs Relacionados (Link)
  - Test Cases (Link)

Métricas:
  - Complejidad (T-shirt: XS, S, M, L, XL)
  - Estimación (Story Points)
  - Esfuerzo Real (Horas)
```

---

### Planificación y Control de Proyectos (PP/PMC)

#### Herramientas de Gestión de Proyectos

| Herramienta | Fortalezas | Mejor Para | Precio |
|-------------|------------|------------|--------|
| **Microsoft Project** | Gantt robusto, integración Office | PMs tradicionales | $10-$30/usuario/mes |
| **Smartsheet** | Flexible, fácil de usar | Equipos colaborativos | $9-$32/usuario/mes |
| **Monday.com** | Visual, customizable | Equipos multifuncionales | $9-$19/usuario/mes |
| **Asana** | Intuitivo, múltiples vistas | Equipos ágiles | $10.99-$24.99/usuario/mes |
| **ClickUp** | Todo-en-uno | Equipos que buscan consolidar | $7-$19/usuario/mes |
| **Basecamp** | Comunicación integrada | Agencias, consultoras | $299/mes ilimitado |
| **Primavera P6** | Proyectos muy complejos | Construcción, EPC | $$$$ Enterprise |

#### Herramientas de Roadmapping

| Herramienta | Descripción | Precio |
|-------------|-------------|--------|
| **ProductPlan** | Roadmaps visuales para productos | $49-$99/mes |
| **Aha!** | Roadmaps estratégicos | $59-$149/usuario/mes |
| **Roadmunk** | Timelines visuales | $19-$99/usuario/mes |

#### Dashboards y Reportes

| Herramienta | Capacidades | Precio |
|-------------|-------------|--------|
| **Power BI** | BI completo, integración Microsoft | $10-$20/usuario/mes |
| **Tableau** | Visualizaciones avanzadas | $15-$70/usuario/mes |
| **Klipfolio** | Dashboards en tiempo real | $49-$799/mes |
| **Geckoboard** | Dashboards TV, KPIs | $39-$699/mes |

---

### Gestión de Configuración (CM)

#### Control de Versiones

| Herramienta | Descripción | Mejor Para | Precio |
|-------------|-------------|------------|--------|
| **Git** (GitHub/GitLab/Bitbucket) | Estándar de industria | Todos | Gratis-$21/usuario/mes |
| **Subversion (SVN)** | Control centralizado | Legacy, binarios grandes | Gratis |
| **Perforce Helix** | Alto rendimiento | Gaming, archivos masivos | $$$ |

#### Artifact Repositories

| Herramienta | Tipo | Mejor Para | Precio |
|-------------|------|------------|--------|
| **JFrog Artifactory** | Universal | Empresas medianas-grandes | $29-$150/mes |
| **Nexus Repository** | Java-centric | Maven/Gradle | Gratis-$$$ |
| **npm Registry** | JavaScript | Node.js projects | Gratis-$7/usuario/mes |
| **NuGet Gallery** | .NET | Proyectos .NET | Gratis |
| **Docker Hub** | Contenedores | Microservicios, containers | Gratis-$9/mes |

#### CI/CD Platforms

| Herramienta | Fortalezas | Mejor Para | Precio |
|-------------|------------|------------|--------|
| **Jenkins** | Flexible, plugins | Customización | Gratis (self-hosted) |
| **GitLab CI/CD** | Integrado con Git | DevOps completo | Gratis-$99/usuario/año |
| **GitHub Actions** | Nativo GitHub, mercado de actions | GitHub users | Gratis-$$$ |
| **Azure Pipelines** | Integración Microsoft | Ecosistema Azure/.NET | Gratis-$40/parallel job |
| **CircleCI** | Rápido, Docker nativo | Startups ágiles | Gratis-$70/mes |
| **Travis CI** | Open source friendly | Proyectos OSS | Gratis-$69/mes |

#### Package Managers

```bash
# Node.js
npm, yarn, pnpm

# Python
pip, poetry, conda

# .NET
NuGet

# Java
Maven, Gradle

# Ruby
gem, bundler

# Go
go modules

# PHP
Composer
```

---

### Medición y Análisis (MA)

#### Herramientas de Métricas de Código

| Herramienta | Métricas | Lenguajes | Precio |
|-------------|----------|-----------|--------|
| **SonarQube** | Calidad, cobertura, seguridad | 25+ | Gratis-$$$ |
| **CodeClimate** | Maintainability, duplication | Múltiples | $50-$400/mes |
| **Codacy** | Code quality automation | Múltiples | Gratis-$15/usuario/mes |
| **Coverity** | Análisis estático avanzado | C/C++, Java, etc | $$$ Enterprise |
| **ESLint** (JavaScript) | Linting | JavaScript/TypeScript | Gratis |
| **Pylint** (Python) | Linting | Python | Gratis |
| **ReSharper** (.NET) | Code quality | C#, VB.NET | $149-$299/año |

#### Herramientas de Cobertura de Pruebas

| Herramienta | Plataforma | Precio |
|-------------|------------|--------|
| **Codecov** | Cloud, múltiples lenguajes | Gratis-$29/mes |
| **Coveralls** | Cloud, integración CI | Gratis-$20/mes |
| **JaCoCo** | Java | Gratis |
| **Coverage.py** | Python | Gratis |
| **Istanbul/NYC** | JavaScript | Gratis |
| **dotCover** | .NET | $149/año |

#### APM y Monitoreo

| Herramienta | Capacidades | Precio |
|-------------|-------------|--------|
| **New Relic** | APM completo, observabilidad | $25-$99/usuario/mes |
| **Datadog** | APM, infraestructura, logs | $15-$23/host/mes |
| **Dynatrace** | AI-powered APM | $$$ Enterprise |
| **AppDynamics** | APM empresarial | $$$ Enterprise |
| **Grafana** | Dashboards, visualización | Gratis-$$$ |
| **Prometheus** | Time-series DB, alerting | Gratis |
| **ELK Stack** | Logs, búsqueda, análisis | Gratis-$$$ |

#### Herramientas Estadísticas

| Herramienta | Descripción | Precio |
|-------------|-------------|--------|
| **Excel** | Análisis básico | Incluido en Office |
| **R** | Análisis estadístico avanzado | Gratis |
| **Python** (pandas, numpy, matplotlib) | Ciencia de datos | Gratis |
| **Minitab** | Control estadístico de procesos | $1,700/licencia |
| **JMP** | Análisis estadístico visual | $2,520/licencia |
| **SPSS** | Análisis estadístico empresarial | $$$ |

---

### Aseguramiento de Calidad (PPQA)

#### Testing Frameworks

**Frontend**
```javascript
// JavaScript/TypeScript
- Jest
- Mocha + Chai
- Cypress (E2E)
- Playwright (E2E)
- Testing Library
```

**Backend**
```
# Java
- JUnit 5
- TestNG
- Mockito
- REST Assured

# Python
- pytest
- unittest
- nose2

# C#/.NET
- xUnit
- NUnit
- MSTest
- SpecFlow (BDD)

# Ruby
- RSpec
- Minitest
```

#### Herramientas de Testing

| Categoría | Herramienta | Descripción | Precio |
|-----------|-------------|-------------|--------|
| **Automatización UI** | Selenium | Web automation estándar | Gratis |
| | Cypress | Modern E2E testing | Gratis-$75/mes |
| | Playwright | Multi-browser automation | Gratis |
| | TestCafe | No requiere WebDriver | Gratis |
| **API Testing** | Postman | API development platform | Gratis-$49/usuario/mes |
| | Insomnia | REST client | Gratis |
| | REST Assured | Java | Gratis |
| | Karate | BDD + API | Gratis |
| **Performance** | JMeter | Load testing | Gratis |
| | Gatling | Load testing as code | Gratis-$$$ |
| | k6 | Modern load testing | Gratis-$$$ |
| | Locust | Python-based | Gratis |
| **Seguridad** | OWASP ZAP | Security testing | Gratis |
| | Burp Suite | Pen testing | Gratis-$399/año |
| | Snyk | Dependency scanning | Gratis-$$$ |
| **Test Management** | TestRail | Test case management | $35-$70/usuario/mes |
| | Zephyr | Jira integration | $10-$25/usuario/mes |
| | qTest | Enterprise TM | $$$ |
| | PractiTest | End-to-end QA | $39-$79/usuario/mes |

---

### Documentación

#### Wikis y Knowledge Base

| Herramienta | Fortalezas | Precio |
|-------------|------------|--------|
| **Confluence** | Integración Jira, espacios | $5.75-$11/usuario/mes |
| **Notion** | Flexible, databases | Gratis-$15/usuario/mes |
| **GitBook** | Docs como código, Git | Gratis-$8/usuario/mes |
| **Read the Docs** | Python-centric | Gratis-$50/mes |
| **Docusaurus** | React-based, OSS | Gratis |
| **MkDocs** | Markdown estático | Gratis |

#### Diagramas y Modelado

| Herramienta | Tipo | Precio |
|-------------|------|--------|
| **Lucidchart** | Diagramas cloud | $9-$30/usuario/mes |
| **Draw.io (diagrams.net)** | Diagramas | Gratis |
| **Miro** | Whiteboard colaborativo | Gratis-$10/usuario/mes |
| **PlantUML** | Diagramas como código | Gratis |
| **Mermaid** | Diagramas en Markdown | Gratis |
| **Enterprise Architect** | UML empresarial | $159-$469/licencia |
| **Visual Paradigm** | Modelado completo | $99-$699/licencia |

#### API Documentation

| Herramienta | Descripción | Precio |
|-------------|-------------|--------|
| **Swagger/OpenAPI** | API spec estándar | Gratis |
| **Postman** | API docs auto-generados | Gratis-$$$ |
| **ReadMe** | Developer hubs | $99-$399/mes |
| **Stoplight** | API design & docs | Gratis-$79/usuario/mes |

---

## 📦 Suites Integradas vs. Best-of-Breed

### Enfoque Suite Integrada

**Opción 1: Microsoft ALM Stack**
```
Azure DevOps (todo-en-uno)
├─ Azure Boards (Jira alternative)
├─ Azure Repos (Git)
├─ Azure Pipelines (CI/CD)
├─ Azure Test Plans (Testing)
└─ Azure Artifacts (Packages)
+
Visual Studio / VS Code
+
Power BI (Dashboards)
```
**Ventajas**: Integración perfecta, single vendor, SSO
**Desventajas**: Lock-in, menos flexibilidad
**Costo**: ~$50-100/usuario/mes (all-in)

---

**Opción 2: Atlassian Stack**
```
Jira (Project Management)
+
Confluence (Documentation)
+
Bitbucket (Git)
+
Bamboo (CI/CD)
+
Jira Service Desk (ITSM)
```
**Ventajas**: Popular, muchas integraciones, gran comunidad
**Desventajas**: Costo escala rápido, complejo de administrar
**Costo**: ~$30-80/usuario/mes

---

**Opción 3: GitLab (DevOps Platform)**
```
GitLab (todo-en-uno)
├─ Git Repos
├─ Issue Tracking
├─ CI/CD
├─ Container Registry
├─ Security Scanning
├─ Wiki
└─ Package Registry
```
**Ventajas**: único producto, DevOps completo, open source
**Desventajas**: UI menos pulida que competidores, curva aprendizaje
**Costo**: Gratis-$99/usuario/año

---

### Enfoque Best-of-Breed

**Opción: Stack Moderno**
```
GitHub (Repos + Actions CI/CD)
+
Linear (Issue tracking moderno, alternativa a Jira)
+
Notion (Docs + Knowledge base)
+
Vercel/Netlify (Deployment frontend)
+
Datadog (Monitoring)
+
SonarQube (Code quality)
```
**Ventajas**: Mejor herramienta para cada tarea, flexibilidad
**Desventajas**: Integración requiere esfuerzo, múltiples vendors
**Costo**: Variable, ~$40-100/usuario/mes

---

## 🎓 Recursos de Aprendizaje

### Libros Esenciales

#### CMMI Específicos

1. **"CMMI for Development: Guidelines for Process Improvement"** ⭐⭐⭐⭐⭐
   - Autores: Mary Beth Chrissis, Mike Konrad, Sandy Shrum
   - El libro oficial del SEI
   - ~700 páginas, referencia completa
   - Precio: ~$70

2. **"CMMI Distilled: A Practical Introduction"** ⭐⭐⭐⭐⭐
   - Autores: Dennis M. Ahern, Aaron Clouse, Richard Turner
   - Versión condensada y práctica
   - ~275 páginas, más accesible
   - Precio: ~$40

3. **"Interpreting the CMMI: A Process Improvement Approach"** ⭐⭐⭐⭐
   - Autoras: Margaret K. Kulpa, Kent A. Johnson
   - Enfoque pragmático de implementación
   - Ejemplos del mundo real
   - Precio: ~$60

4. **"Real Process Improvement Using the CMMI"** ⭐⭐⭐⭐
   - Autores: Michael West, et al.
   - Casos de estudio detallados
   - Lecciones aprendidas
   - Precio: ~$65

#### Gestión de Procesos y Calidad

5. **"The Goal" - Eliyahu M. Goldratt** ⭐⭐⭐⭐⭐
   - Teoría de restricciones (TOC)
   - Novela de negocios
   - Aplicable a procesos

6. **"Lean Software Development" - Mary & Tom Poppendieck** ⭐⭐⭐⭐
   - Principios Lean en software
   - Complementa CMMI

7. **"Accelerate" - Nicole Forsgren, Jez Humble, Gene Kim** ⭐⭐⭐⭐⭐
   - Investigación sobre DevOps
   - Métricas de desempeño
   - Data-driven

### Cursos y Certificaciones

#### Certificaciones CMMI Oficiales

| Certificación | Nivel | Duración | Costo | Proveedor |
|---------------|-------|----------|-------|-----------|
| **CMMI Associate** | Entry | 2 días | $1,500 | CMMI Institute |
| **CMMI Professional** | Intermediate | 5 días | $3,500 | CMMI Institute |
| **CMMI Expert** | Advanced | 10+ días | $8,000+ | CMMI Institute |
| **Certified Instructor** | Teaching | Variable | $$$$$ | CMMI Institute |

**Partners Autorizados**:
- CMMI Institute (oficial): https://cmmiinstitute.com/
- QAI (Quality Assurance Institute)
- Tecnológico de Monterrey (México)
- DXC Technology

#### Cursos Online

| Plataforma | Curso | Duración | Costo | Rating |
|------------|-------|----------|-------|--------|
| **Udemy** | "CMMI for Development v2.0" | 8 hrs | $15-$100 | ⭐⭐⭐⭐ |
| **Coursera** | "Software Processes and Agile" | 4 weeks | Gratis-$49/mes | ⭐⭐⭐⭐ |
| **LinkedIn Learning** | "CMMI Foundations" | 2 hrs | $39.99/mes | ⭐⭐⭐⭐ |
| **Pluralsight** | "Software Process Improvement" | 3 hrs | $29/mes | ⭐⭐⭐⭐ |

#### MOOCs Gratuitos

- **MIT OpenCourseWare**: "Software Engineering" - Gratis
- **Stanford Online**: "SE Processes" - Gratis
- **edX**: Varios cursos sobre calidad de software - Gratis-$99

### Sitios Web y Blogs

#### Sitios Oficiales

- **CMMI Institute**: https://cmmiinstitute.com/
  - Documentación oficial
  - White papers
  - Case studies

- **Software Engineering Institute (SEI)**: https://www.sei.cmu.edu/
  - Investigación
  - Recursos técnicos
  - Publicaciones

#### Blogs y Comunidades

- **CMMI Institute Blog**: https://cmmiinstitute.com/blog
- **InfoQ - Process Improvement**: https://www.infoq.com/process-improvement/
- **DZone - Agile Zone**: https://dzone.com/agile-methodology-training-tools-news
- **Reddit r/softwareengineering**: Discusiones de comunidad

#### Podcasts

- **"Software Engineering Daily"**: Episodios sobre procesos
- **"The Changelog"**: Prácticas de desarrollo
- **"Engineering Culture"**: Cultura de ingeniería

### Estándares Relacionados

| Estándar | Descripción | Relación con CMMI |
|----------|-------------|-------------------|
| **ISO 9001** | Gestión de calidad | Complementario |
| **ISO/IEC 15504 (SPICE)** | Evaluación de procesos de software | Similar, más europeo |
| **ISO/IEC 12207** | Procesos ciclo de vida del software | Base de CMMI |
| **ISO/IEC 27001** | Seguridad de información | Área específica |
| **ISO/IEC 29110** | CMMI para PyMEs | Versión ligera |
| **ITIL** | Gestión de servicios TI | Operaciones |
| **COBIT** | Gobierno de TI | Nivel ejecutivo |

---

## 💡 Herramientas Recomendadas por Tamaño de Empresa

### Startup / Pequeña (5-20 personas)

**Presupuesto**: $50-150/mes

**Stack Recomendado**:
```
GitHub (Repos + Actions): $7/usuario/mes = $140/mes
+
Linear (Issues): $8/usuario/mes = $160/mes (o usar GitHub Issues gratis)
+
Notion (Docs): $10/usuario/mes = $200/mes
+
Codecov (Coverage): Gratis
+
SonarCloud (Code Quality): Gratis para OSS, $10/mes privado

TOTAL: ~$510/mes ($25.50/usuario/mes)

Alternativa Económica:
GitHub + GitHub Projects + GitHub Wiki: $7/usuario/mes = $140/mes
```

---

### Mediana (20-100 personas)

**Presupuesto**: $2,000-5,000/mes

**Opción 1: Atlassian Stack**
```
Jira Software: $7.75/usuario/mes × 100 = $775
Confluence: $5.75/usuario/mes × 100 = $575
Bitbucket: $3/usuario/mes × 100 = $300
SonarQube: $2,000/año = $167/mes

TOTAL: ~$1,817/mes
```

**Opción 2: Microsoft Stack**
```
Azure DevOps: $6/usuario/mes × 100 = $600
Power BI: $10/usuario/mes × 20 (solo PMs) = $200
Office 365: Generalmente ya tienen
SonarQube: $2,000/año = $167/mes

TOTAL: ~$967/mes
```

---

### Grande / Enterprise (100+ personas)

**Presupuesto**: $10,000-50,000/mes

**Stack Enterprise**:
```
Azure DevOps Server (on-prem): $6/usuario × 500 = $3,000
O
Jira Data Center: Licencia perpetua + $12,000/año mantenimiento

GitLab Ultimate: $99/usuario/año × 500 = $4,125/mes

SonarQube Enterprise: $150,000/año = $12,500/mes

Artifactory Enterprise: $29,000/año = $2,417/mes

Dynatrace APM: Enterprise pricing ~$10,000-30,000/mes

TOTAL: ~$30,000-60,000/mes
```

---

## 🚀 Setup de Herramientas para Proyecto ISSEG

### Configuración Recomendada (Nivel 2)

#### Opción A: Microsoft Azure Stack (Recomendada si ya usan Microsoft)

**Herramientas**:
- **Azure DevOps**: Boards, Repos, Pipelines
- **VS Code**: Editor
- **SQL Server**: Base de datos
- **Power BI**: Dashboards

**Costo**: ~$50/mes (equipo de 8 personas)

**Pasos de Setup**:
```powershell
# 1. Crear organización Azure DevOps
# Web: https://dev.azure.com

# 2. Crear proyecto "ISSEG"

# 3. Configurar Boards
# - Crear custom fields para requerimientos
# - Configurar workflow de tickets
# - Crear dashboards

# 4. Configurar Repos
git clone https://dev.azure.com/org/ISSEG/_git/ISSEG
cd ISSEG
# Crear estructura
mkdir -p src/backend src/frontend docs tests

# 5. Configurar Pipeline
# Crear azure-pipelines.yml
```

**azure-pipelines.yml** (ejemplo):
```yaml
trigger:
  - main
  - develop

pool:
  vmImage: 'ubuntu-latest'

stages:
- stage: Build
  jobs:
  - job: BuildBackend
    steps:
    - task: UseDotNet@2
      inputs:
        version: '8.x'
    - script: dotnet build src/backend
      displayName: 'Build Backend'
    - script: dotnet test src/backend/tests
      displayName: 'Run Tests'
    - task: PublishCodeCoverageResults@1
      inputs:
        codeCoverageTool: 'Cobertura'
        summaryFileLocation: '**/coverage.cobertura.xml'

- stage: QualityGate
  jobs:
  - job: SonarQube
    steps:
    - task: SonarQubePrepare@5
    - task: SonarQubeAnalyze@5
    - task: SonarQubePublish@5

- stage: Deploy
  condition: and(succeeded(), eq(variables['Build.SourceBranch'], 'refs/heads/main'))
  jobs:
  - job: DeployDev
    steps:
    - script: echo "Deploy to Dev environment"
```

---

#### Opción B: GitHub Stack (Moderna y flexible)

**Herramientas**:
- **GitHub**: Repos, Projects, Actions, Wiki
- **SonarCloud**: Code quality
- **Codecov**: Coverage
- **VS Code**: Editor

**Costo**: ~$70/mes (Team plan para 8 personas)

**Pasos de Setup**:
```bash
# 1. Crear organización en GitHub
# Web: https://github.com/organizations/plan

# 2. Crear repositorio "ISSEG"
gh repo create org/ISSEG --private

# 3. Configurar estructura
git clone https://github.com/org/ISSEG.git
cd ISSEG

# Crear estructura
mkdir -p .github/workflows src/backend src/frontend docs tests
touch .github/workflows/ci.yml
touch README.md

# 4. Configurar GitHub Projects para gestión
# Web: Projects tab → New Project → Board view
```

**.github/workflows/ci.yml** (ejemplo):
```yaml
name: CI

on:
  push:
    branches: [ main, develop ]
  pull_request:
    branches: [ main, develop ]

jobs:
  build-and-test:
    runs-on: ubuntu-latest
    
    steps:
    - uses: actions/checkout@v3
    
    - name: Setup .NET
      uses: actions/setup-dotnet@v3
      with:
        dotnet-version: '8.0.x'
    
    - name: Restore dependencies
      run: dotnet restore
    
    - name: Build
      run: dotnet build --no-restore
    
    - name: Test
      run: dotnet test --no-build --verbosity normal --collect:"XPlat Code Coverage"
    
    - name: Upload coverage to Codecov
      uses: codecov/codecov-action@v3
      with:
        token: ${{ secrets.CODECOV_TOKEN }}
    
    - name: SonarCloud Scan
      uses: SonarSource/sonarcloud-github-action@master
      env:
        GITHUB_TOKEN: ${{ secrets.GITHUB_TOKEN }}
        SONAR_TOKEN: ${{ secrets.SONAR_TOKEN }}
```

---

## 📋 Checklist de Herramientas para CMMI

### Nivel 2 - Esenciales

- [ ] **Control de versiones**: Git (GitHub/GitLab/Azure Repos)
- [ ] **Issue tracking**: Jira/Azure Boards/GitHub Issues
- [ ] **CI/CD**: GitHub Actions/Azure Pipelines/GitLab CI
- [ ] **Documentación**: Confluence/Notion/GitHub Wiki
- [ ] **Code quality**: SonarQube/SonarCloud
- [ ] **Testing framework**: JUnit/pytest/xUnit
- [ ] **Comunicación**: Slack/Teams

### Nivel 3 - Optimización

- [ ] **Process library**: Confluence/SharePoint
- [ ] **Metrics dashboard**: Power BI/Tableau/Grafana
- [ ] **APM**: New Relic/Datadog
- [ ] **Test management**: TestRail/Zephyr
- [ ] **Artifact repository**: Artifactory/Nexus

### Nivel 4-5 - Avanzadas

- [ ] **Statistical tools**: Minitab/R/Python
- [ ] **Advanced analytics**: ML para predicción
- [ ] **Process mining**: Celonis/ProcessGold

---

**Siguiente documento**: [07-Casos-de-Exito-y-Mejores-Practicas.md](07-Casos-de-Exito-y-Mejores-Practicas.md)

**Documento anterior**: [05-Aplicacion-CMMI-Proyecto-ISSEG.md](05-Aplicacion-CMMI-Proyecto-ISSEG.md)

**Volver al índice**: [00-INDICE-INVESTIGACION-CMMI.md](00-INDICE-INVESTIGACION-CMMI.md)
