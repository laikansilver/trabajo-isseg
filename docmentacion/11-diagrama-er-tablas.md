# Diagrama de Tablas - Estructura Completa de Base de Datos

## Relaciones Entre Tablas (ERD)

```mermaid
erDiagram
    USUARIOS ||--o{ SISTEMAS : crea
    USUARIOS ||--o{ HISTORIAL_CAMBIOS : solicita
    USUARIOS ||--o{ PROBLEMAS_REPORTADOS : reporta
    USUARIOS ||--o{ AUDIT_SISTEMAS_NUEVOS : solicita
    USUARIOS ||--o{ AUDIT_MODIFICACIONES : realiza
    
    AREAS ||--o{ SISTEMAS : contiene
    AREAS ||--o{ USUARIOS_AUTORIZADOS_AREA : asigna
    
    SISTEMAS ||--o{ HISTORIAL_CAMBIOS : tiene
    SISTEMAS ||--o{ PROBLEMAS_REPORTADOS : experimenta
    SISTEMAS ||--o{ UPTIME_SISTEMA : registra
    SISTEMAS ||--o{ AUDIT_SISTEMAS_NUEVOS : audita
    
    HISTORIAL_CAMBIOS ||--o{ AUDIT_MODIFICACIONES : audita
    
    PROBLEMAS_REPORTADOS ||--o{ CONTROL_INCIDENCIAS : tracking
    PROBLEMAS_REPORTADOS ||--o{ ALERTAS_SLA : genera
    
    SLA_DEFINICIONES ||--o{ PROBLEMAS_REPORTADOS : aplica
    
    USUARIOS_AUTORIZADOS_AREA {
        int ID_Autorización
        int ID_Usuario FK
        int ID_Área FK
        string Rol_En_Área
        boolean Puede_Solicitar_Nuevo
        boolean Puede_Solicitar_Modificación
    }

    SISTEMAS {
        int ID_Sistema PK
        string Nombre_Sistema
        int Área_Responsable FK
        int Usuario_Creador FK
        datetime Fecha_Creacion
        enum Estado_Actual
        string Versión_Actual
        int Tiempo_Total_Actividad
        decimal Uptime_Porcentaje
    }

    HISTORIAL_CAMBIOS {
        int ID_Cambio PK
        int ID_Sistema FK
        string Número_Versión
        string Descripción_Cambio
        enum Tipo_Cambio
        int Usuario_Solicitante FK
        int Usuario_Desarrollador FK
        enum Estado_Cambio
        datetime Fecha_Solicitud
        datetime Fecha_Implementación
    }

    PROBLEMAS_REPORTADOS {
        int ID_Incidencia PK
        int ID_Sistema FK
        int Usuario_Reportante FK
        enum Urgencia
        datetime Fecha_Reporte
        text Descripción_Problema
        int Tiempo_Respuesta
        int Tiempo_Resolución
        boolean Tiempo_SLA_Respuesta_OK
        boolean Tiempo_SLA_Resolución_OK
    }

    CONTROL_INCIDENCIAS {
        int ID_Control PK
        int ID_Incidencia FK
        datetime Fecha_Hora_Reporte
        datetime Fecha_Hora_Asignación
        datetime Fecha_Hora_Primera_Respuesta
        datetime Fecha_Hora_Resolución
        int Minutos_Hasta_Respuesta
        int Minutos_Hasta_Resolución
        boolean Cumplió_SLA_Respuesta
        boolean Cumplió_SLA_Resolución
    }

    UPTIME_SISTEMA {
        int ID_Uptime PK
        int ID_Sistema FK
        date Fecha_Inicio
        date Fecha_Fin
        decimal Horas_Disponibles
        decimal Horas_No_Disponibles
        decimal Uptime_Porcentaje
        int Número_Incidentes_Afectadores
    }

    AUDIT_SISTEMAS_NUEVOS {
        int ID_Audit PK
        int ID_Sistema FK
        int Usuario_Solicitante FK
        datetime Fecha_Solicitud
        text Justificación_Sistema
        int Desarrollador_Asignado FK
        int Product_Manager_Asignado FK
        enum Estado_Revisión
        datetime Fecha_Go_Live_Real
    }

    AUDIT_MODIFICACIONES {
        int ID_Audit PK
        int ID_Cambio FK
        int ID_Sistema FK
        string Versión_Anterior
        string Versión_Nueva
        int Usuario_Solicitante FK
        enum Impacto_Estimado
        enum Impacto_Real
        datetime Fecha_Revisión
        datetime Fecha_Fin_Ejecución
        boolean Se_Realizó_Rollback
    }

    SLA_DEFINICIONES {
        int ID_SLA PK
        enum Urgencia
        enum Tipo_Sistema
        int Tiempo_Respuesta_Minutos
        int Tiempo_Resolución_Minutos
        int Escalation_Respuesta_Minutos
    }

    ALERTAS_SLA {
        int ID_Alerta PK
        int ID_Incidencia FK
        enum Tipo_Alerta
        datetime Fecha_Alerta
        int Minutos_Faltantes
        boolean Notificación_Enviada
        boolean Escalation_Realizado
    }

    AREAS {
        int ID_Área PK
        string Nombre_Área
        string Descripción
        int Responsable FK
    }

    USUARIOS {
        int ID_Usuario PK
        string Email
        string Nombre_Completo
        string Contraseña_Hash
        boolean Estado_Activo
        datetime Fecha_Creacion
    }
```

---

## Tabla Resumen: Propósito y Contenido

| # | Tabla | Propósito | Registros Por | Clave Primaria |
|---|-------|-----------|---------------|---|
| 1 | **Sistemas** | Maestro de todos los sistemas | Sistema | ID_Sistema |
| 2 | **Historial_Cambios** | Control de versiones | Modificación | ID_Cambio |
| 3 | **Problemas_Reportados** | Registro de incidencias | Problema | ID_Incidencia |
| 4 | **Control_Incidencias** | Timeline temporal de SLA | Problema | ID_Control |
| 5 | **Uptime_Sistema** | Disponibilidad periódica | Sistema/Período | ID_Uptime |
| 6 | **Audit_Sistemas_Nuevos** | Auditoría de creación | Sistema nuevo | ID_Audit |
| 7 | **Audit_Modificaciones** | Auditoría de cambios | Modificación | ID_Audit |
| 8 | **SLA_Definiciones** | Políticas de SLA | Urgencia/Tipo | ID_SLA |
| 9 | **Alertas_SLA** | Violaciones de SLA | Violación | ID_Alerta |

---

## Flujo de Datos: Cómo Se Conectan

### CASO 1: CREAR SISTEMA NUEVO

```
USUARIO
  ↓
FORMULARIO A (Sistema Nuevo)
  ↓
ISSEG APRUEBA
  ↓
├─→ TABLA: Sistemas (INSERT nuevo registro)
│   └─→ ID_Sistema = auto_increment
│   └─→ Estado = 'Planeación'
│   └─→ Versión = '1.0'
│
├─→ TABLA: Audit_Sistemas_Nuevos (INSERT auditoría)
│   └─→ Usuario_Solicitante
│   └─→ Equipo_Asignado
│   └─→ Timeline_Estimado
│
└─→ TABLA: Uptime_Sistema (INSERT registro inicial)
    └─→ Fecha_Inicio = HOY
    └─→ Uptime_Porcentaje = 0 (no en producción aún)
```

---

### CASO 2: SOLICITAR MODIFICACIÓN

```
USUARIO
  ↓
ELIGE SISTEMA (filtra por área)
  ↓
FORMULARIO B (Describe cambio)
  ↓
ISSEG APRUEBA
  ↓
├─→ TABLA: Historial_Cambios (INSERT nuevo cambio)
│   └─→ ID_Sistema (FK)
│   └─→ Número_Versión++  (1.0 → 1.1 o 1.0 → 2.0)
│   └─→ Descripción_Cambio
│   └─→ Estado = 'En Desarrollo'
│
├─→ TABLA: Audit_Modificaciones (INSERT auditoría)
│   └─→ Versión_Anterior
│   └─→ Versión_Nueva
│   └─→ Impacto_Estimado vs Impacto_Real
│   └─→ Rollback posible: SÍ
│
└─→ TABLA: Sistemas (UPDATE)
    └─→ Versión_Actual = nueva versión
    └─→ Última_Actualización = HOY
```

---

### CASO 3: REPORTAR PROBLEMA

```
USUARIO
  ↓
ELIGE SISTEMA (filtra por área)
  ↓
FORMULARIO PROBLEMA
  ├─ Descripción
  ├─ Urgencia: Crítica/Alta/Media/Baja
  └─ Pasos reproducir
  ↓
ISSEG APRUEBA
  ↓
├─→ TABLA: SLA_Definiciones (LOOKUP)
│   └─→ SELECT * WHERE Urgencia = 'Crítica'
│   └─→ Tiempo_Respuesta = 60 minutos
│   └─→ Tiempo_Resolución = 240 minutos (4 horas)
│
├─→ TABLA: Problemas_Reportados (INSERT incidencia)
│   └─→ ID_Incidencia = auto_increment
│   └─→ Urgencia = 'Crítica'
│   └─→ Fecha_Límite_Respuesta = NOW() + 60 min
│   └─→ Fecha_Límite_Resolución = NOW() + 240 min
│   └─→ Estado = 'Abierto'
│
├─→ TABLA: Control_Incidencias (INSERT timeline)
│   └─→ Fecha_Hora_Reporte = NOW()
│   └─→ Tiempo_Respuesta = 0
│   └─→ Tiempo_Resolución = 0
│   └─→ Cumplió_SLA = pendiente
│
└─→ TABLA: Alertas_SLA (INSERT alerta inicial)
    └─→ Tipo_Alerta = 'Alerta Respuesta'
    └─→ Minutos_Faltantes = 60
```

**DURANTE EL PROCESO:**

```
DESARROLLADOR INICIA INVESTIGACIÓN
  ↓
TABLA: Control_Incidencias (UPDATE)
  └─→ Fecha_Hora_Primera_Respuesta = NOW()
  └─→ Minutos_Hasta_Respuesta = DATEDIFF(NOW(), Fecha_Reporte)
  └─→ ¿Cumplió SLA Respuesta? CALCULAR
  └─→ Si NO → TABLA: Alertas_SLA (INSERT CRÍTICA)

DESARROLLADOR ENCUENTRA SOLUCIÓN
  ↓
TABLA: Problemas_Reportados (UPDATE)
  └─→ Solución_Implementada = "texto de solución"
  └─→ Causa_Raíz = "causa identificada"
  └─→ Estado = 'Solución Implementada'

SOLUCIÓN IMPLEMENTADA Y PROBADA
  ↓
TABLA: Control_Incidencias (UPDATE)
  └─→ Fecha_Hora_Resolución = NOW()
  └─→ Minutos_Hasta_Resolución = DATEDIFF(NOW(), Fecha_Reporte)
  └─→ ¿Cumplió SLA Resolución? CALCULAR

CERRAR INCIDENCIA
  ↓
TABLA: Problemas_Reportados (UPDATE)
  └─→ Estado = 'Cerrado'
  └─→ Fecha_Cierre = NOW()
  └─→ Feedback_Usuario = "¿Satisfecho?"
  └─→ Satisfacción = 1-5 estrellas

TABLA: Control_Incidencias (UPDATE FINAL)
  └─→ Cumplió_SLA_Respuesta = YES/NO
  └─→ Cumplió_SLA_Resolución = YES/NO
  └─→ Número_Reaperturas = ¿Fue reabierto?
```

---

## Ejemplos de Consultas Comunes

### 1. ¿Cuál es el estado actual de cada sistema?

**Respuesta en columnas:**
- Sistema A: En Producción, v2.3.1, 99.5% uptime
- Sistema B: En Desarrollo, v1.0.0, 0% (nuevo)

---

### 2. ¿Qué modificaciones se hicieron a un sistema?

**Respuesta:**
- v2.3.1: "Bugfix - Error en reporte mensual" - 2026-02-01
- v2.3.0: "Feature - Agregar filtro por fecha" - 2026-01-20

---

### 3. ¿Incidencias sin resolver con SLA crítico?

---

### 4. ¿Desempeño de SLA del mes?

---

### 5. ¿Uptime mensual de sistema específico?

---

## Índices Críticos Creados

---

## Capacidad de Base de Datos (Estimaciones)

| Tabla | Registros Año 1 | Tamaño Estimado |
|-------|-----------------|-----------------|
| Sistemas | 50 | 50 KB |
| Historial_Cambios | 500 | 100 KB |
| Problemas_Reportados | 2000 | 200 KB |
| Control_Incidencias | 2000 | 150 KB |
| Uptime_Sistema | 1800 | 100 KB |
| Audit_Sistemas_Nuevos | 50 | 50 KB |
| Audit_Modificaciones | 500 | 100 KB |
| SLA_Definiciones | 4 | 5 KB |
| Alertas_SLA | 500 | 50 KB |
| **TOTAL** | **7,404** | **~800 KB** |

---

**Estado:** ✅ Listo para SQL execution  
**Siguiente paso:** Ejecutar scripts SQL en base de datos destino
