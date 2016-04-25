import pytest
from alarm import Alarm
from sensor_stub import SensorStub
import pytest_mock
from sensor import Sensor
from mock import Mock
#mocking an object 
# mockObject = Mock(Sensor)
# def sample_pressure():
#     # add exceptions here as well for bad parameters
#     return 18
# mockObject.sample_pressure = Mock(side_effect=sample_pressure)

#stubbing an object
# mockObject = Mock(Sensor)
# mockObject.sample_pressure = Mock(return_value=DEFAULT=18)

@pytest.fixture
def high_sensor():
    return SensorStub(25)

@pytest.fixture
def low_sensor():
    return SensorStub(15)

@pytest.fixture
def normal_sensor():
    return SensorStub(18)    

@pytest.fixture
def alarm():
    return Alarm()
    
def test_alarm_is_off_by_default(alarm):
    alarm.check()
    assert not alarm.is_alarm_on
    
def test_check_too_low_pressure_sounds(low_sensor):
    alarm = Alarm(low_sensor)
    alarm.check()
    assert alarm.is_alarm_on
    
def test_check_too_high_pressure_sounds(high_sensor):
    alarm = Alarm(high_sensor)
    alarm.check()
    assert alarm.is_alarm_on
    

def test_check_normal_pressure_doesnt_sound_alarm_with_mock(mocker):
    test_sensor = Mock(Sensor)
    test_sensor.sample_pressure.return_value = 18
    alarm = Alarm(test_sensor)
    alarm.check()
    assert not alarm.is_alarm_on
    

def test_check_normal_pressure_doesnt_sound_alarm(normal_sensor):
    alarm = Alarm(normal_sensor)
    alarm.check()
    assert not alarm.is_alarm_on

