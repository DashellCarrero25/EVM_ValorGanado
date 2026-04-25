# OpenSpec Proposal: Vertical de Login

## Resumen
Implementar la vertical de login para el sistema EVM, incluyendo endpoints, modelo de usuario, autenticación, pruebas unitarias y de integración, y cumplimiento de linter.

## Especificación
- Endpoint: /api/login (POST)
- Modelo: Usuario (campos: id, email, password_hash, nombre, rol)
- Autenticación: JWT simple
- Pruebas: pytest, cobertura >90%
- Linter: .flake8

## Artefactos
- backend/models.py
- backend/main.py
- backend/tests/test_login.py
- backend/evm.py

## Tareas
1. Crear modelo Usuario y migración
2. Implementar endpoint /api/login
3. Implementar autenticación JWT
4. Pruebas unitarias y de integración
5. Validar linter y cobertura

## Estado
- [x] Modelo y migración
- [x] Endpoint y autenticación
- [x] Pruebas
- [x] Linter y cobertura

---
# OpenSpec Proposal: CRUD Proyectos y Actividades

## Resumen
Implementar endpoints CRUD para proyectos y actividades, con pruebas y validación de reglas de negocio.

## Especificación
- Endpoints: /api/proyectos, /api/actividades
- Modelos: Proyecto, Actividad
- Pruebas: pytest, integración
- Linter: .flake8

## Artefactos
- backend/models.py
- backend/main.py
- backend/tests/test_main.py

## Tareas
1. Crear modelos y migraciones
2. Implementar endpoints CRUD
3. Pruebas unitarias e integración
4. Validar linter y cobertura

## Estado
- [x] Modelos y migraciones
- [x] Endpoints CRUD
- [x] Pruebas
- [x] Linter y cobertura

---
# OpenSpec Proposal: Módulo EVM

## Resumen
Implementar módulo de cálculo EVM (PV, EV, AC, CV, SV, CPI, SPI, EAC, VAC) y exponer lógica en endpoints.

## Especificación
- Funciones: calcular_pv, calcular_ev, calcular_ac, calcular_cv, calcular_sv, calcular_cpi, calcular_spi, calcular_eac, calcular_vac
- Pruebas: pytest
- Linter: .flake8

## Artefactos
- backend/evm.py
- backend/tests/test_evm.py

## Tareas
1. Implementar funciones EVM
2. Pruebas unitarias
3. Validar linter

## Estado
- [x] Funciones EVM
- [x] Pruebas
- [x] Linter
