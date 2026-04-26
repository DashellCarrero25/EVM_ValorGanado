# EVM Valor Ganado

Sistema web para la gestión y seguimiento de proyectos mediante la metodología de **Earned Value Management (EVM)**. Permite registrar proyectos y actividades, y calcular automáticamente indicadores como PV, EV, AC, CV, SV, CPI, SPI, EAC y VAC.

---

## Tecnologías

| Capa | Tecnología |
|---|---|
| Backend | Python 3.11+ · FastAPI · SQLAlchemy · Uvicorn |
| Frontend | Angular 17 · Angular Material |
| Base de datos | PostgreSQL 16 |
| Contenedor DB | Docker / Docker Compose |

---

## Requisitos previos

- [Python 3.11+](https://www.python.org/downloads/)
- [Node.js 18+ y npm](https://nodejs.org/)
- [Docker Desktop](https://www.docker.com/products/docker-desktop/) (para levantar PostgreSQL fácilmente)
- Git

---

## Configuración y ejecución local

### 1. Clonar el repositorio

```bash
git clone <url-del-repositorio>
cd EVM_ValorGanado
```

---

### 2. Base de datos (PostgreSQL con Docker)

Levanta el contenedor de PostgreSQL:

```bash
docker-compose up -d
```

Esto crea la base de datos `evm_db` con usuario `evm_user` y contraseña `evm_pass` en el puerto `5432`.

#### Script de inicialización

El archivo `db/import.sql` contiene la definición de tablas y datos de ejemplo. Para ejecutarlo contra la base de datos:

```bash
# Con Docker activo:
docker exec -i evm_postgres psql -U evm_user -d evm_db < db/import.sql
```

O si tienes `psql` instalado localmente:

```bash
psql -h localhost -U evm_user -d evm_db -f db/import.sql
```

> **Nota:** SQLAlchemy también crea las tablas automáticamente al iniciar el backend. El script SQL es necesario únicamente si deseas cargar los datos de ejemplo.

---

### 3. Backend (FastAPI)

#### Crear y activar el entorno virtual

```bash
# Windows (PowerShell)
python -m venv .venv
Set-ExecutionPolicy -Scope Process -ExecutionPolicy RemoteSigned
.\.venv\Scripts\Activate.ps1

# macOS / Linux
python3 -m venv .venv
source .venv/bin/activate
```

#### Instalar dependencias

```bash
pip install -r backend/requirements.txt
```

#### Variables de entorno

Crea un archivo `.env` en la raíz del proyecto (ya incluido en el repo con valores por defecto):

```env
DATABASE_URL=postgresql://evm_user:evm_pass@localhost:5432/evm_db
```

#### Iniciar el servidor

```bash
uvicorn backend.main:app --reload --host 127.0.0.1 --port 8000
```

El backend queda disponible en: `http://127.0.0.1:8000`

#### Documentación del API (OpenAPI / Swagger)

| URL | Descripción |
|---|---|
| `http://127.0.0.1:8000/api-docs` | Swagger UI interactivo |
| `http://127.0.0.1:8000/redoc` | ReDoc |
| `http://127.0.0.1:8000/openapi.json` | Especificación JSON |

---

### 4. Frontend (Angular)

```bash
cd frontend
npm install
npm start
```

El frontend queda disponible en: `http://localhost:4200`

> El proxy de desarrollo (`proxy.conf.json`) redirige automáticamente las llamadas a `/api` hacia el backend en el puerto `8000`.

---

## Ejecutar los tests

```bash
# Desde la raíz del proyecto, con el entorno virtual activo:
.venv\Scripts\python.exe -m pytest backend/tests/ --disable-warnings -v
```

---

## Estructura del proyecto

```
EVM_ValorGanado/
├── backend/
│   ├── main.py          # Endpoints FastAPI (CRUD proyectos, actividades, login)
│   ├── models.py        # Modelos SQLAlchemy
│   ├── database.py      # Conexión a la base de datos
│   ├── services/        # Lógica de cálculo EVM
│   └── tests/           # Tests unitarios e integración
├── frontend/
│   └── src/app/         # Componentes Angular
├── db/
│   └── import.sql       # Script SQL de inicialización (tablas + datos de ejemplo)
├── docker-compose.yml   # Contenedor PostgreSQL
├── .env                 # Variables de entorno (DATABASE_URL)
└── README.md
```

---

## Credenciales de ejemplo

Tras ejecutar `db/import.sql`, el sistema incluye un usuario de prueba:

| Campo | Valor |
|---|---|
| Email | `admin@demo.com` |
| Contraseña | `admin123` |
