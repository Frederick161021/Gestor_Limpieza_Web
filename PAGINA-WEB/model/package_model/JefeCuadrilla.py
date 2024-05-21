from model.package_model.Persona import Persona
from model.package_model.Conexion import Conexion

class JefeCuadrilla(Persona):

    def notificarCuadrilla(activiadad):
        return ''

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
        
    
    