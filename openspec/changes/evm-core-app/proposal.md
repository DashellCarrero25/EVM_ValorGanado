## Why

La gestión de proyectos requiere un control preciso del avance y los costos. Sin una herramienta que calcule automáticamente los indicadores de Valor Ganado (EVM), los líderes de proyecto no pueden anticipar desviaciones ni tomar decisiones informadas a tiempo. Ahora es crucial contar con una solución integral que permita gestionar proyectos, actividades y visualizar el estado real en tiempo real.

## What Changes

- Se crea una API REST para gestionar proyectos y actividades.
- Se implementa el cálculo automático de indicadores EVM (PV, EV, CV, SV, CPI, SPI, EAC, VAC) por actividad y consolidado por proyecto.
- Se expone la interpretación de CPI y SPI en la API.
- Se desarrolla un dashboard frontend para ingresar, editar y visualizar actividades e indicadores.
- Se incluye una gráfica comparativa de PV, EV y AC por actividad.

## Capabilities

### New Capabilities
- `project-management`: CRUD de proyectos y actividades, almacenamiento de datos base.
- `evm-calculation`: Cálculo automático de indicadores EVM y su interpretación.
- `evm-dashboard`: Visualización de actividades, indicadores y estado del proyecto en frontend.

### Modified Capabilities


## Impact

- Backend (API REST, lógica de negocio EVM, modelos de datos)
- Frontend (dashboard, visualización de indicadores, formularios)
- Base de datos (tablas de proyectos y actividades)
- Integración y experiencia de usuario
