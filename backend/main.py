# --- Dependencias y configuración base ---
import os
import sys
from fastapi import FastAPI, HTTPException, Depends, status
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session
from pydantic import BaseModel, ConfigDict
from typing import Annotated, List, Optional

# Permitir importaciones absolutas y relativas desde cualquier ubicación
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from backend.models import Usuario, Proyecto, Actividad
from backend.database import SessionLocal
from backend.services import evm_service

# --- FastAPI app y CORS ---
app = FastAPI(
    title="EVM Valor Ganado API",
    description="API para autenticación y gestión de proyectos EVM.",
    version="1.0.0",
    docs_url="/api-docs",
    redoc_url="/redoc"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

ACTIVIDAD_NO_ENCONTRADA = "Actividad no encontrada"
PROYECTO_NO_ENCONTRADO = "Proyecto no encontrado"
RESPUESTA_404_ACTIVIDAD = {404: {"description": ACTIVIDAD_NO_ENCONTRADA}}
RESPUESTA_404_PROYECTO = {404: {"description": PROYECTO_NO_ENCONTRADO}}

# --- Utilidad de sesión DB ---
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# --- Modelos Pydantic ---
class ProyectoBase(BaseModel):
    nombre: str
    descripcion: Optional[str] = None
    fecha_inicio: str  # ISO date, obligatorio
    fecha_fin: Optional[str] = None
    usuario_responsable_id: int

class ProyectoCreate(ProyectoBase):
    pass

class ProyectoUpdate(BaseModel):
    nombre: Optional[str] = None
    descripcion: Optional[str] = None
    fecha_inicio: Optional[str] = None
    fecha_fin: Optional[str] = None
    usuario_responsable_id: Optional[int] = None

class ProyectoOut(ProyectoBase):
    id: int
    model_config = ConfigDict(from_attributes=True)

class ActividadBase(BaseModel):
    proyecto_id: int
    nombre: str
    bac: float
    avance_planificado: float
    avance_real: float
    ac: float
    fecha_inicio: Optional[str] = None
    fecha_fin: Optional[str] = None

class ActividadCreate(ActividadBase):
    pass

class ActividadUpdate(BaseModel):
    nombre: Optional[str] = None
    bac: Optional[float] = None
    avance_planificado: Optional[float] = None
    avance_real: Optional[float] = None
    ac: Optional[float] = None
    fecha_inicio: Optional[str] = None
    fecha_fin: Optional[str] = None

class InterpretacionEVM(BaseModel):
    cpi_estado: str
    spi_estado: str

class IndicadoresEVM(BaseModel):
    pv: float
    ev: float
    ac: float
    cv: float
    sv: float
    cpi: float
    spi: float
    eac: float
    vac: float
    interpretacion: InterpretacionEVM

class ActividadOut(ActividadBase):
    id: int
    evm: IndicadoresEVM
    model_config = ConfigDict(from_attributes=True)


class ResumenProyectoEVM(BaseModel):
    proyecto_id: int
    proyecto_nombre: str
    total_actividades: int
    indicadores: IndicadoresEVM

# --- Endpoints CRUD Actividades ---
@app.post("/api/actividades", response_model=ActividadOut, status_code=201, summary="Crear actividad")
def crear_actividad(actividad: ActividadCreate, db: Annotated[Session, Depends(get_db)]):
    db_actividad = Actividad(**actividad.dict())
    db.add(db_actividad)
    db.commit()
    db.refresh(db_actividad)
    return evm_service.actividad_to_response(db_actividad)

@app.get("/api/actividades", response_model=List[ActividadOut], summary="Listar actividades")
def listar_actividades(db: Annotated[Session, Depends(get_db)]):
    actividades = db.query(Actividad).all()
    return [evm_service.actividad_to_response(a) for a in actividades]

@app.get("/api/actividades/{actividad_id}", response_model=ActividadOut, summary="Obtener actividad por ID", responses=RESPUESTA_404_ACTIVIDAD)
def obtener_actividad(actividad_id: int, db: Annotated[Session, Depends(get_db)]):
    actividad = db.query(Actividad).filter(Actividad.id == actividad_id).first()
    if not actividad:
        raise HTTPException(status_code=404, detail=ACTIVIDAD_NO_ENCONTRADA)
    return evm_service.actividad_to_response(actividad)

@app.put("/api/actividades/{actividad_id}", response_model=ActividadOut, summary="Actualizar actividad", responses=RESPUESTA_404_ACTIVIDAD)
def actualizar_actividad(actividad_id: int, datos: ActividadUpdate, db: Annotated[Session, Depends(get_db)]):
    actividad = db.query(Actividad).filter(Actividad.id == actividad_id).first()
    if not actividad:
        raise HTTPException(status_code=404, detail=ACTIVIDAD_NO_ENCONTRADA)
    for attr, value in datos.dict(exclude_unset=True).items():
        if value is not None:
            setattr(actividad, attr, value)
    db.commit()
    db.refresh(actividad)
    return evm_service.actividad_to_response(actividad)

@app.delete("/api/actividades/{actividad_id}", status_code=204, summary="Eliminar actividad", responses=RESPUESTA_404_ACTIVIDAD)
def eliminar_actividad(actividad_id: int, db: Annotated[Session, Depends(get_db)]):
    actividad = db.query(Actividad).filter(Actividad.id == actividad_id).first()
    if not actividad:
        raise HTTPException(status_code=404, detail=ACTIVIDAD_NO_ENCONTRADA)
    db.delete(actividad)
    db.commit()
    return None

# --- Endpoints CRUD Proyectos ---
@app.post("/api/proyectos", response_model=ProyectoOut, status_code=201, summary="Crear proyecto")
def crear_proyecto(proyecto: ProyectoCreate, db: Annotated[Session, Depends(get_db)]):
    db_proyecto = Proyecto(
        nombre=proyecto.nombre,
        descripcion=proyecto.descripcion,
        fecha_inicio=proyecto.fecha_inicio,
        fecha_fin=proyecto.fecha_fin,
        usuario_responsable_id=proyecto.usuario_responsable_id
    )
    db.add(db_proyecto)
    db.commit()
    db.refresh(db_proyecto)
    return evm_service.proyecto_to_response(db_proyecto)

@app.get("/api/proyectos", response_model=List[ProyectoOut], summary="Listar proyectos")
def listar_proyectos(db: Annotated[Session, Depends(get_db)]):
    return [evm_service.proyecto_to_response(p) for p in db.query(Proyecto).all()]

@app.get("/api/proyectos/{proyecto_id}", response_model=ProyectoOut, summary="Obtener proyecto por ID", responses=RESPUESTA_404_PROYECTO)
def obtener_proyecto(proyecto_id: int, db: Annotated[Session, Depends(get_db)]):
    proyecto = db.query(Proyecto).filter(Proyecto.id == proyecto_id).first()
    if not proyecto:
        raise HTTPException(status_code=404, detail=PROYECTO_NO_ENCONTRADO)
    return evm_service.proyecto_to_response(proyecto)


@app.get("/api/proyectos/{proyecto_id}/resumen-evm", response_model=ResumenProyectoEVM, summary="Obtener resumen EVM del proyecto", responses=RESPUESTA_404_PROYECTO)
def obtener_resumen_proyecto(proyecto_id: int, db: Annotated[Session, Depends(get_db)]):
    proyecto = db.query(Proyecto).filter(Proyecto.id == proyecto_id).first()
    if not proyecto:
        raise HTTPException(status_code=404, detail=PROYECTO_NO_ENCONTRADO)
    actividades = db.query(Actividad).filter(Actividad.proyecto_id == proyecto_id).all()
    return evm_service.resumen_proyecto_to_response(proyecto, actividades)

@app.put("/api/proyectos/{proyecto_id}", response_model=ProyectoOut, summary="Actualizar proyecto", responses=RESPUESTA_404_PROYECTO)
def actualizar_proyecto(proyecto_id: int, datos: ProyectoUpdate, db: Annotated[Session, Depends(get_db)]):
    proyecto = db.query(Proyecto).filter(Proyecto.id == proyecto_id).first()
    if not proyecto:
        raise HTTPException(status_code=404, detail=PROYECTO_NO_ENCONTRADO)
    for attr, value in datos.dict(exclude_unset=True).items():
        if value is not None:
            setattr(proyecto, attr, value)
    db.commit()
    db.refresh(proyecto)
    return evm_service.proyecto_to_response(proyecto)

@app.delete("/api/proyectos/{proyecto_id}", status_code=204, summary="Eliminar proyecto", responses=RESPUESTA_404_PROYECTO)
def eliminar_proyecto(proyecto_id: int, db: Annotated[Session, Depends(get_db)]):
    proyecto = db.query(Proyecto).filter(Proyecto.id == proyecto_id).first()
    if not proyecto:
        raise HTTPException(status_code=404, detail=PROYECTO_NO_ENCONTRADO)
    db.delete(proyecto)
    db.commit()
    return None

# --- Login ---
class LoginRequest(BaseModel):
    email: str
    password: str

class LoginResponse(BaseModel):
    access_token: str
    token_type: str = "bearer"
    usuario: dict

@app.post(
    "/api/login",
    response_model=LoginResponse,
    summary="Autenticación de usuario",
    description="Permite a un usuario autenticarse con correo y contraseña. Retorna un token de sesión y los datos mínimos del usuario.",
    responses={
        200: {"description": "Login exitoso, retorna token y datos de usuario."},
        401: {"description": "Credenciales incorrectas o usuario no existe."},
        422: {"description": "Datos de entrada inválidos."},
        500: {"description": "Error interno del servidor."}
    }
)
def login(request: LoginRequest, db: Annotated[Session, Depends(get_db)]):
    user = db.query(Usuario).filter(Usuario.email == request.email).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Usuario o contraseña incorrectos")
    # Solo para pruebas/demo: comparar texto plano
    if request.password != user.password_hash:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Usuario o contraseña incorrectos")
    # Generar token simple (uuid4) solo para usuarios válidos
    from uuid import uuid4
    token = str(uuid4())
    return LoginResponse(access_token=token, usuario={"id": user.id, "email": user.email, "nombre": user.nombre})
