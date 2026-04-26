## Why

Contar con un script import.sql bien diseñado es esencial para inicializar la base de datos relacional del proyecto, garantizar integridad referencial y facilitar el desarrollo, pruebas y despliegue. Un modelo relacional claro permite gestionar usuarios, proyectos y actividades, y soportar los cálculos EVM requeridos.

## What Changes

- Diseño y creación del script import.sql para inicializar la base de datos PostgreSQL.
- Definición de tablas y relaciones para usuarios, proyectos, actividades y trazabilidad de cambios.
- Inclusión de restricciones, claves foráneas y datos mínimos de ejemplo.
- Documentación del modelo relacional y sus entidades principales.

## Capabilities

### New Capabilities
- `db-schema`: Definición y documentación del modelo relacional de la base de datos.
- `import-sql-script`: Script SQL inicial para creación y carga de datos mínimos.

### Modified Capabilities
- (Ninguna por ahora)

## Impact

- Base de datos PostgreSQL del proyecto.
- Backend y lógica de negocio que dependen del modelo relacional.
- Flujos de desarrollo, pruebas y despliegue.