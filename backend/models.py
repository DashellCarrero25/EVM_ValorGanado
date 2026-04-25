from sqlalchemy import Column, Integer, String, Boolean, Date, Text, ForeignKey
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Proyecto(Base):
    __tablename__ = "proyectos"
    id = Column(Integer, primary_key=True)
    nombre = Column(String, nullable=False)
    descripcion = Column(Text, nullable=True)
    fecha_inicio = Column(Date, nullable=False)
    fecha_fin = Column(Date, nullable=True)
    usuario_responsable_id = Column(Integer, ForeignKey("usuarios.id"), nullable=False)


# Modelo Actividad para EVM
from sqlalchemy import ForeignKey, Float

class Actividad(Base):
    __tablename__ = "actividades"
    id = Column(Integer, primary_key=True)
    proyecto_id = Column(Integer, ForeignKey("proyectos.id"), nullable=False)
    nombre = Column(String, nullable=False)
    bac = Column(Float, nullable=False)  # Budget at Completion
    avance_planificado = Column(Float, nullable=False)  # % planificado (0-100)
    avance_real = Column(Float, nullable=False)  # % completado (0-100)
    ac = Column(Float, nullable=False)  # Actual Cost
    fecha_inicio = Column(Date, nullable=True)
    fecha_fin = Column(Date, nullable=True)

class Usuario(Base):
    __tablename__ = "usuarios"
    id = Column(Integer, primary_key=True)
    email = Column(String, unique=True, nullable=False)
    password_hash = Column(String, nullable=False)
    nombre = Column(String, nullable=False)
    activo = Column(Boolean, nullable=False, default=True)
