'''import sys
sys.path.append("src")
import psycopg2
import SecretConfig

def ObtenerCursor():
    """
    crea la conexión a la base de datos y retorna un cursor para ejecutar instrucciones
    """
    DATABASE = SecretConfig.PGDATABASE
    USER = SecretConfig.PGUSER
    PASSWORD = SecretConfig.PGPASSWORD
    HOST = SecretConfig.PGHOST
    PORT = SecretConfig.PGPORT
    connection = psycopg2.connect(database=DATABASE, user=USER, password=PASSWORD, host=HOST, port=PORT)

    return connection.cursor(), connection




def crear_tablas():
     
     return """
    CREATE TABLE  IF NOT EXISTS usuarios(
        id SERIAL PRIMARY KEY,
        nombre VARCHAR(100),
        contraseña VARCHAR(100),
        preferenica_estilo VARCHAR(100),
        colores preferidos VARCHAR(100),
        ropa favorita VARCHAR(100)
        );
    CREATE TABLE IF NOT EXISTS prendas (
        id_prenda SERIAL PRIMARY KEY,
        usuario_id INTEGER NOT NULL REFERENCES usuarios(id) ON DELETE CASCADE,
        nombre_prenda VARCHAR(100),
        ocasion VARCHAR(50),
        talla VARCHAR(10),
        temporada VARCHAR(50)
    );
    CREATE TABLE IF NOT EXISTS prenda_outfit(
        id_prenda_outfit SERIAL PRIMARY KEY,
        prenda_id INTEGER NOT NULL REFERENCES prendas(id_prenda) ON DELETE CASCADE,
        usuario_id INTEGER NOT NULL REFERENCES usuarios(id) ON DELETE CASCADE,


     );
"""
cursor, connection = ObtenerCursor()

sql_crear_tablas = crear_tablas()

if not sql_crear_tablas.strip():
     print("revise la funcion crear tablas()")
else:
     cursor.execute(sql_crear_tablas)
     connection.commit()

cursor.close()
connection.close()

'''