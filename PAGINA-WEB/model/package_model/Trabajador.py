import Persona
class Trabajador(Persona):
    
    def __init__(self, trabajadorId, cuadrillaId):
        self._tranbajadorId = trabajadorId
        self._cuadrillaId = cuadrillaId
    
    def get_trabajadorId(self):
        return self._trabajadorId

    def set_trabajadorId(self, trabajadorId):
        self._trabajadorId = trabajadorId

    def get_cuadrillaId(self):
        return self._cuadrillaId

    def set_cuadrillaId(self, cuadrillaId):
        self._cuadrillaId = cuadrillaId