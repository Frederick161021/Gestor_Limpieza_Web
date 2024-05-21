from model.package_model.Persona import Persona
from model.package_model.Conexion import Conexion
from model.package_model.UsuarioDTO import UsuarioDTO

class JefeCuadrilla(Persona):

    def getCuadrillaId(self, jefeId):
        db = Conexion()
        con = db.connect()
        cursor = db.cursor()

        cuadrillaId = None

        try:
            cursor.execute('CALL consultarCuadrillaIdPorPersonaId(%s)', [jefeId])
            cuadrillaId = cursor.fetchall()
        except Exception as e : 
            print('error')
        finally:
            cursor.close()
            db.close()
            return cuadrillaId 
        
    def getTrabajadores(self, cuadrillaId):
        db = Conexion()
        con = db.connect()
        cursor = db.cursor()

        trabajadores = None

        try:
            cursor.execute('CALL consultarTrabajadoresPorCuadrillaId(%s)', [cuadrillaId])
            trabajadores = cursor.fetchall()
        except Exception as e : 
            print('error')
        finally:
            cursor.close()
            db.close()
            return trabajadores 

    def notificarCuadrilla(self, actividad):
        cuadrillaId = self.getCuadrillaId(UsuarioDTO.getPersonaId())
        trabajadores = self.getTrabajadores(cuadrillaId)
        mensaje = "Se le a notificado de la actividad (%s) a los trabajadores:\n", actividad 
        for trabajador in trabajadores:
            mensaje += trabajador[0]
            mensaje += "\n"
        
        return mensaje

    def obtenerActiviadesPendientesAceptar(self):
        db = Conexion()
        con = db.connect()
        cursor = db.cursor()

        actividades = None

        try:
            cursor.execute('CALL traerActividadesPendientesAceptar()')
            actividades = cursor.fetchall()
        except Exception as e : 
            print('error')
        finally:
            cursor.close()
            db.close()
            return actividades   


    def actualizarEstatusActiviades(self, actividadId, estatus):
        db = Conexion()
        con = db.connect()
        cursor = db.cursor()

        respuesta = 0

        try:
            cursor.execute('CALL actualizarEstatusActividadN(%s, %s)', (actividadId, estatus))
            con.commit()
            respuesta = 1
        except Exception as e : 
            print('error')
        finally:
            cursor.close()
            db.close()
            return respuesta

    def obtenerCadillaIdDelJefe(self, jefeId):
        db = Conexion()
        con = db.connect()
        cursor = db.cursor()

        cuadrillaId = 0

        try:
            cursor.execute('CALL actualizarEstatusActividadN(%s)', [jefeId])
            cuadrillaId = cursor.fetchall()
        except Exception as e : 
            print('error')
        finally:
            cursor.close()
            db.close()
            return cuadrillaId
        
    
    def terminarActividad(self, comentarios, imagen):
        usuario = UsuarioDTO()
        actividadId = usuario.getActividadId();
        print(actividadId)
        print(comentarios)
        print(imagen)
        db = Conexion()
        con = db.connect()
        cursor = db.cursor()

        respuesta = 0

        try:
            cursor.execute('CALL terminarActividad(%s, %s, %s)', (actividadId, comentarios, imagen))
            con.commit()
            respuesta = 1
        except Exception as e : 
            print('error')
        finally:
            cursor.close()
            db.close()
            return respuesta