## ADDED Requirements

### Requirement: Interfaz de login
El sistema SHALL proveer una pantalla de login clara, accesible y con feedback visual para errores.

#### Scenario: Visualización de formulario
- **WHEN** el usuario accede a la aplicación sin sesión activa
- **THEN** se muestra el formulario de login con campos para correo y contraseña

#### Scenario: Feedback de error
- **WHEN** el usuario ingresa credenciales incorrectas
- **THEN** se muestra un mensaje de error visible y accesible

#### Scenario: Accesibilidad
- **WHEN** el usuario navega el formulario
- **THEN** todos los campos y botones son accesibles vía teclado y cumplen contraste mínimo
