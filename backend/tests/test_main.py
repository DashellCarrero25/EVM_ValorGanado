import sys
import os
import pytest
from fastapi.testclient import TestClient

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from main import app

client = TestClient(app)

def test_login_success():
    # Asume que existe un usuario de prueba en la base de datos
    response = client.post("/api/login", json={"email": "dashell@correo.com", "password": "contra1234"})
    assert response.status_code == 200
    data = response.json()
    assert "access_token" in data
    assert data["usuario"]["email"] == "dashell@correo.com"

def test_login_fail():
    response = client.post("/api/login", json={"email": "noexiste@correo.com", "password": "x"})
    assert response.status_code == 401

def test_crud_proyecto():
    # Crear
    response = client.post("/api/proyectos", json={
        "nombre": "Proyecto Test",
        "descripcion": "desc",
        "fecha_inicio": "2024-01-01",
        "fecha_fin": "2024-12-31",
        "usuario_responsable_id": 1
    })
    assert response.status_code == 201
    data = response.json()
    assert data["nombre"] == "Proyecto Test"
    pid = data["id"]
    # Listar
    response = client.get("/api/proyectos")
    assert response.status_code == 200
    assert any(p["id"] == pid for p in response.json())
    # Obtener
    response = client.get(f"/api/proyectos/{pid}")
    assert response.status_code == 200
    # Actualizar
    response = client.put(f"/api/proyectos/{pid}", json={"nombre": "Proyecto Modificado", "usuario_responsable_id": 1})
    assert response.status_code == 200
    assert response.json()["nombre"] == "Proyecto Modificado"
    # Eliminar
    response = client.delete(f"/api/proyectos/{pid}")
    assert response.status_code == 204

def test_crud_actividad():
    # Crear proyecto base
    response = client.post("/api/proyectos", json={
        "nombre": "Proyecto para Actividad",
        "descripcion": "desc",
        "fecha_inicio": "2024-01-01",
        "fecha_fin": "2024-12-31",
        "usuario_responsable_id": 1
    })
    assert response.status_code == 201
    proyecto_id = response.json()["id"]
    # Crear actividad
    actividad_data = {
        "proyecto_id": proyecto_id,
        "nombre": "Act 1",
        "bac": 1000,
        "avance_planificado": 50,
        "avance_real": 20,
        "ac": 200,
        "fecha_inicio": "2024-01-01",
        "fecha_fin": "2024-01-31"
    }
    response = client.post("/api/actividades", json=actividad_data)
    assert response.status_code == 201
    data = response.json()
    assert data["nombre"] == "Act 1"
    aid = data["id"]
    # Listar
    response = client.get("/api/actividades")
    assert response.status_code == 200
    assert any(a["id"] == aid for a in response.json())
    # Obtener
    response = client.get(f"/api/actividades/{aid}")
    assert response.status_code == 200
    # Actualizar
    response = client.put(f"/api/actividades/{aid}", json={"nombre": "Act 1 Modificado"})
    assert response.status_code == 200
    assert response.json()["nombre"] == "Act 1 Modificado"
    # Eliminar
    response = client.delete(f"/api/actividades/{aid}")
    assert response.status_code == 204
    # Eliminar proyecto base
    response = client.delete(f"/api/proyectos/{proyecto_id}")
    assert response.status_code == 204


def test_resumen_proyecto_evm():
    response = client.post("/api/proyectos", json={
        "nombre": "Proyecto Resumen",
        "descripcion": "desc",
        "fecha_inicio": "2024-01-01",
        "fecha_fin": "2024-12-31",
        "usuario_responsable_id": 1
    })
    assert response.status_code == 201
    proyecto_id = response.json()["id"]

    response = client.post("/api/actividades", json={
        "proyecto_id": proyecto_id,
        "nombre": "Act Resumen",
        "bac": 1000,
        "avance_planificado": 50,
        "avance_real": 40,
        "ac": 300,
        "fecha_inicio": "2024-01-01",
        "fecha_fin": "2024-01-31"
    })
    assert response.status_code == 201
    actividad_id = response.json()["id"]

    response = client.get(f"/api/proyectos/{proyecto_id}/resumen-evm")
    assert response.status_code == 200
    data = response.json()
    assert data["proyecto_id"] == proyecto_id
    assert data["total_actividades"] == 1
    assert data["indicadores"]["pv"] == 500
    assert data["indicadores"]["ev"] == 400
    assert data["indicadores"]["ac"] == 300
    assert data["indicadores"]["interpretacion"]["cpi_estado"]

    response = client.delete(f"/api/actividades/{actividad_id}")
    assert response.status_code == 204
    response = client.delete(f"/api/proyectos/{proyecto_id}")
    assert response.status_code == 204


def test_resumen_proyecto_sin_actividades():
    response = client.post("/api/proyectos", json={
        "nombre": "Proyecto Vacio",
        "descripcion": "desc",
        "fecha_inicio": "2024-01-01",
        "fecha_fin": "2024-12-31",
        "usuario_responsable_id": 1
    })
    assert response.status_code == 201
    proyecto_id = response.json()["id"]

    response = client.get(f"/api/proyectos/{proyecto_id}/resumen-evm")
    assert response.status_code == 200
    data = response.json()
    assert data["total_actividades"] == 0
    assert data["indicadores"]["pv"] == 0
    assert data["indicadores"]["interpretacion"]["cpi_estado"] == "Sin actividades"

    response = client.delete(f"/api/proyectos/{proyecto_id}")
    assert response.status_code == 204
