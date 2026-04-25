"""Utilidades puras para indicadores EVM."""

from collections.abc import Iterable
from typing import Any

def calcular_pv(bac: float, porcentaje_planificado: float) -> float:
    """Planned Value (PV): BAC * % planificado"""
    return bac * (porcentaje_planificado / 100.0)

def calcular_ev(bac: float, porcentaje_completado: float) -> float:
    """Earned Value (EV): BAC * % completado"""
    return bac * (porcentaje_completado / 100.0)

def calcular_ac(ac: float) -> float:
    """Actual Cost (AC): Costo real incurrido"""
    return ac

def calcular_cv(ev: float, ac: float) -> float:
    """Cost Variance (CV): EV - AC"""
    return ev - ac

def calcular_sv(ev: float, pv: float) -> float:
    """Schedule Variance (SV): EV - PV"""
    return ev - pv

def calcular_cpi(ev: float, ac: float) -> float:
    """Cost Performance Index (CPI): EV / AC"""
    return ev / ac if ac != 0 else 0.0

def calcular_spi(ev: float, pv: float) -> float:
    """Schedule Performance Index (SPI): EV / PV"""
    return ev / pv if pv != 0 else 0.0

def calcular_eac(bac: float, cpi: float) -> float:
    """Estimate at Completion (EAC): BAC / CPI"""
    return bac / cpi if cpi != 0 else 0.0

def calcular_vac(bac: float, eac: float) -> float:
    """Variance at Completion (VAC): BAC - EAC"""
    return bac - eac


def interpretar_cpi(cpi: float) -> str:
    """Interpreta el estado de costos a partir del CPI."""
    if cpi == 0:
        return "Sin avance suficiente"
    if cpi > 1.05:
        return "Bajo presupuesto (óptimo)"
    if cpi >= 0.95:
        return "En presupuesto"
    return "Sobre presupuesto (riesgo)"


def interpretar_spi(spi: float) -> str:
    """Interpreta el estado del cronograma a partir del SPI."""
    if spi == 0:
        return "Sin avance suficiente"
    if spi > 1.05:
        return "Adelantado al cronograma (óptimo)"
    if spi >= 0.95:
        return "En cronograma"
    return "Atrasado (riesgo)"


def calcular_indicadores(bac: float, avance_planificado: float, avance_real: float, ac: float) -> dict[str, Any]:
    """Calcula los indicadores EVM de una actividad a partir de sus insumos."""
    pv = calcular_pv(bac, avance_planificado)
    ev = calcular_ev(bac, avance_real)
    ac_total = calcular_ac(ac)
    cv = calcular_cv(ev, ac_total)
    sv = calcular_sv(ev, pv)
    cpi = calcular_cpi(ev, ac_total)
    spi = calcular_spi(ev, pv)
    eac = calcular_eac(bac, cpi)
    vac = calcular_vac(bac, eac)
    return {
        "pv": round(pv, 2),
        "ev": round(ev, 2),
        "ac": round(ac_total, 2),
        "cv": round(cv, 2),
        "sv": round(sv, 2),
        "cpi": round(cpi, 3),
        "spi": round(spi, 3),
        "eac": round(eac, 2),
        "vac": round(vac, 2),
        "interpretacion": {
            "cpi_estado": interpretar_cpi(cpi),
            "spi_estado": interpretar_spi(spi),
        },
    }


def calcular_indicadores_consolidados(actividades: Iterable[Any]) -> dict[str, Any]:
    """Consolida indicadores EVM de un proyecto a partir de sus actividades."""
    actividades = list(actividades)
    if not actividades:
        return {
            "pv": 0.0,
            "ev": 0.0,
            "ac": 0.0,
            "cv": 0.0,
            "sv": 0.0,
            "cpi": 0.0,
            "spi": 0.0,
            "eac": 0.0,
            "vac": 0.0,
            "interpretacion": {
                "cpi_estado": "Sin actividades",
                "spi_estado": "Sin actividades",
            },
        }

    bac_total = sum(float(actividad.bac) for actividad in actividades)
    pv_total = sum(calcular_pv(float(actividad.bac), float(actividad.avance_planificado)) for actividad in actividades)
    ev_total = sum(calcular_ev(float(actividad.bac), float(actividad.avance_real)) for actividad in actividades)
    ac_total = sum(calcular_ac(float(actividad.ac)) for actividad in actividades)
    cv_total = calcular_cv(ev_total, ac_total)
    sv_total = calcular_sv(ev_total, pv_total)
    cpi_total = calcular_cpi(ev_total, ac_total)
    spi_total = calcular_spi(ev_total, pv_total)
    eac_total = calcular_eac(bac_total, cpi_total)
    vac_total = calcular_vac(bac_total, eac_total)

    return {
        "pv": round(pv_total, 2),
        "ev": round(ev_total, 2),
        "ac": round(ac_total, 2),
        "cv": round(cv_total, 2),
        "sv": round(sv_total, 2),
        "cpi": round(cpi_total, 3),
        "spi": round(spi_total, 3),
        "eac": round(eac_total, 2),
        "vac": round(vac_total, 2),
        "interpretacion": {
            "cpi_estado": interpretar_cpi(cpi_total),
            "spi_estado": interpretar_spi(spi_total),
        },
    }
