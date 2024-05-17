class UsuarioDTO():

    _instance = None

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super().__new__(cls, *args, **kwargs)
        return cls._instance
    

    def getPersonaId(self):
        return self._personaId
    
    def getRolId(self):
        return self._rolId
    
    def getRol(self):
        return self._rol
    
    def getNombre(self):
        return self._nombre
    
    def getApellidoPaterno(self):
        return self._apellidoPaterno

    def getApellidoMaterno(self):
        return self._apellidoMaterno
    
    def getNombreUsuario(self):
        return self._nombreUsuario
    
    def getContraseña(self):
        return self._contraseña
    
    def getEmail(self):
        return self._email
    
    def getTelefono(self):
        return self._telfono
    
    def setData(self, personaId, rolId, rol, nombre, apellidoPaterno, apellidoMaterno, nombreUsuario, contraseña, email, telefono):
        self._personaId = personaId
        self._rolId = rolId
        self._rol = rol
        self._nombre = nombre
        self._apellidoPaterno = apellidoPaterno
        self._apellidoMaterno = apellidoMaterno
        self._nombreUsuario = nombreUsuario
        self._contraseña = contraseña
        self._email = email
        self._telfono = telefono

    @classmethod
    def cerroSesion(cls):
        cls._instance = None