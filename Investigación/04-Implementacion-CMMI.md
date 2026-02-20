# Implementación de CMMI

## 📋 Introducción

La implementación de CMMI es un **viaje de transformación organizacional**, no un proyecto con fecha de término. Requiere compromiso, recursos y una visión de largo plazo. Este documento proporciona una guía práctica para implementar CMMI exitosamente.

## 🎯 Antes de Comenzar: Preguntas Críticas

### ¿Está Lista Mi Organización?

Evalúa estas dimensiones antes de iniciar:

| Dimensión | ✅ Listo | ⚠️ Riesgoso | ❌ No Listo |
|-----------|---------|-------------|-------------|
| **Apoyo de Dirección** | CEO/CTO comprometido activamente | Apoyo verbal sin recursos | No hay interés |
| **Recursos** | Personal y presupuesto asignado | Recursos "si hay tiempo" | Sin recursos |
| **Cultura** | Cultura de mejora continua | Resistencia moderada | Cultura de culpa |
| **Problemas Actuales** | Problemas recurrentes identificados | Algunos problemas | Todo funciona perfecto |
| **Tamaño** | >10 personas | 5-10 personas | <5 personas |
| **Estabilidad** | Organización estable | Cambios moderados | En crisis |

**Interpretación**:
- **Mayoría ✅**: Adelante con confianza
- **Mix ✅/⚠️**: Preparar primero, luego implementar
- **Algún ❌**: Resolver bloqueadores antes de iniciar

### Motivaciones Correctas vs Incorrectas

| ✅ Motivaciones Correctas | ❌ Motivaciones Incorrectas |
|--------------------------|----------------------------|
| Mejorar calidad y eficiencia | Solo para ganar una licitación |
| Escalar el negocio estructuradamente | Porque la competencia lo tiene |
| Reducir problemas recurrentes | Por presión de un cliente |
| Profesionalizar la operación | Para "verse bien" |
| Prepararse para crecimiento | Porque está de moda |

## 🗺️ Roadmap de Implementación

### Visión General (Timeline)

```
┌──────────────────────────────────────────────────────────────┐
│              IMPLEMENTACIÓN CMMI NIVEL 2 Y 3                 │
└──────────────────────────────────────────────────────────────┘

AÑO 1: NIVEL 2
├─ Q1: Preparación (Meses 1-3)
│  ├─ Semanas 1-2: Kick-off y capacitación inicial
│  ├─ Semanas 3-6: GAP Analysis
│  └─ Semanas 7-12: Planificación detallada
│
├─ Q2: Implementación L2 - Parte 1 (Meses 4-6)
│  ├─ REQM: Gestión de Requerimientos
│  ├─ PP: Planificación de Proyectos
│  └─ PMC: Monitoreo y Control
│
├─ Q3: Implementación L2 - Parte 2 (Meses 7-9)
│  ├─ CM: Gestión de Configuración
│  ├─ MA: Medición y Análisis
│  └─ PPQA: Aseguramiento de Calidad
│
└─ Q4: Consolidación y Preparación (Meses 10-12)
   ├─ SAM: Gestión de Proveedores (si aplica)
   ├─ Auditorías internas
   └─ Ajustes basados en lecciones aprendidas

AÑO 2: NIVEL 3
├─ Q1: Planeación Organizacional (Meses 13-15)
│  ├─ OPD: Definición de Procesos Organizacionales
│  ├─ OPF: Enfoque Organizacional en Procesos
│  └─ OT: Capacitación Organizacional
│
├─ Q2: Ingeniería Disciplinada (Meses 16-18)
│  ├─ RD: Desarrollo de Requerimientos
│  ├─ TS: Solución Técnica
│  └─ PI: Integración de Producto
│
├─ Q3: Verificación y Validación (Meses 19-21)
│  ├─ VER: Verificación
│  ├─ VAL: Validación
│  └─ RSKM: Gestión de Riesgos
│
└─ Q4: Integración y Certificación (Meses 22-24)
   ├─ IPM: Gestión Integrada de Proyecto
   ├─ DAR: Análisis y Toma de Decisiones
   ├─ Pre-auditoría SCAMPI
   └─ Auditoría SCAMPI A (opcional)
```

---

## 📊 Fase 1: Preparación (Meses 1-3)

### Paso 1.1: Kick-off y Formación del Equipo (Semanas 1-2)

#### Acciones

1. **Anuncio Oficial**
   - Comunicado de la dirección a toda la organización
   - Explicar el "por qué" y beneficios esperados
   - Presentar la visión y el compromiso

2. **Formación del SEPG (Software Engineering Process Group)**
   
   **Composición Típica**:
   - 1 Process Manager (líder, 100% dedicado)
   - 2-3 Process Engineers (50-70% dedicado)
   - Representantes de cada área (20-30% dedicado):
     * Desarrollo
     * QA
     * Gestión de Proyectos
     * Arquitectura
     * Operaciones

   **Responsabilidades**:
   - Diseñar y documentar procesos
   - Brindar capacitación y coaching
   - Recolectar y analizar métricas
   - Gestionar la mejora de procesos

3. **Formación del Management Steering Committee**
   
   **Composición**:
   - CEO / Director General
   - CTO / Director de Tecnología
   - CFO / Director Financiero
   - VP de Operaciones
   - Process Manager
   
   **Responsabilidades**:
   - Proveer dirección estratégica
   - Aprobar inversiones
   - Remover impedimentos
   - Revisar progreso trimestralmente

4. **Capacitación Inicial**
   - Capacitación de 2-3 días en fundamentos de CMMI
   - Para SEPG: Capacitación intensiva de 5 días
   - Para dirección: Workshop ejecutivo de 1 día
   - Para equipo completo: Sesión de awareness de 2 horas

#### Presupuesto Estimado (Fase 1.1)

| Ítem | Costo Estimado |
|------|----------------|
| Capacitación SEPG (5 días) | $5,000 - $8,000 |
| Capacitación Ejecutiva (1 día) | $2,000 - $3,000 |
| Sesión Awareness (toda empresa) | $1,000 - $2,000 |
| Consultor externo (opcional, 2 sem) | $8,000 - $15,000 |
| **TOTAL** | **$16,000 - $28,000** |

---

### Paso 1.2: GAP Analysis - Evaluación del Estado Actual (Semanas 3-6)

#### Objetivo
Determinar dónde está la organización actualmente versus dónde necesita estar según CMMI.

#### Metodología

1. **Preparación** (Semana 3)
   - Definir alcance de la evaluación
   - Identificar proyectos representativos (2-3)
   - Preparar cuestionarios
   - Programar entrevistas

2. **Recolección de Datos** (Semanas 4-5)
   - **Entrevistas** (1-2 horas c/u):
     * Gerentes de proyecto
     * Desarrolladores
     * QA
     * Stakeholders
   
   - **Revisión de Documentación**:
     * Planes de proyecto existentes
     * Documentos de requerimientos
     * Informes de status
     * Procedimientos (si existen)
     * Registros de defectos
   
   - **Observación**:
     * Seguimiento de reuniones
     * Revisión de herramientas
     * Inspección de repositorios

3. **Análisis** (Semana 6)
   - Mapear prácticas actuales vs. CMMI
   - Identificar fortalezas y debilidades
   - Cuantificar brechas

#### Herramienta: Matriz de GAP Analysis

```
Área de Proceso: REQM - Gestión de Requerimientos

┌─────────────────────────┬──────────┬──────────┬────────────┐
│ Práctica Específica     │ Estado   │ Evidencia│ Brecha     │
├─────────────────────────┼──────────┼──────────┼────────────┤
│ SP 1.1: Entender req.   │ Parcial  │ Emails   │ Falta doc  │
│ SP 1.2: Compromiso      │ No       │ Ninguna  │ ALTA       │
│ SP 1.3: Gestión cambios │ Ad-hoc   │ Jira     │ Media      │
│ SP 1.4: Trazabilidad    │ No       │ Ninguna  │ ALTA       │
│ SP 1.5: Inconsistencias │ Reactivo │ Bugs     │ Media      │
└─────────────────────────┴──────────┴──────────┴────────────┘

Estado: Completo | Parcial | Ad-hoc | No
Brecha: ALTA | Media | Baja | Ninguna

Calificación Área REQM: 35% de cumplimiento
```

#### Ejemplo de Hallazgos

```
═══════════════════════════════════════════════════════
           GAP ANALYSIS SUMMARY - NIVEL 2
═══════════════════════════════════════════════════════

REQM - Gestión de Requerimientos: 35% ██████░░░░░░░░░░░░░░
  ✅ Fortalezas:
     - Se usa Jira para tracking básico
  ❌ Debilidades:
     - No hay matriz de trazabilidad
     - Cambios no son formalmente aprobados
     - No hay compromiso documentado con stakeholders

PP - Planificación de Proyectos: 45% █████████░░░░░░░░░░░
  ✅ Fortalezas:
     - Existen cronogramas en MS Project
     - Se estiman tareas
  ❌ Debilidades:
     - Estimaciones no basadas en datos históricos
     - No hay plan de riesgos
     - Recursos no formalmente comprometidos

PMC - Monitoreo y Control: 50% ██████████░░░░░░░░░░
  ✅ Fortalezas:
     - Reuniones semanales de status
     - Dashboard básico de métricas
  ❌ Debilidades:
     - No se compara actual vs. plan sistemáticamente
     - Acciones correctivas no se documentan

CM - Gestión de Configuración: 70% ██████████████░░░░░░
  ✅ Fortalezas:
     - Git usado consistentemente
     - Branches organizados
     - CI/CD básico implementado
  ❌ Debilidades:
     - No todas las configuraciones versionadas
     - Auditorías de configuración inexistentes

MA - Medición y Análisis: 25% █████░░░░░░░░░░░░░░░
  ✅ Fortalezas:
     - Algunas métricas en Jira
  ❌ Debilidades:
     - No hay plan de medición
     - Métricas no alineadas a objetivos
     - Análisis de datos es informal

PPQA - Aseguramiento de Calidad: 40% ████████░░░░░░░░░░░░
  ✅ Fortalezas:
     - Existe rol de QA
     - Code reviews ocasionales
  ❌ Debilidades:
     - No hay auditorías de proceso
     - No-conformidades no se documentan
     - No hay registros de QA

SAM - Gestión de Proveedores: N/A (No aplica actualmente)

───────────────────────────────────────────────────────
PROMEDIO NIVEL 2: 44%  (Objetivo: 85%+ para certificar)
BRECHA TOTAL: 41 puntos porcentuales
ESFUERZO ESTIMADO: 9-12 meses
───────────────────────────────────────────────────────
```

#### Entregables de GAP Analysis

1. **Reporte de GAP Analysis** (20-30 páginas)
   - Executive Summary
   - Metodología
   - Hallazgos por área de proceso
   - Fortalezas y debilidades
   - Recomendaciones

2. **Matriz de Brechas** (Excel)
   - Detalle práctica por práctica
   - Estado actual
   - Evidencias
   - Prioridad

3. **Presentación a Dirección** (15-20 slides)
   - Resumen ejecutivo
   - Hallazgos clave
   - Inversión requerida
   - Roadmap propuesto

---

### Paso 1.3: Planificación Detallada (Semanas 7-12)

#### Acciones

1. **Definir Objetivos SMART**

   Ejemplo:
   ```
   ❌ MAL: "Mejorar la calidad"
   
   ✅ BIEN: "Reducir la densidad de defectos en producción 
              de 2.5 def/KLOC a 1.0 def/KLOC en 12 meses,
              medido mediante el sistema de tracking de bugs"
   ```

2. **Priorizar Áreas de Proceso**

   Criterios de priorización:
   - **Impacto en objetivos de negocio** (40%)
   - **Magnitud de brecha** (30%)
   - **Facilidad de implementación** (20%)
   - **Dependencias** (10%)

   Ejemplo de priorización Nivel 2:
   ```
   FASE 1 (Meses 4-6):
   1. REQM (Score: 85) - Fundacional
   2. PP (Score: 80) - Fundacional
   3. CM (Score: 75) - Menos brecha, alta facilidad
   
   FASE 2 (Meses 7-9):
   4. PMC (Score: 70) - Depende de PP
   5. MA (Score: 65) - Habilita mejora continua
   6. PPQA (Score: 60) - Verifica compliance
   
   FASE 3 (Meses 10-12):
   7. SAM (Score: 40) - Baja prioridad, solo si aplica
   ```

3. **Crear Plan de Proyecto de Implementación**

   Componentes:
   - WBS detallado
   - Cronograma (Gantt)
   - Presupuesto detallado
   - Plan de recursos
   - Plan de comunicación
   - Plan de gestión de riesgos
   - Criterios de éxito

4. **Definir Quick Wins**

   Identificar mejoras de rápida implementación para generar momentum:
   - Implementar code reviews sistemáticos → 2 semanas
   - Crear template de plan de proyecto → 1 semana
   - Establecer reuniones de status semanales → inmediato
   - Implementar branching strategy en Git → 1 semana
   - Dashboard básico de métricas → 3 semanas

#### Ejemplo de Plan de Proyecto (Resumen)

```
PROYECTO: Implementación CMMI Nivel 2
SPONSOR: CTO
PROJECT MANAGER: Process Manager
DURACIÓN: 12 meses
PRESUPUESTO: $120,000

FASES:
1. Preparación (3 meses) - $28,000
2. Implementación Fase 1 (3 meses) - $35,000
3. Implementación Fase 2 (3 meses) - $35,000
4. Consolidación (3 meses) - $22,000

RECURSOS:
- 1 Process Manager (FTE)
- 2 Process Engineers (0.5 FTE c/u)
- 1 Consultor externo (0.3 FTE)
- Representantes de áreas (0.2 FTE c/u)

HITOS CLAVE:
- M3: GAP Analysis completado
- M6: REQM, PP, CM implementados
- M9: PMC, MA, PPQA implementados
- M11: Pre-auditoría interna
- M12: Nivel 2 operando establemente

RIESGOS TOP 3:
1. Resistencia al cambio (Prob: Alta, Imp: Alto)
   → Mitigación: Programa de change management
2. Falta de tiempo del equipo (Prob: Media, Imp: Alto)
   → Mitigación: Proteger 20% del tiempo
3. Rotación de personal (Prob: Media, Imp: Medio)
   → Mitigación: Documentación exhaustiva
```

---

## 🚀 Fase 2: Implementación de Nivel 2 (Meses 4-12)

### Enfoque General de Implementación por Área de Proceso

Para cada área de proceso, seguir este ciclo:

```
1. DISEÑO (2-3 semanas)
   ├─ Estudiar el área de proceso (SEPG)
   ├─ Identificar mejores prácticas de industria
   ├─ Adaptar al contexto organizacional
   ├─ Diseñar procedimientos y plantillas
   └─ Revisar con stakeholders

2. PILOTO (3-4 semanas)
   ├─ Seleccionar proyecto piloto
   ├─ Capacitar al equipo piloto
   ├─ Ejecutar proceso en el piloto
   ├─ Recolectar feedback
   └─ Analizar resultados

3. AJUSTE (1-2 semanas)
   ├─ Incorporar lecciones aprendidas
   ├─ Simplificar donde sea posible
   ├─ Actualizar documentación
   └─ Preparar para rollout

4. ROLLOUT (2-3 semanas)
   ├─ Capacitar a todos los equipos
   ├─ Desplegar proceso en todos los proyectos
   ├─ Proveer soporte intensivo
   └─ Monitorear adopción

5. INSTITUCIONALIZACIÓN (continuo)
   ├─ Auditorías periódicas (PPQA)
   ├─ Coaching y refuerzo
   ├─ Recolección de métricas
   └─ Mejora continua
```

---

### Implementación REQM - Gestión de Requerimientos

#### Semana 1-2: Diseño

**Artefactos a crear**:

1. **Procedimiento de Gestión de Requerimientos**
   ```
   PROC-REQM-001: Procedimiento de Gestión de Requerimientos
   
   1. Propósito
   2. Alcance
   3. Roles y Responsabilidades
      - Product Owner: Propietario de requerimientos
      - Business Analyst: Documentar y analizar
      - Tech Lead: Validar factibilidad técnica
      - QA: Validar testabilidad
   4. Proceso
      4.1 Captura de Requerimientos
      4.2 Análisis y Documentación
      4.3 Revisión y Aprobación
      4.4 Gestión de Cambios
      4.5 Trazabilidad
   5. Plantillas
   6. Herramientas
   7. Métricas
   ```

2. **Plantilla de Especificación de Requerimientos**
   ```
   [TEMPLATE-REQ-001.docx]
   
   1. Información del Requerimiento
      - ID: REQ-XXXX
      - Título
      - Prioridad: Alta/Media/Baja
      - Estado: Propuesto/Aprobado/Implementado/Verificado
      - Fuente: [Stakeholder]
      - Fecha de creación
   
   2. Descripción
      - Descripción detallada
      - Justificación de negocio
      - Criterios de aceptación
   
   3. Trazabilidad
      - Requerimientos relacionados
      - Casos de uso / Historias de usuario
      - Diseño: [Enlaces a documentos de diseño]
      - Código: [Enlaces a commits/PRs]
      - Pruebas: [Enlaces a casos de prueba]
   
   4. Historial de Cambios
      - [Tabla con cambios]
   ```

3. **Matriz de Trazabilidad (Excel/Jira)**
   ```
   | Req ID | Título | Diseño | Código | Pruebas | Estado |
   |--------|--------|--------|--------|---------|--------|
   | REQ-001| Login  | DES-01 | PR-123 | TC-001  | Done   |
   ```

4. **Proceso de Gestión de Cambios**
   ```
   Solicitud de Cambio
       ↓
   [¿Impacto Menor?] → Sí → Aprobación de Product Owner
       ↓ No                      ↓
   Análisis de Impacto      Actualizar Req
       ↓                         ↓
   CCB (Change Control Board)   Notificar Equipo
       ↓                         ↓
   Decisión: Aprobar/Rechazar/Diferir
       ↓ Aprobar
   Actualizar Plan y Cronograma
       ↓
   Comunicar a Stakeholders
   ```

#### Semana 3-6: Piloto

**Proyecto Piloto**: Sistema de Tickets ISSEG - Formulario A

**Actividades**:
1. **Capacitación del equipo** (1 día)
   - Workshop de 4 horas sobre el proceso
   - Hands-on con plantillas
   - Q&A

2. **Ejecución del piloto** (3 semanas)
   - Capturar 20-30 requerimientos del Formulario A
   - Documentar usando plantillas
   - Crear matriz de trazabilidad
   - Procesar 3-5 cambios de requerimientos
   - Reunión semanal de lecciones aprendidas

3. **Medición**
   ```
   Métricas recolectadas:
   - Tiempo promedio para documentar un requerimiento: 25 min
   - % de requerimientos con trazabilidad completa: 85%
   - Número de cambios de requerimientos: 4
   - Tiempo promedio de procesamiento de cambio: 2 días
   - Satisfacción del equipo (1-5): 4.2
   ```

4. **Feedback del equipo**
   ```
   Positivo:
   + "La plantilla es clara y fácil de usar"
   + "La trazabilidad ayuda a entender el impacto"
   + "El proceso de cambios evita sorpresas"
   
   A Mejorar:
   - "La plantilla tiene campos que no siempre aplican"
   - "Jira debería integrarse mejor con la matriz"
   - "Necesitamos un campo para prioridad técnica"
   ```

#### Semana 7-8: Ajuste

**Cambios incorporados**:
- ✅ Simplificar plantilla: campos opcionales claramente marcados
- ✅ Integrar matriz de trazabilidad en Jira mediante custom fields
- ✅ Agregar campo "Complejidad Técnica" (T-shirt sizing)
- ✅ Crear guía rápida de 1 página
- ✅ Grabar video tutorial de 10 minutos

#### Semana 9-12: Rollout

**Despliegue**:
1. **Capacitación masiva**
   - 3 sesiones de 2 horas (para acomodar horarios)
   - Todos los roles: PM, Dev, QA, PO

2. **Soporte intensivo** (primeras 2 semanas)
   - Office hours diarios (1 hora)
   - Slack channel #cmmi-reqm-support
   - Process Engineer embedded en equipos

3. **Monitoreo de adopción**
   ```
   Dashboard de Adopción - REQM
   
   Semana 9: ██████░░░░░░░░░░░░░░ 30% adopción
   Semana 10: ██████████░░░░░░░░░░ 50% adopción
   Semana 11: ███████████████░░░░░ 75% adopción
   Semana 12: ███████████████████░ 95% adopción
   
   Indicadores:
   - % de requerimientos documentados con template: 95%
   - % con trazabilidad: 89%
   - % de cambios siguiendo proceso: 92%
   ```

4. **Auditoría PPQA** (Semana 12)
   - Revisar muestreo de 10 requerimientos
   - Verificar adherencia al proceso
   - Reportar no-conformidades
   - Acciones correctivas

#### Resultado: REQM Implementado ✅

---

### Tiempo y Recursos por Área de Proceso

| Área | Diseño | Piloto | Ajuste | Rollout | **Total** | Esfuerzo SEPG |
|------|--------|--------|--------|---------|-----------|---------------|
| REQM | 2 sem | 4 sem | 2 sem | 4 sem | **12 sem** | 200 hrs |
| PP | 3 sem | 4 sem | 2 sem | 3 sem | **12 sem** | 220 hrs |
| PMC | 2 sem | 3 sem | 1 sem | 3 sem | **9 sem** | 160 hrs |
| CM | 2 sem | 3 sem | 2 sem | 3 sem | **10 sem** | 180 hrs |
| MA | 3 sem | 4 sem | 2 sem | 3 sem | **12 sem** | 210 hrs |
| PPQA | 2 sem | 3 sem | 1 sem | 2 sem | **8 sem** | 140 hrs |
| SAM | 2 sem | 2 sem | 1 sem | 2 sem | **7 sem** | 120 hrs |

**Notas**:
- Áreas se implementan en paralelo (overlap)
- Timeline total: ~10-12 meses para Nivel 2 completo
- Esfuerzo SEPG total: ~1,230 horas (~0.75 FTE por 12 meses)

---

## 📈 Fase 3: Implementación de Nivel 3 (Meses 13-24)

### Diferencia Clave con Nivel 2

En **Nivel 2**, cada proyecto puede tener sus propios procesos.
En **Nivel 3**, la organización define procesos estándar que todos adaptan.

### Pasos Principales

#### 1. Crear la Biblioteca Organizacional de Procesos (Meses 13-15)

**Componentes**:

```
📚 Biblioteca Organizacional de Procesos (OPL)
├── 📁 Procesos Estándar
│   ├── PROC-STD-001: Proceso Estándar de Desarrollo
│   ├── PROC-STD-002: Proceso Estándar de Gestión de Proyectos
│   ├── PROC-STD-003: Proceso Estándar de Soporte
│   └── PROC-STD-004: Proceso Estándar de Gestión
│
├── 📁 Guías de Tailoring
│   ├── GUIDE-TAIL-001: Cómo Adaptar Procesos
│   ├── GUIDE-TAIL-002: Tailoring para Proyectos Ágiles
│   └── GUIDE-TAIL-003: Tailoring para Proyectos Pequeños
│
├── 📁 Plantillas y Ejemplos
│   ├── 50+ plantillas
│   └── Ejemplos completados
│
├── 📁 Activos de Proceso
│   ├── Lecciones aprendidas
│   ├── Best practices
│   ├── Estimaciones históricas
│   └── Métricas organizacionales
│
└── 📁 Herramientas y Ambiente
    ├── Configuración de herramientas estándar
    └── Ambiente de desarrollo tipo
```

**Proceso Estándar - Ejemplo Simplificado**:

```
PROCESO ESTÁNDAR DE DESARROLLO
═══════════════════════════════

1. INICIACIÓN
   ├─ 1.1 Kick-off del proyecto
   ├─ 1.2 Análisis de viabilidad
   ├─ 1.3 Charter del proyecto [Plantilla]
   └─ 1.4 Identificación de stakeholders

2. PLANIFICACIÓN
   ├─ 2.1 Definir alcance [Plantilla WBS]
   ├─ 2.2 Estimar esfuerzo [Guía de estimación]
   ├─ 2.3 Crear cronograma [Plantilla MS Project]
   ├─ 2.4 Planificar recursos
   ├─ 2.5 Identificar riesgos [Plantilla]
   └─ 2.6 Aprobar plan [Checklist]

3. ANÁLISIS DE REQUERIMIENTOS
   ├─ 3.1 Elicitar requerimientos [Técnicas]
   ├─ 3.2 Documentar requerimientos [Plantilla]
   ├─ 3.3 Analizar y priorizar [Método MoSCoW]
   └─ 3.4 Baseline de requerimientos

4. DISEÑO
   ├─ 4.1 Arquitectura de alto nivel [Plantilla]
   ├─ 4.2 Diseño detallado [Estándares UML]
   ├─ 4.3 Diseño de base de datos [Estándares]
   └─ 4.4 Revisión de diseño [Checklist]

5. IMPLEMENTACIÓN
   ├─ 5.1 Codificación [Estándares de código]
   ├─ 5.2 Code review [Proceso]
   ├─ 5.3 Pruebas unitarias [>80% cobertura]
   └─ 5.4 Integración continua [Pipeline]

6. PRUEBAS
   ├─ 6.1 Pruebas de integración [Plan]
   ├─ 6.2 Pruebas de sistema [Plan]
   ├─ 6.3 Pruebas de aceptación (UAT) [Plan]
   └─ 6.4 Gestión de defectos [Proceso]

7. DESPLIEGUE
   ├─ 7.1 Preparación del ambiente [Checklist]
   ├─ 7.2 Migración de datos [Procedimiento]
   ├─ 7.3 Despliegue [Runbook]
   └─ 7.4 Verificación post-despliegue [Smoke tests]

8. CIERRE
   ├─ 8.1 Documentación final
   ├─ 8.2 Lecciones aprendidas [Plantilla]
   ├─ 8.3 Métricas del proyecto [Dashboard]
   └─ 8.4 Celebración del equipo 🎉

═══════════════════════════════
PUNTOS DE TAILORING:
- Proyectos <3 meses: Simplificar docs
- Proyectos Ágiles: Sprints en lugar de fases
- Proyectos de mantenimiento: Omitir Análisis
```

#### 2. Programa de Capacitación Organizacional (OT)

**Curriculum**:

```
PLAN DE CAPACITACIÓN ORGANIZACIONAL
════════════════════════════════════

ONBOARDING (Todos los nuevos)
├─ Día 1: Inducción a la empresa
├─ Día 2: Procesos estándar (4 hrs)
├─ Día 3: Herramientas (4 hrs)
└─ Semana 2: Mentoring 1-on-1

ROLES ESPECÍFICOS

📊 Project Managers (40 hrs/año)
├─ Gestión de proyectos con procesos estándar (16 hrs)
├─ Análisis de métricas y reporting (8 hrs)
├─ Gestión de riesgos avanzada (8 hrs)
└─ Liderazgo y soft skills (8 hrs)

💻 Desarrolladores (32 hrs/año)
├─ Estándares de código y buenas prácticas (8 hrs)
├─ TDD y testing avanzado (8 hrs)
├─ Revisiones de código efectivas (4 hrs)
├─ Arquitectura y patrones de diseño (8 hrs)
└─ Nueva tecnología [variable] (4 hrs)

🔍 QA Engineers (36 hrs/año)
├─ Procesos de testing (8 hrs)
├─ Automatización de pruebas (12 hrs)
├─ Auditorías PPQA (8 hrs)
└─ Herramientas de testing (8 hrs)

🏗️ Arquitectos (40 hrs/año)
├─ Arquitectura empresarial (16 hrs)
├─ Evaluación de tecnologías (8 hrs)
├─ Revisión de diseño (8 hrs)
└─ Tendencias tecnológicas (8 hrs)

TODOS LOS ROLES
└─ Conferencias/Certificaciones externas: Budget anual disponible
```

**Métodos de Capacitación**:
- 🎓 Cursos formales (presencial/online)
- 🎥 Videos y tutoriales
- 📚 Documentación y guías
- 👥 Mentoring y coaching
- 🔄 Comunidades de práctica
- 🎤 Brown bag sessions (lunch & learn)

#### 3. Mejora Continua Institucionalizada (OPF)

**Ciclo de Mejora**:

```
┌─────────────────────────────────────────────────┐
│ CICLO DE MEJORA ORGANIZACIONAL (Trimestral)    │
└─────────────────────────────────────────────────┘

MES 1: RECOLECCIÓN Y ANÁLISIS
├─ Recolectar métricas de todos los proyectos
├─ Analizar tendencias
├─ Identificar áreas problemáticas
└─ Recolectar feedback de equipos

MES 2: IDENTIFICACIÓN DE MEJORAS
├─ Sesión de brainstorming con SEPG
├─ Priorizar propuestas de mejora
├─ Estimar impacto y esfuerzo
└─ Aprobar 2-3 mejoras (Steering Committee)

MES 3: PILOTO E IMPLEMENTACIÓN
├─ Implementar mejora en proyecto piloto
├─ Evaluar resultados
├─ Ajustar basado en feedback
└─ Desplegar si es exitoso

CONTINUO: MONITOREO
└─ Dashboard de proceso en tiempo real
```

**Canales de Propuesta de Mejoras**:
- **Formal**: Form en intranet "Proponer Mejora"
- **Retrospectivas**: De proyectos y sprints
- **Buzón de sugerencias**: Anónimo
- **Kaizen events**: Sessions trimestrales
- **Auditorías PPQA**: Hallazgos disparan mejoras

---

## 💰 Costos de Implementación

### Presupuesto Típico para Empresa Mediana (50 personas)

#### NIVEL 2 (12 meses)

| Categoría | Detalle | Costo |
|-----------|---------|-------|
| **Personal Interno** | | |
| | Process Manager (FTE) | $90,000 |
| | Process Engineers (2 x 0.5 FTE) | $70,000 |
| | Tiempo de equipo (15% x 50 personas) | $180,000* |
| **Consultoría Externa** | | |
| | Consultor CMMI (0.3 FTE) | $50,000 |
| | Auditoría SCAMPI Clase B (opcional) | $15,000 |
| **Capacitación** | | |
| | Capacitación CMMI para SEPG | $8,000 |
| | Capacitación para equipo | $15,000 |
| **Herramientas** | | |
| | Jira, Confluence, etc. (si no existen) | $10,000 |
| | Herramientas de métricas (Power BI, etc.) | $5,000 |
| **Otros** | | |
| | Viajes y materiales | $5,000 |
| | Contingencia (10%) | $45,000 |
| **TOTAL NIVEL 2** | | **$493,000** |

*Nota: $180k representa costo de oportunidad, no gasto adicional

#### NIVEL 3 (12 meses adicionales)

| Categoría | Costo |
|-----------|-------|
| Personal y consultoría | $180,000 |
| Capacitación organizacional | $40,000 |
| Herramientas adicionales | $10,000 |
| Auditoría SCAMPI A (certificación) | $50,000 |
| Contingencia | $28,000 |
| **TOTAL NIVEL 3** | **$308,000** |

#### TOTAL NIVEL 2 + 3: $801,000 en 24 meses

### ROI Esperado

**Beneficios Cuantitativos** (conservador, a partir de mes 18):

| Beneficio | Ahorro Anual |
|-----------|--------------|
| Reducción de retrabajo (20% → 8%) | $120,000 |
| Menos defectos en producción (40% reducción) | $80,000 |
| Proyectos a tiempo (50% → 80%) | $100,000 |
| Reducción de rotación (30% → 15%) | $75,000 |
| Eficiencia en onboarding | $30,000 |
| **TOTAL BENEFICIOS ANUALES** | **$405,000** |

**ROI**:
- Inversión total 2 años: $801,000
- Beneficio Año 3: $405,000
- **Payback: ~2 años**
- **ROI a 5 años: 150%** ($1.2M beneficio vs $0.8M inversión)

---

## ⚠️ Factores Críticos de Éxito

### Top 10 Factores de Éxito

1. ✅ **Compromiso visible de la Dirección**
   - Participación activa en reuniones
   - Comunicación constante del "por qué"
   - Proveer recursos necesarios

2. ✅ **SEPG competente y dedicado**
   - Personas con credibilidad técnica
   - Tiempo protegido para la iniciativa
   - Habilidades de facilitación y cambio

3. ✅ **Enfoque en valor, no en conformidad**
   - Diseñar procesos útiles, no burocráticos
   - Demostrar beneficios tangibles
   - Medir lo que importa

4. ✅ **Implementación incremental**
   - No hacer todo a la vez
   - Quick wins tempranos
   - Aprender y ajustar

5. ✅ **Comunicación efectiva y constante**
   - Town halls trimestrales
   - Newsletters mensuales
   - Celebrar logros

6. ✅ **Capacitación adecuada**
   - Todos entienden el "por qué"
   - Capacitación práctica, no teórica
   - Soporte post-capacitación

7. ✅ **Procesos pragmáticos y ágiles**
   - Adaptables al contexto
   - Documentación justa y necesaria
   - Compatible con metodologías ágiles

8. ✅ **Herramientas que faciliten, no compliquen**
   - Integración de herramientas
   - Automatización de métricas
   - Fácil acceso a información

9. ✅ **Gestión activa de resistencia**
   - Identificar y trabajar con escépticos
   - Mostrar beneficios con datos
   - Involucrar a influencers

10. ✅ **Medición y demostración de valor**
    - Métricas antes y después
    - Casos de éxito internos
    - ROI documentado

### Top 10 Errores a Evitar

1. ❌ **Implementar "por el libro" sin adaptar**
2. ❌ **Enfocarse solo en la certificación, no en la mejora real**
3. ❌ **Crear procesos burocráticos y pesados**
4. ❌ **No involucrar a los equipos en el diseño**
5. ❌ **Subestimar el esfuerzo de cambio cultural**
6. ❌ **Falta de compromiso de la dirección**
7. ❌ **Implementar todo a la vez**
8. ❌ **No medir ni demostrar beneficios**
9. ❌ **Capacitación insuficiente**
10. ❌ **No gestionar activamente la resistencia**

---

## 📋 Checklist de Implementación

### Antes de Comenzar

- [ ] Apoyo explícito del CEO/CTO
- [ ] Presupuesto aprobado
- [ ] Process Manager identificado y comprometido
- [ ] SEPG formado
- [ ] Objetivos de negocio claros
- [ ] Expectativas realistas de tiempo

### Durante la Implementación

#### Cada Área de Proceso
- [ ] Diseño completado y revisado
- [ ] Piloto ejecutado exitosamente
- [ ] Feedback incorporado
- [ ] Rollout planificado
- [ ] Capacitación impartida
- [ ] Adopción monitoreada
- [ ] Auditoría PPQA pasada

#### Cada Mes
- [ ] Reporte de progreso al Steering Committee
- [ ] Métricas de adopción revisadas
- [ ] Feedback recolectado
- [ ] Ajustes implementados
- [ ] Comunicación a la organización

#### Cada Trimestre
- [ ] Revisión de beneficios realizados
- [ ] Análisis de ROI parcial
- [ ] Ajuste de plan si necesario
- [ ] Celebración de logros

### Antes de Certificación (Si aplica)

- [ ] Todas las áreas del nivel implementadas
- [ ] Procesos ejecutándose por 3+ meses
- [ ] Auditoría interna exitosa
- [ ] Evidencias documentadas
- [ ] Equipo preparado para SCAMPI
- [ ] Pre-evaluación SCAMPI B completada

---

**Siguiente documento**: [05-Aplicacion-CMMI-Proyecto-ISSEG.md](05-Aplicacion-CMMI-Proyecto-ISSEG.md)

**Documento anterior**: [03-Areas-de-Proceso-CMMI.md](03-Areas-de-Proceso-CMMI.md)

**Volver al índice**: [00-INDICE-INVESTIGACION-CMMI.md](00-INDICE-INVESTIGACION-CMMI.md)
