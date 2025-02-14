import pytest
from Bombillo_Manual import Interruptor
from Sensor_Movimiento import Sensores

@pytest.fixture
def manual():
    return Interruptor(test_mode=True)  # Si es necesario el modo de prueba

@pytest.fixture
def sensor ():
    return Sensores(test_mode=True)

def test_estado_inicial_interruptor(manual):    
    assert manual.state is False  # Estado inicial, debe estar apagado

def test_estado_inicial(manual):       
    manual.señal("ON") 
    assert manual.state is True  # Debe encenderse
    
def test_apagado(manual):  
    manual.señal("OFF")  
    assert manual.state is False  # Debe apagarse

def test_sensor_initial_state(sensor):  
    assert sensor.luz_on is False  # Al inicio, debe estar apagado

def test_sensor_detect_person(sensor):    
    sensor.hay_persona(True)
    assert sensor.luz_on is True  # Debe encenderse si hay una persona

def test_sensor_no_person(sensor):    
    sensor.hay_persona(False)
    assert sensor.luz_on is False  # Debe apagarse si no hay nadie


