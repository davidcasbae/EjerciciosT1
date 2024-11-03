import os
import sys
def main():
    padre = os.pipe()
    hijo = os.pipe()

    mensajePadre = "Soy Padre"

    pid = os.fork()

    if pid < 0:
        print("no se ha podido crear el proceso")
        sys.exit()
    elif pid > 0:
        os.close(padre[0])
        os.write(padre[1], mensajePadre.encode())
        os.close(padre[1])

        os.close(hijo[1])
        respuesta = os.read(hijo[0], 1024).decode()
        print(f"mensaje recibido del hijo: {respuesta}")
        os.close(hijo[0])
    else:
        os.close(padre[1])
        mensaje = os.read(padre[0], 1024).decode()
        os.close(padre[0])

        mensajeMayus = mensaje.encode().upper()

        os.close(hijo[0])
        os.write(hijo[1], mensajeMayus)
        os.close(hijo[1])
if __name__ == "__main__":
    main()