## ADDED Requirements

### Requirement: Visualización de indicadores y gráficas
El sistema SHALL mostrar en el dashboard los indicadores EVM, tablas de actividades y gráficas comparativas de PV, EV y AC.

#### Scenario: Visualización de tabla
- **WHEN** el usuario accede al dashboard de un proyecto
- **THEN** el sistema muestra la tabla de actividades con sus indicadores

#### Scenario: Visualización de gráfica
- **WHEN** el usuario accede al dashboard de un proyecto
- **THEN** el sistema muestra una gráfica comparativa de PV, EV y AC por actividad

#### Scenario: Estado visual de CPI y SPI
- **WHEN** se muestran los indicadores
- **THEN** el sistema resalta visualmente el estado de CPI y SPI
