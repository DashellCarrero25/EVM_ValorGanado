## ADDED Requirements

### Requirement: Cálculo automático de indicadores EVM
El sistema SHALL calcular automáticamente los indicadores PV, EV, CV, SV, CPI, SPI, EAC y VAC para cada actividad y de forma consolidada por proyecto.

#### Scenario: Cálculo por actividad
- **WHEN** se registran o actualizan los datos de una actividad
- **THEN** el sistema recalcula y retorna los indicadores EVM para esa actividad

#### Scenario: Cálculo consolidado
- **WHEN** se solicita el resumen de un proyecto
- **THEN** el sistema retorna los indicadores EVM consolidados del proyecto

### Requirement: Interpretación de indicadores
El sistema SHALL interpretar y mostrar el estado de CPI y SPI (eficiencia en costos y cronograma).

#### Scenario: Interpretación de CPI y SPI
- **WHEN** se calculan los indicadores
- **THEN** el sistema indica si el proyecto está bajo/sobre presupuesto y adelantado/atrasado
