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