from model.package_model.Conexion import Conexion

class Colonia:

    # def __init__(self, cve, codigoPostal, nombreColonia, tipoAsentamiento, municipio, estado, ciudad, lat, lon):
    #     self._cve = cve
    #     self._codigoPostal = codigoPostal
    #     self._nombreColonia = nombreColonia
    #     self._tipoAsentamiento = tipoAsentamiento
    #     self._municipio = municipio
    #     self._estado = estado
    #     self._ciudad = ciudad
    #     self._lat = lat
    #     self._lon = lon
    
    def getColoniasPorNombre(self, nombreColonia):
        db = Conexion()
        con = db.connect()
        cursor = db.cursor()

        colonias = None

        try:
            cursor.execute('CALL consultarPorNombreColonia(%s)', [nombreColonia])
            colonias = cursor.fetchall()
        except Exception as e:
            print("error")
        finally:
            cursor.close()
            db.close()
            return colonias

    def agregarColonia(self, coloniaId):
        db = Conexion()
        con = db.connect()
        cursor = db.cursor()

        resultado = 0

        try:
            cursor.execute('CALL crearColoniasSeleccionadas(%s)', [coloniaId])
            con.commit()
            resultado = 1
        except Exception as e:
            print("error")
        finally:
            cursor.close()
            db.close()
            return resultado
        
    def buscarColonias(self):
        db = Conexion()
        con = db.connect()
        cursor = db.cursor()

        colonias = None

        try:
            cursor.execute('CALL consultarColoniasSeleccionadas()')
            colonias = cursor.fetchall()
        except Exception as e:
            print("error")
        finally:
            cursor.close()
            db.close()
            return colonias
