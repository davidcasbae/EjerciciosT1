import os
import sys
def main():
    pipePadre = os.pipe()
    pipeHijo = os.pipe()

    mensajePadre = "Soy Padre"

    pid = os.fork()

    if pid < 0:
        print("no se ha podido crear el proceso")
        sys.exit()
    elif pid > 0:
        os.close(pipePadre[0])
        os.write(pipePadre[1], mensajePadre.encode())
        os.close(pipePadre[1])

        os.close(pipeHijo[1])
        respuesta = os.read(pipeHijo[0], 1024).decode()
        print(f"mensaje recibido del hijo: {respuesta}")
        os.close(pipeHijo[0])
    else:
        os.close(pipePadre[1])
        mensaje = os.read(pipePadre[0], 1024).decode()
        os.close(pipePadre[0])

        mensajeMayus = mensaje.encode().upper()

        os.close(pipeHijo[0])
        os.write(pipeHijo[1], mensajeMayus)
        os.close(pipeHijo[1])
if __name__ == "__main__":
    main()