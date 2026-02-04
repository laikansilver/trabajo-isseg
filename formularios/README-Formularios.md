# Índice de Formularios - ISSEG

**Documentación en Markdown de los 4 Formularios del Sistema**

---

## 📋 Resumen Comparativo de Formularios

| Aspecto | Form A: Sistema Nuevo | Form B: Modificación | Form C: Requerimientos | Form Problema |
|--------|----------------------|----------------------|----------------------|---------------|
| **ID Auto** | SN-YYYY-NNNN | MOD-YYYY-NNNN | Sin ID | INC-YYYY-NNNN |
| **Propósito** | Solicitar nuevo sistema | Solicitar cambios en sistema existente | Detallar requerimientos post-aprobación | Reportar errores/bugs |
| **Secciones** | 7 | 8 | 7 | 7 |
| **Campos Totales** | 25+ | 25+ | 50+ | 20+ |
| **Tiempo Completar** | 15-20 min | 12-15 min | 30-45 min | 10-15 min |
| **Requiere Aprobación** | **SÍ (ISSEG)** | **SÍ (ISSEG)** | No (validación PM) | **No** |
| **SLA/Seguimiento** | Por aprobación | Por urgencia | N/A | **Automático por urgencia** |
| **Paso Siguiente** | Form C (si aprueba) | Implementación | Desarrollo | Resolución técnica |

---

## 📄 Formulario A: Solicitud de Sistema Nuevo

**Archivo:** [Formulario-A-Sistema-Nuevo.md](./Formulario-A-Sistema-Nuevo.md)

**Cuándo se usa:** Cuando se necesita un sistema completamente nuevo

**Flujo:** Usuario → ISSEG aprueba/rechaza → Si aprueba → Pasa a Form C

**Ejemplo de Casos:**
- Nuevo sistema de gestión de inventario
- Portal de autoservicio para empleados
- Sistema de ticketing
- Aplicación móvil para clientes

### Campos Principales:
1. **Información General** - Quién solicita, cuándo, contacto
2. **Descripción del Sistema** - Nombre, tipo, problema que resuelve
3. **Justificación** - Por qué, beneficios esperados
4. **Alcance Preliminar** - Funcionalidades, integraciones, plataforma
5. **Recursos y Timeline** - Presupuesto, deadline, personas
6. **Documentación** - Archivos, aclaraciones adicionales
7. **Aprobaciones** - Firma del jefe

**Información a Recolectar:** 25+ campos (datos operacionales + justificación empresarial)

---

## 📄 Formulario B: Solicitud de Modificación

**Archivo:** [Formulario-B-Modificacion.md](./Formulario-B-Modificacion.md)

**Cuándo se usa:** Cuando se necesita cambiar/mejorar un sistema existente

**Flujo:** Usuario → ISSEG aprueba/rechaza → Si aprueba → Implementación

**Ejemplo de Casos:**
- Agregar nueva funcionalidad a sistema existente
- Corregir errores conocidos
- Mejorar rendimiento
- Cambiar interfaz de usuario
- Integración con otro sistema
- Actualizar seguridad

### Campos Principales:
1. **Identificación** - Qué sistema, versión actual
2. **Descripción del Cambio** - Tipo de cambio, módulos afectados
3. **Análisis de Necesidad** - Razón, situación actual vs deseada
4. **Análisis de Impacto** - Urgencia, usuarios afectados, migración necesaria
5. **Detalles Técnicos** - Especificación de desarrollo
6. **Contexto y Referencias** - Ticket de error, documentación
7. **Soluciones Temporales** - Workaround disponible (mientras se resuelve)

**Información a Recolectar:** 25+ campos (datos de cambio + análisis de impacto)

---

## 📄 Formulario C: Levantamiento de Requerimientos

**Archivo:** [Formulario-C-Requerimientos.md](./Formulario-C-Requerimientos.md)

**Cuándo se usa:** DESPUÉS de que Form A fue aprobado. Para detallar qué exactamente se va a construir

**Flujo:** Form A aprobado → Form C se completa con PM y equipo técnico → Inicia desarrollo

**Responsables:** Product Manager + Equipo de Desarrollo + Usuario de negocio

**Documentación que Genera:**
- Especificación técnica del sistema
- Diagrama de roles y usuarios
- Lista de requerimientos funcionales (RF)
- Requerimientos no funcionales (RNF - rendimiento, seguridad, etc.)

### Campos Principales:
1. **Información del Proyecto** - ID, PM asignado, responsable
2. **Objetivos y Alcance** - Qué sí y qué no incluye
3. **Actores y Roles** - Quiénes usan qué (tabla dinámica)
4. **Módulos Funcionales** - Desglose de componentes
5. **Requerimientos Funcionales (RF)** - Mínimo 10 RF específicos con criterios de aceptación
6. **Reglas de Negocio** - Validaciones, restricciones, cálculos
7. **Requerimientos No Funcionales (RNF)** - Rendimiento, seguridad, escalabilidad, SLA

**Información a Recolectar:** 50+ campos (especificación técnica detallada)

---

## 📄 Formulario Problema: Reporte de Incidencias

**Archivo:** [Formulario-Problema-Incidencia.md](./Formulario-Problema-Incidencia.md)

**Cuándo se usa:** Cuando hay un error, bug o fallo en un sistema en producción

**Flujo:** Usuario reporta → ISSEG asigna equipo técnico → Resolución automática según SLA

**Automatizaciones Incluidas:**
- SLA automático (1h, 4h, 8h, 24h según urgencia)
- Notificación automática al equipo técnico
- Badge visual (🔴🟠🟡🟢) según urgencia
- Almacenamiento de evidencia (screenshots, logs)

### Campos Principales:
1. **Identificación** - Quién reporta, cuándo, contacto
2. **Sistema Afectado** - Qué sistema, módulo, versión
3. **Descripción** - Qué está mal, pasos para reproducir
4. **Impacto y Urgencia** - Cuántos afectados, SLA automático
5. **Contexto Técnico** - Navegador, SO, mensaje de error
6. **Evidencia** - Screenshots, videos, logs
7. **Confirmación** - Autorización para contacto de seguimiento

**Información a Recolectar:** 20+ campos (datos técnicos + contexto del error)

---

## 🔄 Flujo de Procesos

```
┌─────────────────────────────────────────────────────────────────┐
│                    USUARIO IDENTIFICA NECESIDAD                 │
└────────────────────────────┬────────────────────────────────────┘
                             │
                    ¿Tipo de necesidad?
                             │
         ┌───────────────────┼───────────────────┐
         │                   │                   │
    Sistema nuevo      Modificación        Bug/Problema
         │                   │                   │
         ▼                   ▼                   ▼
    FORMULARIO A        FORMULARIO B       FORMULARIO PROBLEMA
    "Sistema Nuevo"    "Modificación"     "Incidencia"
         │                   │                   │
         │             ┌─────▼──────┐           │
         │             │ ¿APROBADO? │           │
         │             └─────┬──────┘           │
         │                   │                   │
         │              SÍ/NO                   │ (Automático)
         │             /     \                  │
         │        SÍ /         \ NO              │
         │       /               \               │
         ▼      ▼                 ▼              ▼
    FORMULARIO C    RECHAZADO    RESOLUCIÓN
    "Requerimientos" (Fin)       TÉCNICA
         │                         │
         ▼                         ▼
    DESARROLLO              CIERRE/ESCALADA
```

---

## 📊 Matriz de Decisión

**¿Cuál formulario usar?**

### Pregunta 1: ¿Ya existe un sistema para esto?

**NO** → Usa **FORMULARIO A** (Sistema Nuevo)

**SÍ** → Ve a Pregunta 2

---

### Pregunta 2: ¿Está fallando el sistema?

**SÍ** → Usa **FORMULARIO PROBLEMA** (Incidencia)

**NO** → Ve a Pregunta 3

---

### Pregunta 3: ¿Se necesita cambiar algo en el sistema existente?

**SÍ** → Usa **FORMULARIO B** (Modificación)

**NO** → No requiere formulario (revisar documentación existente)

---

### Pregunta 4: ¿Fue aprobado un Sistema Nuevo?

**SÍ** → Usa **FORMULARIO C** (Requerimientos - para detallar qué construir)

**NO** → Esperar aprobación o revisar si necesita Form B para mejoras

---

## 📋 Checklist por Rol

### Usuario/Solicitante
- [ ] ¿Identifiqué claramente el problema o necesidad?
- [ ] ¿Completé todos los campos obligatorios?
- [ ] ¿Adjunté evidencia (screenshots, documentos)?
- [ ] ¿Mi gerente está informado y de acuerdo?
- [ ] ¿Ingresé correctamente mi contacto?

### Gerente/Jefe Directo
- [ ] ¿Revisé y valido la necesidad?
- [ ] ¿Tengo presupuesto para esto? (solo Form A y B)
- [ ] ¿Puedo aprobar el cambio?
- [ ] ¿Informo a mi equipo si es aprobado?

### ISSEG (Revisor)
- [ ] ¿Todos los campos obligatorios están completos?
- [ ] ¿La prioridad es la correcta?
- [ ] ¿Hay impacto en otros sistemas?
- [ ] ¿Apruebo o requiero más información?
- [ ] ¿Asigno equipo de desarrollo?

### Equipo Técnico (Form C)
- [ ] ¿Completé requerimientos funcionales (mín. 10)?
- [ ] ¿Documenté requerimientos no funcionales?
- [ ] ¿Defino roles y permisos?
- [ ] ¿Identifico módulos y dependencias?
- [ ] ¿Estoy listo para iniciar desarrollo?

---

## 🔗 Relación con Base de Datos

Cada formulario alimenta una o más tablas:

| Formulario | Tabla Principal | Tablas Secundarias |
|-----------|-----------------|-------------------|
| **A: Sistema Nuevo** | `Sistemas` | `Audit_Sistemas_Nuevos`, `Historial_Cambios` |
| **B: Modificación** | `Historial_Cambios` | `Audit_Modificaciones`, `Control_Incidencias` |
| **C: Requerimientos** | Documento (no tabla) | Documentación en Wiki/Confluence |
| **Problema** | `Problemas_Reportados` | `Control_Incidencias`, `SLA_Definiciones`, `Alertas_SLA` |

---

## 📞 Soporte

**¿Dudas sobre qué formulario usar?**
1. Consultar matriz de decisión (arriba)
2. Revisar ejemplos de casos de uso
3. Contactar a ISSEG: `isseg@empresa.com`

**¿Dudas sobre cómo llenar un formulario?**
1. Consultar archivo `.md` del formulario
2. Revisar descripción de cada campo
3. Contactar a tu gerente o ISSEG

---

**Versión:** 2.0  
**Última actualización:** 2026  
**Autor:** ISSEG - Área de Sistemas
