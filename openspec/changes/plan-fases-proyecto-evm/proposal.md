## Why

El proyecto busca dotar a los líderes de proyecto de una herramienta integral para registrar y analizar el avance de sus actividades bajo la metodología de Valor Ganado (EVM), permitiendo identificar desviaciones en tiempo y presupuesto en tiempo real. Es necesario abordar el desarrollo por fases para asegurar calidad, trazabilidad y cumplimiento de estándares.

## What Changes

- Diseño y definición de la arquitectura general del sistema (backend, frontend, base de datos, integración OpenSpec).
- Implementación de la gestión de proyectos y actividades (CRUD).
- Cálculo automático de indicadores EVM y su interpretación.
- Visualización de indicadores y gráficas en dashboard.
- Cobertura de pruebas unitarias y de integración.
- Documentación OpenAPI para el backend.
- Integración continua y control de calidad (linter, CI/CD).
- Documentación del proceso de desarrollo y decisiones (AI_PROCESS.md).

## Capabilities

### New Capabilities
- `proyecto-crud`: Gestión de proyectos (crear, editar, eliminar, listar).
- `actividad-crud`: Gestión de actividades asociadas a proyectos.
- `evm-calculo`: Cálculo y validación de indicadores EVM.
- `dashboard-visualizacion`: Visualización de indicadores, tablas y gráficas.
- `api-documentacion`: Documentación OpenAPI accesible y completa.
- `proceso-documentacion`: Documentación del proceso y decisiones de IA.

### Modified Capabilities
- (Ninguna por ahora)

## Impact

- Código backend (FastAPI), frontend (Angular), y base de datos (PostgreSQL).
- APIs RESTful y contratos OpenAPI.
- Flujos de integración continua y control de calidad.
- Artefactos OpenSpec y documentación de proceso.