import pytest
from Bombillo_Manual import Interruptor
from Sensor_Movimiento import Sensores

@pytest.fixture
def Manual ():
    return Interruptor()

@pytest.fixture
def Sensor ():
    return Sensores()

def test_estado_inicial_interruptor(Interruptor):    
    assert Interruptor.state is False  # Estado inicial, debe estar apagado

def test_encendido_apagado(Interruptor):       
    assert Interruptor.state is True  # Debe encenderse
    
def test_apagado(Interruptor):  
    assert Interruptor.state is False  # Debe apagarse

def test_sensor_initial_state(Sensores):  
    assert Sensores.luz_on is False  # Al inicio, debe estar apagado

def test_sensor_detect_person(Sensores):    
    assert Sensores.luz_on is True  # Debe encenderse si hay una persona

def test_sensor_no_person(Sensores):    
    assert Sensores.luz_on is False  # Debe apagarse si no hay nadie


