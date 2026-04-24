import pytest
from fastapi.testclient import TestClient

import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from main import app
from models import Usuario
from database import SessionLocal, engine
from sqlalchemy.orm import sessionmaker

client = TestClient(app)

# Setup test database (in-memory or test schema)
TestSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

def setup_test_user():
    db = TestSessionLocal()
    db.query(Usuario).delete()
    user = Usuario(
        correo="test@example.com",
        nombre="Test User",
        password="testpass123"  # Contraseña en texto plano para entorno demo/internal
    )
    db.add(user)
    db.commit()
    db.close()

@pytest.fixture(autouse=True)
def setup():
    setup_test_user()
    yield
    # Optionally clean up

def test_login_success():
    response = client.post("/api/login", json={"correo": "test@example.com", "password": "testpass123"})
    assert response.status_code == 200
    data = response.json()
    assert "access_token" in data
    assert data["usuario"]["correo"] == "test@example.com"

def test_login_wrong_password():
    response = client.post("/api/login", json={"correo": "test@example.com", "password": "wrongpass"})
    assert response.status_code == 401
    assert response.json()["detail"] == "Usuario o contraseña incorrectos"

def test_login_user_not_found():
    response = client.post("/api/login", json={"correo": "nouser@example.com", "password": "irrelevant"})
    assert response.status_code == 401
    assert response.json()["detail"] == "Usuario o contraseña incorrectos"
