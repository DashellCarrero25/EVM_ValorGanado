## ADDED Requirements

### Requirement: Modelo relacional de base de datos
El sistema SHALL definir un modelo relacional en PostgreSQL para usuarios, proyectos y actividades, asegurando integridad referencial y normalización.

#### Scenario: Creación de tablas
- **WHEN** se ejecuta el script import.sql
- **THEN** se crean las tablas usuarios, proyectos y actividades con sus relaciones y restricciones

#### Scenario: Integridad referencial
- **WHEN** se elimina un usuario o proyecto
- **THEN** se eliminan en cascada los proyectos/actividades asociadas según corresponda

### Requirement: Restricciones y claves
El sistema SHALL definir claves primarias, foráneas, restricciones NOT NULL y UNIQUE donde aplique.

#### Scenario: Email único
- **WHEN** se intenta insertar un usuario con email duplicado
- **THEN** la base de datos rechaza la operación
