from model.package_model.Persona import Persona
from model.package_model.Conexion import Conexion
from model.package_model.UsuarioDTO import UsuarioDTO

class Administrador(Persona):

    def agregarPersona(self, id, rolId, nombre, apellidoPaterno, apellidoMaterno, usuario, contraseña, correo, telefono):
        db = Conexion()
        con = db.connect()
        cursor = db.cursor()

        respuesta = 0

        try:
            cursor.execute('CALL crearPersona(%s, %s, %s, %s, %s, %s, %s, %s, %s)', (id, rolId, nombre, apellidoPaterno, apellidoMaterno, usuario, contraseña, correo, telefono))
            con.commit()
            respuesta  = 1
        except Exception as e:
            print("error")
        finally:
            cursor.close()
            db.close()
            return respuesta
    
    def buscarPersona(self, id):
        db = Conexion()
        con = db.connect()
        cursor = db.cursor()

        usuario = None

        try:
            cursor.execute('CALL consultarPorIdPersona(%s)', [id])
            usuario  = cursor.fetchall()
            usuario = usuario[0]
        except Exception as e:
            print("error")
        finally:
            cursor.close()
            db.close()
            return usuario
    
    def actualizarPersona(self, id, rolId, nombre, apellidoPaterno, apellidoMaterno, usuario, contraseña, correo, telfono):
        db = Conexion()
        con = db.connect()
        cursor = db.cursor()

        respuesta = 0

        try:
            cursor.execute('CALL actualizarPersona(%s, %s, %s, %s, %s, %s, %s, %s, %s)', (id, rolId, nombre, apellidoPaterno, apellidoMaterno, usuario, contraseña, correo, telfono))
            con.commit()
            respuesta  = 1
        except Exception as e:
            print("error")
        finally:
            cursor.close()
            db.close()
            return respuesta


    def eliminarPersona(self, id):
        db = Conexion()
        con = db.connect()
        cursor = db.cursor()

        respuesta = 0

        try:
            cursor.execute('CALL eliminarPersona(%s)', [id])
            con.commit()
            respuesta = 1
        except Exception as e:
            print("error")
        finally:
            cursor.close()
            db.close()
            return respuesta


    def getUsuarios(self):
        db = Conexion()
        db.connect()
        cursor = db.cursor()

        usuarios = None

        try:
            cursor.execute('CALL consultarPersona()')
            usuarios = cursor.fetchall()
        except Exception as e:
            print("error")
        finally:
            cursor.close()
            db.close()
            return usuarios
        


    def notificarJefeCuadrilla(jefeCuadrilla, nuevoTrabajo):
        return ''