## ADDED Requirements

### Requirement: Gestión de actividades
El sistema SHALL permitir crear, editar, eliminar y listar actividades asociadas a un proyecto.

#### Scenario: Crear actividad
- **WHEN** el usuario envía los datos mínimos requeridos para una actividad
- **THEN** el sistema crea la actividad y la asocia al proyecto correspondiente

#### Scenario: Editar actividad
- **WHEN** el usuario modifica los datos de una actividad existente
- **THEN** el sistema actualiza la actividad y retorna los datos actualizados

#### Scenario: Eliminar actividad
- **WHEN** el usuario solicita eliminar una actividad existente
- **THEN** el sistema elimina la actividad y confirma la operación

#### Scenario: Listar actividades
- **WHEN** el usuario solicita la lista de actividades de un proyecto
- **THEN** el sistema retorna todas las actividades asociadas a ese proyecto
