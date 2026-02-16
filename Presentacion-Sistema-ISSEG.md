# Sistema de Gestión ISSEG
## Presentación General del Sistema

**Fecha:** Febrero 2026  
**Versión:** 2.0  
**Área:** ISSEG - Gestión de Sistemas

---

# 📋 Agenda de la Presentación

1. **Visión General del Sistema**
2. **Problemática Actual**
3. **Solución Propuesta**
4. **Los 4 Formularios**
5. **Flujos de Trabajo**
6. **Base de Datos y Arquitectura**
7. **Beneficios y Resultados Esperados**
8. **Próximos Pasos**

---

# 1️⃣ Visión General del Sistema

## ¿Qué es el Sistema ISSEG?

**Sistema integral de gestión de solicitudes, modificaciones y problemas** para todos los sistemas informáticos de la organización.

### Objetivos Principales:

✅ **Centralizar** todas las solicitudes en un solo lugar

✅ **Estandarizar** los procesos de solicitud y aprobación

✅ **Automatizar** el seguimiento con SLA (Service Level Agreement)

✅ **Auditar** todos los cambios y decisiones

✅ **Mejorar** los tiempos de respuesta y resolución

---

# 2️⃣ Problemática Actual

## ¿Qué problemas estamos resolviendo?

### ❌ **ANTES** (Sin el sistema):

- Solicitudes por email, llamadas telefónicas, pasillos
- No hay registro centralizado
- Se pierden solicitudes
<!-- SLA (Service Level Agreement) - Acuerdo de Nivel de Servicio
Un SLA es un contrato o acuerdo que establece los niveles de servicio esperados 
entre un proveedor y un cliente. Define métricas como:

- Tiempo de respuesta máximo
- Disponibilidad del servicio (uptime)
- Tiempos de resolución de incidentes
- Penalizaciones por incumplimiento

En este contexto, la falta de seguimiento de tiempos SLA significa que el sistema 
ISSEG no tiene implementado un mecanismo para monitorear y garantizar que se cumplan 
los compromisos de tiempo de servicio establecidos con los usuarios. -->
- No hay seguimiento de tiempos (SLA)
- Difícil priorizar qué es urgente
- No hay historial de cambios
- Aprobaciones verbales sin registro
- Falta de documentación técnica

---

# 2️⃣ Problemática Actual (continuación)

## Impacto en la Operación

| Problema | Consecuencia |
|----------|--------------|
| **Pérdida de solicitudes** | Usuarios frustrados, trabajo duplicado |
| **Sin priorización** | Proyectos importantes retrasados |
| **Sin SLA** | No se cumple con tiempos de respuesta |
| **Sin documentación** | Dependencia de personas clave |
| **Sin auditoría** | Riesgos de cumplimiento y seguridad |
| **Sin historial** | Se repiten los mismos problemas |

---

# 3️⃣ Solución Propuesta

## ✅ **DESPUÉS** (Con el sistema):

### 🎯 **Solicitudes Controladas**
- Formularios estandarizados
- Registro automático con ID único
- Toda la información necesaria capturada

### ⏱️ **SLA Automático**
- Tiempos de respuesta definidos
- Alertas automáticas
- Seguimiento en tiempo real

### 📊 **Trazabilidad Completa**
- Auditoría de todos los cambios
- Historial completo
- Reportes ejecutivos

---

# 3️⃣ Solución Propuesta (continuación)

## Componentes del Sistema

```
┌─────────────────────────────────────────────────────┐
│              SISTEMA ISSEG v2.0                     │
├─────────────────────────────────────────────────────┤
│                                                     │
│  📝 4 FORMULARIOS ESTANDARIZADOS                    │
│     ├─ Formulario A: Sistema Nuevo                 │
│     ├─ Formulario B: Modificación                  │
│     ├─ Formulario C: Requerimientos                │
│     └─ Formulario Problema: Incidencias            │
│                                                     │
│  🔄 3 FLUJOS DE TRABAJO                             │
│     ├─ Flujo Sistema Nuevo                         │
│     ├─ Flujo Modificación                          │
│     └─ Flujo Resolución Problemas                  │
│                                                     │
│  💾 BASE DE DATOS (9 tablas)                        │
│     ├─ Sistemas                                    │
│     ├─ Historial_Cambios                           │
│     ├─ Problemas_Reportados                        │
│     ├─ Control_Incidencias                         │
│     └─ ... (5 tablas más)                          │
│                                                     │
│  🔐 CONTROL DE ACCESO                               │
│     ├─ Autenticación                               │
│     ├─ Autorización por Roles                      │
│     └─ Permisos por Área                           │
│                                                     │
└─────────────────────────────────────────────────────┘
```

---

# 4️⃣ Los 4 Formularios

## Comparativa Rápida

| Formulario | Cuándo Usar | ID | Tiempo | Aprobación |
|-----------|-------------|-----|--------|------------|
| **A: Sistema Nuevo** | Necesito un sistema completamente nuevo | SN-2026-XXXX | 15-20 min | ✅ SÍ (ISSEG) |
| **B: Modificación** | Cambiar sistema existente | MOD-2026-XXXX | 12-15 min | ✅ SÍ (ISSEG) |
| **C: Requerimientos** | Detallar qué construir (post-aprobación) | N/A | 30-45 min | ⚠️ Validación PM |
| **Problema** | Reportar error/bug | INC-2026-XXXX | 10-15 min | ❌ NO (automático) |

---

# 4️⃣ Formulario A: Sistema Nuevo

## 🆕 Solicitud de Sistema Nuevo

**Propósito:** Cuando necesitas un sistema que **NO existe**

### Ejemplos de Uso:
- Sistema de gestión de inventario
- Portal de empleados
- App móvil para clientes
- Sistema de ticketing
- Plataforma de reportes

### Datos que se Capturan (25+ campos):

✅ **Quién** solicita, **cuándo**, **contacto**  
✅ **Qué** sistema necesita (nombre, tipo, descripción)  
✅ **Por qué** lo necesita (justificación, beneficios)  
✅ **Para qué** (alcance, funcionalidades, usuarios)  
✅ **Recursos** (timeline, equipo disponible)  
✅ **Aprobación** del jefe directo

---

# 4️⃣ Formulario A: Sistema Nuevo (continuación)

## Secciones del Formulario

```
┌─────────────────────────────────────────────────┐
│  FORMULARIO A: SISTEMA NUEVO                    │
├─────────────────────────────────────────────────┤
│                                                 │
│  1️⃣ Información General (7 campos)              │
│     • ID: SN-2026-XXXX (automático)             │
│     • Nombre, Área, Email, Teléfono             │
│                                                 │
│  2️⃣ Descripción del Sistema (4 campos)          │
│     • Nombre sistema, Tipo                      │
│     • Problema que resuelve                     │
│                                                 │
│  3️⃣ Justificación (6 campos)                    │
│     • Beneficios esperados                      │
│     • Prioridad: Crítica/Alta/Media/Baja        │
│     • Usuarios estimados                        │
│                                                 │
│  4️⃣ Alcance Preliminar (4 campos)               │
│     • Funcionalidades principales               │
│     • Integraciones necesarias                  │
│     • Plataforma (Web/Desktop/Mobile)           │
│                                                 │
│  5️⃣ Recursos y Timeline (2 campos)              │
│     • Fecha límite                              │
│     • Recursos humanos disponibles              │
│                                                 │
│  6️⃣ Documentación (2 campos)                    │
│     • Archivos adjuntos                         │
│                                                 │
│  7️⃣ Aprobaciones (3 campos) ⭐                   │
│     • Aprobación jefe directo (obligatorio)     │
│                                                 │
└─────────────────────────────────────────────────┘
```

---

# 4️⃣ Formulario B: Modificación

## 🔧 Solicitud de Modificación

**Propósito:** Cambiar o mejorar un sistema **que YA existe**

### Ejemplos de Uso:
- Agregar nueva funcionalidad
- Corregir errores conocidos
- Mejorar rendimiento
- Cambiar interfaz de usuario
- Integrar con otro sistema
- Actualizar medidas de seguridad

### Datos que se Capturan (25+ campos):

✅ **Qué sistema** se va a modificar  
✅ **Tipo de cambio** (nueva funcionalidad, corrección, mejora...)  
✅ **Por qué** es necesario el cambio  
✅ **Impacto** en usuarios y otros sistemas  
✅ **Urgencia** y SLA automático  
✅ **Solución temporal** (workaround) si existe

---

# 4️⃣ Formulario B: Modificación (continuación)

## Análisis de Impacto Integrado

**Pregunta Clave:** ¿Qué tan urgente y qué tan crítico es?

| Urgencia | SLA Respuesta | SLA Resolución | Uso |
|----------|---------------|----------------|-----|
| **Inmediata** 🔴 | 1 hora | 4 horas | Sistemas caídos, pérdida datos |
| **Alta** 🟠 | 4 horas | 8 horas | Afecta operación diaria |
| **Media** 🟡 | 8 horas | 16 horas | Mejoras importantes |
| **Baja** 🟢 | 24 horas | 48 horas | Optimizaciones |

### Otras Validaciones:
- ¿Cuántos usuarios afecta?
- ¿Afecta otros sistemas?
- ¿Requiere migración de datos?
- ¿Requiere capacitación?

---

# 4️⃣ Formulario C: Requerimientos

## 📐 Levantamiento de Requerimientos Detallado

**Propósito:** Documentar **QUÉ exactamente** se va a construir

**⚠️ IMPORTANTE:** Solo se completa **DESPUÉS** de que el Formulario A fue **APROBADO**

### ¿Quiénes participan?
- 👤 **Product Manager** (líder)
- 💻 **Equipo de Desarrollo** (técnicos)
- 🏢 **Usuario de Negocio** (define necesidades)

### Documentación que Genera (11 campos):
✅ Especificación técnica completa  
✅ Roles y permisos de usuarios  
✅ **Mínimo 10 Requerimientos Funcionales (RF)**  
✅ Requerimientos No Funcionales (RNF): rendimiento, seguridad  
✅ Reglas de negocio y validaciones  
✅ Módulos y dependencias

---

# 4️⃣ Formulario C: Requerimientos (continuación)

## Ejemplo de Requerimientos Funcionales

| ID | Descripción | Prioridad | Criterio de Aceptación |
|----|-------------|-----------|------------------------|
| RF-001 | El sistema debe permitir registro de usuarios con email único | Crítica | Usuario creado, email confirmado, no duplicados |
| RF-002 | El sistema debe generar reporte PDF de actividades mensuales | Alta | PDF generado en < 5 segundos |
| RF-003 | El sistema debe validar integridad de datos antes de guardar | Crítica | Validaciones ejecutadas, errores mostrados |
| RF-004 | El sistema debe enviar notificaciones por email | Media | Email enviado en < 30 segundos |
| RF-005 | El sistema debe permitir exportar datos a Excel | Media | Archivo .xlsx generado correctamente |

**Mínimo:** 10 RF obligatorios  
**Recomendado:** 15-30 RF para sistemas medianos

---

# 4️⃣ Formulario C: Requerimientos (continuación)

## Requerimientos No Funcionales (RNF)

| Categoría | Ejemplo de Especificación |
|-----------|---------------------------|
| **Rendimiento** | Tiempo de respuesta < 2 segundos<br>Soportar 500 usuarios concurrentes |
| **Seguridad** | Encriptación SSL/TLS<br>Autenticación OAuth 2.0<br>Control de acceso basado en roles (RBAC) |
| **Escalabilidad** | Soportar crecimiento de 10x usuarios en 2 años |
| **Disponibilidad** | 99.9% uptime (SLA)<br>Mantenimiento: sábados 2-6 AM |
| **Compatibilidad** | Chrome, Firefox, Safari, Edge<br>Windows 10+, macOS, Linux |
| **Usabilidad** | Cumplir WCAG 2.1 Level AA (accesibilidad) |
| **Backup** | Backup diario incremental<br>RTO (Recovery Time Objective) < 4 horas |

---

# 4️⃣ Formulario Problema: Incidencias

## 🚨 Reporte de Problemas/Incidencias

**Propósito:** Reportar **errores, bugs o fallos** en sistemas en producción

### Ejemplos de Uso:
- Sistema no carga (error 500)
- Botón no funciona
- Datos incorrectos en reporte
- Integración falló
- Usuario no puede acceder
- Rendimiento muy lento

### Características Especiales:

🔴 **SLA Automático** (calculado por urgencia)  
🆔 **ID Auto-generado** (INC-2026-XXXX)  
📧 **Notificación Automática** al equipo técnico  
📎 **Evidencia** (screenshots, videos, logs)  
❌ **NO requiere aprobación** (resolución inmediata)

---

# 4️⃣ Formulario Problema: Incidencias (continuación)

## SLA Automático Visual

```
┌────────────────────────────────────────────────────┐
│  NIVEL DE URGENCIA → SLA AUTOMÁTICO               │
├────────────────────────────────────────────────────┤
│                                                    │
│  🔴 CRÍTICA                                        │
│     • Respuesta: 1 hora                           │
│     • Resolución: 4 horas                         │
│     • Uso: Sistema caído, pérdida de datos        │
│                                                    │
│  🟠 ALTA                                           │
│     • Respuesta: 4 horas                          │
│     • Resolución: 8 horas                         │
│     • Uso: Afecta operación diaria                │
│                                                    │
│  🟡 MEDIA                                          │
│     • Respuesta: 8 horas                          │
│     • Resolución: 16 horas                        │
│     • Uso: Errores no críticos                    │
│                                                    │
│  🟢 BAJA                                           │
│     • Respuesta: 24 horas                         │
│     • Resolución: 48 horas                        │
│     • Uso: Mejoras cosméticas                     │
│                                                    │
└────────────────────────────────────────────────────┘
```

---

# 5️⃣ Flujos de Trabajo

## Matriz de Decisión: ¿Qué Formulario Usar?

```
                    ¿Ya existe un sistema?
                            │
                 ┌──────────┴──────────┐
                NO                    SÍ
                 │                     │
                 ▼                     ▼
          FORMULARIO A        ¿Está fallando?
        "Sistema Nuevo"               │
                               ┌──────┴──────┐
                              SÍ            NO
                               │             │
                               ▼             ▼
                      FORMULARIO         FORMULARIO B
                       PROBLEMA         "Modificación"
                      "Incidencia"
```

### Caso Especial:
**¿Form A fue aprobado?**  
→ Sí → Completar **FORMULARIO C** (Requerimientos)

---

# 5️⃣ Flujo 1: Sistema Nuevo

## De la Idea a la Producción

```
1️⃣ SOLICITUD
   Usuario completa Formulario A
   ↓
   ID: SN-2026-0001 generado
   ↓
   Aprobación Jefe ✅
   ↓
   
2️⃣ REVISIÓN ISSEG
   ✅ Aprueba → Continúa
   ❌ Rechaza → Fin (notificar razón)
   ↓
   
3️⃣ LEVANTAMIENTO DE REQUERIMIENTOS
   PM + Dev + Usuario completan Formulario C
   ↓
   Especificación técnica completa
   ↓
   
4️⃣ DESARROLLO
   Equipo de desarrollo construye el sistema
   ↓
   Testing y validación
   ↓
   
5️⃣ DESPLIEGUE
   Sistema en producción
   ↓
   Registro en BD: tabla Sistemas
   ↓
   Capacitación y documentación
   ↓
   
6️⃣ CIERRE
   Notificación a usuario
   Auditoría completa registrada
```

**Tiempo Estimado:** 2-6 meses (depende de complejidad)

---

# 5️⃣ Flujo 2: Modificación

## Cambios Controlados en Sistemas Existentes

```
1️⃣ SOLICITUD
   Usuario completa Formulario B
   ↓
   ID: MOD-2026-0001 generado
   ↓
   Sistema: ERP v3.2 (auto-detectado)
   ↓
   
2️⃣ ANÁLISIS DE IMPACTO
   ¿Urgencia? → Alta 🟠
   ↓
   SLA: Respuesta 4h / Resolución 8h
   ↓
   ¿Afecta otros sistemas? → Sí (CRM)
   ↓
   
3️⃣ REVISIÓN ISSEG
   ✅ Aprueba → Continúa
   ❌ Rechaza → Fin
   ↓
   
4️⃣ IMPLEMENTACIÓN
   Desarrollo del cambio
   ↓
   Testing en ambiente QA
   ↓
   Migración de datos (si aplica)
   ↓
   
5️⃣ DESPLIEGUE
   Cambio en producción
   ↓
   Registro en BD: tabla Historial_Cambios
   ↓
   Versión actualizada: v3.2 → v3.3
   ↓
   
6️⃣ CIERRE
   Notificación a usuarios
   Capacitación (si aplica)
   Auditoría registrada
```

**Tiempo Estimado:** 1-4 semanas (depende de urgencia)

---

# 5️⃣ Flujo 3: Resolución de Problemas

## Atención Rápida a Incidencias

```
1️⃣ REPORTE
   Usuario completa Formulario Problema
   ↓
   ID: INC-2026-0001 generado (automático)
   ↓
   Urgencia seleccionada: CRÍTICA 🔴
   ↓
   
2️⃣ ASIGNACIÓN AUTOMÁTICA
   SLA: 1h respuesta / 4h resolución
   ↓
   Notificación automática → Equipo técnico
   ↓
   Badge visual 🔴 en dashboard
   ↓
   
3️⃣ DIAGNÓSTICO
   Equipo técnico revisa evidencia
   ↓
   Screenshots, logs, descripción
   ↓
   Pasos para reproducir
   ↓
   
4️⃣ RESOLUCIÓN
   Implementar fix
   ↓
   Testing y validación
   ↓
   Despliegue del fix
   ↓
   
5️⃣ VERIFICACIÓN
   Usuario confirma resolución ✅
   ↓
   Registro en BD: tabla Problemas_Reportados
   ↓
   Tiempo respuesta: 45 min ✅ (< 1h)
   Tiempo resolución: 3h 20min ✅ (< 4h)
   ↓
   
6️⃣ CIERRE
   Incidencia cerrada
   Análisis de causa raíz
   Prevención de futuros problemas
```

**Tiempo Estimado:** 1h - 48h (según SLA)

---

# 6️⃣ Base de Datos y Arquitectura

## Esquema de Base de Datos (9 Tablas)

```
┌─────────────────────────────────────────────────────────┐
│              BASE DE DATOS ISSEG                        │
├─────────────────────────────────────────────────────────┤
│                                                         │
│  📊 TABLAS PRINCIPALES (Datos de Negocio)               │
│                                                         │
│  1. Sistemas                                            │
│     • ID, Nombre, Tipo, Versión, Estado                │
│     • Área responsable, PM asignado                    │
│     • Fecha producción, Uptime                         │
│                                                         │
│  2. Historial_Cambios                                   │
│     • ID_Cambio, ID_Sistema, Versión                   │
│     • Tipo cambio, Descripción, Impacto                │
│     • Usuario solicitante, Fecha                       │
│                                                         │
│  3. Problemas_Reportados                                │
│     • ID_Problema, ID_Sistema, Urgencia                │
│     • Descripción, Usuario reportante                  │
│     • Fecha reporte, Estado, Asignado a                │
│                                                         │
│  4. Control_Incidencias                                 │
│     • ID_Incidencia, ID_Problema                       │
│     • Fecha inicio, Fecha resolución                   │
│     • Tiempo respuesta, Tiempo resolución              │
│     • Cumple SLA (Sí/No)                               │
│                                                         │
│  5. Uptime_Sistema                                      │
│     • ID_Sistema, Fecha, Uptime %                      │
│     • Downtime minutos, Incidencias                    │
│                                                         │
└─────────────────────────────────────────────────────────┘
```

---

# 6️⃣ Base de Datos y Arquitectura (continuación)

## Tablas de Auditoría y Control

```
┌─────────────────────────────────────────────────────────┐
│  🔍 TABLAS DE AUDITORÍA (Trazabilidad)                  │
│                                                         │
│  6. Audit_Sistemas_Nuevos                               │
│     • ID_Solicitud (SN-YYYY-XXXX)                      │
│     • Datos completos del Formulario A                 │
│     • Estado: Pendiente/Aprobado/Rechazado             │
│     • Aprobador, Fecha aprobación, Comentarios         │
│                                                         │
│  7. Audit_Modificaciones                                │
│     • ID_Modificación (MOD-YYYY-XXXX)                  │
│     • Datos completos del Formulario B                 │
│     • Estado, SLA asignado                             │
│                                                         │
│  🎯 TABLAS DE SLA (Automatización)                      │
│                                                         │
│  8. SLA_Definiciones                                    │
│     • Tipo (Sistema Nuevo, Modificación, Problema)     │
│     • Urgencia (Crítica, Alta, Media, Baja)            │
│     • Tiempo_Respuesta, Tiempo_Resolución              │
│                                                         │
│  9. Alertas_SLA                                         │
│     • ID_Alerta, ID_Incidencia/ID_Modificación         │
│     • Tipo alerta (50%, 75%, 100%, Vencido)            │
│     • Fecha alerta, Notificado a                       │
│                                                         │
└─────────────────────────────────────────────────────────┘
```

---

# 6️⃣ Arquitectura de Seguridad

## Control de Acceso y Autorización

### 🔐 Niveles de Acceso

| Rol | Permisos | Formularios que Puede Usar |
|-----|----------|---------------------------|
| **Usuario Final** | Crear solicitudes propias, ver propias | A, B, Problema |
| **Jefe de Área** | + Aprobar solicitudes de su área | A, B |
| **ISSEG Revisor** | + Ver todas, aprobar/rechazar, asignar | Todos (solo lectura C) |
| **ISSEG Admin** | + Modificar configuración, SLA | Todos |
| **PM/Developer** | + Completar Form C, actualizar estado | C (edición) |
| **Auditor** | Solo lectura de todo | Ninguno (solo lectura) |

### 🛡️ Seguridad Implementada
- ✅ Autenticación (login único empresarial)
- ✅ Autorización por roles (RBAC)
- ✅ Permisos por área/departamento
- ✅ Auditoría de todos los accesos
- ✅ Encriptación de datos sensibles

---

# 7️⃣ Beneficios y Resultados Esperados

## 📈 KPIs (Indicadores Clave de Desempeño)

| KPI | Meta Año 1 | Cómo se Mide |
|-----|-----------|--------------|
| **Solicitudes Perdidas** | < 1% | Total registradas vs total procesadas |
| **Cumplimiento SLA** | > 95% | Incidencias resueltas en tiempo vs total |
| **Tiempo Promedio Respuesta (Crítica)** | < 1 hora | Promedio tiempo primera respuesta |
| **Tiempo Promedio Resolución (Alta)** | < 8 horas | Promedio tiempo resolución |
| **Satisfacción Usuario** | > 85% | Encuesta post-resolución |
| **Documentación Completa** | 100% | Sistemas con Form C completo |
| **Uptime Promedio** | > 99% | Disponibilidad mensual de sistemas |

---

# 7️⃣ Beneficios por Stakeholder

## 👥 ¿Quién Gana y Qué Gana?

### 👤 **Usuarios Finales**
✅ Proceso claro para solicitar sistemas/cambios  
✅ Seguimiento en tiempo real de su solicitud  
✅ Tiempos de respuesta garantizados (SLA)  
✅ No se pierden solicitudes  

### 👔 **Gerentes/Jefes de Área**
✅ Visibilidad de todas las solicitudes de su área  
✅ Aprobaciones digitales con trazabilidad  
✅ Reportes ejecutivos de proyectos  
✅ Mejor asignación de recursos  

### 💻 **Equipo ISSEG**
✅ Centralización de solicitudes (no más emails/llamadas)  
✅ Priorización automática  
✅ Métricas y reportes en tiempo real  
✅ Auditoría completa para cumplimiento  

### 🏢 **Organización**
✅ Mejor gobierno de TI  
✅ Cumplimiento normativo  
✅ Reducción de riesgos  
✅ Mayor eficiencia operativa  

---

# 7️⃣ Comparativa Antes/Después

## 📊 Resultados Esperados

| Métrica | ANTES (Sin Sistema) | DESPUÉS (Con Sistema) | Mejora |
|---------|--------------------|-----------------------|--------|
| **Solicitudes perdidas** | ~15-20% | < 1% | ✅ 95% reducción |
| **Tiempo registro solicitud** | 30-60 min (emails) | 10-20 min (formulario) | ✅ 50% más rápido |
| **Visibilidad para usuario** | ❌ Ninguna | ✅ Completa (dashboard) | ✅ 100% |
| **Cumplimiento SLA** | No definido | > 95% | ✅ Nuevo |
| **Auditoría** | Manual/incompleta | ✅ Automática 100% | ✅ Nuevo |
| **Documentación sistemas** | 30-40% | 100% | ✅ +60% |
| **Tiempo resolución promedio** | Variable (días/semanas) | Por SLA (horas/días) | ✅ 70% reducción |

---

# 8️⃣ Próximos Pasos

## 🚀 Plan de Implementación

### **Fase 1: Piloto** (Mes 1-2)
- [ ] Implementar sistema en ambiente de pruebas
- [ ] Entrenar a 5-10 usuarios piloto
- [ ] Probar los 4 formularios
- [ ] Ajustar según feedback

### **Fase 2: Despliegue Gradual** (Mes 3-4)
- [ ] Lanzar a 25% de la organización
- [ ] Capacitación masiva
- [ ] Migrar solicitudes históricas importantes
- [ ] Monitorear KPIs

### **Fase 3: Adopción Completa** (Mes 5-6)
- [ ] Lanzar a 100% de la organización
- [ ] Hacer obligatorio el uso del sistema
- [ ] Reportes ejecutivos mensuales
- [ ] Optimizaciones continuas

---

# 8️⃣ Recursos Necesarios

## 👥 Equipo de Proyecto

| Rol | Dedicación | Responsabilidad |
|-----|-----------|-----------------|
| **Product Manager** | 100% | Liderazgo, roadmap, priorización |
| **Desarrollador Backend** | 100% | API, base de datos, lógica negocio |
| **Desarrollador Frontend** | 100% | Formularios, dashboards, UX |
| **QA/Tester** | 50% | Testing, validación, calidad |
| **UX/UI Designer** | 25% | Diseño de formularios e interfaces |
| **DevOps** | 25% | Infraestructura, CI/CD, monitoreo |
| **Capacitador** | 50% (temporal) | Training, documentación de usuario |

### � Recursos Requeridos
- **Desarrollo:** 6 meses x equipo
- **Infraestructura:** Servidor, BD, almacenamiento
- **Licencias:** Herramientas de desarrollo, monitoreo
- **Capacitación:** Material, sesiones, soporte

---

# 8️⃣ Riesgos y Mitigación

## ⚠️ Riesgos Identificados

| Riesgo | Probabilidad | Impacto | Mitigación |
|--------|--------------|---------|------------|
| **Resistencia al cambio** | Alta | Medio | Capacitación, comunicación clara de beneficios |
| **Formularios muy largos** | Media | Alto | Validar con usuarios, simplificar campos opcionales |
| **SLA muy agresivos** | Media | Alto | Empezar conservador, ajustar con datos reales |
| **Falta de adopción** | Media | Alto | Hacer obligatorio, soporte 24/7 inicial |
| **Datos históricos incompletos** | Alta | Bajo | Migrar solo lo crítico, documentar gaps |
| **Integración con sistemas legacy** | Media | Medio | APIs, middleware, plan B manual |

---

# 🎯 Conclusión

## Sistema ISSEG: Transformando la Gestión de TI

### ✅ **Lo que Logramos:**

1. **Estandarización** → 4 formularios claros y completos
2. **Automatización** → SLA automáticos, notificaciones, IDs
3. **Trazabilidad** → Auditoría completa, historial permanente
4. **Eficiencia** → Reducción 70% en tiempos de resolución
5. **Transparencia** → Visibilidad completa para todos

### 🚀 **Próximos Pasos Inmediatos:**

1. **Aprobación** de la propuesta
2. **Asignación** de equipo y recursos
3. **Inicio** de desarrollo (Fase 1)
4. **Piloto** en 2 meses

---

# 📞 Contacto y Preguntas

## ¿Preguntas?

**Documentación Completa:**
- 📄 Formularios en `/formularios/*.md`
- 📊 Diagramas de flujo en `/documentacion/*.md`
- 🗄️ Esquema de BD en `/documentacion/05-esquema-base-datos.md`


**¡Gracias por su atención!**

---

# ANEXOS

---

# ANEXO A: Ejemplo Formulario A Completo

## Ejemplo Real: Sistema de Gestión de Inventario

```
markdown
═══════════════════════════════════════════════════════
FORMULARIO A: SOLICITUD DE SISTEMA NUEVO
═══════════════════════════════════════════════════════

ID SOLICITUD: SN-2026-0042 (auto-generado)
FECHA: 05/02/2026 10:45 AM

---

1️⃣ INFORMACIÓN GENERAL

Nombre Completo: María Fernández López
Cargo: Jefa de Almacén
Área: Logística
Email: mfernandez@empresa.com
Teléfono: 555-1234

---

2️⃣ DESCRIPCIÓN DEL SISTEMA

Nombre del Sistema: Sistema de Gestión de Inventario (SGI)
Tipo: Web Application

Descripción General:
Sistema web para controlar entradas, salidas y stock de
materiales en almacén. Debe permitir registro en tiempo
real, generación de reportes y alertas de stock mínimo.

Problema que Resuelve:
Actualmente llevamos inventario en Excel, lo que genera:
- Errores de conteo manual
- No hay visibilidad en tiempo real
- Pérdida de materiales por falta de control
- Reportes manuales que toman 2 días

---

3️⃣ JUSTIFICACIÓN Y ALCANCE

Justificación:
El inventario actual tiene pérdidas estimadas de $50K/año
por errores de conteo y materiales vencidos. Un sistema
automatizado reduciría errores en 90% y permitiría mejor
planificación de compras.

Beneficios Esperados:
☑ Ahorro de tiempo
☑ Reducción de errores
☑ Automatización de procesos
☑ Reducción de costos
☐ Mejora servicio al cliente
☐ Cumplimiento normativo

Usuarios Estimados: 15 usuarios
Prioridad: ALTA
Criticidad: Esencial

Áreas Involucradas:
☑ Logística (principal)
☑ Compras
☑ Finanzas
☐ Ventas
☐ RH

---

4️⃣ ALCANCE PRELIMINAR

Funcionalidades Principales:
- Registro de entradas (compras, devoluciones)
- Registro de salidas (ventas, requisiciones)
- Control de stock en tiempo real
- Alertas automáticas de stock mínimo
- Generación de reportes (Excel, PDF)
- Gestión de ubicaciones en almacén
- Trazabilidad de lotes y fechas de vencimiento

Integraciones Necesarias:
- Sistema de compras (SAP)
- Sistema contable (para valorización)
- Email (notificaciones)

Plataforma: Web (navegador)
Acceso: Interno (red empresarial)

---

5️⃣ RECURSOS Y TIMELINE

Fecha Límite: 30/06/2026 (cierre fiscal Q2)
Recursos Humanos: 1 usuario tiempo completo para levantamiento

---

6️⃣ DOCUMENTACIÓN ADICIONAL

Archivos Adjuntos:
- proceso_actual_inventario.pdf (2.3 MB)
- layout_almacen.jpg (1.1 MB)
- reporte_perdidas_2025.xlsx (850 KB)

Comentarios Adicionales:
Es crítico tener el sistema operativo antes del cierre
fiscal de Q2. Actualmente tenemos auditoría pendiente
y esto nos ayudaría a demostrar control.

---

7️⃣ APROBACIONES

☑ Confirmo que mi Jefe Directo está de acuerdo
Nombre Jefe: Roberto Sánchez (Director Logística)
Email Jefe: rsanchez@empresa.com

═══════════════════════════════════════════════════════
ENVIADO: 05/02/2026 10:47 AM
ESTADO: Pendiente de Revisión ISSEG
═══════════════════════════════════════════════════════
```

---

# ANEXO B: Glosario de Términos

| Término | Definición |
|---------|------------|
| **SLA** | Service Level Agreement - Acuerdo de nivel de servicio (tiempos garantizados) |
| **ISSEG** | Área de Sistemas - Responsable de gestión de sistemas |
| **PM** | Product Manager - Responsable de producto/proyecto |
| **RF** | Requerimiento Funcional - Qué debe hacer el sistema |
| **RNF** | Requerimiento No Funcional - Cómo debe funcionar (rendimiento, seguridad, etc.) |
| **RBAC** | Role-Based Access Control - Control de acceso basado en roles |
| **Uptime** | Tiempo que un sistema está disponible/funcionando |
| **Downtime** | Tiempo que un sistema está caído/no disponible |
| **KPI** | Key Performance Indicator - Indicador clave de desempeño |
| **RTO** | Recovery Time Objective - Tiempo objetivo de recuperación |
| **Workaround** | Solución temporal mientras se resuelve el problema definitivo |
| **MVP** | Minimum Viable Product - Producto mínimo viable |
| **QA** | Quality Assurance - Aseguramiento de calidad |
| **CI/CD** | Continuous Integration/Continuous Deployment - Integración y despliegue continuo |

---

# ANEXO C: Contactos Útiles

## Equipo ISSEG

| Nombre | Rol | Email | Ext |
|--------|-----|-------|-----|
| TBD | Director ISSEG | director.isseg@empresa.com | 1000 |
| TBD | Product Manager | pm.isseg@empresa.com | 1100 |
| TBD | Líder Técnico | tech.lead@empresa.com | 1200 |
| TBD | Soporte Usuario | soporte@empresa.com | 1500 |

## Soporte por Tipo de Consulta

- **¿Qué formulario usar?** → soporte@empresa.com
- **Problemas técnicos** → tech.lead@empresa.com
- **Solicitudes urgentes** → director.isseg@empresa.com
- **Capacitación** → training@empresa.com

---

**FIN DE LA PRESENTACIÓN**
