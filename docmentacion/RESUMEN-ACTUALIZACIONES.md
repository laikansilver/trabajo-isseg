# RESUMEN DE ACTUALIZACIONES - MAPA ÚNICO INTEGRAL Y REGISTROS

**Fecha:** 4 de febrero de 2026  
**Cambios Realizados:** Integración completa de los 3 tipos de solicitudes + registros

---

## ✅ CAMBIOS IMPLEMENTADOS

### 1. Mapa Único Integral Mejorado (Archivo: 01-diagrama-flujo-tickets.md)

**Sección 0 - COMPLETAMENTE REESCRITA:**

#### Antes:
- Solo incluía 2 opciones: Modificación + Reporte
- Sin referencia a creación de sistemas nuevos
- Sin registros en BD

#### Ahora:
- ✅ **3 Opciones Principales:**
  1. **Crear Sistema Nuevo** (con Formulario A → Formulario C → Registro en BD)
  2. **Solicitar Modificación** (con control de versiones)
  3. **Reportar Problema** (con SLA e urgencias)

- ✅ **Registros en Base de Datos Específicos:**
  - Tabla: Sistemas (para sistemas nuevos)
  - Tabla: Historial_Cambios (para modificaciones)
  - Tabla: Problemas_Reportados (para incidencias)
  - Tabla: Control_Incidencias (para tiempos SLA)
  - Tabla: Audit_Sistemas_Nuevos
  - Tabla: Audit_Modificaciones

- ✅ **Inclusión de Auditorías:**
  - Cada acción se registra en auditoría correspondiente
  - Trazabilidad completa

---

### 2. Archivo Nuevo: 10-tablas-registros-control.md

**Propósito:** Especificación técnica completa de tablas de BD

**Contenido:**

#### A. Tablas Principales (9 tablas):

1. **Sistemas** - Registro maestro
   - ID_Sistema, Nombre, Estado, Versión
   - Control de tiempo de actividad
   - Equipo asignado
   - Uptime y disponibilidad

2. **Historial_Cambios** - Control de versiones
   - Número_Versión (1.0, 1.1, 2.0, etc.)
   - Tipo_Cambio (Bugfix, Feature, Mejora, Seguridad)
   - Estado del cambio
   - Usuario responsable
   - Información de rollback

3. **Problemas_Reportados** - Incidencias
   - ID_Incidencia, Urgencia (Crítica/Alta/Media/Baja)
   - SLA_Tiempo_Respuesta (en minutos)
   - SLA_Tiempo_Resolución
   - Solución_Implementada
   - Causa_Raíz
   - Feedback del usuario
   - Tiempo real vs SLA

4. **Control_Incidencias** - Timeline temporal
   - Fecha_Hora por cada estado
   - Minutos acumulados
   - Cumplimiento de SLA
   - Reaperturas

5. **Uptime_Sistema** - Disponibilidad
   - Período (inicio-fin)
   - Horas disponibles/no disponibles
   - Porcentaje uptime
   - Incidentes que afectaron

6. **Audit_Sistemas_Nuevos** - Auditoría de creación
   - Usuario solicitante
   - Equipo asignado
   - Timeline estimado vs real
   - Desvíos

7. **Audit_Modificaciones** - Auditoría de cambios
   - Versión anterior vs nueva
   - Impacto estimado vs real
   - Testing realizado
   - Rollback realizado

8. **SLA_Definiciones** - Política de SLA
   - Urgencia → Tiempos de respuesta/resolución
   - Escalations
   - Managers de escalation

9. **Alertas_SLA** - Violaciones de SLA
   - Tipo alerta
   - Notificaciones enviadas
   - Escalations realizados

#### B. Queries SQL Listos (5 queries principales):

1. **Sistemas Creados en Período** - Reporte de nuevos sistemas
2. **Modificaciones Realizadas** - Reporte de cambios
3. **Incidencias Abiertas por Urgencia** - Estado actual de problemas
4. **Uptime por Sistema** - Disponibilidad mensual
5. **Desempeño de SLA** - Cumplimiento de acuerdos

---

## 📊 CONTROL COMPLETO AHORA INCLUYE:

### Para Sistemas Nuevos:
- ✅ Creación en tabla Sistemas
- ✅ Estado (Planeación → Desarrollo → Pruebas → Producción)
- ✅ Versión inicial (1.0)
- ✅ Equipo asignado
- ✅ Auditoría completa
- ✅ Timeline estimado vs real

### Para Modificaciones:
- ✅ Registro en Historial_Cambios
- ✅ Incremento de versión (1.0 → 1.1 → 2.0)
- ✅ Tipo de cambio registrado
- ✅ Usuario desarrollador responsable
- ✅ Impacto estimado vs real
- ✅ Testing registrado
- ✅ Rollback disponible si falla
- ✅ Auditoría de quién, qué, cuándo

### Para Problemas Reportados:
- ✅ Urgencia (Crítica/Alta/Media/Baja)
- ✅ SLA automático según urgencia
- ✅ Alertas si se incumple SLA
- ✅ Escalation automática
- ✅ Tiempo real de respuesta
- ✅ Tiempo real de resolución
- ✅ Solución implementada (texto)
- ✅ Causa raíz documentada
- ✅ Feedback del usuario
- ✅ Reaperturas permitidas y registradas

### Para Tiempo de Actividad:
- ✅ Uptime diario/mensual
- ✅ Porcentaje de disponibilidad
- ✅ Tiempo no disponible
- ✅ Tiempo mantenimiento
- ✅ Incidentes que afectaron uptime
- ✅ Historial de caídas

### Para Auditoría:
- ✅ Audit_Sistemas_Nuevos (creación)
- ✅ Audit_Modificaciones (cambios)
- ✅ Registro completo: quién, qué, cuándo
- ✅ Desvíos de estimación
- ✅ Motivos de rechazo

---

## 📁 ARCHIVOS ACTUALIZADOS

| Archivo | Cambio | Estado |
|---------|--------|--------|
| **01-diagrama-flujo-tickets.md** | Sección 0 reescrita completamente | ✅ Actualizado |
| **10-tablas-registros-control.md** | NUEVO - Especificación BD completa | ✅ Creado |
| **3. Diagrama de Proceso Principal...mmd** | Ya incluye el mapa actualizado | ✅ Consistente |

---

## 🎯 MAPEO: SOLICITUD → TABLA BD → AUDITORÍA

### CREAR SISTEMA NUEVO
```
Usuario → Formulario A → Revisión ISSEG → Asignación Equipo → Formulario C 
→ TABLA: Sistemas (ID_Sistema, Estado=Planeación, Versión=1.0)
→ TABLA: Audit_Sistemas_Nuevos (Usuario, Equipo, Timeline)
→ TABLA: Uptime_Sistema (Inicio de registro de disponibilidad)
```

### SOLICITAR MODIFICACIÓN
```
Usuario → Selecciona Sistema → Formulario B → Revisión ISSEG → Asignación Dev
→ TABLA: Historial_Cambios (Versión++, Tipo_Cambio, Estado=En Desarrollo)
→ TABLA: Audit_Modificaciones (Qué, Quién, Cuándo, Impacto)
→ TABLA: Sistemas.Última_Actualización (actualiza fecha)
```

### REPORTAR PROBLEMA
```
Usuario → Selecciona Sistema → Describe Problema → Define Urgencia 
→ Sistema Calcula SLA → Revisión ISSEG → Asignación
→ TABLA: Problemas_Reportados (Urgencia, SLA, Estado=Abierto)
→ TABLA: Control_Incidencias (Timeline, Tiempos acumulados)
→ TABLA: Alertas_SLA (Si se incumple)
→ TABLA: SLA_Definiciones (Lookup de tiempos)
```

---

## 💡 EJEMPLOS DE CONSULTAS DISPONIBLES

### Ejemplo 1: ¿Cuántos sistemas se crearon en enero?
→ Respuesta directa del archivo 10

### Ejemplo 2: ¿Qué versión tiene cada sistema?
→ Puede traerse de Sistemas + Historial_Cambios

### Ejemplo 3: ¿Incidencias sin resolver con SLA vencido?
→ Genera alertas automáticas

### Ejemplo 4: ¿Uptime del mes?
→ Para dashboard ejecutivo

---

## 🔄 FLUJO DE DATOS COMPLETO

```
USUARIO
  ↓
DASHBOARD (ve sistemas filtrados por área)
  ↓
SELECCIONA ACCIÓN (Crear/Modificar/Reportar)
  ↓
LLENA FORMULARIO (A, B o Problema)
  ↓
ISSEG REVISA (Aprueba/Rechaza)
  ↓
SI APROBADO:
  ├─ Crear Sistema → BD (Sistemas) → Auditoría (Audit_Sistemas_Nuevos)
  ├─ Modificar → BD (Historial_Cambios) → Auditoría (Audit_Modificaciones)
  └─ Reportar Problema → BD (Problemas_Reportados) → Control (Control_Incidencias)
  ↓
SEGUIMIENTO EN TIEMPO REAL:
  ├─ Estado del sistema
  ├─ Versión actual
  ├─ Uptime %
  ├─ SLA de problemas
  ├─ Alertas de incumplimiento
  └─ Auditoría completa
```

---

## ✨ NUEVAS CAPACIDADES

### 1. Control de Versiones Automático
- Cada modificación incrementa versión
- Historial completo de cambios
- Rollback documentado

### 2. SLA Automático por Urgencia
- Crítica: 1 hora respuesta, 4 horas resolución
- Alta: 4 horas respuesta, 8 horas resolución
- Media: 8 horas respuesta, 16 horas resolución
- Baja: 24 horas respuesta, 48 horas resolución

### 3. Escalation Automática
- Si se incumple SLA → Alerta
- Si sigue incumplido → Escalation a manager
- Registro de escalaciones

### 4. Uptime Tracking
- Registro diario de disponibilidad
- Cálculo automático de %
- Correlación con incidentes

### 5. Auditoría Completa
- Todo cambio registrado
- Quién lo hizo
- Cuándo lo hizo
- Por qué lo hizo
- Impacto real vs estimado

---

## 📋 CHECKLIST DE IMPLEMENTACIÓN

- [x] Mapa único integral rediseñado
- [x] 3 tipos de solicitudes completamente especificadas
- [x] 9 tablas de BD diseñadas
- [x] Registros de auditoría implementados
- [x] SLA y alertas definidas
- [x] Control de versiones especificado
- [x] Uptime tracking diseñado
- [x] 5 queries principales incluidas
- [x] Documentación técnica completa

---

## 🎓 PRÓXIMOS PASOS

1. **Crear tablas en BD** (ejecutar scripts SQL del archivo 10)
2. **Implementar validaciones** (verificar permisos antes de cada acción)
3. **Crear triggers** (para actualizar campos calculados automáticamente)
4. **Desarrollar alertas** (email cuando se incumple SLA)
5. **Implementar dashboard** (mostrar métricas en tiempo real)

---

**ESTADO:** ✅ DISEÑO COMPLETO Y LISTO PARA IMPLEMENTACIÓN
