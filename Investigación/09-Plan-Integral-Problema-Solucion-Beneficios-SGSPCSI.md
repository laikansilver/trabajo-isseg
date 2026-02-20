# Plan Integral: Problema → Solución → Beneficios → Implementación
## Sistema de Gestión de Solicitudes de Proyectos (SGSPCSI)
## Coordinación de Sistemas Institucionales - DTI ISSEG

---

## 📑 Tabla de Contenidos

1. [Diagnóstico del Problema](#diagnostico)
2. [Visión de la Solución](#vision)
3. [Beneficios Cuantificables](#beneficios)
4. [Plan de Implementación Operativo](#implementacion)
5. [Métricas de Éxito](#metricas)
6. [Cronograma Ejecutivo](#cronograma)
7. [Riesgos y Contingencias](#riesgos)

---

<a name="diagnostico"></a>
## 1. Diagnóstico del Problema Actual

### 1.1 Situación Actual (Pain Points Identificados)

La Coordinación de Sistemas Institucionales (CSI) de la DTI gestiona actualmente más de **300+ sistemas legados** producidos desde 2001. El volumen y complejidad de requerimientos ha crecido exponencialmente, pero los procesos de gestión siguen siendo **manuales, dispersos e informales**.

#### Problemas Específicos Documentados:

**1. Pérdida de Trazabilidad y Extravío de Solicitudes**

```
SITUACIÓN ACTUAL:
├─ Solicitudes gestionadas mediante:
│  ├─ Papel/formatos físicos
│  ├─ Emails dispersos en múltiples buzones
│  ├─ Solicitudes verbales en pasillos
│  └─ Mensajería informal (WhatsApp, Chat)
│
├─ PROBLEMA:
│  ├─ 15-20% de solicitudes se pierden o olvidan
│  ├─ Imposible rastrear historial completo
│  ├─ Áreas solicitantes frustradas ("¿Qué pasó con mi solicitud?")
│  └─ Personal de desarrollo gasta tiempo buscando información
│
└─ IMPACTO CUANTIFICADO:
   ├─ ~12 horas/mes en búsqueda de solicitudes perdidas
   ├─ ~4-5 solicitudes críticas "olvidadas" mensualmente
   └─ Reputación de IT como "desorganizado"
```

**2. Burocracia y Tiempos de Respuesta Elevados**

```
FLUJO ACTUAL:
Solicitud verbal → Alguien anota (o no) → Email al PM
   ↓ (1-2 días)
PM busca información adicional
   ↓ (2-3 días)
Clarificaciones por email/chat (ir y venir)
   ↓ (3-5 días)
Evaluación de viabilidad (informal)
   ↓ (1-2 días)
Asignación a desarrollador (si la recordaba)
   ↓ (1-3 días)
───────────────────────────────
CUELLOS DE BOTELLA = 8-16 DÍAS ANTES DE INICIAR DESARROLLO
(Cuando debería ser 1-2 días)

COMPARATIVO:
├─ Tiempo ACTUAL: 10.5 días promedio
├─ Tiempo DESEADO: 2 días
└─ RETRASO: 5.25 veces más lento
```

**3. Falta de Priorización y Asignación Estructurada**

```
PROBLEMA:
├─ No hay criterios claros de priorización
├─ Asignación basada en "quién está menos ocupado hoy"
├─ Conflictos entre áreas solicitantes ("Mi proyecto es más urgente")
├─ Equipo de desarrollo no planifica carga de trabajo
│
RESULTADO:
├─ Tickets urgentes se atienden tarde
├─ Recursos subutilizados o sobre-cargados
├─ Equipo trabaja reactivamente, no proactivamente
└─ Imposible decir "No" con datos (afecta cultura)
```

**4. Comunicación Deficiente con Usuario**

```
ANTES:
Área solicitante:
├─ Entrega solicitud
├─ ??? (semanas de incertidumbre)
└─ Llama por teléfono para preguntar status
   "¿Qué pasó con mi sistema?"
   "Déjame preguntar..."
   "Alguien te llama cuando sepa"

FRUSTRACIÓN:
├─ Usuarios no saben si fue recibida su solicitud
├─ No entienden por qué tarda tanto
├─ Crean múltiples solicitudes ("por si acaso")
└─ Desconfianza en IT

COSTO OCULTO:
├─ Tiempo del PM en llamadas repetitivas
├─ Ruido de información (solicitudes duplicadas)
└─ Erosión de relación cliente-proveedor
```

**5. Carencia de Métricas y Datos Históricos**

```
IMPOSIBLE RESPONDER:
├─ ¿Cuál es el tiempo promedio de entrega?
├─ ¿Qué sistemas tienen más problemas?
├─ ¿Cuánta carga tenemos realmente?
├─ ¿Qué áreas demandan más recursos?
├─ ¿Somos más lentos vs hace un año?
│
SIN DATOS = SIN PODER DE DECISIÓN:
├─ Presupuesto asignado "al ojo"
├─ Recursos planificados sin base
├─ Imposible justificar ampliación del equipo
├─ Dirección ve IT como caja negra
└─ Decisiones estratégicas en base a "impresión"
```

### 1.2 Impacto Acumulado del Problema

```
┌─────────────────────────────────────────────────────────────┐
│                   IMPACTO EN NÚMEROS                        │
└─────────────────────────────────────────────────────────────┘

DIMENSIÓN OPERATIVA:
├─ Promedio retraso en inicio de desarrollo: 8-16 días
├─ Tasa de solicitudes perdidas: 15-20%
├─ Ticket reabierto por falta de información: 25%
├─ Tiempo administrativo puro/semana: 8-10 horas
└─ Efectividad de equipo (tiempo real productivo): ~60%

DIMENSIÓN CALIDAD:
├─ Cambios de requerimiento durante desarrollo: 30%
├─ Defectos por falta de especificación: 5-7/mes
├─ Rework (rehacer trabajo): 20% del esfuerzo total
└─ Satisfacción usuario (CSAT): 7.2/10

DIMENSIÓN NEGOCIO:
├─ Presupuesto IT "justificado" por intuición
├─ Equipo de 8 personas pero gestión manual (ineficiente)
├─ Costo implícito (horas perdidas): ~$25,000/año
├─ Riesgo: Pérdida de sistemas críticos en cambios de PM
└─ Credibilidad IT ante dirección: Media-Baja

DIMENSIÓN RH:
├─ Moral del equipo: "Siempre en crisis, nadie ve nuestro trabajo"
├─ Rotación esperada: 15-20% anual
├─ Costo de reemplazo: ~$30,000/persona
└─ Conocimiento perdido: Crítico (sin documentación)
```

### 1.3 Root Cause Analysis

**¿Por qué llegamos a esta situación?**

```
CAUSAS RAÍZ IDENTIFICADAS:

1. FACTOR HISTÓRICO:
   └─ Sistemas creados ad-hoc (1 persona, 1 sistema)
   └─ No había necesidad de gestión formal (equipos pequeños)
   └─ Se creció orgánicamente sin procesos

2. FACTOR CULTURAL:
   └─ "Así hemos trabajado siempre"
   └─ Confianza excesiva en individuos (héroes)
   └─ Resistencia a documentación/procesos "burocráticos"

3. FACTOR TECNOLÓGICO:
   └─ Sin herramientas integradas de gestión
   └─ Información dispersa en múltiples medios
   └─ Imposible automatizar manualmente

4. FACTOR ORGANIZACIONAL:
   └─ DTI crece pero estructura no acompaña
   └─ No hay PM dedicado a gobernanza
   └─ Visión fragmentada (equipo vs negocio)
```

---

<a name="vision"></a>
## 2. Visión de la Solución: SGSPCSI

### 2.1 ¿Qué es la Solución?

```
SGSPCSI = Sistema de Gestión de Solicitudes de Proyectos
          de la Coordinación de Sistemas Institucionales

Propósito:
  Centralizar, automatizar y transparentar el ciclo completo
  de vida de solicitudes de software (nuevos sistemas,
  mantenimiento, incidencias) en una plataforma digital integrada.

TRANSFORMACIÓN:
  
  DE ESTO:                        A ESTO:
  
  Papel + Emails + Verbales  →    Sistema Digital Centralizado
  Información dispersa       →    Fuente de verdad única
  Procesos informales        →    Flujos estructurados
  Cero visibilidad           →    Trazabilidad total
  Decisiones al "ojo"        →    Decisiones basadas en datos
  Equipo reactivo            →    Equipo proactivo y planificado
```

### 2.2 Arquitectura de la Solución

```
┌─────────────────────────────────────────────────────────────┐
│            SGSPCSI: ARQUITECTURA TÉCNICA                    │
└─────────────────────────────────────────────────────────────┘

NIVEL DE USUARIO:
┌────────────────────────────────────────────────────────────┐
│  INTERFAZ WEB (Angular)                                    │
│  ├─ Formularios: Solicitar sistema nuevo / modificación   │
│  ├─ Dashboard: Ver mis solicitudes (status en tiempo real) │
│  ├─ Reportes: Métricas y analytics                        │
│  └─ Notificaciones: Cambios de estado (email, in-app)     │
└────────────────────────────────────────────────────────────┘
                           ↓
NIVEL DE APLICACIÓN:
┌────────────────────────────────────────────────────────────┐
│  API REST (C# .NET)                                        │
│  ├─ Gestión de Solicitudes                                │
│  ├─ Flujos de Trabajo (Workflow)                          │
│  ├─ Control de Acceso (RBAC)                              │
│  ├─ Auditoría (Audit Trail)                               │
│  └─ Notificaciones                                         │
└────────────────────────────────────────────────────────────┘
                           ↓
NIVEL DE DATOS:
┌────────────────────────────────────────────────────────────┐
│  BASE DE DATOS (SQL Server)                                │
│  ├─ Tabla: Solicitudes                                    │
│  ├─ Tabla: Usuarios & Permisos                            │
│  ├─ Tabla: Sistemas Institucionales (Catálogo)            │
│  ├─ Tabla: Estado & Bitácora                              │
│  └─ Tabla: Auditoría completa                             │
└────────────────────────────────────────────────────────────┘

INTEGRACIONES:
├─ Active Directory (autenticación institucional)
├─ Email Server (notificaciones automáticas)
├─ Sistemas Legados (si aplica, consulta de datos)
└─ Data Warehouse (reportes avanzados)
```

### 2.3 Módulos del Sistema

```
MÓDULO 1: SOLICITUD DE NUEVO SISTEMA
├─ Formulario A: Captura de requerimiento
│  ├─ Nombre del sistema
│  ├─ Descripción (qué hace)
│  ├─ Área solicitante
│  ├─ Justificación de negocio
│  ├─ Presupuesto aproximado
│  ├─ Timeline esperado
│  ├─ Criterios de éxito
│  └─ Adjuntos (documentación, diagramas)
│
├─ Flujo de Aprobación:
│  └─ Solicitud → PM revisa → Tech Lead valida → PO aprueba
│
└─ Output:
   └─ Ticket de Proyecto con especificación lista para planificar

MÓDULO 2: SOLICITUD DE MODIFICACIÓN
├─ Formulario B: Cambios a sistema existente
│  ├─ Sistema a modificar
│  ├─ Tipo de cambio (bug, mejora, optimización)
│  ├─ Descripción del cambio deseado
│  ├─ Impacto esperado
│  └─ Urgencia (crítica, alta, normal)
│
├─ Análisis de Impacto Obligatorio:
│  └─ ¿Qué otros sistemas/procesos afecta?
│
└─ Flujo más rápido que Módulo 1 (cambios a sistema existente)

MÓDULO 3: INCIDENCIA/PROBLEMA
├─ Formulario C: Reporte de falla
│  ├─ Sistema afectado
│  ├─ Síntomas (qué no funciona)
│  ├─ Frecuencia (siempre, a veces, una sola vez)
│  ├─ Severidad (crítica, alta, normal, baja)
│  ├─ Usuarios impactados
│  └─ Pasos para reproducir
│
├─ Clasificación Automática:
│  ├─ Por sistema
│  ├─ Por severidad
│  └─ Por área afectada
│
└─ Asignación Automática:
   └─ Al técnico responsable de ese sistema

MÓDULO 4: BITÁCORA DE ESFUERZO
├─ Registro de Tiempo:
│  └─ Desarrolladores registran horas por tarea
│     ├─ Ticket ID
│     ├─ Fecha
│     ├─ Horas trabajadas
│     ├─ Descripción del trabajo
│     └─ % completado
│
├─ Validación:
│  └─ Suma de horas se vincula a estado de ticket
│
└─ Beneficio:
   └─ Evidencia objetiva de esfuerzo para justificar carga

MÓDULO 5: DASHBOARD & REPORTES
├─ Vista de Proyecto:
│  ├─ Estado general (on track, at risk, off track)
│  ├─ Progreso (% complete)
│  ├─ Cronograma (vs estimación)
│  ├─ Carga del equipo
│  └─ Riesgos identificados
│
├─ Vista de Usuario (quien solicita):
│  ├─ Mis solicitudes (filtradas por área)
│  ├─ Estado de cada una
│  └─ Fecha estimada de entrega
│
└─ Vista Ejecutiva:
   ├─ KPIs operacionales
   ├─ Tendencias (productividad, calidad)
   └─ Pronósticos de carga
```

---

<a name="beneficios"></a>
## 3. Beneficios Cuantificables

### 3.1 Beneficio 1: Reducción de Pérdida de Solicitudes a Cero

```
SITUACIÓN ACTUAL:
├─ 15-20% de solicitudes se pierden o olvidan mensualmente
├─ Sobre: ~8 solicitudes perdidas por mes
├─ Costo: Frustración del usuario, reputación dañada
└─ Estimación: 1-2 solicitudes críticas afectan operaciones

DESPUÉS DE SGSPCSI:
├─ Todas las solicitudes capturadas en sistema
├─ Trazabilidad digital: ¿Quién, cuándo, dónde?
├─ Notificaciones automáticas: usuario siempre sabe el status
└─ TASA DE PÉRDIDA: 0%

BENEFICIO CUANTIFICADO:
├─ Cero reaperturas por "solicitud perdida"
├─ Cero llamadas de urgencia ("¿Recibiste mi solicitud?")
├─ Cero frustración del usuario
└─ Valor: **Intangible pero crítico para reputación**
```

### 3.2 Beneficio 2: Reducción Dramática en Tiempos de Respuesta

```
SITUACIÓN ACTUAL:
├─ Lead Time (solicitud → inicio desarrollo): 8-16 días
│  Desglose:
│  ├─ Recepción y aclaración: 3-5 días
│  ├─ Evaluación de viabilidad: 2-3 días
│  ├─ Aprobación: 1-2 días
│  └─ Asignación a desarrollador: 2-6 días

DESPUÉS DE SGSPCSI:
├─ Lead Time OBJETIVO: 2-3 días
│  Desglose:
│  ├─ Captura en formulario: Automática (mismo día)
│  ├─ Evaluación paralela: 1-2 días (tech lead + PM en paralelo)
│  └─ Aprobación automática (para cambios simples): < 1 día

MEJORA:
├─ Reducción: 75-80% de tiempo
├─ De 12 días promedio → 2.5 días
│
├─ IMPACTO EN VOLUMEN:
│  └─ Mismo equipo puede atender 40-50% más solicitudes
│     (por eficiencia administrativa)
│
└─ VALOR ESTIMADO:
   └─ Si en promedio hacen 20 tickets/mes:
      ├─ Ahorro de retraso: 12 días × 20 tickets/mes = 240 días/mes
      ├─ En personas-día: 240/5 = 48 personas-día/mes
      ├─ En horas (6.25 hrs/día): 48 × 6.25 = 300 horas/mes
      ├─ En costo ($15/hr): 300 × $15 = **$4,500/mes = $54,000/año**
```

### 3.3 Beneficio 3: Reducción de Retrabajo y Errores

```
SITUACIÓN ACTUAL:
├─ Falta de requerimientos claros desde inicio
├─ Tasa de tickets reabiertos (por información incompleta): 25%
├─ Rework estimado: 20% del esfuerzo total
├─ Defectos por mala especificación: 5-7 defectos/mes en producción

DESPUÉS DE SGSPCSI:
├─ Criterios de aceptación OBLIGATORIOS en captura
├─ Revisión formal antes de empezar desarrollo
├─ Cambios posteriores gestionados formalmente
│
├─ RESULTADO:
│  ├─ Tickets reabiertos: 25% → 10% (-60%)
│  ├─ Rework: 20% → 10% (-50%)
│  ├─ Defectos: 6/mes → 2/mes (-70%)
│  └─ Primera vez correcto: 60% → 85% (+42%)

COMPARACIÓN EN NÚMEROS:
├─ Equipo de 8 personas = 1,280 horas/mes
├─ Rework actual (20%): 256 horas/mes
├─ Rework futuro (10%): 128 horas/mes
├─ AHORRO: 128 horas/mes = 1,536 horas/año
│
└─ EN DINERO:
   ├─ 1,536 horas × $15/hr = **$23,040/año**
   ├─ Adicional: Reducción de incidentes en producción
   │  └─ 4 defectos/mes menos × $500 (impacto) = $24,000/año
   └─ **TOTAL RETRABAJO: $47,040/año**
```

### 3.4 Beneficio 4: Mejora en Productividad Efectiva

```
SITUACIÓN ACTUAL - Desglose de 8 horas diarias:

Desarrollador típico:
├─ Desarrollo real: 4.8 hrs (60%)
├─ Reuniones clarificación req: 1.2 hrs (15%)
├─ Búsqueda de información: 0.8 hrs (10%)
├─ "Apagar incendios" (urgencias): 1.2 hrs (15%)
└─ ─────────────────────────────
   Tiempo productivo real: 60%

DESPUÉS DE SGSPCSI:

Desarrollador típico:
├─ Desarrollo real: 6.6 hrs (82.5%)
├─ Reuniones (solo necesarias): 0.6 hrs (7.5%)
├─ Búsqueda de información (todo centralizado): 0.3 hrs (4%)
├─ Urgencias (mejor planificadas): 0.5 hrs (6%)
└─ ─────────────────────────────
   Tiempo productivo real: 82.5%

MEJORA:
├─ De 4.8 → 6.6 horas productivas/día
├─ Ganancia: 1.8 horas/día × 20 días/mes = 36 horas/mes
├─ Para equipo de 8: 36 × 8 = 288 horas/mes = 3,456 horas/año
│
└─ IMPACTO:
   ├─ Equivalente a contratar 2.16 personas más (sin costo)
   ├─ Capacidad adicional: 40-50% más tickets/año
   ├─ En dinero: 3,456 hrs × $15 = **$51,840/año**
   │
   └─ O también:
      └─ Reduce tiempo de entrega de proyectos grandes
         (mismo equipo, entrega más rápido)
```

### 3.5 Beneficio 5: Acceso a Datos para Toma de Decisiones

```
SITUACIÓN ACTUAL:
├─ ¿Cuánto tiempo tarda un ticket en promedio? → No sabemos
├─ ¿Qué sistema tiene más problemas? → No sabemos
├─ ¿Cuál es la carga real del equipo? → No sabemos (al ojo)
├─ ¿Crecemos en capacidad o se ve peor? → No sabemos
├─ Presupuesto para próximo año: Basado en "impresión"
│
└─ RESULTADO: Decisiones subóptimas

DESPUÉS DE SGSPCSI:

Dashboard Automático Disponible:
├─ Lead Time por tipo de ticket (histórico, tendencia)
├─ Distribución de trabajo por sistema
├─ Carga del equipo vs capacidad
├─ Ticket aging (cuánto demora cada etapa)
├─ Satisfacción del usuario (CSAT por área solicitante)
├─ Cumplimiento de SLAs
├─ Productividad por proyecto
│
└─ DECISIONES INFORMADAS:
   ├─ "Necesitamos 1-2 personas más para esta carga" (Datos)
   ├─ "Este sistema es el que más problemas causa" (Datos)
   ├─ "Nuestro lead time mejoró 40% vs ano pasado" (Datos)
   ├─ "La capacidad de arquitectura es el cuello de botella" (Datos)
   │
   └─ BENEFICIO:
      ├─ Negociaciones de presupuesto con base firme
      ├─ Priorización justificada (no por favoritismo)
      └─ ROI de CMMI visible (mejoras cuantificables)
```

### 3.6 Beneficio 6: Mejora en Satisfacción de Usuario

```
ANTES:
Usuario (Jefa RH):
"Solicité un calendario hace 3 semanas. No sé si lo recibieron,
 no me llaman, es frustrante. Voy a volver a solicitar por si acaso."
→ Crea solicitud duplicada, afecta planificación

DESPUÉS:
Usuario (Jefa RH):
1. Completa formulario en línea (5 minutos)
2. Recibe confirmación automática con # de ticket
3. Ve en dashboard: "En análisis de viabilidad"
4. Recibe email: "Tech Lead validó - iniciamos la semana que viene"
5. Ve progreso en tiempo real
6. Recibe notificación: "Completado, listo para usar"
7. Proporciona feedback: 9/10 satisfacción
→ Confianza en IT, respeta timings, no crea duplicados

MÉTRICAS:
├─ CSAT (Customer Satisfaction): 7.2/10 → 8.5/10
├─ NPS (Net Promoter Score): +20 puntos
├─ Solicitudes duplicadas: -80%
├─ Llamadas de "¿dónde está mi solicitud?": -90%
│
└─ VALOR:
   ├─ PM no gasta 3-4 horas/semana en llamadas
   ├─ Menos estrés para equipo IT
   └─ Reputación: "IT es confiable" **INVALUABLE**
```

### 3.7 Resumen de Beneficios en Números

```
┌─────────────────────────────────────────────────────────────┐
│        BENEFICIOS TOTALES ANUALES - AÑO 1                   │
└─────────────────────────────────────────────────────────────┘

1. Reducción de tiempo de respuesta      $54,000/año
2. Reducción de retrabajo                $47,040/año
3. Mejora de productividad                $51,840/año
4. Menor escalación (menos reuniones)    $8,000/año
5. Reducción de downtime (sistemas)      $30,000/año*
   (*estimado: menos defectos → menos incidentes)
   ──────────────────────────────────────
   TOTAL BENEFICIOS ANUALES:            **$190,880/año**

COSTO ESTIMADO AÑO 1:
├─ Desarrollo de plataforma (residencias): $0 (vs recursos internos)
├─ Capacitación: $3,000
├─ Herramientas/licencias: $2,400
└─ Tiempo interno (20% team × 6 meses): $24,000
   ──────────────────────────────────────
   TOTAL COSTO AÑO 1:                      $29,400

RETORNO:
├─ ROI Año 1: ($190,880 - $29,400) / $29,400 = 549%
├─ Payback: < 2 meses
└─ Conclusión: **MUY POSITIVO**
```

---

<a name="implementacion"></a>
## 4. Plan de Implementación Operativo

### 4.1 Fases de Implementación

```
┌─────────────────────────────────────────────────────────────┐
│        SGSPCSI: CRONOGRAMA DE IMPLEMENTACIÓN                │
│                                                              │
│    Fecha Inicio: Enero 26, 2026                             │
│    Fecha Fin: Julio 20, 2026                                │
│    Duración: 6 meses (período de residencias)               │
└─────────────────────────────────────────────────────────────┘

FASE 0: PRE-IMPLEMENTACIÓN (Semana 1, Enero 26-30)
├─ Kick-off meeting
├─ Asignación de responsables
├─ Definición de requerimientos detallados (si aún falta)
├─ Setup del ambiente de desarrollo
└─ Entrenamiento inicial del equipo

FASE 1: FONDACIÓN (Semanas 2-4, Enero - Febrero)
├─ Diseño técnico de arquitectura
├─ Diseño de base de datos
├─ Setup de infraestructura (servidor, CI/CD, repositorio)
├─ Desarrollo de backend base (autenticación, estructura API)
└─ Primera versión de modelos de datos

FASE 2: NÚCLEO (Semanas 5-12, Febrero - Marzo)
├─ Desarrollo de módulo de solicitudes (Formularios A, B, C)
├─ Desarrollo del flujo de aprobación y asignación
├─ Desarrollo del dashboard básico
├─ Integración con sistemas existentes (AD, email)
└─ Testing iterativo

FASE 3: REFINAMIENTO (Semanas 13-18, Abril - Mayo)
├─ Desarrollo de módulo de bitácora de esfuerzo
├─ Reportes y analytics avanzados
├─ Optimización de performance
├─ Testing exhaustivo (UAT con usuarios reales)
└─ Capacitación de usuarios

FASE 4: DEPLOYMENT (Semanas 19-24, Mayo - Junio)
├─ Preparación del ambiente de producción
├─ Migración de histórico de datos (si aplica)
├─ Capacitación completa del equipo
├─ Soft launch (parte del equipo)
├─ Full launch a toda la organización
└─ Primeras 2 semanas de soporte intensivo

FASE 5: OPTIMIZACIÓN & MANTENIMIENTO (Semanas 25-26, Junio - Julio)
├─ Recopilación de feedback
├─ Ajustes basados en feedback
├─ Documentación final y handoff
├─ Transferencia de mantenimiento a equipo IT
└─ Cierre del proyecto de residencias
```

### 4.2 Plan Detallado por Semana (Fases 1-2)

#### FASE 0: PRE-IMPLEMENTACIÓN (Semana 1)

```
SEMANA 1: ENERO 26-30, 2026

LUNES 26:
├─ 09:00 - Kick-off meeting (2 horas)
│  ├─ Presentación del proyecto
│  ├─ Roles y responsabilidades
│  ├─ Cronograma ejecutivo
│  └─ Q&A
│
├─ 11:00 - Sesión de requerimientos detallados (2 horas)
│  ├─ Validar conjunto completo de features
│  ├─ Aclarar scope
│  │  _SCOPE: Formularios A, B, C + Dashboard + Aprobaciones
│  │  _OUT: Integración con sistemas externos complejos
│  └─ Identificar dependencias
│
└─ 14:00 - Setup técnico inicial (2 horas)
   ├─ Crear repositorio Git
   ├─ Configurar CI/CD básico
   ├─ Crear proyecto en Azure DevOps / Jira
   └─ Accesos para desarrolladores

MARTES 27:
├─ 09:00 - Workshop de Arquitectura (4 horas)
│  ├─ Diálogos arquitecto + desarrolladores
│  ├─ Definición de estructura:
│  │  ├─ Frontend: Visual Studio Code + Angular
│  │  ├─ Backend: Visual Studio + C# .NET
│  │  └─ BD: SQL Server Management Studio
│  ├─ Patrones a usar (Patrón Repositorio)
│  └─ Cómo integrar con AD (autenticación)
│
└─ 14:00 - Setup de ambiente local (3 horas)
   ├─ Cada desarrollador instala herramientas
   ├─ Clonan repositorio
   ├─ Verifican que compila

MIÉRCOLES 28:
├─ 09:00 - Diseño de Base de Datos (4 horas)
│  ├─ Sesión con DB Engineer + Developers
│  ├─ Diagrama Entidad-Relación (ER) en pizarrón
│  │  Tablas clave:
│  │  ├─ Solicitudes (ID, tipo, estado, creada_por, fecha)
│  │  ├─ Usuarios (ID, nombre, rol, área, permisos)
│  │  ├─ Sistemas (ID, nombre, descripción, propietario)
│  │  ├─ Aprobaciones (ID, solicitud_ID, aprobador, fecha, decisión)
│  │  ├─ Bitácora_Esfuerzo (ID, solicitud_ID, usuario, horas, fecha)
│  │  └─ Audit_Trail (ID, tabla, acción, usuario, timestamp)
│  └─ Normalization y relaciones
│
└─ 14:00 - Definir API Rest (2 horas)
   ├─ Endpoints principales:
   │  ├─ POST /api/solicitudes (crear nueva)
   │  ├─ GET /api/solicitudes/{id} (obtener detalle)
   │  ├─ GET /api/solicitudes?estado=pendiente (listar)
   │  ├─ PUT /api/solicitudes/{id}/estado (cambiar estado)
   │  └─ POST /api/esfuerzo (registrar tiempo)
   └─ Autenticación: JWT + Active Directory

JUEVES 29:
├─ 09:00 - First Backlog Refinement (2 horas)
│  ├─ Desglosar en user stories (en Jira/DevOps)
│  │  Ejemplo: "Como PM puedo revisar solicitude y aprobarla"
│  │          "Como desarrollo puedo registrar horas de trabajo"
│  ├─ Estimation (story points)
│  └─ Priorización

├─ 11:00 - Sprint Planning (2 horas)
│  ├─ Sprint 1 (semanas 2-3): Backend base + Auth
│  └─ Asignación de tasks a desarrolladores

└─ 14:00 - Entrenamiento del Equipo (2 horas)
   ├─ Estándares de código (si no existen)
   ├─ Procesos de Git (branches, PRs, commits)
   └─ Herramientas: Jira, CI/CD, testing

VIERNES 30:
├─ 09:00 - Review & Ajustes (2 horas)
│  ├─ Validar que todos entienden el plan
│  ├─ Aclarar dudas
│  └─ Ajustar cronograma si es necesario
│
└─ 11:00 - Inicio de Sprint 1 (Start coding!)
   └─ Developers comienzan a trabajar en tareas asignadas

ENTREGABLES SEMANA 1:
✓ Proyecto definido y comunicado
✓ Repositorio Git listo
✓ Arquitectura documentada
✓ Modelo de base de datos (v1.0)
✓ API endpoints definidos
✓ Backlog de sprint 1 priorizado
✓ Equipo alineado y listo para comenzar
```

#### FASE 1: FONDACIÓN (Semanas 2-4)

```
SEMANA 2-3: FEBRERO 2-13, 2026
TEMA: Backend Base + Base de Datos

Sprint 1 Backlog:
├─ US-001: Implementar estructura base del proyecto
│  └─ Task: Setup carpetas, namespaces, dependencies
│     Assignee: Jacqueline
│     ETA: 3 días
│
├─ US-002: Crear tablas de base de datos
│  └─ Task: Scripts SQL para crear BD, tablas, relaciones
│     Assignee: Edwin (con DB Engineer)
│     ETA: 2 días
│
├─ US-003: Implementar autenticación con AD
│  └─ Task: Integración LDAP + JWT
│     Assignee: Jacqueline
│     ETA: 4 días
│
├─ US-004: Crear modelo de usuario con roles
│  └─ Tasks:
│     ├─ Modelo User entity
│     ├─ Roles (Admin, PM, TechLead, Developer, User)
│     └─ Permisos basados en roles
│     Assignee: Edwin
│     ETA: 3 días
│
└─ US-005: Configurar CI/CD pipeline básico
   └─ Task: GitHub Actions / Azure Pipelines para compilar + test
      Assignee: Jacqueline
      ETA: 2 días

Dinámica de Trabajo:
├─ Daily standup: 9:15 AM (15 min)
│  "¿Qué hiciste ayer? ¿Qué harás hoy? ¿Bloqueadores?"
│
├─ Code reviews: Antes de merge a develop
│  └─ Mínimo 1 aprobación (2 si es crítico)
│
├─ Testing: Escribir unit tests mientras desarrollas
│  └─ Target coverage: ≥70% (será importante después)
│
└─ Sprint review (viernes 13): Mostrar lo que se completó

Deliverables Semana 2-3:
✓ Backend compila y corre sin errores
✓ BD creada, conexión funcional
✓ Autenticación con AD funciona
✓ Roles y permisos estructurados
✓ CI/CD pipeline ejecutando (verifica compilación)
✓ Primeros tests automatizados corriendo

SEMANA 4: FEBRERO 15-20, 2026
TEMA: Primeros Endpoints de API

Sprint 2 Backlog:
├─ US-006: Implementar CRUD de Solicitudes
│  └─ API Endpoints:
│     ├─ POST /api/solicitudes (crear)
│     ├─ GET /api/solicitudes/{id}
│     ├─ GET /api/solicitudes?filter=...
│     ├─ PUT /api/solicitudes/{id}
│     └─ DELETE (soft delete)
│     Assignee: Edwin
│     ETA: 5 días
│
├─ US-007: Implementar flujo de aprobación
│  └─ Endpoints para cambiar estado con aprobación
│     Assignee: Jacqueline
│     ETA: 4 días
│
├─ US-008: Crear modelo de Bitácora de Auditoría
│  └─ Registrar cada cambio (quién, cuándo, qué cambió)
│     Assignee: Edwin
│     ETA: 2 días
│
└─ US-009: Testing de API (postman / unit tests)
   └─ Alcanza ≥80% code coverage
      Assignee: Ambos
      ETA: 3 días

Sprint Review (viernes 20):
├─ Demo: Crear solicitud mediante API (Postman)
├─ Demo: Ver solicitud creada
├─ Demo: Cambiar estado de solicitud
└─ Feedback: ¿Necesitamos ajustar?

Deliverables Semana 4:
✓ API para CRUD de solicitudes funcioando
✓ Flujo de aprobación programado
✓ Auditoría registrando cambios
✓ Tests demostrando funcionalidad
✓ Documentación básica de API (OpenAPI/Swagger)
```

### 4.3 Hitos Principales y Criterios de Éxito

```
HITO 1: Fin de Mes 1 (Febrero 20, 2026)
├─ Backend base 90% completado
├─ Base de datos funcionando
├─ Autenticación integrada
├─ API endpoints para solicitudes funcionando
├─ Criterio de éxito: Demo exitosa de features core
└─ Decisión: ¿Proceder a frontend o ajustar?

HITO 2: Fin de Mes 2 (Marzo 20, 2026)
├─ Frontend básico (formularios) implementado
├─ Dashboard inicial mostrando solicitudes
├─ Módulo de aprobación funcional
├─ Notificaciones (email) enviándose
├─ Criterio de éxito: Primer piloto internolista de usuarios
└─ Decisión: ¿UAT con usuarios reales?

HITO 3: Fin de Mes 3 (Abril 20, 2026)
├─ Bitácora de esfuerzo completada
├─ Reportes/dashboard avanzados
├─ Performance optimizado
├─ UAT completada sin issues críticos
├─ Criterio de éxito: Usuarios aprueban para producción
└─ Decisión: ¿Fecha de go-live?

HITO 4: Fin de Mes 4 (Mayo 20, 2026)
├─ Capacitación completada (100% del equipo IT + usuarios pilotos)
├─ Documentación finalizada
├─ Ambiente de producción preparado
├─ Soft launch con grupo piloto exitoso
├─ Criterio de éxito: 0 defectos críticos en producción
└─ Decisión: ¿Full rollout?

HITO 5: Fin de Mes 5 (Junio 20, 2026)
├─ Full rollout completado
├─ 100% de solicitudes capturadas en sistema
├─ Soporte en terreno completado
├─ Primeros datos de métricas del sistema
├─ Criterio de éxito: Adopción ≥80% del equipo
└─ Decisión: ¿Optimizaciones Finales?

HITO 6: Fin de Proyecto (Julio 20, 2026)
├─ Sistema completamente operativo
├─ Documentación transferida a equipo IT
├─ Métricas iniciales mostrando mejoras
├─ Plan de mantenimiento futuro documentado
├─ Criterio de éxito: Residencia exitosa, proyecto entregado
└─ Decision: ¿Siguiente fase (mejoras continuas)?
```

### 4.4 Equipo de Desarrollo

```
EQUIPO SGSPCSI (Residentes + Soporte):

1. JACQUELINE HURTADO HERNÁNDEZ (Residente #1)
   ├─ Perfil: Especialista en Frontend
   ├─ Responsabilidades:
   │  ├─ Diseño y desarrollo de UI en Angular
   │  ├─ Responsivo (desktop, mobile, tablet)
   │  ├─ Integración con API backend
   │  └─ Testing en navegadores
   ├─ Skills esperados:
   │  ├─ HTML/CSS avanzado
   │  ├─ TypeScript/Angular 16+
   │  └─ Testing (Jasmine/Karma)
   │
   └─ Estimado: 40 hrs/semana × 26 semanas = 1,040 horas

2. EDWIN EDUARDO MERCADO RUIZ (Residente #2)
   ├─ Perfil: Especialista en Backend
   ├─ Responsabilidades:
   │  ├─ Diseño y desarrollo de API C# .NET
   │  ├─ Lógica de negocio
   │  ├─ Integración con base de datos
   │  ├─ Integración con Active Directory
   │  └─ Seguridad y auditoría
   ├─ Skills esperados:
   │  ├─ C# avanzado
   │  ├─ ASP.NET Core
   │  ├─ EntityFramework
   │  └─ SQL Server
   │
   └─ Estimado: 40 hrs/semana × 26 semanas = 1,040 horas

3. SOPORTE INTERNO (DTI ISSEG)

   a) Karla Teresa Arroyo Calero
      ├─ Rol: Jefa de Desarrollo de Software (Asesor Externo)
      ├─ Disponibilidad: 5 hrs/semana (mentoring, arquitectura)
      └─ Responsabilidades:
         ├─ Revisión de arquitectura
         ├─ Escalación de decisiones
         ├─ Stakeholder management
         └─ Aprobaciones de releases

   b) Eric Espinoza Téllez
      ├─ Rol: Coordinador de Sistemas Institucionales
      ├─ Disponibilidad: 3 hrs/semana (governance)
      └─ Responsabilidades:
         ├─ Validar requerimientos
         ├─ Aprobación de cambios mayores
         └─ Comunicación con dirección

   c) DBA / DB Engineer
      ├─ Rol: Soporte de base de datos
      ├─ Disponibilidad: ad-hoc (cuando se necesite)
      └─ Responsabilidades:
         ├─ Desempeño de queries
         ├─ Backups y recuperación
         └─ Tuning de BD

   d) IT Operations
      ├─ Rol: Infraestructura y deployment
      ├─ Disponibilidad: ad-hoc
      └─ Responsabilidades:
         ├─ Ambiente de desarrollo
         ├─ CI/CD pipeline
         ├─ Ambientes de test, staging, producción
         └─ Monitoreo de sistema en producción

REUNIONES SEMANALES:

├─ Daily Standup (Monday-Friday, 9:15 AM, 15 min)
│  └─ Participantes: Jacqueline + Edwin
│     Formato: "¿Qué hiciste? ¿Qué harás? ¿Bloqueadores?"
│
├─ Sprint Planning (Monday semana 1 de sprint, 10:00 AM, 2 hrs)
│  └─ Participantes: Jacqueline + Edwin + Karla + Asesor técnico
│     Contenido: Refinamiento de backlog, asignación de tasks
│
├─ Sprint Review (Friday semana 2 de sprint, 4:00 PM, 1.5 hrs)
│  └─ Participantes: Team + Stakeholders
│     Contenido: Demo de features, feedback
│
├─ Retrospective (Friday after review, 5:30 PM, 1 hr)
│  └─ Participantes: Jacqueline + Edwin + Karla
│     Contenido: ¿Qué salió bien? ¿Qué mejorar?
│
└─ Weekly Status (Thursday, 2:00 PM, 1 hr)
   └─ Participantes: Karla + Eric + Dev leads
      Contenido: Reporte de avance, issues, decisiones
```

### 4.5 Tecnologías y Herramientas

```
FRONTEND:
├─ Framework: Angular 16 (TypeScript)
├─ Build tool: Angular CLI
├─ Testing: Jasmine + Karma
├─ UI components: Material Design or Bootstrap 5
├─ HTTP client: HttpClientModule (built-in)
└─ State management: NgRx (if needed)

BACKEND:
├─ Framework: ASP.NET Core 8.0
├─ Language: C#
├─ Database ORM: Entity Framework Core
├─ Pattern: Repository pattern + Dependency Injection
├─ Authentication: JWT + Active Directory integration
├─ Testing: xUnit + Moq
├─ API documentation: Swagger/OpenAPI
└─ Logging: Serilog

DATABASE:
├─ Engine: SQL Server 2022 (or latest)
├─ Admin: SQL Server Management Studio
├─ Migrations: EF Core Migrations
└─ Backup strategy: Daily + off-site replication

DEVOPS & TOOLS:
├─ Version control: Git + GitHub/Azure Repos
├─ CI/CD: GitHub Actions / Azure Pipelines
├─ Project management: Azure DevOps / Jira
├─ Code review: Pull Requests
├─ Testing: Automated tests + manual UAT
├─ Deployment: blue-green deployment strategy
├─ Monitoring: Application Insights (Azure)
└─ Environments: Dev → Test → Staging → Production

SECURITY:
├─ Authentication: Active Directory (LDAP)
├─ Authorization: Role-Based Access Control (RBAC)
├─ Data encryption: SSL/TLS in transit, encryption at rest
├─ Audit trail: All actions logged with timestamp + user
├─ Secrets management: Azure Key Vault
└─ Code security: SonarQube scans + OWASP compliance
```

---

<a name="metricas"></a>
## 5. Métricas de Éxito

### 5.1 Métricas de Proceso (Durante Implementación)

```
MÉTRICA 1: Cumplimiento de Cronograma
├─ Definición: % de hitos completados en tiempo vs plan
├─ Target: ≥95%
├─ Cómo medir: Fecha real vs fecha planeada de cada hito
├─ Frecuencia: Semanal
└─ Rojo: <90%, Amarillo: 90-94%, Verde: ≥95%

MÉTRICA 2: Calidad de Código
├─ Definición: Code coverage de tests automatizados
├─ Target: ≥70% (preferiblemente ≥80%)
├─ Cómo medir: SonarQube o herramienta de cobertura
├─ Frecuencia: Diaria (con cada commit)
└─ Rojo: <60%, Amarillo: 60-69%, Verde: ≥70%

MÉTRICA 3: Bug Detection Rate
├─ Definición: # de bugs encontrados antes de producción
├─ Target: Encontrar issues antes de que lleguen a users
├─ Cómo medir: # bugs en UAT vs # bugs en producción
├─ Frecuencia: Semanal
└─ Ideal: 95%+ bugs encontrados en testing

MÉTRICA 4: Sprint Velocity
├─ Definición: Story points completados por sprint
├─ Target: Consistente (establecer baseline, mantener ritmo)
├─ Cómo medir: Suma de points de tasks completadas
├─ Frecuencia: Fin de cada sprint
└─ Uso: Pronosticar cuándo termina el proyecto

MÉTRICA 5: Team Satisfaction
├─ Definición: Moral y satisfacción del equipo de desarrollo
├─ Target: ≥7/10 (escala 1-10)
├─ Cómo medir: Encuesta anónima cada 2 semanas
├─ Frecuencia: Bi-semanal
└─ Rojo: <6, Amarillo: 6-6.9, Verde: ≥7
```

### 5.2 Métricas de Impacto (Post-Implementación)

```
MÉTRICA 1: Lead Time (Tiempo de Respuesta)
├─ Definición: Días desde "Solicitud creada" hasta "Desarrollo inicia"
├─ Baseline: 10.5 días (actual)
├─ Target: 2-3 días (mejora de 75%)
├─ Cómo medir: Automático del sistema (fecha creación - fecha inicio)
├─ Frecuencia: Diaria (dashboard)
├─ Éxito: 80% de solicitudes < 3 días

MÉTRICA 2: Tasa de Solicitudes Perdidas
├─ Definición: % de solicitudes que se pierden o "se olvidan"
├─ Baseline: 15-20%
├─ Target: 0%
├─ Cómo medir: Auditoría de tickets no alocados + quejas de usuarios
├─ Frecuencia: Mensual
├─ Éxito: 6 meses sin un solo reporte de "solicitud perdida"

MÉTRICA 3: Ticket Reopened Rate
├─ Definición: % de tickets reabiertos por información incompleta
├─ Baseline: 25%
├─ Target: <10%
├─ Cómo medir: Tickets con status "Reabierto" / Total tickets
├─ Frecuencia: Mensual
├─ Éxito: Menos de 10% después de 3 meses

MÉTRICA 4: Team Productivity
├─ Definición: Porcentaje de tiempo en desarrollo real vs administrativo
├─ Baseline: 60% (4.8 hrs/día productivas)
├─ Target: 80% (6.6 hrs/día productivas)
├─ Cómo medir: Encuesta + observación
├─ Frecuencia: Trimestral
├─ Éxito: Equipo reporta menos interrupciones

MÉTRICA 5: System Uptime (si impacta los sistemas)
├─ Definición: % de tiempo que SGSPCSI está disponible
├─ Target: 99%+ (máx 40 min downtime/mes)
├─ Cómo medir: Monitoreo automático (Application Insights)
├─ Frecuencia: Continua (alertas si cae)
└─ Éxito: 99.5% uptime durante primer año

MÉTRICA 6: User Adoption
├─ Definición: % de usuarios usando el sistema para solicitudes
├─ Target: 80% en mes 1 (post-launch), 95% en mes 3
├─ Cómo medir: # de usuarios activos / # de usuarios esperados
├─ Frecuencia: Semanal
└─ Rojo: <60%, Amarillo: 60-79%, Verde: ≥80%

MÉTRICA 7: User Satisfaction (CSAT)
├─ Definición: Satisfacción de usuarios con SGSPCSI
├─ Baseline: N/A (nuevo sistema)
├─ Target: ≥8/10 (escala 1-10)
├─ Cómo medir: Encuesta post-solicitud o mensual
├─ Frecuencia: Con cada transacción o mensual
└─ Éxito: 80%+ de usuarios dan 8+ puntos

MÉTRICA 8: Defect Rate (Producción)
├─ Definición: # de bugs reportados en sistema en producción
├─ Target: <5 bugs críticos/mes, <10 normales/mes
├─ Cómo medir: Sistema de ticketing para issues de SGSPCSI
├─ Frecuencia: Semanal
└─ Trending: Debería bajar o mantenerse estable
```

### 5.3 Dashboard de Métricas (Post-Implementación)

```
┌─────────────────────────────────────────────────────────────┐
│         DASHBOARD SGSPCSI - MÉTRICAS EN VIVO                │
└─────────────────────────────────────────────────────────────┘

SECCIÓN 1: SALUD DEL SISTEMA
├─ Sistema Status: 🟢 EN LÍNEA (99.7% uptime)
├─ Solicitudes hoy: 12 creadas, 8 en proceso, 4 completadas
├─ Performance: Respuesta API <200ms | DB queries <100ms
└─ Alertas: 0 críticas, 0 advertencias

SECCIÓN 2: SOLICITUDES
├─ Solicitudes Totales YTD: 245
│  ├─ Tipo A (nuevos sistemas): 45 (18%)
│  ├─ Tipo B (modificaciones): 120 (49%)
│  ├─ Tipo C (problemas): 80 (33%)
│  │
│  └─ Por Estado:
│     ├─ Completadas: 180 (73%)
│     ├─ En Desarrollo: 45 (18%)
│     └─ En Análisis: 20 (8%)
│
└─ Lead Time:
   ├─ Mediana: 2.3 días (TARGET: 2-3 días) ✓
   ├─ P95: 5.1 días (90% de solicitudes < 5 días) ✓
   └─ Histórico: 10.5 días (mejora del 78%) ✓

SECCIÓN 3: CALIDAD
├─ Tickets Reabiertos: 8% (TARGET: <10%) ✓
├─ Defectos por Sistema: [Gráfico de sistemas más problemáticos]
│  ├─ Sistema X: 12 defectos (necesita atención)
│  ├─ Sistema Y: 5 defectos (ok)
│  └─ Sistema Z: 2 defectos (excelente)
│
└─ Cumplimiento de Criterios Aceptación: 94% ✓

SECCIÓN 4: EQUIPO & CAPACIDAD
├─ Esfuerzo Registrado este mes: 312 horas
│  ├─ Jacqueline: 156 horas
│  └─ Edwin: 156 horas
│
├─ Carga de Trabajo:
│  ├─ Desarrollador A: 85% utilizado (adecuado)
│  ├─ Desarrollador B: 82% utilizado (adecuado)
│  └─ Equipo promedio: 83.5% (sin sobrecarga)
│
└─ Productividad Efectiva: 78% (gana 18% vs baseline 60%)

SECCIÓN 5: USUARIO & SATISFACCIÓN
├─ Usuarios Activos: 42 / 50 (84% adoption)
├─ Solicitudes por Área:
│  ├─ RH: 38 solicitudes (16%)
│  ├─ Finanzas: 45 solicitudes (18%)
│  ├─ Operaciones: 72 solicitudes (29%)
│  └─ Otros: 90 solicitudes (37%)
│
├─ Satisfacción (CSAT): 8.6/10 (85% de usuarios ≥8/10) ✓
│
└─ Tiempo promedio respuesta a usuario: 0.3 horas (instant)

SECCIÓN 6: FINANCIERO (ROI)
├─ Horas Ahorradas (vs proceso manual): 180 hrs/mes
├─ Retrabajo Reducido: 45 hrs/mes
├─ Total Impacto: 225 hrs/mes = $3,375/mes
├─ YTD Impacto: $16,875 (3 meses post-launch)
└─ ROI: Proyecto pagado en 1.7 meses

ALERTA: ¿Algún indicador rojo?
     ├─ SÍ → Ejecutar plan de remedio
     └─ NO → Continuar operación normal
```

---

<a name="cronograma"></a>
## 6. Cronograma Ejecutivo

```
┌─────────────────────────────────────────────────────────────┐
│        SGSPCSI: CRONOGRAMA DE ALTO NIVEL                    │
│                                                              │
│  PROYECTO DE RESIDENCIAS PROFESIONALES                      │
│  DURACIÓN: 26 SEMANAS (Enero 26 - Julio 20, 2026)          │
└─────────────────────────────────────────────────────────────┘

SEMANA   FECHA       MES        FASE                  HITO
─────────────────────────────────────────────────────────────────

1        26-30 ene   Enero      Pre-Implementación   ✓ Kickoff
2-3      2-20 feb    Febrero    Fondación            ✓ Backend base
4        15-20 feb   Febrero    Fondación            ✓ API funcionando
5-9      1-13 mar    Marzo      Núcleo               ✓ Frontend UI 50%
10-12    17-27 mar   Marzo      Núcleo               ✓ Aprobaciones
13-15    31 mar-10 abr Abril    Refinamiento         ✓ Dashboard
16-18    14-24 abr   Abril      Refinamiento         ✓ UAT completa
19-20    28 abr-8 may Mayo      Deployment           ✓ Prod preparations
21-22    12-22 may   Mayo       Deployment           ✓ Soft launch
23-24    26 may-5 jun Junio     Deployment           ✓ Full launch
25-26    9-20 jul    Julio      Optimización         ✓ Cierre proyecto

RESUMEN POR FASE:

FASE 0: Pre-Implementación (1 semana)
├─ Duración: 1 semana
├─ Entregables: Plan detallado, equipo listo
└─ Riesgo: Bajo

FASE 1: Fondación (3 semanas, Feb 2-20)
├─ Duración: 3 semanas
├─ Entregables: Backend base, API, BD funcionando
├─ Hitos:
│  └─ Feb 20: Backend 90% completo
└─ Riesgo: Bajo-Medio (dependencias técnicas)

FASE 2: Núcleo (8 semanas, Feb 2 - Mar 27)
├─ Duración: 8 semanas
├─ Entregables: Frontend, formularios, aprobaciones
├─ Hitos:
│  ├─ Mar 6: UI básica funciona
│  ├─ Mar 13: Solicitudes capturables
│  └─ Mar 27: Flujo completo funciona
└─ Riesgo: Medio (integración frontend-backend)

FASE 3: Refinamiento (5 semanas, Mar 31 - Apr 24)
├─ Duración: 5 semanas
├─ Entregables: Bitácora, reportes, optimización
├─ Hitos:
│  ├─ Apr 10: Bitácora de esfuerzo lista
│  ├─ Apr 17: Reportes funcionando
│  └─ Apr 24: UAT completada sin críticos
└─ Riesgo: Bajo (refinamiento de features existentes)

FASE 4: Deployment (6 semanas, Apr 28 - Jun 5)
├─ Duración: 6 semanas
├─ Entregables: Sistema en producción, usuarios capacitados
├─ Hitos:
│  ├─ May 8: Producción lista
│  ├─ May 22: Soft launch con 20% de usuarios
│  └─ Jun 5: Full launch a 100% de usuarios
└─ Riesgo: Medio (ejecución en vivo)

FASE 5: Optimización & Cierre (2 semanas, Jun 9 - Jul 20)
├─ Duración: 2 semanas
├─ Entregables: Documentación, handoff, cierre
├─ Hitos:
│  └─ Jul 20: Proyecto completado
└─ Riesgo: Bajo (post-launch support, minor fixes)

PUNTOS CRÍTICOS (Posibles adelantos/retrasos):

RIESGO 1: Integración Frontend-Backend (Semana 5-7)
├─ Impacto: +1 a +2 semanas si hay issues
├─ Mitigación: Integración temprana (semana 3-4), tests exhaustivos
└─ Plan B: Sprint adicional en Fase 3

RIESGO 2: UAT descubre defectos mayores (Semana 15-18)
├─ Impacto: +2 a +3 semanas de fixes
├─ Mitigación: Testing iterativo, feedback temprano
└─ Plan B: Soft launch con funcionalidades reducidas, luego completas

RIESGO 3: Ambientes de producción no listos (Semana 19)
├─ Impacto: Retraso de 1-2 semanas
├─ Mitigación: Coordinar con IT Operations desde semana 1
└─ Plan B: Usar ambiente staging como producción temporal

RIESGO 4: Adopción de usuarios menor a esperado (Semana 21-23)
├─ Impacto: Objetivos no alcanzados
├─ Mitigación: Capacitación iterativa, feedback constante
└─ Plan B: Hacer sistema obligatorio con fecha cutoff
```

---

<a name="riesgos"></a>
## 7. Riesgos y Contingencias

### 7.1 Registro de Riesgos

```
RIESGO 1: Cambios de requerimientos durante desarrollo
├─ Probabilidad: ALTA (70%)
├─ Impacto: ALTO (puede retrasar 2-4 semanas)
├─ Severidad: ALTA
│
├─ Descripción:
│  Stakeholders descubren nuevas necesidades o clasifican
│  requerimientos diferentes a los originales
│
├─ Causas raíz:
│  ├─ Requerimientos iniciales incompletos
│  ├─ Stakeholders no alineados desde inicio
│  └─ Descubrimientos durante desarrollo
│
├─ Mitigación (Prevención):
│  ├─ Requirements review muy rigurosa en Week 1
│  ├─ Walkthrough con Karla + Eric del scope
│  ├─ Documento frozen (firmas de stakeholders)
│  └─ Control de cambios formal (CR process)
│
├─ Contingencia (Si ocurre):
│  ├─ Change Request formal evaluado
│  ├─ Impacto en cronograma documentado
│  ├─ Decisión: Incluir en sprint actual, próximo sprint, o posponer
│  └─ Comunicación clara de implicaciones

└─ Propietario del Riesgo: PM + Karla

───────────────────────────────────────────────────────

RIESGO 2: Integración con Active Directory falla
├─ Probabilidad: MEDIA (40%)
├─ Impacto: MEDIO-ALTO (bloquea progress 1-2 semanas)
├─ Severidad: MEDIA
│
├─ Descripción:
│  Problemas con integración LDAP a AD institucional
│  (permisos, conectividad, formato de datos)
│
├─ Mitigación:
│  ├─ Coordinación temprana con IT Security
│  ├─ Testing local en ambiente de desarrollo
│  ├─ Documentación de AD structure (gaps, users, groups)
│  └─ Consultoría con especialista en AD si es necesario
│
├─ Contingencia:
│  ├─ Fallback: Implementar usuario/contraseña local
│  ├─ UAT en ambiente con mock AD si es necesario
│  └─ Final launch puede ser con AD después

└─ Propietario: Edwin (Backend) + IT Security

───────────────────────────────────────────────────────

RIESGO 3: Performance de sistema degrada con volumen
├─ Probabilidad: MEDIA (45%)
├─ Impacto: ALTO (sistema lento = no adoptado)
├─ Severidad: MEDIA-ALTA
│
├─ Descripción:
│  Después de go-live, con múltiples usuarios,
│  queries se vuelven lentas o sistema crashea
│
├─ Mitigación:
│  ├─ Load testing en fase pre-producción (semana 18)
│  ├─ Simulación de 50+ usuarios concurrentes
│  ├─ Database indexing optimizado
│  ├─ Caché implementation (if needed)
│  └─ Query optimization desde inicio
│
├─ Contingencia:
│  ├─ Database tuning inmediato
│  ├─ Redistribución de load (horizontal scaling)
│  ├─ Features no críticas deshabilitadas si es necesario
│  └─ Soft launch puede ser con capacidad limitada

└─ Propietario: Edwin + DBA

───────────────────────────────────────────────────────

RIESGO 4: Baja adopción de usuarios post-launch
├─ Probabilidad: MEDIA (50%)
├─ Impacto: MÉDIO (proyecto "éxito técnico, fracaso de adopción")
├─ Severidad: MEDIA
│
├─ Descripción:
│  Usuarios siguen usando método antiguo (email, verbal)
│  Sistema existe pero no se usa
│
├─ Causas:
│  ├─ Capacitación insuficiente
│  ├─ Sistema no intuitivo
│  ├─ Resistencia al cambio
│  └─ Incentivos no alineados
│
├─ Mitigación (Desde inicio):
│  ├─ Capacitación iterativa (no solo al final)
│  ├─ User feedback loops frecuentes
│  ├─ Champions nombrados en cada área
│  ├─ Comunicación frecuente de beneficios
│  ├─ Sistema fácil de usar (UX/UI testing)
│  └─ Éxito para usuarios "early adopters" promocionado
│
├─ Contingencia:
│  ├─ Campañas de adopción intensivas (semana 21-25)
│  ├─ Incentivos: "Quien use sistema gana acceso a features nuevas"
│  ├─ Hacer sistema obligatorio (fecha cutoff)
│  ├─ Soporte intensivo (helpdesk, sesiones 1-on-1)
│  └─ Quick wins iterativos (mejoras rápidas basadas en feedback)

└─ Propietario: Karla + PM

───────────────────────────────────────────────────────

RIESGO 5: Disponibilidad de residentes (ausencias, emergencias)
├─ Probabilidad: BAJA-MEDIA (25-30%)
├─ Impacto: ALTO (+2-4 semanas si alguien se va)
├─ Severidad: ALTA
│
├─ Descripción:
│  Problemas personales de Jacqueline o Edwin
│  ausencias,cambio de proyecto, etc → proyecto atrasado
│
├─ Mitigación:
│  ├─ Documentación clara de cada módulo
│  ├─ Code reviews frecuentes (ambos entienden todo)
│  ├─ Pair programming en tareas críticas
│  ├─ Documentación en vivo (no al final)
│  └─ Contacto con backup developer antes de inicio
│
├─ Contingencia:
│  ├─ Backup developer asignado rápidamente
│  ├─ Priorización de tareas (terminar features core primero)
│  ├─ Posible contratación de consultor ad-hoc
│  └─ Timeline ajustado

└─ Propietario: Karla

───────────────────────────────────────────────────────

RIESGO 6: Infraestructura IT no preparada a tiempo
├─ Probabilidad: BAJA (20%)
├─ Impacto: ALTO (retraso crítico en go-live)
├─ Severidad: ALTA
│
├─ Descripción:
│  Servidores, BD, ambientes (dev, test, prod) no listos
│  en tiempo para soft launch (semana 21)
│
├─ Mitigación:
│  ├─ Planificación de infraestructura en semana 1
│  ├─ Coordinación semanal con IT Operations
│  ├─ Provisioning de ambientes en semana 10 (no al final)
│  ├─ Testing de ambientes en semana 15
│  └─ Documento claro de SLAs (uptime, performance)
│
├─ Contingencia:
│  ├─ Usar ambiente compartido temporalmente
│  ├─ Cloud deployment (Azure, AWS) como alternativa
│  ├─ Escalation a CTO si es necesario
│  └─ Timeline ajustado

└─ Propietario: IT Operations + Karla

───────────────────────────────────────────────────────

SUMMARY RIESGO/MITIGACIÓN:

Riesgo | Prob | Impact | Sev | Status | Owner | Acción
─────────────────────────────────────────────────────
1      | HIGH | HIGH   | H   | 🟡    | PM    | CR Control
2      | MED  | MED-H  | M   | 🟡    | Edwin | AD Testing
3      | MED  | HIGH   | M-H | 🟢    | Edwin | Load Test
4      | MED  | MED    | M   | 🟡    | Karla | Adopción Plan
5      | LOW  | HIGH   | H   | 🟢    | Karla | Documentación
6      | LOW  | HIGH   | H   | 🟢    | IT-Op | Provisioning

Acciones Inmediatas (Semana 1):
✓ Coordinar con IT Operations (Risk #6)
✓ Revisar requerimientos congelados (Risk #1)
✓ Coordinar con IT Security sobre AD (Risk #2)
```

### 7.2 Plan de Contingencia General

```
SI PROYECTO SE ATRASA >2 SEMANAS:
├─ Opción 1: Reducir scope
│  └─ Posponer "bitácora de esfuerzo" (menos crítico)
│     Focus en formularios + aprobaciones + dashboard básico
│
├─ Opción 2: Acelerar timeline
│  └─ Más recursos (contratar consultor)
│
├─ Opción 3: Extender timeline
│  └─ Soft launch en Agosto, full launch Sept
│     (afecta período de residencias, pero viable)
│
└─ Decisión: Karla + Eric (depende de situación)

SI UAT DESCUBRE PROBLEMAS GRAVES (Semana 18):
├─ Opción 1: Fix rápido en 1-2 semanas
│  └─ Si es factible, proceder a staging
│
├─ Opción 2: Posponer soft launch
│  └─ 1-2 semanas más de fixes + re-UAT
│
├─ Opción 3: Reducir scope de soft launch
│  └─ Go live con funcionalidades limitadas
│     (solo formulario A, no B ni C)
│
└─ Criterio: Defectos críticos = ajustable
            Defectos de arch = crítico, requiere revisión

SI ADOPCIÓN ES BAJA POST-LAUNCH (<60%):
├─ Semana 21-22: Investigar causas
│  ├─ Encuestas a usuarios
│  ├─ Sesiones de feedback
│  └─ Identificar pain points del sistema

├─ Semana 22-25:campaña de adopción
│  ├─ Capacitación intensiva
│  ├─ Quick fixes basados en feedback
│  ├─ Champions program (usuarios clave promotingando)
│  └─ Incentivos (features nuevas, gamification)

├─ Semana 25-26: Decisión
│  ├─ Si >70%: Éxito, continuar mejora
│  ├─ Si 50-70%: Aceptable, continuar support post-proyecto
│  └─ Si <50%: Evaluar si continuar o volver a manual

└─ Plan B extremo: Sistema manejado manualmente por PM
                   (valida que código funciona, pero no es adoptado)
```

---

## 8. Conclusión Ejecutiva

### Resumen del Plan

```
PROBLEMA: Gestión manual, dispersa e ineficiente de 300+ sistemas

SOLUCIÓN: SGSPCSI - Plataforma digital centralizada

BENEFICIOS:
├─ Lead time: 10.5 días → 2.5 días (-75%)
├─ Solicitudes perdidas: 15-20% → 0% (fin de pérdidas)
├─ Retrabajo: 20% → 10% (ahorro $47k/año)
├─ Productividad: 60% → 80% (equivale a 2.16 personas)
├─ Satisfacción usuario: 7.2 → 8.5/10 (mejora 18%)
├─ Defectos en producción: 6/mes → 2/mes (-70%)
│
└─ TOTAL IMPACTO AÑO 1: ~$190k en beneficios, $29k en costo
   ROI: 549% | Payback: <2 meses

IMPLEMENTACIÓN: 26 semanas usando residentes
├─ Jacqueline Hurtado (Frontend/Angular)
├─ Edwin Mercado (Backend/C#)
├─ Soporte de Karla Arroyo (Jefa de Desarrollo)
└─ Equipo IT ISSEG (infraestructura, bd, seguridad)

TECNOLOGÍA: Angular + C# .NET + SQL Server
(Stack actual ISSEG, capacitación mínima)

RIESGO: MANEJABLE
├─ Riesgos principales identificados
├─ Mitigaciones preventivas activas
│ └─ Plans B en lugar para cada riesgo
└─ Gobierno claro (Karla + Eric como decision makers)

ÉXITO MEDIDO BY:
├─ % Lead time mejora
├─ % Adopción de usuarios
├─ CSAT ≥8/10
├─ Defectos <5 críticos/mes
└─ Sistema uptime 99%+

PRÓXIMOS PASOS:
1. Aprobación de este plan (Semana 1)
2. Kick-off oficial y asignación de recursos
3. Inicio de construcción (Leak Week de Febrero)
4. Go-live Soft (Mayo 22)
5. Go-live Full (Junio 5)
6. Cierre del proyecto (Julio 20)
```

---

**Documento Completo: Plan Integral SGSPCSI**
**Creado: 20 de Febrero de 2026**
**Para: Instituto de Seguridad Social del Estado de Guanajuato (ISSEG)**
**Residentes: Jacqueline Hurtado, Edwin Mercado**
**Asesor Externo: Karla Teresa Arroyo Calero**
