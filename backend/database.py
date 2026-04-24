import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from backend.models import Base

# Cargar variables de entorno desde .env si existe
from dotenv import load_dotenv
load_dotenv(os.path.join(os.path.dirname(os.path.dirname(__file__)), '.env'))

DATABASE_URL = os.getenv("DATABASE_URL", "postgresql://evm_user:evm_pass@localhost:5432/evm_db")

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Crear tablas si no existen
Base.metadata.create_all(bind=engine)
