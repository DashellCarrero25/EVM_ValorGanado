## ADDED Requirements

### Requirement: Documentación OpenAPI
El sistema SHALL exponer la documentación OpenAPI de la API en /docs y /openapi.json, incluyendo descripciones, esquemas de request/response y códigos de error.

#### Scenario: Acceso a documentación
- **WHEN** el usuario accede a /docs o /openapi.json
- **THEN** el sistema muestra la documentación generada automáticamente y actualizada
