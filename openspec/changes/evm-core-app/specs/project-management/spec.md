## ADDED Requirements

### Requirement: CRUD de proyectos y actividades
El sistema SHALL permitir crear, editar, eliminar y listar proyectos y actividades. Cada actividad estará asociada a un proyecto y almacenará los datos base requeridos para el cálculo EVM.

#### Scenario: Crear proyecto
- **WHEN** el usuario envía los datos de un nuevo proyecto
- **THEN** el sistema crea el proyecto y lo retorna con su identificador

#### Scenario: Editar actividad
- **WHEN** el usuario actualiza los datos de una actividad existente
- **THEN** el sistema guarda los cambios y retorna la actividad actualizada

#### Scenario: Eliminar proyecto
- **WHEN** el usuario solicita eliminar un proyecto
- **THEN** el sistema elimina el proyecto y todas sus actividades asociadas

#### Scenario: Listar actividades
- **WHEN** el usuario solicita las actividades de un proyecto
- **THEN** el sistema retorna la lista de actividades con sus datos base
