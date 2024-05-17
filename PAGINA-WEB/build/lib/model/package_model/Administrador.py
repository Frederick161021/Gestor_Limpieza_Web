import Persona

class Administrador(Persona):

    def __init__(self, administradorId):
        self._administradorId = administradorId

    def setAdminsitradorId(self, administradorId):
        self._administradorId = administradorId

    def getAdministradorId(self):
        return self._administradorId

    def notificarJefeCuadrilla(jefeCuadrilla, nuevoTrabajo):
        return ''