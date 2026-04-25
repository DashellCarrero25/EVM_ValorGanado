-- Tabla de usuarios
CREATE TABLE usuarios (
    id SERIAL PRIMARY KEY,
    email VARCHAR(100) NOT NULL UNIQUE,
    password_hash VARCHAR(255) NOT NULL,
    nombre VARCHAR(100) NOT NULL,
    activo BOOLEAN NOT NULL DEFAULT TRUE
);

-- Tabla de proyectos
CREATE TABLE proyectos (
    id SERIAL PRIMARY KEY,
    nombre VARCHAR(100) NOT NULL,
    descripcion TEXT,
    fecha_inicio DATE NOT NULL,
    fecha_fin DATE,
    usuario_responsable_id INTEGER NOT NULL REFERENCES usuarios(id) ON DELETE CASCADE
);

-- Tabla de actividades
CREATE TABLE actividades (
    id SERIAL PRIMARY KEY,
    proyecto_id INTEGER NOT NULL REFERENCES proyectos(id) ON DELETE CASCADE,
    nombre VARCHAR(100) NOT NULL,
    bac NUMERIC(14,2) NOT NULL,
    avance_planificado NUMERIC(5,2) NOT NULL,
    avance_real NUMERIC(5,2) NOT NULL,
    ac NUMERIC(14,2) NOT NULL
    fecha_inicio DATE,
    fecha_fin DATE
);

-- Datos de ejemplo
INSERT INTO usuarios (email, password_hash, nombre, activo) VALUES
    ('admin@demo.com', 'admin123', 'Admin Demo', TRUE);

INSERT INTO proyectos (nombre, descripcion, fecha_inicio, fecha_fin, usuario_responsable_id) VALUES
    ('Proyecto Ejemplo', 'Proyecto de ejemplo para pruebas', '2026-04-01', '2026-12-31', 1);

INSERT INTO actividades (proyecto_id, nombre, bac, avance_planificado, avance_real, ac) VALUES
    (1, 'Actividad Inicial', 10000.00, 20.00, 10.00, 1200.00);
