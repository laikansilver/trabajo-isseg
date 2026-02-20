# Aplicación de CMMI al Proyecto ISSEG

## 📋 Contexto del Proyecto ISSEG

### Descripción del Sistema

**ISSEG** es un sistema integral de gestión de tickets, incidencias y proyectos que incluye:

#### Componentes Principales
1. **Sistema de Tickets Multi-formulario**
   - Formulario A: Sistema Nuevo
   - Formulario B: Modificación de Sistema Existente
   - Formulario C: Requerimientos Específicos
   - Formulario de Problemas e Incidencias

2. **Control de Usuarios y Permisos**
   - Autenticación técnica
   - Control por áreas
   - Roles y permisos granulares
   - Integración con Active Directory (planificada)

3. **Dashboard de Gestión**
   - Inventario de proyectos
   - Métricas y KPIs
   - Seguimiento de tickets

4. **Módulos de Soporte**
   - Gestión de estados de tickets
   - Registro y auditoría en BD
   - Sistema de notificaciones

### Estado Actual del Proyecto

**Documentación Existente**:
- ✅ Diagramas de flujo definidos
- ✅ Formularios estructurados
- ✅ Diagramas de control de acceso
- ✅ Matriz de implementación
- ✅ Diagrama ER de tablas
- ✅ Flujos integrados completos

**Nivel de Madurez Estimado**: **Nivel 1-2 (Transición)**

El proyecto muestra buenas prácticas de documentación, pero aún no tiene procesos formales institucionalizados.

---

## 🎯 Evaluación CMMI Inicial del Proyecto ISSEG

### GAP Analysis Específico

#### NIVEL 2 - Evaluación por Área de Proceso

##### 1. REQM - Gestión de Requerimientos: 60% ██████████████░░░░░░

**✅ Fortalezas**:
- Requerimientos bien documentados en formularios estructurados
- Campos claramente definidos para cada tipo de solicitud
- Trazabilidad básica a través de IDs de tickets

**❌ Debilidades**:
- No hay proceso formal de gestión de cambios de requerimientos
- Falta matriz de trazabilidad completa (req → diseño → código → pruebas)
- No hay baseline formal de requerimientos
- Falta proceso de obtención de compromiso de stakeholders

**📊 Evidencias Actuales**:
```
✅ Formulario-A-Sistema-Nuevo.md
✅ Formulario-B-Modificacion.md
✅ Formulario-C-Requerimientos.md
✅ Formulario-Problema-Incidencia.md
❌ Matriz de trazabilidad
❌ Proceso de gestión de cambios
❌ Registro de compromisos
```

**🎯 Acciones Recomendadas**:
1. Crear proceso formal de gestión de cambios de requerimientos
2. Implementar matriz de trazabilidad en herramienta (Jira/Azure DevOps)
3. Definir proceso de aprobación de requerimientos con stakeholders
4. Establecer baselines de requerimientos por versión/release

---

##### 2. PP - Planificación de Proyectos: 50% ██████████░░░░░░░░░░

**✅ Fortalezas**:
- Existe matriz de implementación (documentada en 09-matriz-implementacion.md)
- Estructuración clara de componentes del sistema
- Identificación de dependencias en diagramas de flujo

**❌ Debilidades**:
- No hay plan de proyecto formal (cronograma, recursos, presupuesto)
- Falta documento de estimaciones de esfuerzo
- No hay identificación formal de riesgos
- No existe WBS (Work Breakdown Structure) detallado

**📊 Evidencias Actuales**:
```
✅ 09-matriz-implementacion.md (estructura parcial)
✅ Diagramas de flujo (muestran secuencia)
❌ Plan de proyecto formal
❌ Cronograma con hitos
❌ Plan de gestión de riesgos
❌ Estimaciones documentadas
```

**🎯 Acciones Recomendadas**:
1. Crear plan de proyecto completo usando plantilla estándar
2. Desarrollar WBS detallado del proyecto ISSEG
3. Realizar estimaciones formales (Planning Poker, PERT, etc.)
4. Identificar y documentar riesgos con plan de mitigación
5. Definir cronograma con hitos medibles

---

##### 3. PMC - Monitoreo y Control: 40% ████████░░░░░░░░░░░░

**✅ Fortalezas**:
- Sistema de tracking de tickets (implica monitoreo básico)
- Diagrama de estados de tickets (control de flujo)

**❌ Debilidades**:
- No hay dashboard de seguimiento del proyecto
- Falta proceso de reuniones de seguimiento regulares
- No se compara avance vs. plan
- No hay proceso de gestión de acciones correctivas
- Métricas no son recolectadas sistemáticamente

**📊 Evidencias Actuales**:
```
✅ 8. Diagrama de Estados del Ticket.mmd
✅ 03-dashboard-inventario-proyectos.md (por implementar)
❌ Dashboard de proyecto en tiempo real
❌ Actas de reuniones de seguimiento
❌ Registro de acciones correctivas
❌ Análisis de varianza (earned value)
```

**🎯 Acciones Recomendadas**:
1. Implementar dashboard de gestión del proyecto (como el documentado)
2. Establecer reuniones de seguimiento semanales con agenda estándar
3. Definir métricas clave (KPIs) y recolectarlas consistentemente
4. Crear proceso de gestión de issues y acciones correctivas
5. Implementar análisis de varianza simple (cronograma y costos)

---

##### 4. SAM - Gestión de Proveedores: N/A

**Estado**: No aplica actualmente (proyecto interno sin proveedores externos identificados)

**Consideración futura**: Si se contrata servicios de cloud (Azure, AWS) o consultoría externa, activar esta área.

---

##### 5. MA - Medición y Análisis: 35% ███████░░░░░░░░░░░░░

**✅ Fortalezas**:
- Dashboard de inventario y proyectos planificado (doc 03)
- Identificación de algunos indicadores (estados de tickets)

**❌ Debilidades**:
- No hay plan de medición alineado a objetivos
- Métricas no están definidas formalmente
- No hay procedimiento de recolección de datos
- Falta análisis de datos y reportes

**📊 Evidencias Actuales**:
```
✅ 03-dashboard-inventario-proyectos.md (planificado)
❌ Plan de medición (GQM)
❌ Definición formal de métricas
❌ Procedimiento de recolección
❌ Dashboard implementado
```

**🎯 Acciones Recomendadas**:
1. Definir objetivos de medición usando GQM (Goal-Question-Metric)
   ```
   Ejemplo:
   GOAL: Mejorar tiempo de resolución de tickets
   QUESTION: ¿Cuál es el tiempo promedio de resolución?
   METRIC: Tiempo de resolución promedio por tipo de ticket
   ```
2. Especificar 10-15 métricas clave del proyecto
3. Automatizar recolección de métricas (desde BD del sistema)
4. Implementar el dashboard planificado
5. Establecer reuniones mensuales de análisis de métricas

---

##### 6. PPQA - Aseguramiento de Calidad: 45% █████████░░░░░░░░░░░

**✅ Fortalezas**:
- Documentación estructurada y completa
- Diagramas de control y validación
- Proceso de diseño disciplinado

**❌ Debilidades**:
- No hay rol formal de QA
- No se realizan auditorías de proceso
- Falta checklist de calidad para entregables
- No hay proceso de code review documentado
- No existe registro de no-conformidades

**📊 Evidencias Actuales**:
```
✅ Documentación completa (06-resumen-ejecutivo.md)
✅ Diagramas de validación (existentes)
❌ Plan de QA
❌ Checklists de calidad
❌ Registro de auditorías
❌ Proceso de code review
```

**🎯 Acciones Recomendadas**:
1. Designar responsable de QA (puede ser rol part-time)
2. Crear checklist de calidad para cada entregable
3. Implementar proceso formal de code review
4. Establecer auditorías mensuales de proceso
5. Crear registro de no-conformidades y acciones correctivas

---

##### 7. CM - Gestión de Configuración: 55% ███████████░░░░░░░░░

**✅ Fortalezas**:
- Estructura organizada de carpetas y archivos
- Nomenclatura consistente de documentos
- Control de versiones implícito (COMPLETADO-V2.0.md)

**❌ Debilidades**:
- No se menciona uso de control de versiones (Git)
- Falta estrategia de branching si usa Git
- No hay proceso de gestión de cambios de configuración
- No se documentan líneas base (baselines)

**📊 Evidencias Actuales**:
```
✅ Estructura organizada de carpetas
✅ COMPLETADO-V2.0.md (control de versión manual)
❌ Repositorio Git configurado
❌ Estrategia de branching
❌ Proceso de gestión de cambios
❌ Documentación de baselines
```

**🎯 Acciones Recomendadas**:
1. Si no está en Git, migrar inmediatamente
2. Establecer estrategia de branching (Git Flow o GitHub Flow)
3. Configurar CI/CD pipeline básico
4. Definir proceso de gestión de cambios de configuración
5. Documentar baselines por versión/release

---

### Resumen de Nivel 2

```
╔══════════════════════════════════════════════════════════╗
║        EVALUACIÓN CMMI NIVEL 2 - PROYECTO ISSEG          ║
╚══════════════════════════════════════════════════════════╝

REQM  ██████████████░░░░░░ 60%
PP    ██████████░░░░░░░░░░ 50%
PMC   ████████░░░░░░░░░░░░ 40%
SAM   N/A (No aplica)
MA    ███████░░░░░░░░░░░░░ 35%
PPQA  █████████░░░░░░░░░░░ 45%
CM    ███████████░░░░░░░░░ 55%

─────────────────────────────────────────────────────────
PROMEDIO NIVEL 2: 48% (Objetivo: 85%+ para consolidar)
BRECHA: 37 puntos porcentuales
ESTIMACIÓN: 6-9 meses para alcanzar Nivel 2
─────────────────────────────────────────────────────────

✅ FORTALEZAS PRINCIPALES:
  • Excelente documentación y organización
  • Requerimientos bien estructurados
  • Diseño disciplinado y detallado

❌ ÁREAS DE OPORTUNIDAD:
  • Falta formalización de procesos
  • No hay medición sistemática
  • Seguimiento y control insuficientes
```

---

## 🎯 Plan de Acción CMMI para Proyecto ISSEG

### Fase 1: Fundamentos (Meses 1-3)

#### Objetivo: Establecer prácticas básicas de gestión de proyectos

**Mes 1: Infraestructura y Herramientas**

| Semana | Acción | Entregable | Responsable |
|--------|--------|------------|-------------|
| 1-2 | Configurar repositorio Git y CI/CD | Repo + pipeline básico | Tech Lead |
| 1-2 | Configurar Jira/Azure DevOps | Proyecto configurado | PM |
| 3 | Migrar requerimientos a herramienta | Tickets creados | BA |
| 4 | Configurar dashboard de métricas | Dashboard v1 | PM |

**Mes 2: Definición de Procesos**

| Semana | Acción | Entregable | Responsable |
|--------|--------|------------|-------------|
| 5-6 | Crear proceso de gestión de requerimientos | PROC-REQM-001 | Process Owner |
| 7 | Crear plantilla de plan de proyecto | TEMPLATE-PP-001 | PM |
| 8 | Definir proceso de code review | PROC-CR-001 | Tech Lead |

**Mes 3: Implementación Inicial**

| Semana | Acción | Entregable | Responsable |
|--------|--------|------------|-------------|
| 9 | Crear plan de proyecto ISSEG completo | Plan v1.0 | PM |
| 10 | Matriz de trazabilidad de requerimientos | Matriz en Jira | BA |
| 11-12 | Capacitación del equipo en procesos | Equipo capacitado | Process Owner |

---

### Fase 2: Consolidación Nivel 2 (Meses 4-6)

#### Objetivo: Ejecutar proyecto con procesos de Nivel 2

**Actividades Continuas**:

```
SEMANAL:
├─ Lunes: Planning de la semana (1 hora)
├─ Lunes-Jueves: Ejecución con procesos
├─ Viernes AM: Code reviews
├─ Viernes PM: Status meeting (30 min)
└─ Viernes: Actualizar métricas en dashboard

MENSUAL:
├─ Semana 4: Revisión de métricas del mes
├─ Semana 4: Análisis de varianza (cronograma y costos)
├─ Semana 4: Auditoría PPQA
└─ Semana 4: Identificar mejoras

TRIMESTRAL:
└─ Evaluación de madurez de procesos
```

**Hitos Clave**:

| Mes | Hito | Criterio de Éxito |
|-----|------|-------------------|
| 4 | Módulo de Autenticación desarrollado | Con todos los procesos nivel 2 |
| 5 | Formularios A, B, C implementados | >85% adherencia a procesos |
| 6 | Dashboard y reportes funcionales | Auditoría PPQA aprobada |

---

### Fase 3: Avanzar hacia Nivel 3 (Meses 7-12)

#### Objetivo: Estandarización organizacional

**Solo si aplica**: Si ISSEG es parte de una organización mayor, proceder con Nivel 3.

**Acciones**:
1. Documentar "Proceso Estándar ISSEG" basado en lo aprendido
2. Crear activos reutilizables para proyectos futuros
3. Establecer programa de capacitación
4. Implementar gestión proactiva de riesgos
5. Análisis causal de defectos encontrados

---

## 📋 Plantillas Específicas para ISSEG

### Plantilla 1: Especificación de Requerimiento

```markdown
# REQUERIMIENTO: [ID] - [Título]

## 1. INFORMACIÓN GENERAL
- **ID**: REQ-ISSEG-XXX
- **Módulo**: [Autenticación | Tickets | Dashboard | Admin]
- **Tipo**: [Funcional | No Funcional | Interfaz | Datos]
- **Prioridad**: [Alta | Media | Baja]
- **Estado**: [Propuesto | Aprobado | En Desarrollo | Implementado | Verificado]
- **Fuente**: [Nombre del stakeholder]
- **Área**: [Desarrollo | TI | Administración | Soporte]
- **Fecha Creación**: [DD/MM/YYYY]
- **Versión**: [1.0]

## 2. DESCRIPCIÓN
[Descripción clara y completa del requerimiento en lenguaje natural]

## 3. JUSTIFICACIÓN
[Por qué es necesario este requerimiento, problema que resuelve, valor de negocio]

## 4. CRITERIOS DE ACEPTACIÓN
- [ ] Criterio 1: [Descripción específica y medible]
- [ ] Criterio 2: [Descripción específica y medible]
- [ ] Criterio 3: [Descripción específica y medible]

## 5. DEPENDENCIAS
- **Requiere**: [REQ-ISSEG-XXX, REQ-ISSEG-YYY]
- **Relacionado con**: [REQ-ISSEG-ZZZ]

## 6. TRAZABILIDAD
- **Diseño**: [LINK a documento de diseño]
- **Código**: [LINK a PR/commit]
- **Pruebas**: [LINK a casos de prueba]
- **Documentación**: [LINK a docs]

## 7. ESTIMACIÓN
- **Esfuerzo**: [X horas/días] 
- **Complejidad**: [Baja | Media | Alta | Muy Alta]

## 8. NOTAS TÉCNICAS
[Consideraciones técnicas, restricciones, alternativas evaluadas]

## 9. HISTORIAL DE CAMBIOS
| Versión | Fecha | Autor | Cambio |
|---------|-------|-------|--------|
| 1.0 | DD/MM/YYYY | Nombre | Creación inicial |
```

**Ejemplo Completado**:

```markdown
# REQUERIMIENTO: REQ-ISSEG-001 - Autenticación con Active Directory

## 1. INFORMACIÓN GENERAL
- **ID**: REQ-ISSEG-001
- **Módulo**: Autenticación
- **Tipo**: Funcional
- **Prioridad**: Alta
- **Estado**: Aprobado
- **Fuente**: Director de TI
- **Área**: TI
- **Fecha Creación**: 19/02/2026
- **Versión**: 1.0

## 2. DESCRIPCIÓN
El sistema debe permitir que los usuarios se autentiquen usando sus 
credenciales de Active Directory de la organización, sin necesidad de 
crear cuentas separadas en el sistema ISSEG.

## 3. JUSTIFICACIÓN
- Simplificar gestión de usuarios (una sola fuente de verdad)
- Mejorar seguridad (políticas centralizadas de contraseñas)
- Reducir fricción para usuarios (no recordar otra contraseña)
- Cumplir con política de seguridad organizacional

## 4. CRITERIOS DE ACEPTACIÓN
- [ ] Usuario puede iniciar sesión con su usuario/contraseña de AD
- [ ] Si las credenciales son válidas en AD, se crea sesión en ISSEG
- [ ] Si falla autenticación, muestra mensaje de error claro
- [ ] Los roles y permisos se asignan localmente en ISSEG
- [ ] Timeout de sesión: 30 minutos de inactividad
- [ ] Funciona con usuarios de todos los dominios organizacionales

## 5. DEPENDENCIAS
- **Requiere**: Acceso de red al servidor de AD
- **Relacionado con**: REQ-ISSEG-002 (Gestión de Roles)

## 6. TRAZABILIDAD
- **Diseño**: [LINK - diagrama de autenticación]
- **Código**: [Pendiente]
- **Pruebas**: [Pendiente]
- **Documentación**: 05-modulo-autenticacion-tecnico.md

## 7. ESTIMACIÓN
- **Esfuerzo**: 20 horas
- **Complejidad**: Media

## 8. NOTAS TÉCNICAS
- Usar LDAP para conectar con AD
- Librería recomendada: System.DirectoryServices (C#) o ldap3 (Python)
- Configurar endpoint de AD en archivo de configuración
- No almacenar contraseñas de AD en ISSEG
- Considerar caché de autenticación para offline (opcional)

## 9. HISTORIAL DE CAMBIOS
| Versión | Fecha | Autor | Cambio |
|---------|-------|-------|--------|
| 1.0 | 19/02/2026 | Process Owner | Creación inicial |
```

---

### Plantilla 2: Plan de Proyecto ISSEG

```markdown
# PLAN DE PROYECTO: ISSEG v1.0

## 1. INFORMACIÓN GENERAL
- **Nombre del Proyecto**: Sistema ISSEG - Sistema de Gestión de Tickets
- **Project Manager**: [Nombre]
- **Sponsor**: [Nombre, Cargo]
- **Fecha de Inicio**: [DD/MM/YYYY]
- **Fecha de Fin Estimada**: [DD/MM/YYYY]
- **Presupuesto**: $[XXX,XXX]
- **Versión del Plan**: 1.0

## 2. OBJETIVOS DEL PROYECTO

### Objetivos de Negocio
1. [ej: Reducir tiempo de procesamiento de tickets en 40%]
2. [ej: Centralizar gestión de solicitudes de TI]
3. [ej: Mejorar visibilidad de proyectos en curso]

### Objetivos de Proyecto (SMART)
1. Entregar sistema funcional con 4 tipos de formularios para [fecha]
2. Implementar control de usuarios con 5 roles diferentes
3. Dashboard operacional con 15 métricas clave
4. 100 usuarios piloto en operación para [fecha]

## 3. ALCANCE

### Incluye (In Scope)
- ✅ Formulario A: Sistema Nuevo
- ✅ Formulario B: Modificación
- ✅ Formulario C: Requerimientos
- ✅ Formulario de Problemas/Incidencias
- ✅ Módulo de autenticación con AD
- ✅ Control de permisos por área
- ✅ Dashboard de inventario y métricas
- ✅ Gestión de estados de tickets
- ✅ Reportes básicos

### No Incluye (Out of Scope)
- ❌ App móvil nativa
- ❌ Integración con sistemas ERP
- ❌ BI avanzado y analítica predictiva
- ❌ Automatización de flujos (workflow engine)

## 4. ENTREGABLES

| # | Entregable | Criterio de Aceptación | Fecha |
|---|------------|------------------------|-------|
| 1 | Diseño de arquitectura | Aprobado por Tech Lead y CTO | [fecha] |
| 2 | Módulo de autenticación | 100% casos de prueba pasan | [fecha] |
| 3 | Formularios A, B, C, Problema | UAT aprobado por usuarios clave | [fecha] |
| 4 | Control de permisos | Matriz de permisos verificada | [fecha] |
| 5 | Dashboard | 15 métricas operando en tiempo real | [fecha] |
| 6 | Base de datos | Diseño normalizado, respaldado | [fecha] |
| 7 | Manual de usuario | Revisado por 3 usuarios | [fecha] |
| 8 | Sistema en producción | 100 usuarios piloto operando | [fecha] |

## 5. CRONOGRAMA

### Resumen de Fases

| Fase | Duración | Inicio | Fin | Hitos |
|------|----------|--------|-----|-------|
| Iniciación | 2 sem | [fecha] | [fecha] | Plan aprobado |
| Diseño | 4 sem | [fecha] | [fecha] | Diseño aprobado |
| Desarrollo | 12 sem | [fecha] | [fecha] | Código completo |
| Pruebas | 4 sem | [fecha] | [fecha] | UAT aprobado |
| Despliegue | 2 sem | [fecha] | [fecha] | Go-live |
| Soporte Post-Go-Live |4 sem | [fecha] | [fecha] | Estabilización |

### WBS (Work Breakdown Structure) - Resumen

```
1. ISSEG
   1.1 Gestión de Proyecto (continuo)
   1.2 Diseño
       1.2.1 Arquitectura de sistema
       1.2.2 Diseño de base de datos
       1.2.3 Diseño de UI/UX
   1.3 Desarrollo - Backend
       1.3.1 API de autenticación
       1.3.2 API de gestión de tickets
       1.3.3 API de usuarios y permisos
       1.3.4 API de dashboard
   1.4 Desarrollo - Frontend
       1.4.1 Módulo de login
       1.4.2 Formularios (A, B, C, Problema)
       1.4.3 Dashboard
       1.4.4 Administración
   1.5 Base de Datos
       1.5.1 Diseño ER
       1.5.2 Scripts DDL
       1.5.3 Datos maestros
   1.6 Pruebas
       1.6.1 Pruebas unitarias
       1.6.2 Pruebas de integración
       1.6.3 Pruebas de sistema
       1.6.4 UAT
   1.7 Documentación
       1.7.1 Manual de usuario
       1.7.2 Manual técnico
       1.7.3 Manual de administración
   1.8 Despliegue
       1.8.1 Ambiente de producción
       1.8.2 Migración de datos
       1.8.3 Capacitación
       1.8.4 Go-live
```

## 6. EQUIPO Y RECURSOS

### Roles y Responsabilidades

| Rol | Persona | % Dedicación | Responsabilidades |
|-----|---------|--------------|-------------------|
| Sponsor | [Nombre] | 5% | Aprobar decisiones clave, proveer recursos |
| Project Manager | [Nombre] | 100% | Gestión integral del proyecto |
| Tech Lead | [Nombre] | 80% | Arquitectura, revisiones técnicas |
| Backend Dev 1 | [Nombre] | 100% | APIs y lógica de negocio |
| Backend Dev 2 | [Nombre] | 100% | Base de datos y stored procedures |
| Frontend Dev 1 | [Nombre] | 100% | UI de formularios |
| Frontend Dev 2 | [Nombre] | 100% | Dashboard y administración |
| QA Engineer | [Nombre] | 100% | Pruebas y QA |
| UX Designer | [Nombre] | 30% | Diseño de interfaces |
| DBA | [Nombre] | 20% | Diseño y optimización de BD |

### Recursos Adicionales

| Recurso | Cantidad | Costo | Notas |
|---------|----------|-------|-------|
| Servidor Desarrollo | 1 VM | $200/mes | Azure/AWS |
| Servidor QA | 1 VM | $200/mes | Azure/AWS |
| Servidor Producción | 1 VM | $500/mes | Azure/AWS |
| SQL Server Licencia | 1 | $X,XXX | Si no enterprise agreement |
| Jira/Azure DevOps | 10 usuarios | $XX/mes | |

## 7. PRESUPUESTO

| Categoría | Costo |
|-----------|-------|
| Personal (6 meses) | $XXX,XXX |
| Infraestructura | $X,XXX |
| Licencias de software | $X,XXX |
| Capacitación | $X,XXX |
| Contingencia (15%) | $XX,XXX |
| **TOTAL** | **$XXX,XXX** |

## 8. RIESGOS

| # | Riesgo | Prob | Imp | Estrategia | Responsable |
|---|--------|------|-----|------------|-------------|
| R1 | Integración con AD falla | Media | Alto | Mitigar: POC temprano en semana 2 | Tech Lead |
| R2 | Requerimientos cambian frecuentemente | Alta | Medio | Aceptar: Proceso ágil de cambios | PM |
| R3 | Usuarios no disponibles para UAT | Media | Alto | Mitigar: Reservar tiempo con 1 mes anticip | Sponsor |
| R4 | Rotación de personal clave | Baja | Alto | Transferir: Documentación exhaustiva | PM |
| R5 | Rendimiento de BD insuficiente | Media | Medio | Mitigar: Pruebas de carga tempranas | DBA |

## 9. COMUNICACIÓN

### Plan de Comunicación

| Audiencia | Qué | Cuándo | Cómo | Responsable |
|-----------|-----|--------|------|-------------|
| Sponsor | Status, issues críticos | Quincenal | Reunión 30 min | PM |
| Equipo | Status, bloqueadores | Diario | Daily standup 15 min | PM |
| Stakeholders | Progreso, demos | Mensual | Presentación 1 hora | PM |
| Usuarios finales | Avances, capacitación | Mensual | Email + demos | PM |
| Dirección | Executive summary | Mensual | Dashboard + reporte | PM |

## 10. GESTIÓN DE CALIDAD

### Criterios de Calidad

| Aspecto | Métrica | Objetivo |
|---------|---------|----------|
| Funcionalidad | % casos de uso pasan UAT | 100% |
| Rendimiento | Tiempo de respuesta | <2 segundos |
| Disponibilidad | Uptime | >99% |
| Código | Cobertura de pruebas unitarias | >80% |
| Código | Calidad (SonarQube) | Grade A |
| Usabilidad | SUS Score | >70 |
| Defectos | Densidad de defectos | <0.5/KLOC |

### Revisiones de Calidad

- Code reviews: 100% del código
- Revisión de diseño: Antes de iniciar desarrollo
- UAT: Antes de despliegue a producción
- Auditoría de seguridad: Antes de go-live

## 11. CRITERIOS DE ÉXITO

### Criterios Obligatorios
- ✅ Todos los entregables completados y aceptados
- ✅ Todos los casos de UAT aprobados
- ✅ Sistema operando en producción con 100 usuarios piloto
- ✅ Cero defectos críticos abiertos
- ✅ Documentación completa entregada
- ✅ Capacitación impartida a usuarios y admins

### Criterios de Excelencia
- 🏆 Proyecto completado dentro del presupuesto
- 🏆 Proyecto completado a tiempo (±5%)
- 🏆 Satisfacción de usuarios >8/10
- 🏆 Cero defectos mayores en primeros 30 días

## 12. APROBACIONES

| Rol | Nombre | Firma | Fecha |
|-----|--------|-------|-------|
| Sponsor | [Nombre] | _______ | ___/___/______ |
| Project Manager | [Nombre] | _______ | ___/___/______ |
| Tech Lead | [Nombre] | _______ | ___/___/______ |

---
**Versión**: 1.0  
**Fecha**: [DD/MM/YYYY]  
**Próxima Revisión**: [DD/MM/YYYY]
```

---

### Plantilla 3: Matriz de Trazabilidad ISSEG

```
MATRIZ DE TRAZABILIDAD - PROYECTO ISSEG
═══════════════════════════════════════════════════════════════════════════════

| Req ID | Requerimiento | Diseño | Código | Pruebas | Estado | Notas |
|--------|---------------|--------|--------|---------|--------|-------|
| REQ-001| Auth con AD   | DES-001| PR#45  | TC-001-010 | ✅ Done | |
| REQ-002| Formulario A  | DES-005| PR#52  | TC-020-035 | 🔄 InProg | Falta validaciones |
| REQ-003| Permisos área | DES-008| PR#48  | TC-040-052 | ✅ Done | |
| REQ-004| Dashboard KPI | DES-012| -      | -       | 📋 ToDo | Inicia sem 10 |
| REQ-005| Formulario B  | DES-006| PR#55  | TC-036-045 | 🔄 InProg | |
...
```

**Herramienta Recomendada**: Implementar custom fields en Jira para automatizar esta matriz.

---

## 🎯 Métricas Clave para Proyecto ISSEG

### Dashboard de Proyecto (Implementar)

```
╔═══════════════════════════════════════════════════════════╗
║         DASHBOARD PROYECTO ISSEG - Sprint 5               ║
╚═══════════════════════════════════════════════════════════╝

CRONOGRAMA:
├─ Avance: 65% ███████████████████▌░░░░░░░░░░░ (Plan: 60%)
├─ SPI: 1.08 🟢 (Adelantado)
└─ Fecha estimada: 15/Mayo/2026 (Original: 20/Mayo/2026)

PRESUPUESTO:
├─ Gastado: $78,000 de $120,000
├─ CPI: 0.96 🟡 (4% sobre presupuesto)
└─ EAC: $125,000 (5% overrun proyectado)

ALCANCE:
├─ Requerimientos: 45/65 completados (69%)
├─ Funcionalidad: 40% implementado
└─ Cambios aprobados: 8 (impacto: +2 semanas)

CALIDAD:
├─ Defectos abiertos: 12 (3 críticos, 9 menores)
├─ Cobertura código: 78% (objetivo: 80%)
├─ Code reviews: 95% realizados
└─ Densidad defectos: 0.6/KLOC (objetivo: <1.0) 🟢

RIESGOS:
├─ Riesgos activos: 3
├─ 🔴 R3: Disponibilidad usuarios UAT (Alto)
└─ 🟡 R5: Performance BD (Medio)

EQUIPO:
├─ Velocidad: 42 story points (promedio: 40) 🟢
├─ Disponibilidad: 95% (1 dev enfermo semana pasada)
└─ Moral: 8.2/10 🟢
```

### Métricas Semanales a Recolectar

```markdown
## MÉTRICAS SEMANALES - ISSEG

### Progreso
- [ ] Story points completados
- [ ] Requerimientos cerrados
- [ ] % completitud de sprint

### Calidad
- [ ] Nuevos defectos reportados
- [ ] Defectos cerrados
- [ ] Defectos críticos abiertos
- [ ] Resultado de code reviews

### Eficiencia
- [ ] Velocidad del equipo (SP/sprint)
- [ ] Tiempo promedio de cycle time
- [ ] % de tiempo en reuniones

### Proceso
- [ ] % de requerimientos con trazabilidad
- [ ] % de código con code review
- [ ] % de commits con tests
```

---

## 🏆 Beneficios Esperados de Implementar CMMI en ISSEG

### Corto Plazo (3-6 meses)

| Beneficio | Métrica | Situación Actual | Meta |
|-----------|---------|------------------|------|
| Visibilidad del proyecto | Dashboard actualizado | No existe | Tiempo real |
| Gestión de cambios | Tiempo de aprobación | Ad-hoc | <48 horas |
| Calidad de código | Code reviews | 20% | 100% |
| Trazabilidad | Req con trazabilidad completa | 10% | 90% |

### Mediano Plazo (6-12 meses)

| Beneficio | Métrica | Impacto |
|-----------|---------|---------|
| Predictibilidad | Precisión de estimaciones | ±30% → ±10% |
| Calidad | Defectos en producción | -50% |
| Eficiencia | Tiempo de desarrollo | -20% (menos retrabajo) |
| Documentación | Docs actualizadas | 60% → 95% |

### Largo Plazo (12+ meses)

- 🎯 **Replicabilidad**: Procesos del proyecto ISSEG sirven de base para futuros proyectos
- 📚 **Conocimiento**: Menor dependencia de individuos específicos
- 🚀 **Escalabilidad**: Capacidad de crecer el equipo sin pérdida de calidad
- 🏆 **Reputación**: Proyecto ISSEG como caso de éxito interno

---

## 📝 Conclusión y Siguientes Pasos

### Resumen Ejecutivo

El proyecto ISSEG tiene una excelente base documental y de diseño (60% de madurez en REQM), pero requiere **formalización de procesos** para alcanzar consistencia y predictibilidad.

**Inversión estimada**: 6-9 meses, ~150-200 horas de esfuerzo adicional del equipo
**ROI esperado**: Mayor predictibilidad, menos defectos, proyecto entregado a tiempo

### Pasos Inmediatos (Próximas 2 semanas)

1. ✅ **Decisión**: Revisar este documento con Sponsor y decidir si proceder
2. ✅ **Herramientas**: Configurar Jira/Azure Dev Ops + repositorio Git
3. ✅ **Plan**: Crear plan de proyecto usando plantilla provista
4. ✅ **Kick-off**: Reunión de equipo para presentar procesos CMMI ligeros

### Primeros 30 Días

1. Implementar proceso de gestión de requerimientos
2. Crear matriz de trazabilidad
3. Establecer reuniones de seguimiento semanal
4. Configurar dashboard de métricas básico
5. Implementar proceso de code review

### Quick Wins (Resultados Rápidos)

- **Semana 1**: Repositorio Git configurado con CI/CD básico
- **Semana 2**: Template de plan de proyecto completado
- **Semana 3**: Dashboard básico de métricas operando
- **Semana 4**: Primer sprint con procesos Nivel 2 completo

---

**Siguiente documento**: [06-Herramientas-y-Recursos.md](06-Herramientas-y-Recursos.md)

**Documento anterior**: [04-Implementacion-CMMI.md](04-Implementacion-CMMI.md)

**Volver al índice**: [00-INDICE-INVESTIGACION-CMMI.md](00-INDICE-INVESTIGACION-CMMI.md)
