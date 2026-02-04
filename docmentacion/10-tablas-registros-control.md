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

```sql
CREATE TABLE Sistemas (
    ID_Sistema INT PRIMARY KEY AUTO_INCREMENT,
    Nombre_Sistema VARCHAR(100) NOT NULL UNIQUE,
    Descripcion_Sistema TEXT,
    Área_Responsable INT NOT NULL,
    Usuario_Creador INT NOT NULL,
    Fecha_Creacion DATETIME DEFAULT CURRENT_TIMESTAMP,
    
    -- Estados posibles: Planeación, En Desarrollo, En Pruebas, En Producción, Mantenimiento, Descontinuado
    Estado_Actual ENUM('Planeación','En Desarrollo','En Pruebas','En Producción','Mantenimiento','Descontinuado') DEFAULT 'Planeación',
    
    -- Control de Versiones
    Versión_Actual VARCHAR(10) DEFAULT '1.0.0',
    Última_Actualización DATETIME,
    
    -- Justificación inicial
    Justificación_Sistema TEXT,
    Alcance_Sistema TEXT,
    Beneficios_Esperados TEXT,
    
    -- Fechas hito
    Fecha_Inicio_Desarrollo DATETIME,
    Fecha_Fin_Desarrollo DATETIME,
    Fecha_Go_Live DATETIME,
    
    -- Equipo asignado
    Desarrollador_Principal INT,
    Product_Manager_Asignado INT,
    Arquitecto_Asignado INT,
    
    -- Disponibilidad
    Tiempo_Total_Actividad INT DEFAULT 0, -- en horas
    Uptime_Porcentaje DECIMAL(5,2) DEFAULT 0.00,
    
    -- Contacto
    Email_Responsable VARCHAR(100),
    Teléfono_Responsable VARCHAR(20),
    
    Activo BOOLEAN DEFAULT 1,
    
    FOREIGN KEY (Área_Responsable) REFERENCES Áreas(ID_Área),
    FOREIGN KEY (Usuario_Creador) REFERENCES Usuarios(ID_Usuario),
    FOREIGN KEY (Desarrollador_Principal) REFERENCES Usuarios(ID_Usuario),
    FOREIGN KEY (Product_Manager_Asignado) REFERENCES Usuarios(ID_Usuario),
    
    INDEX idx_area (Área_Responsable),
    INDEX idx_estado (Estado_Actual),
    INDEX idx_fecha (Fecha_Creacion)
);
```

---

## 2. Tabla: Historial_Cambios (Control de Versiones)

**Propósito:** Registrar todas las modificaciones realizadas a sistemas existentes

```sql
CREATE TABLE Historial_Cambios (
    ID_Cambio INT PRIMARY KEY AUTO_INCREMENT,
    ID_Sistema INT NOT NULL,
    Número_Versión VARCHAR(10) NOT NULL,
    
    -- Descripción del cambio
    Descripción_Cambio TEXT NOT NULL,
    Tipo_Cambio ENUM('Bugfix','Feature','Mejora','Seguridad','Performance') NOT NULL,
    
    -- Módulos afectados
    Módulos_Afectados VARCHAR(255),
    Impacto_Estimado ENUM('Bajo','Medio','Alto','Crítico') DEFAULT 'Bajo',
    
    -- Responsable
    Usuario_Solicitante INT NOT NULL,
    Usuario_Desarrollador INT NOT NULL,
    Desarrollador_Responsable INT,
    
    -- Fechas y estado
    Fecha_Solicitud DATETIME DEFAULT CURRENT_TIMESTAMP,
    Fecha_Inicio_Desarrollo DATETIME,
    Fecha_Fin_Desarrollo DATETIME,
    Fecha_Implementación DATETIME,
    
    Estado_Cambio ENUM('Solicitado','En Desarrollo','En Pruebas','Aprobado','Implementado','Rechazado') DEFAULT 'Solicitado',
    
    -- Notas
    Notas_Implementación TEXT,
    Motivo_Rechazo VARCHAR(255),
    
    -- Rollback
    Permite_Rollback BOOLEAN DEFAULT 1,
    Instrucciones_Rollback TEXT,
    
    -- Auditoría
    Aprobado_Por INT,
    Fecha_Aprobación DATETIME,
    
    FOREIGN KEY (ID_Sistema) REFERENCES Sistemas(ID_Sistema),
    FOREIGN KEY (Usuario_Solicitante) REFERENCES Usuarios(ID_Usuario),
    FOREIGN KEY (Usuario_Desarrollador) REFERENCES Usuarios(ID_Usuario),
    FOREIGN KEY (Desarrollador_Responsable) REFERENCES Usuarios(ID_Usuario),
    FOREIGN KEY (Aprobado_Por) REFERENCES Usuarios(ID_Usuario),
    
    INDEX idx_sistema (ID_Sistema),
    INDEX idx_estado (Estado_Cambio),
    INDEX idx_fecha (Fecha_Solicitud),
    INDEX idx_version (Número_Versión)
);
```

---

## 3. Tabla: Problemas_Reportados (Incidencias)

**Propósito:** Registrar todos los problemas/incidencias reportados en sistemas

```sql
CREATE TABLE Problemas_Reportados (
    ID_Incidencia INT PRIMARY KEY AUTO_INCREMENT,
    ID_Sistema INT NOT NULL,
    
    -- Información del reporte
    Usuario_Reportante INT NOT NULL,
    Fecha_Reporte DATETIME DEFAULT CURRENT_TIMESTAMP,
    Descripción_Problema TEXT NOT NULL,
    
    -- Severidad
    Urgencia ENUM('Crítica','Alta','Media','Baja') DEFAULT 'Media',
    
    -- SLA (Acuerdo de Nivel de Servicio)
    SLA_Tiempo_Respuesta INT, -- en minutos según urgencia
    Fecha_Límite_Respuesta DATETIME,
    Fecha_Límite_Resolución DATETIME,
    
    -- Detalles del problema
    Módulo_Afectado VARCHAR(100),
    Funcionalidad_Afectada VARCHAR(255),
    Usuarios_Impactados INT DEFAULT 1,
    Pasos_Para_Reproducir TEXT,
    
    -- Asignación
    Responsable_Asignado INT,
    Fecha_Asignación DATETIME,
    
    -- Resolución
    Solución_Implementada TEXT,
    Causa_Raíz VARCHAR(255),
    
    -- Estados posibles
    Estado_Actual ENUM('Abierto','En Investigación','Identificada Causa','Solución En Progreso','Solución Implementada','Cerrado','Reabierto') DEFAULT 'Abierto',
    
    Fecha_Resolución DATETIME,
    
    -- Tiempos
    Tiempo_Respuesta INT, -- en minutos (real)
    Tiempo_Resolución INT, -- en minutos (real)
    Tiempo_SLA_Respuesta_OK BOOLEAN,
    Tiempo_SLA_Resolución_OK BOOLEAN,
    
    -- Seguimiento
    Fecha_Cierre DATETIME,
    Usuario_Cierre INT,
    Feedback_Usuario TEXT,
    Satisfacción ENUM('Muy Insatisfecho','Insatisfecho','Neutral','Satisfecho','Muy Satisfecho'),
    
    FOREIGN KEY (ID_Sistema) REFERENCES Sistemas(ID_Sistema),
    FOREIGN KEY (Usuario_Reportante) REFERENCES Usuarios(ID_Usuario),
    FOREIGN KEY (Responsable_Asignado) REFERENCES Usuarios(ID_Usuario),
    FOREIGN KEY (Usuario_Cierre) REFERENCES Usuarios(ID_Usuario),
    
    INDEX idx_sistema (ID_Sistema),
    INDEX idx_estado (Estado_Actual),
    INDEX idx_urgencia (Urgencia),
    INDEX idx_fecha (Fecha_Reporte),
    INDEX idx_sla (Tiempo_SLA_Respuesta_OK, Tiempo_SLA_Resolución_OK)
);
```

---

## 4. Tabla: Control_Incidencias (Seguimiento Temporal)

**Propósito:** Registrar el timeline y tiempos de respuesta de cada incidencia

```sql
CREATE TABLE Control_Incidencias (
    ID_Control INT PRIMARY KEY AUTO_INCREMENT,
    ID_Incidencia INT NOT NULL UNIQUE,
    
    -- Tiempos iniciales
    Fecha_Hora_Reporte DATETIME NOT NULL,
    Fecha_Hora_Asignación DATETIME,
    Fecha_Hora_Primera_Respuesta DATETIME,
    Fecha_Hora_Inicio_Resolución DATETIME,
    Fecha_Hora_Resolución DATETIME,
    Fecha_Hora_Cierre DATETIME,
    
    -- Estados y transiciones
    Estado_00_Abierto BOOLEAN DEFAULT 1,
    Estado_01_Investigación BOOLEAN DEFAULT 0,
    Estado_02_Causa_Identificada BOOLEAN DEFAULT 0,
    Estado_03_Solución_En_Progreso BOOLEAN DEFAULT 0,
    Estado_04_Solución_Implementada BOOLEAN DEFAULT 0,
    Estado_05_Cerrado BOOLEAN DEFAULT 0,
    
    -- Tiempos acumulados (en minutos)
    Minutos_Hasta_Asignación INT DEFAULT 0,
    Minutos_Hasta_Respuesta INT DEFAULT 0,
    Minutos_Hasta_Resolución INT DEFAULT 0,
    Minutos_Hasta_Cierre INT DEFAULT 0,
    
    -- Indicadores
    Cumplió_SLA_Respuesta BOOLEAN DEFAULT 0,
    Cumplió_SLA_Resolución BOOLEAN DEFAULT 0,
    Fue_Reabierto BOOLEAN DEFAULT 0,
    Número_Reaperturas INT DEFAULT 0,
    
    -- Notas
    Notas_Seguimiento TEXT,
    
    FOREIGN KEY (ID_Incidencia) REFERENCES Problemas_Reportados(ID_Incidencia),
    
    INDEX idx_incidencia (ID_Incidencia),
    INDEX idx_sla (Cumplió_SLA_Respuesta, Cumplió_SLA_Resolución)
);
```

---

## 5. Tabla: Uptime_Sistema (Disponibilidad)

**Propósito:** Registrar el tiempo de actividad e inactividad de cada sistema

```sql
CREATE TABLE Uptime_Sistema (
    ID_Uptime INT PRIMARY KEY AUTO_INCREMENT,
    ID_Sistema INT NOT NULL,
    
    -- Período
    Fecha_Inicio DATE NOT NULL,
    Fecha_Fin DATE NOT NULL,
    
    -- Disponibilidad
    Horas_Disponibles DECIMAL(10,2),
    Horas_No_Disponibles DECIMAL(10,2),
    Horas_Mantenimiento DECIMAL(10,2),
    
    -- Cálculos
    Uptime_Porcentaje DECIMAL(5,2),
    
    -- Estados
    Estado ENUM('Normal','Degradado','Caído','Mantenimiento') DEFAULT 'Normal',
    
    -- Incidentes que afectaron uptime
    Número_Incidentes_Afectadores INT DEFAULT 0,
    ID_Incidencias_Afectadoras VARCHAR(255),
    
    -- Notas
    Observaciones TEXT,
    
    FOREIGN KEY (ID_Sistema) REFERENCES Sistemas(ID_Sistema),
    
    INDEX idx_sistema (ID_Sistema),
    INDEX idx_fecha (Fecha_Inicio, Fecha_Fin),
    INDEX idx_uptime (Uptime_Porcentaje)
);
```

---

## 6. Tabla: Audit_Sistemas_Nuevos

**Propósito:** Auditoría completa de creación de nuevos sistemas

```sql
CREATE TABLE Audit_Sistemas_Nuevos (
    ID_Audit INT PRIMARY KEY AUTO_INCREMENT,
    ID_Sistema INT NOT NULL,
    
    -- Solicitud
    Usuario_Solicitante INT NOT NULL,
    Fecha_Solicitud DATETIME DEFAULT CURRENT_TIMESTAMP,
    
    -- Justificación
    Justificación_Sistema TEXT,
    Alcance TEXT,
    Beneficios TEXT,
    
    -- Revisión ISSEG
    Revisado_Por INT,
    Fecha_Revisión DATETIME,
    Estado_Revisión ENUM('Aprobado','Rechazado','Pendiente') DEFAULT 'Pendiente',
    Motivo_Rechazo TEXT,
    
    -- Asignación de equipo
    Desarrollador_Asignado INT,
    Product_Manager_Asignado INT,
    Arquitecto_Asignado INT,
    Fecha_Asignación_Equipo DATETIME,
    
    -- Requerimientos
    Formulario_C_Completo BOOLEAN DEFAULT 0,
    Fecha_Requerimientos_Completos DATETIME,
    
    -- Timeline
    Fecha_Inicio_Estimada DATE,
    Fecha_Fin_Estimada DATE,
    Fecha_Go_Live_Estimada DATE,
    
    -- Seguimiento real
    Fecha_Inicio_Real DATETIME,
    Fecha_Fin_Real DATETIME,
    Fecha_Go_Live_Real DATETIME,
    
    -- Desvíos
    Desvío_Estimación_Días INT,
    
    FOREIGN KEY (ID_Sistema) REFERENCES Sistemas(ID_Sistema),
    FOREIGN KEY (Usuario_Solicitante) REFERENCES Usuarios(ID_Usuario),
    FOREIGN KEY (Revisado_Por) REFERENCES Usuarios(ID_Usuario),
    FOREIGN KEY (Desarrollador_Asignado) REFERENCES Usuarios(ID_Usuario),
    FOREIGN KEY (Product_Manager_Asignado) REFERENCES Usuarios(ID_Usuario),
    
    INDEX idx_sistema (ID_Sistema),
    INDEX idx_estado (Estado_Revisión),
    INDEX idx_fecha (Fecha_Solicitud)
);
```

---

## 7. Tabla: Audit_Modificaciones

**Propósito:** Auditoría detallada de todas las modificaciones realizadas

```sql
CREATE TABLE Audit_Modificaciones (
    ID_Audit INT PRIMARY KEY AUTO_INCREMENT,
    ID_Cambio INT NOT NULL,
    
    -- Qué cambió
    ID_Sistema INT NOT NULL,
    Versión_Anterior VARCHAR(10),
    Versión_Nueva VARCHAR(10),
    
    -- Solicitud
    Usuario_Solicitante INT NOT NULL,
    Motivo_Cambio TEXT,
    Descripción_Cambio TEXT,
    
    -- Estimaciones
    Impacto_Estimado ENUM('Bajo','Medio','Alto','Crítico') DEFAULT 'Bajo',
    Impacto_Real ENUM('Bajo','Medio','Alto','Crítico'),
    
    -- Revisión y aprobación
    Revisado_Por INT,
    Fecha_Revisión DATETIME,
    Estado_Revisión ENUM('Aprobado','Rechazado','Pendiente') DEFAULT 'Pendiente',
    
    -- Ejecución
    Ejecutado_Por INT,
    Fecha_Inicio_Ejecución DATETIME,
    Fecha_Fin_Ejecución DATETIME,
    
    -- Testing post-cambio
    Testing_Realizado BOOLEAN DEFAULT 0,
    Responsable_Testing INT,
    Fecha_Testing DATETIME,
    Resultado_Testing ENUM('Pasó','Falló','Parcial'),
    
    -- Rollback
    Se_Realizó_Rollback BOOLEAN DEFAULT 0,
    Fecha_Rollback DATETIME,
    Motivo_Rollback TEXT,
    
    -- Usuarios impactados
    Número_Usuarios_Impactados INT,
    Notificación_Enviada BOOLEAN DEFAULT 0,
    Fecha_Notificación DATETIME,
    
    FOREIGN KEY (ID_Cambio) REFERENCES Historial_Cambios(ID_Cambio),
    FOREIGN KEY (ID_Sistema) REFERENCES Sistemas(ID_Sistema),
    FOREIGN KEY (Usuario_Solicitante) REFERENCES Usuarios(ID_Usuario),
    FOREIGN KEY (Revisado_Por) REFERENCES Usuarios(ID_Usuario),
    FOREIGN KEY (Ejecutado_Por) REFERENCES Usuarios(ID_Usuario),
    FOREIGN KEY (Responsable_Testing) REFERENCES Usuarios(ID_Usuario),
    
    INDEX idx_cambio (ID_Cambio),
    INDEX idx_sistema (ID_Sistema),
    INDEX idx_fecha (Fecha_Revisión)
);
```

---

## 8. Tabla: SLA_Definiciones

**Propósito:** Definir los SLA por tipo de incidencia y urgencia

```sql
CREATE TABLE SLA_Definiciones (
    ID_SLA INT PRIMARY KEY AUTO_INCREMENT,
    
    -- Criterio
    Urgencia ENUM('Crítica','Alta','Media','Baja') NOT NULL UNIQUE,
    Tipo_Sistema ENUM('Producción','Testing','Desarrollo','Infraestructura') DEFAULT 'Producción',
    
    -- Tiempos SLA (en minutos)
    Tiempo_Respuesta_Minutos INT NOT NULL,
    Tiempo_Resolución_Minutos INT NOT NULL,
    
    -- Escalation
    Escalation_Respuesta_Minutos INT,
    Escalation_Resolución_Minutos INT,
    Manager_Escalation_Respuesta INT,
    Manager_Escalation_Resolución INT,
    
    -- Descripción
    Descripción TEXT,
    Ejemplos TEXT,
    
    -- Activo
    Activo BOOLEAN DEFAULT 1,
    Fecha_Actualización DATETIME DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    
    FOREIGN KEY (Manager_Escalation_Respuesta) REFERENCES Usuarios(ID_Usuario),
    FOREIGN KEY (Manager_Escalation_Resolución) REFERENCES Usuarios(ID_Usuario)
);
```

---

## 9. Tabla: Alertas_SLA

**Propósito:** Registrar violaciones y alertas de SLA

```sql
CREATE TABLE Alertas_SLA (
    ID_Alerta INT PRIMARY KEY AUTO_INCREMENT,
    ID_Incidencia INT NOT NULL,
    
    -- Tipo de alerta
    Tipo_Alerta ENUM('Alerta Respuesta','Crítica Respuesta','Alerta Resolución','Crítica Resolución') NOT NULL,
    
    -- Tiempos
    Fecha_Alerta DATETIME DEFAULT CURRENT_TIMESTAMP,
    Minutos_Faltantes INT,
    
    -- Notificación
    Notificación_Enviada BOOLEAN DEFAULT 1,
    Fecha_Notificación DATETIME,
    Notificado_A INT,
    
    -- Escalation
    Escalation_Realizado BOOLEAN DEFAULT 0,
    Fecha_Escalation DATETIME,
    Escalado_A INT,
    
    -- Resolución de alerta
    Resuelta BOOLEAN DEFAULT 0,
    Fecha_Resolución DATETIME,
    Notas TEXT,
    
    FOREIGN KEY (ID_Incidencia) REFERENCES Problemas_Reportados(ID_Incidencia),
    FOREIGN KEY (Notificado_A) REFERENCES Usuarios(ID_Usuario),
    FOREIGN KEY (Escalado_A) REFERENCES Usuarios(ID_Usuario),
    
    INDEX idx_incidencia (ID_Incidencia),
    INDEX idx_tipo (Tipo_Alerta),
    INDEX idx_fecha (Fecha_Alerta)
);
```

---

## Queries Útiles para Reportes

### 1. Sistemas Creados en el Período

```sql
SELECT 
    s.ID_Sistema,
    s.Nombre_Sistema,
    a.Nombre_Área,
    u.Nombre as Usuario_Creador,
    s.Fecha_Creacion,
    s.Estado_Actual,
    asn.Fecha_Asignación_Equipo
FROM Sistemas s
LEFT JOIN Áreas a ON s.Área_Responsable = a.ID_Área
LEFT JOIN Usuarios u ON s.Usuario_Creador = u.ID_Usuario
LEFT JOIN Audit_Sistemas_Nuevos asn ON s.ID_Sistema = asn.ID_Sistema
WHERE s.Fecha_Creacion BETWEEN @FechaInicio AND @FechaFin
ORDER BY s.Fecha_Creacion DESC;
```

### 2. Modificaciones Realizadas en el Período

```sql
SELECT 
    hc.ID_Cambio,
    s.Nombre_Sistema,
    hc.Número_Versión,
    hc.Tipo_Cambio,
    hc.Descripción_Cambio,
    u1.Nombre as Solicitante,
    u2.Nombre as Desarrollador,
    hc.Fecha_Solicitud,
    hc.Fecha_Implementación,
    hc.Estado_Cambio
FROM Historial_Cambios hc
JOIN Sistemas s ON hc.ID_Sistema = s.ID_Sistema
LEFT JOIN Usuarios u1 ON hc.Usuario_Solicitante = u1.ID_Usuario
LEFT JOIN Usuarios u2 ON hc.Desarrollador_Responsable = u2.ID_Usuario
WHERE hc.Fecha_Solicitud BETWEEN @FechaInicio AND @FechaFin
ORDER BY hc.Fecha_Solicitud DESC;
```

### 3. Incidencias Abiertas por Urgencia

```sql
SELECT 
    pr.ID_Incidencia,
    pr.Urgencia,
    s.Nombre_Sistema,
    pr.Descripción_Problema,
    pr.Usuario_Reportante,
    pr.Responsable_Asignado,
    pr.Fecha_Reporte,
    pr.Fecha_Límite_Resolución,
    TIMESTAMPDIFF(MINUTE, pr.Fecha_Reporte, NOW()) as Minutos_Abierto,
    CASE 
        WHEN TIMESTAMPDIFF(MINUTE, pr.Fecha_Reporte, NOW()) > ci.SLA_Tiempo_Respuesta 
        THEN 'SLA VIOLADO' 
        ELSE 'En tiempo' 
    END as Estado_SLA
FROM Problemas_Reportados pr
JOIN Sistemas s ON pr.ID_Sistema = s.ID_Sistema
JOIN Control_Incidencias ci ON pr.ID_Incidencia = ci.ID_Incidencia
WHERE pr.Estado_Actual != 'Cerrado'
ORDER BY pr.Urgencia DESC, pr.Fecha_Reporte ASC;
```

### 4. Uptime por Sistema en el Mes

```sql
SELECT 
    s.Nombre_Sistema,
    u.Fecha_Inicio,
    u.Fecha_Fin,
    u.Uptime_Porcentaje,
    u.Horas_Disponibles,
    u.Horas_No_Disponibles,
    u.Horas_Mantenimiento,
    u.Número_Incidentes_Afectadores
FROM Uptime_Sistema u
JOIN Sistemas s ON u.ID_Sistema = s.ID_Sistema
WHERE YEAR(u.Fecha_Inicio) = YEAR(CURDATE()) 
  AND MONTH(u.Fecha_Inicio) = MONTH(CURDATE())
ORDER BY u.Uptime_Porcentaje ASC;
```

### 5. Desempeño de SLA por Mes

```sql
SELECT 
    MONTH(pr.Fecha_Reporte) as Mes,
    pr.Urgencia,
    COUNT(*) as Total_Incidencias,
    SUM(CASE WHEN pr.Tiempo_SLA_Respuesta_OK THEN 1 ELSE 0 END) as Respuesta_OK,
    SUM(CASE WHEN pr.Tiempo_SLA_Resolución_OK THEN 1 ELSE 0 END) as Resolución_OK,
    ROUND(100.0 * SUM(CASE WHEN pr.Tiempo_SLA_Respuesta_OK THEN 1 ELSE 0 END) / COUNT(*), 2) as %_Respuesta_OK,
    ROUND(100.0 * SUM(CASE WHEN pr.Tiempo_SLA_Resolución_OK THEN 1 ELSE 0 END) / COUNT(*), 2) as %_Resolución_OK
FROM Problemas_Reportados pr
WHERE pr.Fecha_Reporte >= DATE_SUB(NOW(), INTERVAL 3 MONTH)
GROUP BY MONTH(pr.Fecha_Reporte), pr.Urgencia
ORDER BY Mes DESC, pr.Urgencia;
```

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
