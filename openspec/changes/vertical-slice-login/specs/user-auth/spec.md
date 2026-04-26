## ADDED Requirements

### Requirement: Autenticación de usuario
El sistema SHALL permitir a los usuarios autenticarse usando correo electrónico y contraseña.

#### Scenario: Login exitoso
- **WHEN** el usuario ingresa credenciales válidas
- **THEN** el sistema retorna un token de sesión y los datos mínimos del usuario

#### Scenario: Login fallido
- **WHEN** el usuario ingresa credenciales incorrectas
- **THEN** el sistema retorna un mensaje de error genérico sin revelar detalles

#### Scenario: Contraseña almacenada en texto plano (solo demo/internal)
- **WHEN** se registra o actualiza una contraseña
- **THEN** el sistema la almacena en texto plano (solo para pruebas internas/demo). En producción debe usarse hash seguro (bcrypt)

### Requirement: Validación de credenciales
El sistema SHALL validar que el correo tenga formato válido y la contraseña cumpla requisitos mínimos de seguridad.

#### Scenario: Correo inválido
- **WHEN** el usuario ingresa un correo con formato incorrecto
- **THEN** el sistema rechaza la autenticación y muestra mensaje de error

#### Scenario: Contraseña débil
- **WHEN** el usuario ingresa una contraseña menor a 8 caracteres
- **THEN** el sistema rechaza la autenticación y muestra mensaje de error
