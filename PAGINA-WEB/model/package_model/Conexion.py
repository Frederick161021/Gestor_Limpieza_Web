import mysql.connector

class Conexion:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance.connection = None
        return cls._instance

    def connect(self):
        if self.connection is None:
            self.connection = mysql.connector.connect(
                host = 'localhost',
                port = 3307,
                user = 'root',
                password = '',
                database = 'limpieza'
            )
            print("Conexión a la base de datos exitosa!")
        else:
            print("Ya se habia establecido connexión a la base de datos!")
        return self.connection
    
    def cursor(self):
        return self.connection.cursor()

    def close(self):
        if self.connection is not None:
            self.connection.close()
            print("La conexión a la base de datos se ha cerrado!")
            self.connection = None
        else:
            print("No se esta conectado a ninguna base de datos!")
