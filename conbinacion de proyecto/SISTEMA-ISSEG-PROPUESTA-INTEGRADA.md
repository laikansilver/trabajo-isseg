# 🚀 Sistema de Gestión de Solicitudes ISSEG
## Propuesta Integrada Completa

**Fecha:** Febrero 2026  
**Versión:** 3.0 - INTEGRADA  
**Institución:** Instituto de Seguridad Social del Estado de Guanajuato (ISSEG)  
**Período del Proyecto:** Enero - Julio 2026 (7 meses)

---

## 📑 Tabla de Contenidos

1. [Visión General](#visión-general)
2. [Los Cuatro Formularios](#los-cuatro-formularios)
3. [Procesos Integrados](#procesos-integrados)
4. [Diagramas de Arquitectura](#diagramas-de-arquitectura)
5. [Comparación Detallada](#comparación-detallada)
6. [Arquitectura Técnica](#arquitectura-técnica)
7. [Beneficios Esperados](#beneficios-esperados)
8. [Plan de Implementación](#plan-de-implementación)

---

# Visión General

## ¿Qué es el Sistema ISSEG?

Un **sistema integral de gestión de solicitudes** que centraliza, estandariza y automatiza todos los procesos relacionados con:

- ✅ Solicitudes de sistemas nuevos
- ✅ Solicitudes de modificaciones
- ✅ Levantamiento de requerimientos técnicos
- ✅ Reportes de urgencias/incidencias

## Objetivos Principales

| Objetivo | Descripción |
|----------|-------------|
| **Centralizar** | Todas las solicitudes en un solo lugar |
| **Estandarizar** | Los procesos de solicitud y aprobación |
| **Automatizar** | El seguimiento con SLA automático |
| **Auditar** | Todos los cambios y decisiones |
| **Mejorar** | Los tiempos de respuesta y resolución |

## Problemática Actual vs Solución

### ❌ ANTES (Sin Sistema)
- Solicitudes por email, llamadas, pasillos
- No hay registro centralizado
- Se pierden solicitudes
- Sin seguimiento de tiempos (SLA)
- Difícil priorizar urgencias
- Sin historial de cambios
- Aprobaciones verbales sin registro
- Falta documentación técnica

### ✅ DESPUÉS (Con Sistema)
- Formularios estandarizados y centralizados
- ID único para cada solicitud
- Toda la información capturada
- SLA automático con alertas
- Sistema inteligente de priorización
- Auditoría completa de operaciones
- Todas las decisiones registradas
- Documentación automatizada

---

# Los Cuatro Formularios

## 📋 Formulario A: Solicitud de Sistema Nuevo

**ID Asignado:** `SN-YYYY-NNNN`  
**Estado:** Requiere Aprobación (ISSEG)  

### ¿Cuándo se usa?
Cuando se necesita crear un **sistema completamente nuevo** que no existe en la organización.

### Flujo del Proceso

```
1. Usuario llena Formulario A
   ↓
2. ISSEG evalúa viabilidad
   ├─ Presupuesto
   ├─ Recursos disponibles
   └─ Factibilidad técnica
   ↓
3. Decisión de ISSEG
   ├─ ✅ Aprobado → Asigna PM + Equipo → Pasa a Form C
   └─ ❌ Rechazado → Notifica motivos → FIN
```

### Campos Principales (11 campos)

1. Información General (Quién, cuándo, contacto)
2. Nombre sugerido para el sistema
3. Descripción/Justificación
4. Beneficios esperados
5. Alcance preliminar (funcionalidades)
6. Plataforma propuesta
7. Timeline y deadline estimado
8. Recursos disponibles
9. Documentación de apoyo
10. Presupuesto estimado
11. Riesgos identificados

### Casos de Uso Típicos

- 💼 Portal de Autoservicio para empleados
- 🎫 Sistema de Ticketing (gestión de solicitudes)
- 📱 Aplicación Móvil para afiliados
- 📦 Sistema de Gestión de Inventario
- 👥 Sistema de Control de Recursos Humanos

---

## 🔧 Formulario B: Solicitud de Modificación

**ID Asignado:** `MOD-YYYY-NNNN`  
**Estado:** Requiere Aprobación (ISSEG)  

### ¿Cuándo se usa?
Cuando se necesita **cambiar, mejorar o corregir** un sistema existente que ya está en operación.

### Tipos de Cambios (Clasificación de Mantenimiento)

| Tipo | Descripción | Ejemplo |
|------|-------------|---------|
| 🐛 **Correctivo** | Resolver errores o fallas | "El sistema falla al generar reportes en Excel" |
| ✨ **Perfectivo** | Mejorar rendimiento/UX | "Agregar búsqueda avanzada al catálogo" |
| 🔄 **Adaptativo** | Adaptarse a nuevas regulaciones | "Implementar nuevos cálculos de ley financiera" |
| 🔗 **Integrativo** | Integrar con otros sistemas | "Conectar con sistema de Nómina" |

### Flujo del Proceso

```
1. Usuario identifica sistema y cambio deseado
   ↓
2. ISSEG analiza impacto
   ├─ Usuarios afectados
   ├─ Urgencia/prioridad
   ├─ Complejidad
   └─ Recursos necesarios
   ↓
3. Aprobación/Rechazo
   ├─ ✅ Aprobado → Equipo de desarrollo implementa
   └─ ❌ Rechazado → Notifica con motivos
```

### Campos Principales (13 campos)

1. Sistema a modificar (catálogo)
2. Versión actual del sistema
3. Tipo de cambio (correctivo/perfectivo/etc)
4. Módulos/áreas afectadas
5. Situación actual (cómo está ahora)
6. Situación deseada (cómo se quiere)
7. Razón/justificación del cambio
8. Cantidad de usuarios impactados
9. Nivel de urgencia (baja/media/alta/crítica)
10. Pasos para reproducir (si es error)
11. Capturas de pantalla/evidencias
12. Especificación técnica detallada
13. Contacto del solicitante

---

## 📄 Formulario C: Levantamiento de Requerimientos Técnicos

**Estado:** Solo para sistemas aprobados  
**Responsables:** PM + Equipo Técnico + Usuario de Negocio  

### ¿Cuándo se usa?
**DESPUÉS** de que el Formulario A fue aprobado. Se completa detalladamente con PM y equipo técnico para especificar exactamente qué se va a construir.

### Secciones Principales (9 Secciones Exhaustivas)

1. **Contexto y Marco Teórico**
   - Cómo funciona actualmente el área
   - Procesos de negocio existentes
   - Herramientas actuales

2. **Problemática Específica**
   - Qué falla exactamente
   - Impacto operativo
   - Pérdidas asociadas

3. **Alcances y Delimitaciones**
   - QUÉ SÍ hace el sistema
   - QUÉ NO hace el sistema

4. **Actores y Roles**
   - Tabla de quiénes usan qué
   - Permisos por rol
   - Responsabilidades

5. **Módulos Funcionales**
   - Desglose de componentes
   - Flujo de procesos

6. **Requerimientos Funcionales (RF - Mínimo 10)**
   - Descripción clara de cada funcionalidad
   - Criterios de aceptación

7. **Reglas de Negocio**
   - Validaciones obligatorias
   - Restricciones del dominio

8. **Requerimientos No Funcionales (RNF)**
   - Rendimiento esperado
   - Seguridad
   - Disponibilidad (SLA)

9. **Criterios de Aceptación**
   - Cómo sabremos que funciona correctamente
   - Pruebas de validación

---

## 🚨 Formulario Urgencia: Reporte de Incidencias

**ID Asignado:** `INC-YYYY-NNNN`  
**Ruta:** Express (Respuesta INMEDIATA)  

### ¿Cuándo se usa?
Para reportar **fallas críticas y urgencias** que impactan operaciones inmediatas de ISSEG.

### Características Clave

✅ **No requiere aprobación** - Se atiende de inmediato  
✅ **SLA Crítico** - Respuesta en menos de 2 horas  
✅ **Puede pausar proyectos** - Si es suficientemente crítica  
✅ **Escalación automática** - Si no se resuelve en SLA  

### Flujo Especial

```
Usuario reporta urgencia
   ↓
Sistema genera INC-ID automáticamente
   ↓
Dispatcher recibe notificación INMEDIATA
   ↓
¿Es crítica y requiere pausa de proyecto?
├─ SÍ → Notifica a Project Managers
│        └─ Pausa proyecto en curso
│           └─ Asigna desarrollador a urgencia
└─ NO → Asigna a cola normal de urgencias
   ↓
Desarrollo + Resolución
   ↓
✅ Notificación automática al usuario
```

### Campos Capturados (14 campos)

1. Sistema afectado
2. Descripción detallada del problema
3. Impacto (# usuarios afectados)
4. Nivel de severidad (crítica/alta/media/baja)
5. Pasos para reproducir error
6. Capturas de pantalla/evidencias
7. Versión del sistema
8. Navegador/dispositivo afectado
9. ¿Funcionaba antes? ¿Cuándo paró?
10. ¿Hay workaround disponible?
11. Nombre del reportante
12. Teléfono de contacto
13. Correo electrónico
14. Departamento/área del usuario

---

# Procesos Integrados

## 🔄 Matriz de Decisión: ¿Cuál Formulario Usar?

| Situación | Usar Formulario | Urgencia | Aprobación | SLA |
|-----------|-----------------|----------|-----------|-----|
| Necesito un sistema completamente nuevo | **A** | Normal | SÍ - ISSEG | 5-10 días |
| Quiero cambiar un sistema existente | **B** | Normal/Alta | SÍ - ISSEG | 3-5 días |
| Form A fue aprobado, detallo requerimientos | **C** | Normal | NO - PM | Variable |
| El sistema NO funciona, falla crítica | **Urgencia** | CRÍTICA | NO | ≤ 2 horas |

## 📊 Ruta 1: Nuevo Sistema (Flujo Normal)

```
┌─ Usuario llena Formulario A
│  └─ Justificación, beneficios, alcance
│
├─ ISSEG realiza evaluación
│  └─ Presupuesto, recursos, viabilidad técnica
│
├─ ¿Aprobado?
│  │
│  ├─ SÍ ↓
│  │  ├─ Se asigna PM + Equipo técnico
│  │  ├─ Se notifica a usuario
│  │  └─ Procede a siguiente paso
│  │
│  └─ NO ↓
│     └─ Se notifica rechazo + motivos → FIN
│
├─ Usuario llena Formulario C (Requerimientos)
│  └─ Con colaboración de PM y equipo técnico
│
├─ Se validan requerimientos
│  ├─ ¿Están claros? → Sí ↓
│  └─ ¿Hay ambigüedades? → Se aclaran
│
├─ Inicia especificación técnica
│  └─ Diseño de BD, arquitectura, mockups
│
└─ Desarrollo e Implementación
   └─ Coding → Testing → Deployment → ✅ LIVE
```

## 🚨 Ruta 2: Urgencias (Ruta Express)

```
┌─ Usuario reporta falla CRÍTICA
│  └─ Llena Formulario Urgencia en menos de 5 minutos
│
├─ Sistema genera ID automáticamente: INC-YYYYNNNN
│
├─ Validación automática de severidad
│  ├─ CRÍTICA → Notificación URGENTE al Dispatcher
│  ├─ ALTA → Notificación al PM
│  └─ MEDIA → Cola normal
│
├─ ¿Es CRÍTICA y puede pausar otros?
│  │
│  ├─ SÍ ↓
│  │  ├─ Notifica a Project Managers
│  │  ├─ Pausa proyecto en curso (si aplica)
│  │  └─ Reasigna desarrollador a urgencia
│  │
│  └─ NO ↓
│     └─ Va a cola de urgencias normales
│
├─ Dispatcher BUSCA disponibilidad
│  └─ Asigna al desarrollador más capacitado
│
├─ Developer atiende INMEDIATAMENTE
│  ├─ Diagnostica problema
│  ├─ Busca causa raíz
│  └─ Ofrece solución
│
├─ ¿Se resuelve?
│  │
│  ├─ SÍ ↓
│  │  ├─ Se implementa fix
│  │  ├─ Se verifica en producción
│  │  └─ ✅ Se notifica a usuario
│  │
│  └─ Necesita más tiempo ↓
│     └─ Se registra progreso + ETA nueva
│
└─ Ticket se CIERRA
   └─ Con registro de horas + causa raíz
```

---

# Diagramas de Arquitectura

## 1️⃣ Autenticación y Control de Acceso

```
🔐 FLUJO DE AUTENTICACIÓN

User Login
   ↓
Validar: ¿Email + Password correcto?
   ├─ NO → Error → Reintentar
   └─ SÍ ↓
   
Cargar Usuario + Área + Rol
   ↓
¿Usuario ACTIVO en base de datos?
   ├─ NO → Bloquear acceso
   └─ SÍ ↓

Consultar tabla Roles x Permisos
   ├─ Rol_ID + Area_ID
   └─ Obtener lista de permisos
   
¿Usuario autorizado en SU área?
   ├─ NO → Acceso SOLO LECTURA
   └─ SÍ ↓

Cargar Dashboard
   ├─ Mis Solicitudes
   ├─ Mis Sistemas
   ├─ Mi Bandeja de Aprobación
   └─ Mis Incidencias Asignadas
```

## 2️⃣ Validación de Permisos por Área

```
✅ VALIDACIÓN DE PERMISOS

¿Usuario existe en tabla Usuarios?
   ├─ NO → BLOQUEAR acceso
   └─ SÍ ↓

¿Área_ID del usuario es válido?
   ├─ NO → Sin permisos
   └─ SÍ ↓

¿Rol_ID del usuario es válido?
   ├─ NO → Asignar Rol por defecto (LECTOR)
   └─ SÍ ↓

Consultar tabla Permisos
   ├─ WHERE Rol_ID = X AND Area_ID = Y
   └─ Obtener permisos específicos
   
¿Usuario tiene permiso para esta acción?
   ├─ NO → Mensaje "Acceso Denegado"
   └─ SÍ ↓

✅ ACCIÓN PERMITIDA
```

## 3️⃣ Filtrado Inteligente de Sistemas

```
FILTRADO DE SISTEMAS POR ÁREA

Obtener Area_ID del usuario
   ↓
Consultar tabla Áreas_Sistemas
   │
   ├─ Sistema pertenece a mi área?
   │  └─ SÍ → Mostrar ✅
   │
   ├─ Sistema es COMPARTIDO (multi-area)?
   │  └─ SÍ → Mostrar ✅
   │
   ├─ Sistema requiere permiso ESPECIAL?
   │  ├─ ¿Tengo permiso?
   │  │  ├─ SÍ → Mostrar ✅
   │  │  └─ NO → Ocultar ❌
   │  └─ NO → Mostrar ✅
   │
   └─ RESULTADO: Lista filtrada solo para el usuario
```

## 4️⃣ Estados del Ticket (Ciclo de Vida)

```
ESTADOS Y TRANSICIONES DE TICKET

1. NUEVO
   ├─ Se genera ID automáticamente
   ├─ Se registra timestamp
   └─ se notifica a ISSEG o Dispatcher
   ↓
2. EN ESPERA / DRAFT
   ├─ Usuario puede editar antes de enviar
   └─ O sistema espera revisión
   ↓
3. EN REVISIÓN
   ├─ Se asigna a evaluador/aprobador
   └─ En análisis
   ↓
4. ¿DECISIÓN?
   ├─ ✅ APROBADO → Siguiente estado
   ├─ ❌ RECHAZADO → CERRADO (con motivo)
   └─ 🔄 REQUIERE CAMBIOS → Retorna al usuario
   ↓
5. ASIGNADO
   ├─ Se asigna a persona/equipo
   └─ Se notifica al asignado
   ↓
6. EN PROGRESO
   ├─ Se comienza el trabajo
   └─ Se registran horas
   ↓
7. EN PRUEBAS
   ├─ Se valida el resultado
   ├─ ✅ OK → Siguiente
   └─ 🐛 Errores → Retorna a EN PROGRESO
   ↓
8. COMPLETADO
   ├─ Se verifica en producción
   └─ Usuario final da OK
   ↓
9. ✅ CERRADO
   └─ Fin del ciclo, archivo en historial
```

## 5️⃣ Matriz de Permisos por Rol

```
MATRIZ DE CONTROL DE ACCESO (RBAC)

┌─────────────────────────┬────────┬────────┬─────────┬─────────────┬────────┐
│ Función / Permiso       │ LECTOR │ USUARIO│ CREADOR │ APROBADOR   │ ADMIN  │
├─────────────────────────┼────────┼────────┼─────────┼─────────────┼────────┤
│ Ver solicitudes         │ ✅ Mías│ ✅ Mías│ ✅ Mías │ ✅ TODAS    │ ✅ ALL │
│ Crear solicitudes       │   ❌   │ ✅ A,B │ ✅ TODAS│ ✅ TODAS    │ ✅ ALL │
│ Aprobar/Rechazar        │   ❌   │   ❌   │   ❌    │ ✅ Su Área  │ ✅ ALL │
│ Ver reportes            │   ❌   │ ✅ Básico│ ✅ Básico│ ✅ Avanzado │ ✅ ALL │
│ Exportar datos          │   ❌   │   ❌   │   ❌    │ ✅ Su Área  │ ✅ ALL │
│ Editar otro usuario     │   ❌   │   ❌   │   ❌    │   ❌        │ ✅ ALL │
│ Ver auditoría           │   ❌   │   ❌   │   ❌    │   ❌        │ ✅ ALL │
│ Configurar sistema      │   ❌   │   ❌   │   ❌    │   ❌        │ ✅ ALL │
└─────────────────────────┴────────┴────────┴─────────┴─────────────┴────────┘
```

---

# Comparación Detallada

## Tabla Comparativa de los 4 Formularios

| Aspecto | Form A | Form B | Form C | Urgencia |
|---------|--------|--------|--------|----------|
| **ID Asignado** | SN-YYYY-NNNN | MOD-YYYY-NNNN | (Usa Form A) | INC-YYYY-NNNN |
| **Propósito** | Nuevo sistema | Cambios/mejoras | Requerimientos detallados | Fallas críticas |
| **Campos** | 11 | 13 | 11 (en 9 secciones) | 14 |
| **Aprobación Requerida** | ✅ ISSEG | ✅ ISSEG | ❌ (PM valida) | ❌ (Inmediato) |
| **SLA** | 5-10 días | 3-5 días | Variable | ≤ 2 Horas |
| **Complejidad** | Media | Media | Alta | Baja |
| **Documentación** | Moderada | Moderada | Exhaustiva | Mínima |
| **Puede pausar otros** | ❌ No | ❌ No | ❌ No | ✅ Sí (si crítica) |
| **Responsable Principal** | Usuario + ISSEG | Usuario + ISSEG | PM + Equipo técnico | Developer asignado |
| **Pasos a seguir** | Form C (si aprueba) | Implementación directa | Especificación técnica | Resolución inmediata |
| **¿Requiere IT?** | Evaluación | Evaluación | Desarrollo | Desarrollo urgente |

---

# Arquitectura Técnica

## 🏗️ Stack Tecnológico

| Capa | Tecnología | Descripción |
|------|-----------|-------------|
| **Frontend** | Angular 15+ | SPA con TypeScript, Reactive Forms, Material Design |
| **Backend** | ASP.NET Core 7+ | API RESTful, Entity Framework, Dependency Injection |
| **Database** | SQL Server 2019+ | Catálogos normalizados, Stored Procedures, Triggers |
| **Seguridad** | Azure AD / OAuth | Autenticación centralizada, 2FA, Encryption |
| **Infrastructure** | Cloud Ready | Azure o On-Premise, Scalable, HA |

## 📊 Tablas Principales de Base de Datos

### Tabla: Usuarios
```
ID_Usuario (PK)
Email (UNIQUE)
Password_Hash
Nombre_Completo
Area_ID (FK)
Rol_ID (FK)
Activo (BOOLEAN)
Fecha_Creacion
Fecha_Ultimo_Login
```

### Tabla: Áreas
```
ID_Area (PK)
Nombre (UNIQUE)
Descripción
Responsable_ID (FK)
Activa (BOOLEAN)
Fecha_Creacion
```

### Tabla: Roles
```
ID_Rol (PK)
Nombre (UNIQUE)
Descripción
Activo (BOOLEAN)
Fecha_Creacion
```

### Tabla: Permisos
```
ID_Permiso (PK)
Rol_ID (FK)
Area_ID (FK)
Permiso_Code (UNIQUE)
Descripción
Activo (BOOLEAN)
```

### Tabla: Solicitudes_Nuevos (Form A)
```
ID_Solicitud (PK) = "SN-YYYY-NNNN"
Usuario_ID (FK)
Nombre_Sistema
Descripción
Justificacion
Beneficios
Alcance
Plataforma
Timeline
Presupuesto
Estado (NUEVO, EN_REVISION, APROBADO, RECHAZADO)
Aprobador_ID (FK)
Comentarios_Aprobacion
Fecha_Creacion
Fecha_Decision
```

### Tabla: Solicitudes_Modificacion (Form B)
```
ID_Solicitud (PK) = "MOD-YYYY-NNNN"
Usuario_ID (FK)
Sistema_ID (FK)
Tipo_Cambio (CORRECTIVO, PERFECTIVO, ADAPTATIVO, INTEGRATIVO)
Descripcion_Cambio
Situacion_Actual
Situacion_Deseada
Urgencia (BAJA, MEDIA, ALTA, CRITICA)
Estado (NUEVO, ASIGNADO, EN_PROGRESO, COMPLETADO, CERRADO)
Asignado_A (FK)
Horas_Estimadas
Horas_Reales
Fecha_Creacion
Fecha_Implementacion
```

### Tabla: Requerimientos (Form C)
```
ID_Requerimiento (PK)
Solicitud_ID (FK)
Contexto_Area
Problematica
Alcances
Exclusiones
Usuarios_Cantidad
Modulos (JSON)
RF_Count (int)
RNF_Array (JSON)
Criterios_Aceptacion (TEXT)
Fecha_Creacion
```

### Tabla: Incidencias (Form Urgencia)
```
ID_Incidencia (PK) = "INC-YYYY-NNNN"
Sistema_ID (FK)
Usuario_ID (FK)
Descripcion
Pasos_Reproducir
Severidad (BAJA, MEDIA, ALTA, CRITICA)
Estado (NUEVO, EN_PROGRESO, RESUELTO, CERRADO)
Asignado_A (FK)
Workaround_Disponible (BOOLEAN)
Fecha_Creacion
Fecha_Asignacion
Fecha_Resolucion
Horas_Dedicadas
```

### Tabla: Sistemas (Catálogo Master)
```
ID_Sistema (PK)
Nombre (UNIQUE)
Descripcion
Version (int)
Area_ID (FK)
Responsable_Desarrollo (FK)
Activo (BOOLEAN)
Fecha_Creacion
Fecha_Ultima_Actualizacion
URL_Acceso
```

### Tabla: Auditoria
```
ID_Auditoria (PK)
Usuario_ID (FK)
Accion (CREATE, UPDATE, DELETE, APPROVE, REJECT)
Tabla_Afectada (Solicitudes_Nuevos, Usuarios, etc)
ID_Registro_Afectado
Valores_Antes (JSON)
Valores_Despues (JSON)
Razon_Cambio (TEXT)
IP_Address
User_Agent
Timestamp (DATETIME)
```

---

# Beneficios Esperados

## 📈 Impacto Cuantificable

| Métrica | Antes | Después | Mejora |
|---------|-------|---------|--------|
| **Tiempo promedio de resolución** | 15-20 días | 3-5 días | ↓ 75% |
| **Solicitudes perdidas anualmente** | ~20% | 0% | ↓ 100% |
| **Documentación disponible** | 30% | 100% | ↑ 70% |
| **Horas de auditoría/mes** | 80 horas | 2 horas | ↓ 97.5% |
| **Cumplimiento de SLA** | 60% | 99% | ↑ 39% |
| **Reclamos por procesos** | 50/año | ~5/año | ↓ 90% |

## ✨ Beneficios por Stakeholder

### Para Usuarios Finales
- ✅ Portal de autoservicio intuitivo
- ✅ Seguimiento en tiempo real
- ✅ Notificaciones automáticas
- ✅ Historial completo de cambios

### Para Managers/Jefes de Área
- ✅ Dashboards ejecutivos
- ✅ Métricas de productividad
- ✅ Reportes automáticos
- ✅ Análisis de tendencias de solicitudes

### Para Equipo de Desarrollo
- ✅ Requerimientos claros y sin ambigüedades
- ✅ Priorización automática e inteligente
- ✅ Documentación integral y organizada
- ✅ Trazabilidad de cambios

### Para la Institución (ISSEG)
- ✅ Auditoría completa y automática
- ✅ Cumplimiento normativo
- ✅ Control de riesgos
- ✅ Trazabilidad total
- ✅ Mejora de imagen institucional

---

# Plan de Implementación

## 📅 Cronograma General

**Período:** Enero - Julio 2026 (7 meses)  
**Modalidad:** Residencia Profesional  
**Especialidad:** Ciberseguridad e Ingeniería de Sistemas

### Fases del Proyecto

1. **Enero - Análisis y Diseño**
   - Especificación completa del sistema
   - Diseño de arquitectura
   - Diseño de base de datos
   - Especificación de seguridad

2. **Febrero-Marzo - Desarrollo Fase 1**
   - Backend: APIs REST
   - Frontend: Interfaces básicas
   - Seguridad: Autenticación/Autorización

3. **Abril-Mayo - Desarrollo Fase 2**
   - Implementación de formularios completos
   - Integraciones
   - Reportes y dashboards
   - Auditoría

4. **Junio - Testing y Optimización**
   - Pruebas unitarias
   - Pruebas de integración
   - Pruebas de seguridad
   - Optimización de performance

5. **Julio - Implementación en Producción**
   - Capacitación a usuarios
   - Deploy a producción
   - Soporte inicial
   - Documentación final

---

## 🎯 Próximos Pasos

1. **Validación** - Revisar esta propuesta con stakeholders
2. **Ajustes** - Incorporar feedback y mejorar documentación
3. **Aprobación Formal** - Obtener firma de directivos
4. **Inicio Desarrollo** - Comenzar Fase 1 en Enero 2026
5. **Seguimiento** - Reuniones de avance cada 2 semanas

---

## 📞 Contacto e Información

**Instituto de Seguridad Social del Estado de Guanajuato (ISSEG)**  
Departamento de Desarrollo TI  

**Proyecto:** Sistema de Gestión de Solicitudes  
**Fecha:** Febrero 2026  
**Versión:** 3.0 - INTEGRADA

---

**Esta documentación integra:**
- ✅ Los 4 formularios completos
- ✅ Diagramas de arquitectura
- ✅ Procesos de negocio
- ✅ Comparativas detalladas
- ✅ Especificación técnica
- ✅ Beneficios esperados
- ✅ Plan de implementación

**Archivo generado:** Combinación de proyecto ISSEG (Febrero 2026)
