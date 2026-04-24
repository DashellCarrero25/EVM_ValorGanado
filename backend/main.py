import os
import sys
from fastapi import FastAPI, HTTPException, Depends, status
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session
from pydantic import BaseModel
from typing import Annotated

# Permitir importaciones absolutas y relativas desde cualquier ubicación
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from backend.models import Usuario
from backend.database import SessionLocal


SECRET_KEY = os.getenv("SECRET_KEY", "supersecret")
ALGORITHM = "HS256"

# --- Diagnóstico de conexión a la base de datos ---
from sqlalchemy import text
print("[EVM] DATABASE_URL:", os.getenv("DATABASE_URL"))
try:
    db_diag = SessionLocal()
    print("[EVM] Usuarios en DB:", db_diag.execute(text("SELECT email FROM usuarios")).fetchall())
    db_diag.close()
except Exception as e:
    import traceback
    print("[EVM] ERROR de conexión a la base de datos:")
    traceback.print_exc()

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

class LoginRequest(BaseModel):
    email: str
    password: str

class LoginResponse(BaseModel):
    access_token: str
    token_type: str = "bearer"
    usuario: dict

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

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
    try:
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
    except Exception as e:
        import traceback
        traceback.print_exc()
        raise HTTPException(status_code=500, detail=f"Internal Server Error: {e}")
