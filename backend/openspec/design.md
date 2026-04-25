# OpenSpec: Diseño Vertical Login

## Diagrama de flujo
- Usuario envía email/password
- Backend valida credenciales
- Si ok, retorna JWT y datos usuario
- Si error, retorna 401

## Estructura de archivos
- models.py: clase Usuario
- main.py: endpoint /api/login
- tests/test_login.py: pruebas

---
# OpenSpec: Diseño CRUD Proyectos y Actividades

## Diagrama de flujo
- CRUD proyectos: alta, baja, modificación, consulta
- CRUD actividades: alta, baja, modificación, consulta
- Validaciones: relaciones, rangos, unicidad

## Estructura de archivos
- models.py: clases Proyecto, Actividad
- main.py: endpoints
- tests/test_main.py: pruebas

---
# OpenSpec: Diseño Módulo EVM

## Diagrama de flujo
- Recibe datos de actividad
- Calcula indicadores EVM
- Retorna resultados

## Estructura de archivos
- evm.py: funciones
- tests/test_evm.py: pruebas
