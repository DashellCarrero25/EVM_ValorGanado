## Context

El sistema será una aplicación fullstack compuesta por un backend en FastAPI, frontend en Angular y base de datos PostgreSQL. El desarrollo se realizará por fases, priorizando la trazabilidad y la calidad mediante integración con OpenSpec y CI/CD. El contexto incluye la necesidad de cálculos EVM confiables, visualización clara y documentación exhaustiva del proceso y decisiones.

## Goals / Non-Goals

**Goals:**
- Definir una arquitectura modular y escalable.
- Permitir gestión de proyectos y actividades vía API REST.
- Calcular y exponer indicadores EVM y su interpretación.
- Visualizar datos y gráficas en dashboard.
- Garantizar cobertura de pruebas y calidad de código.
- Documentar el API y el proceso de desarrollo.

**Non-Goals:**
- No se abordarán integraciones con sistemas externos en esta fase.
- No se implementarán funcionalidades fuera del alcance EVM.

## Decisions

- FastAPI para backend por su soporte OpenAPI y rapidez de desarrollo.
- Angular para frontend por robustez y experiencia en el equipo.
- PostgreSQL como base de datos relacional.
- Uso de OpenSpec para trazabilidad de cambios y requisitos.
- Organización de cambios por feature/HU para releases frecuentes.
- Validaciones estrictas en backend para datos EVM.
- Documentación automática de API con FastAPI.

## Risks / Trade-offs

- [Riesgo] Complejidad en cálculos EVM y casos borde → Mitigación: pruebas unitarias exhaustivas y validación cruzada.
- [Riesgo] Sincronización entre backend y frontend en interpretación de indicadores → Mitigación: contratos claros y pruebas de integración.
- [Riesgo] Falta de documentación de decisiones → Mitigación: AI_PROCESS.md obligatorio y revisiones periódicas.

## Migration Plan

1. Fase de diseño y definición de specs.
2. Implementación incremental por feature (CRUD, cálculos, visualización, documentación, CI/CD).
3. Validación y pruebas en cada fase.
4. Documentación y entrega.

## Open Questions

- ¿Cómo manejar la actualización masiva de actividades/proyectos?
- ¿Qué nivel de personalización visual se requiere en el dashboard?