## ADDED Requirements

### Requirement: Script SQL inicial
El sistema SHALL proveer un script import.sql que cree la estructura mínima de la base de datos y cargue datos de ejemplo.

#### Scenario: Ejecución exitosa
- **WHEN** se ejecuta el script en una base de datos vacía
- **THEN** todas las tablas y relaciones se crean sin errores y se insertan datos de ejemplo

### Requirement: Datos de ejemplo
El sistema SHALL incluir al menos un usuario, un proyecto y una actividad de ejemplo en el script.

#### Scenario: Datos mínimos
- **WHEN** se ejecuta el script
- **THEN** existen registros de ejemplo en cada tabla para pruebas y desarrollo
