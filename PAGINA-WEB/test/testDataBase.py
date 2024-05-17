import model.package_model.Conexion as Conexion

#Test de prueba de connexion de Base de datos
db = Conexion.Conexion()
db.connect()

#Test de funcionamiento de patron de diseño singleton al conectar la base de datos
db = Conexion.Conexion()
db.connect()

#Test para Cerrar la base de datos
db.close()
db.close()