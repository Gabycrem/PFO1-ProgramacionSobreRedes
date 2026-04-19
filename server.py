import socket
import sqlite3
from datetime import datetime

def init_db():
    conn = sqlite3.connect("database.db")
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS mensajes (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            contenido TEXT,
            fecha_envio TEXT,
            ip_cliente TEXT
        )
    """)
    conn.commit()
    conn.close()

def guardar_mensaje(contenido, ip):
    conn = sqlite3.connect("database.db")
    cursor = conn.cursor()
    fecha = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    cursor.execute("""
        INSERT INTO mensajes (contenido, fecha_envio, ip_cliente)
        VALUES (?, ?, ?)
    """, (contenido, fecha, ip))

    conn.commit()
    conn.close()

def init_socket():
    try:
        server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server.bind(("localhost", 5000))
        server.listen(5)
        print("Servidor escuchando en localhost: 5000...")
        return server
    except Exception as e:
        print("Error al iniciar el servidor:", e)

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

if __name__ == "__main__":
    init_db()
    server = init_socket()
    manejar_conexiones(server)