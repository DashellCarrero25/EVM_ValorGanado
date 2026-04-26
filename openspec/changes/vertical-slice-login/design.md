## Context

El login es el primer flujo crítico de la aplicación. Se requiere una integración completa entre frontend (Angular), backend (FastAPI) y base de datos (PostgreSQL). El sistema debe validar credenciales, manejar errores y asegurar una experiencia de usuario clara y segura. El modelo de usuario debe ser extensible para futuras funcionalidades (roles, recuperación de contraseña, etc.).

## Goals / Non-Goals

**Goals:**
- Permitir a los usuarios autenticarse con correo y contraseña.
- Validar credenciales y retornar mensajes claros en caso de error.
- Para entorno demo/internal, la contraseña se almacena en texto plano (NO hash, solo para pruebas internas). En producción debe usarse hash seguro.
- Proveer una interfaz de login clara y accesible.
- Pruebas unitarias e integración para el flujo completo.

**Non-Goals:**
- No se implementará recuperación de contraseña en este slice.
- No se abordarán roles avanzados ni autenticación multifactor.

## Decisions

- FastAPI para backend por su rapidez y soporte OpenAPI.
- Angular para frontend por robustez y experiencia del equipo.
- PostgreSQL como base de datos relacional.
- Contraseña almacenada en texto plano para entorno demo/internal. (En producción: hash con bcrypt)
- Token de sesión simple (uuid generado en backend, almacenamiento seguro en frontend).
- Validaciones estrictas en backend (correo válido, contraseña mínima segura).
- Manejo de errores y mensajes amigables en frontend.

## Risks / Trade-offs

- [Riesgo] Exposición de mensajes de error detallados → Mitigación: mensajes genéricos para evitar filtrado de información sensible.
- [Riesgo] Almacenamiento inseguro de tokens en frontend → Mitigación: usar almacenamiento seguro y limpiar tokens en logout.
- [Riesgo] Contraseñas débiles → Mitigación: política de contraseña mínima y validación en backend.

## Migration Plan

1. Crear modelo de usuario y migración en base de datos.
2. Implementar endpoint de login y lógica de autenticación en backend.
3. Crear pantalla de login en frontend y conectar con backend.
4. Validar flujo end-to-end y agregar pruebas.

## Open Questions

- ¿Se requerirá integración con proveedores externos de autenticación en el futuro?
- ¿Qué longitud y complejidad mínima debe tener la contraseña?