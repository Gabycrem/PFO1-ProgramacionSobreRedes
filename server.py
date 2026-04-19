import socket
import sqlite3
from datetime import datetime

# Función para iniciar la base de datos.
# Si el archivo no existe, SQLite lo crea automáticamente.
# También crea la tabla mensaje si todavía no existe. 
def init_db():
    # Establece conexión con la base de datos SQLite
    conn = sqlite3.connect("database.db")
    # Crea un cursor para ejecutar sentencias SQL
    cursor = conn.cursor()
    # Crea la tabla mensajes con los campos pedidos en la consigna
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS mensajes (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            contenido TEXT,
            fecha_envio TEXT,
            ip_cliente TEXT
        )
    """)
    # Guarda los cambios realizados en la base
    conn.commit()
    # Cierra la conexión con la base de datos
    conn.close()

#Función para guardar los mensajes en la base de datos
def guardar_mensaje(contenido, ip):
    
    conn = sqlite3.connect("database.db")
    cursor = conn.cursor()
    # Obtiene la fecha y hora actual del sistema
    fecha = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    # Inserta el contenido del mensaje, la fecha y la IP del cliente
    cursor.execute("""
        INSERT INTO mensajes (contenido, fecha_envio, ip_cliente)
        VALUES (?, ?, ?)
    """, (contenido, fecha, ip))

    conn.commit()
    conn.close()

#Función para iniciar el socket del servidor
def init_socket():
    try:
        server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server.bind(("localhost", 5000))
        server.listen(5)
        print("Servidor escuchando en localhost: 5000...")
        return server
    except Exception as e:
        print("Error al iniciar el servidor:", e)

# Función principal para aceptar conexiones de clientes y procesar mensajes
def manejar_conexiones(server):
    while True:
        cliente_socket, addr = server.accept()
        print(f"Conexión desde {addr}")

        try:
            mensaje = cliente_socket.recv(1024).decode()
            print("Mensaje recibido:", mensaje)

            guardar_mensaje(mensaje, addr[0])

            respuesta = f"Mensaje recibido: {datetime.now()}"
            cliente_socket.send(respuesta.encode())

        except Exception as e:
            print("Error al manejar cliente:", e)

        finally:
            cliente_socket.close()
# Punto de entrada principal del programa
if __name__ == "__main__":
    init_db()
    server = init_socket()
    if server:
        manejar_conexiones(server)