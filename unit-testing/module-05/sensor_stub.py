class SensorStub:
    def __init__(self, pressure):
        self._pressure = pressure
        
    def sample_pressure(self):
        return self._pressure