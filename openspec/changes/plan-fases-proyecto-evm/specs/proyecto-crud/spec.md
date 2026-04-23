## ADDED Requirements

### Requirement: Gestión de proyectos
El sistema SHALL permitir crear, editar, eliminar y listar proyectos.

#### Scenario: Crear proyecto
- **WHEN** el usuario envía los datos mínimos requeridos para un proyecto
- **THEN** el sistema crea el proyecto y lo retorna con su identificador

#### Scenario: Editar proyecto
- **WHEN** el usuario modifica los datos de un proyecto existente
- **THEN** el sistema actualiza el proyecto y retorna los datos actualizados

#### Scenario: Eliminar proyecto
- **WHEN** el usuario solicita eliminar un proyecto existente
- **THEN** el sistema elimina el proyecto y confirma la operación

#### Scenario: Listar proyectos
- **WHEN** el usuario solicita la lista de proyectos
- **THEN** el sistema retorna todos los proyectos registrados
