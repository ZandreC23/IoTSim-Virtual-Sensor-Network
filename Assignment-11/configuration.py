class Configuration:
    def __init__(self):
        self._update_frequency = 5
    
    def get_update_frequency(self) -> int:
        return self._update_frequency