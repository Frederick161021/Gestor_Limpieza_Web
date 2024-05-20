from model.package_model.Conexion import Conexion

class Cuadrilla():

    def getJefeSinCuadrilla(self):
        print('Estas en el mendigo metodo xd')
        db = Conexion()
        con = db.connect()
        cursor = db.cursor()

        jefes = None

        try:
            cursor.execute('CALL consultarJefesSinCuadrilla()')
            jefes = cursor.fetchall()
            

        except Exception as e:
            print("error")
        finally:
            cursor.close()
            db.close()
            return jefes
        
    def getTrabajadoresSinCuadrilla(self):
        db = Conexion()
        con = db.connect()
        cursor = db.cursor()

        trabajadores = None

        try:
            cursor.execute('CALL consultarTrabajadoresSinCuadrilla()')
            trabajadores = cursor.fetchall()
            print("trabajadores disponibles xd")
            print(trabajadores)

        except Exception as e:
            print("error")
        finally:
            cursor.close()
            db.close()
            return  trabajadores
        
    def getCuadrillas(self):
        db = Conexion()
        con = db.connect()
        cursor = db.cursor()

        cuadrillas = None

        try:
            cursor.execute('CALL consultarCuadrillas()')
            cuadrillas = cursor.fetchall()
            print (cuadrillas)

        except Exception as e:
            print("error")
        finally:
            cursor.close()
            db.close()
            return  cuadrillas
        
    def getTrabajadoresCuadrillas(self):
        db = Conexion()
        con = db.connect()
        cursor = db.cursor()

        trabajadores = None

        try:
            cursor.execute('CALL consultarTrabajadoresCuadrilla()')
            trabajadores = cursor.fetchall()

        except Exception as e:
            print("error")
        finally:
            cursor.close()
            db.close()
            return  trabajadores
    
    def agregarTrabajadorACuadrilla(self, trabajadorId, cuadrillaId):
        db = Conexion()
        con = db.connect()
        cursor = db.cursor()

        resultado = 0

        try:
            cursor.execute('CALL agregarTrabajadorCuadrilla(%s, %s)', (trabajadorId, cuadrillaId))
            con.commit()
            resultado = 1
        except Exception as e:
            print("error")
        finally:
            cursor.close()
            db.close()
            return resultado
        
    
    def eliminarTrabajadorACuadrilla(self, trabajadorId, cuadrillaId):
        db = Conexion()
        con = db.connect()
        cursor = db.cursor()

        resultado = 0

        try:
            cursor.execute('CALL eliminarTrabajadorCuadrilla(%s, %s)', (trabajadorId, cuadrillaId))
            con.commit()
            resultado = 1
        except Exception as e:
            print("error")
        finally:
            cursor.close()
            db.close()
            return resultado
        
        
    def crearCuadrilla(self, nombreCuadrilla):
        db = Conexion()
        con = db.connect()
        cursor = db.cursor()

        resultado = 0

        try:
            cursor.execute('CALL crearCuadrillaN(%s)', [nombreCuadrilla])
            con.commit()
            resultado = 1
        except Exception as e:
            print("error")
        finally:
            cursor.close()
            db.close()
            return resultado
        
        
    def actualizarCuadrilla(self , cuadrillaId, nombreCuadrilla):
        db = Conexion()
        con = db.connect()
        cursor = db.cursor()

        resultado = 0

        try:
            cursor.execute('CALL actualizarCuadrillaNombre(%s, %s)', (cuadrillaId, nombreCuadrilla))
            con.commit()
            resultado = 1
        except Exception as e:
            print("error")
        finally:
            cursor.close()
            db.close()
            return resultado

        
    def getCuadrillaId(self, nombreCuadrilla):
        db = Conexion()
        con = db.connect()
        cursor = db.cursor()

        cuadrillaId = None

        try:
            cursor.execute('CALL consultarPorNombreCuadrillaId(%s)', [nombreCuadrilla])
            cuadrillaId = cursor.fetchall()
        except Exception as e:
            print("error")
        finally:
            cursor.close()
            db.close()
            return cuadrillaId
        

    def getNombreCuadrilla(self, cuadillaId):
        db = Conexion()
        con = db.connect()
        cursor = db.cursor()

        nombreCuadrilla = None

        try:
            cursor.execute('CALL consultarNobreCuadrilla(%s)', [cuadillaId])
            nombreCuadrilla= cursor.fetchall()
        except Exception as e:
            print("error")
        finally:
            cursor.close()
            db.close()
            return nombreCuadrilla
    

    def getEmpleadosCuadrilla(self, cuadillaId):
        db = Conexion()
        con = db.connect()
        cursor = db.cursor()

        miembrosCuadrilla = None

        try:
            cursor.execute('CALL consultarMiembosCuadrillaPorId(%s)', [cuadillaId])
            miembrosCuadrilla = cursor.fetchall()
        except Exception as e:
            print("error")
        finally:
            cursor.close()
            db.close()
            return miembrosCuadrilla
        

    def eliminarCuadrilla(self, cuadillaId):
        db = Conexion()
        con = db.connect()
        cursor = db.cursor()

        respuesta = 0

        try:
            cursor.execute('CALL eliminarCuadrilla(%s)', [cuadillaId])
            con.commit()
            respuesta = 1
        except Exception as e:
            print("error")
        finally:
            cursor.close()
            db.close()
            return respuesta