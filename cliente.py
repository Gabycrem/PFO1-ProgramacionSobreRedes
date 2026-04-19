import socket

def iniciar_cliente():
    while True:
        mensaje = input('Dejanos un mensaje ("exit" para salir): ')

        if mensaje.lower() == "exit":
            break

        try:
            cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            cliente.connect(("localhost", 5000))

            cliente.send(mensaje.encode())

            respuesta = cliente.recv(1024).decode()
            print("Servidor:", respuesta)

            cliente.close()

        except Exception as e:
            print("Error de conexión:", e)

if __name__ == "__main__":
    iniciar_cliente()