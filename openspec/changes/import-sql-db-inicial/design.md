## Context

El proyecto requiere una base de datos relacional en PostgreSQL para soportar la gestión de usuarios, proyectos y actividades, así como el cálculo de indicadores EVM. El script import.sql debe crear la estructura mínima necesaria, asegurar integridad referencial y permitir la carga de datos de ejemplo para desarrollo y pruebas.

## Goals / Non-Goals

**Goals:**
- Definir un modelo relacional claro y normalizado para usuarios, proyectos y actividades.
- Incluir restricciones, claves primarias y foráneas para asegurar integridad.
- Permitir la carga de datos mínimos de ejemplo.
- Facilitar la extensión futura para trazabilidad y auditoría.

**Non-Goals:**
- No se incluirán tablas para autenticación avanzada, auditoría detallada ni historiales en esta versión inicial.
- No se abordarán migraciones automáticas ni versionado de esquema.

## Decisions

- Tabla `usuarios` con campos id, email, password_hash, nombre, activo.
- Tabla `proyectos` con id, nombre, descripcion, fecha_inicio, fecha_fin, usuario_responsable_id (FK a usuarios).
- Tabla `actividades` con id, proyecto_id (FK), nombre, bac, avance_planificado, avance_real, ac.
- Restricciones NOT NULL y UNIQUE donde aplique (ej: email de usuario).
- Datos de ejemplo para al menos un usuario, un proyecto y una actividad.
- Uso de claves foráneas para mantener relaciones y ON DELETE CASCADE donde corresponda.

## Risks / Trade-offs

- [Riesgo] Cambios futuros en el modelo pueden requerir migraciones manuales → Mitigación: documentar claramente el modelo y mantener el script actualizado.
- [Riesgo] Datos de ejemplo pueden interferir con datos reales en producción → Mitigación: separar scripts de desarrollo y producción.

## Migration Plan

1. Crear script import.sql con sentencias CREATE TABLE y restricciones.
2. Agregar sentencias INSERT para datos mínimos de ejemplo.
3. Probar el script en entorno local y ajustar según feedback.

## Open Questions

- ¿Se requerirán tablas adicionales para logs o auditoría en el futuro?
- ¿Qué otros campos serían útiles en usuarios, proyectos o actividades?