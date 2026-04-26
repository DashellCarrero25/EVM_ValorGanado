"""Servicios para ensamblar respuestas EVM y de proyecto."""

from collections.abc import Iterable
from typing import Any

from backend import evm


def proyecto_to_response(proyecto: Any) -> dict[str, Any]:
    return {
        "id": proyecto.id,
        "nombre": proyecto.nombre,
        "descripcion": proyecto.descripcion,
        "fecha_inicio": proyecto.fecha_inicio.isoformat() if proyecto.fecha_inicio else None,
        "fecha_fin": proyecto.fecha_fin.isoformat() if proyecto.fecha_fin else None,
        "usuario_responsable_id": proyecto.usuario_responsable_id,
    }


def actividad_to_response(actividad: Any) -> dict[str, Any]:
    indicadores = evm.calcular_indicadores(
        bac=actividad.bac,
        avance_planificado=actividad.avance_planificado,
        avance_real=actividad.avance_real,
        ac=actividad.ac,
    )

    return {
        "id": actividad.id,
        "proyecto_id": actividad.proyecto_id,
        "nombre": actividad.nombre,
        "bac": actividad.bac,
        "avance_planificado": actividad.avance_planificado,
        "avance_real": actividad.avance_real,
        "ac": actividad.ac,
        "fecha_inicio": actividad.fecha_inicio.isoformat() if actividad.fecha_inicio else None,
        "fecha_fin": actividad.fecha_fin.isoformat() if actividad.fecha_fin else None,
        "evm": indicadores,
    }


def resumen_proyecto_to_response(proyecto: Any, actividades: Iterable[Any]) -> dict[str, Any]:
    actividades = list(actividades)
    indicadores = evm.calcular_indicadores_consolidados(actividades)

    return {
        "proyecto_id": proyecto.id,
        "proyecto_nombre": proyecto.nombre,
        "total_actividades": len(actividades),
        "indicadores": indicadores,
    }
