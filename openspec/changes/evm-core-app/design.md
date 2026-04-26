## Context

Actualmente, la gestión de proyectos y actividades se realiza de forma manual o con herramientas dispersas, dificultando el seguimiento de indicadores clave como Valor Ganado (EVM). Se requiere una solución integral que centralice la información y automatice el cálculo de métricas para una toma de decisiones ágil.

## Goals / Non-Goals

**Goals:**
- API REST para CRUD de proyectos y actividades.
- Cálculo automático de indicadores EVM (PV, EV, CV, SV, CPI, SPI, EAC, VAC) por actividad y consolidado por proyecto.
- Interpretación automática de CPI y SPI.
- Dashboard frontend para gestión y visualización en tiempo real.
- Gráfica comparativa de PV, EV y AC.

**Non-Goals:**
- No se implementará autenticación avanzada ni roles en este cambio.
- No se abordará la exportación de datos ni integración con sistemas externos.
- No se incluye un diseño visual avanzado, solo claridad y funcionalidad.

## Decisions

- FastAPI para backend por su rapidez y soporte OpenAPI.
- Angular para frontend por robustez y experiencia del equipo.
- PostgreSQL como base de datos relacional.
- Modelo de datos: Proyecto (id, nombre), Actividad (id, proyecto_id, nombre, BAC, % planificado, % completado, AC).
- Lógica de negocio EVM en módulo separado (evm.py) para facilitar pruebas unitarias.
- Cálculo de indicadores y su interpretación en backend, frontend solo consume y visualiza.
- Gráficas con librería estándar de Angular (ej: ng2-charts).

## Risks / Trade-offs

- [Riesgo] Errores en fórmulas EVM → Mitigación: pruebas unitarias exhaustivas, validación con ejemplos reales.
- [Riesgo] Complejidad en consolidación de indicadores → Mitigación: diseño modular y pruebas por capa.
- [Riesgo] UI poco intuitiva → Mitigación: enfoque en claridad, feedback de usuarios.

## Migration Plan

1. Crear modelos y migraciones de base de datos.
2. Implementar endpoints REST y lógica de negocio EVM.
3. Desarrollar dashboard frontend y visualizaciones.
4. Validar flujo end-to-end y agregar pruebas.

## Open Questions
- ¿Se requiere soporte multiusuario o solo un líder de proyecto?
- ¿Qué nivel de auditoría o historial de cambios se necesita?
