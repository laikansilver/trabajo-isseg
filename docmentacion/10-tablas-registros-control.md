# Tablas de Registros y Control - Sistema Gestión de Tickets

## Descripción General

Este documento especifica las tablas de la base de datos necesarias para registrar y controlar:
- ✅ Sistemas nuevos creados
- ✅ Modificaciones y control de versiones
- ✅ Problemas reportados (urgencia, tiempo de respuesta, soluciones)
- ✅ Tiempo de actividad y uptime de sistemas
- ✅ Auditoría completa de cambios

---

## 1. Tabla: Sistemas (Sistema Nuevo)

**Propósito:** Registro maestro de todos los sistemas en la organización

---

## 2. Tabla: Historial_Cambios (Control de Versiones)

**Propósito:** Registrar todas las modificaciones realizadas a sistemas existentes

---

## 3. Tabla: Problemas_Reportados (Incidencias)

**Propósito:** Registrar todos los problemas/incidencias reportados en sistemas

---

## 4. Tabla: Control_Incidencias (Seguimiento Temporal)

**Propósito:** Registrar el timeline y tiempos de respuesta de cada incidencia

---

## 5. Tabla: Uptime_Sistema (Disponibilidad)

**Propósito:** Registrar el tiempo de actividad e inactividad de cada sistema

---

## 6. Tabla: Audit_Sistemas_Nuevos

**Propósito:** Auditoría completa de creación de nuevos sistemas

---

## 7. Tabla: Audit_Modificaciones

**Propósito:** Auditoría detallada de todas las modificaciones realizadas

---

## 8. Tabla: SLA_Definiciones

**Propósito:** Definir los SLA por tipo de incidencia y urgencia

---

## 9. Tabla: Alertas_SLA

**Propósito:** Registrar violaciones y alertas de SLA

---

## Queries Útiles para Reportes

### 1. Sistemas Creados en el Período

### 2. Modificaciones Realizadas en el Período

### 3. Incidencias Abiertas por Urgencia

### 4. Uptime por Sistema en el Mes

### 5. Desempeño de SLA por Mes

---

## Resumen de Tablas Creadas

| Tabla | Propósito | Registros |
|-------|-----------|-----------|
| **Sistemas** | Mastro de sistemas | Uno por sistema |
| **Historial_Cambios** | Modificaciones y versiones | Uno por cambio |
| **Problemas_Reportados** | Incidencias reportadas | Uno por problema |
| **Control_Incidencias** | Timeline de incidencias | Uno por problema |
| **Uptime_Sistema** | Disponibilidad periódica | Diario/Mensual |
| **Audit_Sistemas_Nuevos** | Auditoría de nuevos | Uno por sistema nuevo |
| **Audit_Modificaciones** | Auditoría de cambios | Uno por cambio |
| **SLA_Definiciones** | Definición de SLA | Uno por urgencia/tipo |
| **Alertas_SLA** | Violaciones de SLA | Cuando ocurren |

Total: **9 tablas** para control completo de todo el ciclo de vida de sistemas y problemas.
