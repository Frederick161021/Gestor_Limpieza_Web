from abc import ABC, abstractmethod
from model.package_model.Conexion import Conexion
from model.package_model.UsuarioDTO import UsuarioDTO


class Persona(ABC):
        

    def __init__(self):
        self._nombre = None
        self._rol = None
        self._apellidoPaterno = None
        self._apellidoMaterno = None
        self._nombreUsuario = None
        self._contraseña = None
        self._email = None
        self._telefono = None

    def inicializar(self, nombre, rol, apellidoPaterno, apellidoMaterno, nombreUsuario, contraseña, email, telefono):
        self._nombre = nombre
        self._rol = rol
        self._apellidoPaterno = apellidoPaterno
        self._apellidoMaterno = apellidoMaterno
        self._nombreUsuario = nombreUsuario
        self._contraseña = contraseña
        self._email = email
        self._telefono = telefono


    def getUsuario(self, usuario, contraseña):
        db = Conexion()
        con = db.connect()
        cursor = db.cursor()

        user = None

        try:
            cursor.execute('CALL consultarPorUsuarioPersona(%s)', [usuario])
            user = cursor.fetchall()
            if usuario == user[0][6]:
                print ('El nombre de usuario es correcto!')
                if contraseña == user[0][7]:
                    print('La contraseña es correcta!')
                    self._personaId = user [0][0]
                    self._rolId = user[0][1]
                    self._rol = user[0][2]
                    self._nombre = user[0][3]
                    self._apellidoPaterno = user[0][3]
                    self._apellidoMaterno = user[0][4]
                    self._nombreUsuario = user[0][5]
                    self._contraseña = user[0][6]
                    self._email = user[0][7]
                    self._telefono = user[0][8]
                    
                    userDTO = UsuarioDTO()
                    userDTO.setData(self._personaId, self._rolId, self._rol, self._nombre, self._apellidoPaterno, self._apellidoMaterno, self._nombreUsuario, self._contraseña, self._email, self._telefono)

                    print('Aceso al sistema!')
                else:
                    print('La contraseña no es correcta!')
            else:
                    print('El nombre del usuario no es correcto!')

        except Exception as e:
            print("error")
        finally:
            cursor.close()
            db.close()
            return user
        

    def getCuadrillaIdPertenece(self, personaId):

        db = Conexion()
        con = db.connect()
        cursor = db.cursor()

        cuadrillaId = None

        try:
            cursor.execute('CALL consultarCuadrillaPertenece(%s)', [personaId])
            data = cursor.fetchall()

            cuadrillaId = data[0][1]

        except Exception as e:
            print("error")
        finally:
            cursor.close()
            db.close()
            return cuadrillaId
        
        
    def getActiviadesPorEstatus(self, estatus, personaId):
        db = Conexion()
        con = db.connect()
        cursor = db.cursor()

        actividadesPendientes = None

        try:
            cursor.execute('CALL consultarPorEstatusActividad(%s, %s)', (estatus, personaId))
            actividadesPendientes = cursor.fetchall()
        except Exception as e:
            print("error")
        finally:
            cursor.close()
            db.close()
            return actividadesPendientes
        
    
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