## Why

El login es el primer punto de acceso y validación de usuarios en la aplicación. Implementar un vertical slice de login permite validar la integración end-to-end entre frontend, backend y base de datos, asegurando que la autenticación y la experiencia de usuario funcionen correctamente desde el inicio.

## What Changes

- Implementación de la pantalla de login en el frontend.
- Creación del endpoint de autenticación en el backend.
- Modelado de la tabla de usuarios en la base de datos.
- Validación de credenciales y manejo de errores de autenticación.
- Pruebas unitarias e integración para el flujo de login.

## Capabilities

### New Capabilities
- `user-auth`: Autenticación de usuarios mediante correo y contraseña.
- `login-ui`: Interfaz de usuario para login y manejo de errores.

### Modified Capabilities
- (Ninguna por ahora)

## Impact

- Código frontend (Angular) y backend (FastAPI).
- Base de datos (tabla de usuarios).
- Experiencia de usuario y seguridad de acceso.