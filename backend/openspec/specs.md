# OpenSpec: Especificaciones Vertical Login

## Esquema de Usuario
- id: int
- email: str
- password_hash: str
- nombre: str
- rol: str

## Endpoint /api/login
- Método: POST
- Request: { email, password }
- Response: { access_token, usuario }
- Errores: 401 credenciales inválidas

## Reglas de negocio
- El email debe existir y el password coincidir
- El token debe ser JWT válido

---
# OpenSpec: Especificaciones CRUD Proyectos y Actividades

## Esquema Proyecto
- id: int
- nombre: str
- descripcion: str
- fecha_inicio: date
- fecha_fin: date
- usuario_responsable_id: int

## Esquema Actividad
- id: int
- proyecto_id: int
- nombre: str
- bac: float
- avance_planificado: float
- avance_real: float
- ac: float
- fecha_inicio: date
- fecha_fin: date

## Endpoints
- /api/proyectos [GET, POST]
- /api/proyectos/{id} [GET, PUT, DELETE]
- /api/actividades [GET, POST]
- /api/actividades/{id} [GET, PUT, DELETE]

## Reglas de negocio
- No se puede eliminar un proyecto con actividades asociadas
- Los avances deben estar entre 0 y 100

---
# OpenSpec: Especificaciones Módulo EVM

## Funciones
- calcular_pv(bac, avance_planificado)
- calcular_ev(bac, avance_real)
- calcular_ac(ac)
- calcular_cv(ev, ac)
- calcular_sv(ev, pv)
- calcular_cpi(ev, ac)
- calcular_spi(ev, pv)
- calcular_eac(bac, cpi)
- calcular_vac(bac, eac)

## Reglas
- Todos los valores >= 0
- Si divisor es 0, retornar 0
