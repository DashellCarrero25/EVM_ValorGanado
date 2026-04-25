## ADDED Requirements

### Requirement: Visualización de actividades e indicadores
El sistema SHALL mostrar una tabla de actividades con sus indicadores EVM calculados y los indicadores consolidados del proyecto.

#### Scenario: Visualización de tabla
- **WHEN** el usuario accede al dashboard de un proyecto
- **THEN** el sistema muestra la tabla de actividades y los indicadores consolidados

### Requirement: Estado visual de CPI y SPI
El sistema SHALL mostrar visualmente si el proyecto está bajo/sobre presupuesto y adelantado/atrasado según CPI y SPI.

#### Scenario: Estado visual de indicadores
- **WHEN** se muestran los indicadores
- **THEN** el sistema resalta visualmente el estado de CPI y SPI (verde/rojo, íconos, etc.)

### Requirement: Gráfica comparativa PV, EV, AC
El sistema SHALL mostrar una gráfica que compare PV, EV y AC por actividad.

#### Scenario: Visualización de gráfica
- **WHEN** el usuario accede al dashboard
- **THEN** el sistema muestra la gráfica comparativa de PV, EV y AC
