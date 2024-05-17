from abc import ABC, abstractmethod
class Persona(ABC):
    def __init__(self):
        self = self

    def __init__(self, nombreUsuario, contraseña):
        self._nombreUsuairo = nombreUsuario
        self._contraseña = contraseña
        self.buscarUsuario()

    def __init__(self, nombre, rol, apellidoPaterno, apellidoMaterno, nombreUsuario, contraseña, email, telefono):
        self._nombre = nombre
        self._rol = rol
        self._apellidoPaterno = apellidoPaterno
        self._apellidoMaterno = apellidoMaterno
        self._nombreUsuairo = nombreUsuario
        self._contraseña = contraseña
        self._email = email
        self._telefono = telefono

    def _buscarUsuario():
        return ''
    
    def setNombre(self, nombre):
        self._nombre = nombre
    
    def getNombre(self):
        return self._nombre
    
    def setRol(self, rol):
        self._rol = rol
    
    def getNombre(self):
        return self._rol
    
    def setApellidoPaterno(self, apellido):
        self._apellidoPaterno = apellido
    
    def getApellidoPaterno(self):
        return self._apellidoPaterno
    
    def setApellidoMaterno(self, apellido):
        self._apellidoMaterno = apellido
    
    def getApellidoMaterno(self):
        return self._apellidoMaterno
    
    def setNombreUsuario(self, nombreUsuario):
        self._nombreUsuario = nombreUsuario
    
    def getNombreUsuario(self):
        return self._nombreUsuario
    
    def setContraseña(self, contraseña):
        self._contraseña = contraseña
    
    def getContraseña(self):
        return self._contraseña
    
    def setEmail(self, email):
        self._email = email
    
    def getEmail(self):
        return self._email
    
    def setTelefono(self, telefono):
        self._telefono = telefono
    
    def getTelefono(self):
        return self._telefono