from model.package_model.Conexion import Conexion

class Actividad:

    def obtenerActvidades(self):
        db = Conexion()
        con = db.connect()
        cursor = db.cursor()

        actividades = None

        try:
            cursor.execute('CALL consultarHistorialActividad()')
            actividades = cursor.fetchall()
        except Exception as e :
            print('error')
        finally:
            cursor.close()
            db.close()
            return actividades
        
    def obtenerCudrillasNombre(self):
        db = Conexion()
        con = db.connect()
        cursor = db.cursor()

        cuadrillas = None

        try:
            cursor.execute('CALL consultarCuadrillaNombresActivas()')
            cuadrillas = cursor.fetchall()
        except Exception as e :
            print('error')
        finally:
            cursor.close()
            db.close()
            return cuadrillas 

    def obetenerColoniasNombre(self):
        db = Conexion()
        con = db.connect()
        cursor = db.cursor()

        colonias = None

        try:
            cursor.execute('CALL consultarColoniasNombre()')
            colonias = cursor.fetchall()
        except Exception as e :
            print('error')
        finally:
            cursor.close()
            db.close()
            return colonias 
        
    def agregarActividad(self, descripcion, fecha, cuadrillaId, coloniaId):
        db = Conexion()
        con = db.connect()
        cursor = db.cursor()

        respuesta = 0
        print(fecha)
        try:
            cursor.execute('CALL crearParaAdminHistorialActividad(%s, %s, %s, %s, %s)', (coloniaId, cuadrillaId, descripcion, fecha, 1))
            con.commit()
            respuesta = 1
        except Exception as e :
            print('error')
        finally:
            cursor.close()
            db.close()
            return respuesta 
