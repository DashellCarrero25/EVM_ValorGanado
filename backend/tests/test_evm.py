import pytest
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import evm


class ActividadStub:
    def __init__(self, bac, avance_planificado, avance_real, ac):
        self.bac = bac
        self.avance_planificado = avance_planificado
        self.avance_real = avance_real
        self.ac = ac

def test_calcular_pv():
    assert evm.calcular_pv(1000, 50) == 500
    assert evm.calcular_pv(2000, 0) == 0
    assert evm.calcular_pv(1500, 100) == 1500

def test_calcular_ev():
    assert evm.calcular_ev(1000, 25) == 250
    assert evm.calcular_ev(2000, 0) == 0
    assert evm.calcular_ev(1500, 100) == 1500

def test_calcular_ac():
    assert evm.calcular_ac(500) == 500
    assert evm.calcular_ac(0) == 0

def test_calcular_cv():
    assert evm.calcular_cv(500, 400) == 100
    assert evm.calcular_cv(300, 400) == -100

def test_calcular_sv():
    assert evm.calcular_sv(500, 400) == 100
    assert evm.calcular_sv(300, 400) == -100

def test_calcular_cpi():
    assert evm.calcular_cpi(500, 400) == 1.25
    assert evm.calcular_cpi(0, 400) == 0
    assert evm.calcular_cpi(400, 0) == 0

def test_calcular_spi():
    assert evm.calcular_spi(500, 400) == 1.25
    assert evm.calcular_spi(0, 400) == 0
    assert evm.calcular_spi(400, 0) == 0

def test_calcular_eac():
    assert evm.calcular_eac(1000, 2) == 500
    assert evm.calcular_eac(1000, 0) == 0

def test_calcular_vac():
    assert evm.calcular_vac(1000, 800) == 200
    assert evm.calcular_vac(1000, 1200) == -200


def test_calcular_indicadores_consolidados_sin_actividades():
    indicadores = evm.calcular_indicadores_consolidados([])
    assert indicadores["pv"] == 0
    assert indicadores["ev"] == 0
    assert indicadores["ac"] == 0
    assert indicadores["interpretacion"]["cpi_estado"] == "Sin actividades"


def test_calcular_indicadores_consolidados_con_ac_cero():
    actividades = [
        ActividadStub(1000, 50, 25, 0),
        ActividadStub(500, 100, 100, 0),
    ]

    indicadores = evm.calcular_indicadores_consolidados(actividades)

    assert indicadores["pv"] == 1000
    assert indicadores["ev"] == 750
    assert indicadores["ac"] == 0
    assert indicadores["cpi"] == 0
    assert indicadores["spi"] == 0.75


def test_interpretaciones_evm():
    assert evm.interpretar_cpi(1.1) == "Bajo presupuesto (óptimo)"
    assert evm.interpretar_cpi(1.0) == "En presupuesto"
    assert evm.interpretar_cpi(0.8) == "Sobre presupuesto (riesgo)"
    assert evm.interpretar_spi(1.1) == "Adelantado al cronograma (óptimo)"
    assert evm.interpretar_spi(1.0) == "En cronograma"
    assert evm.interpretar_spi(0.8) == "Atrasado (riesgo)"
