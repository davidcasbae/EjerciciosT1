import psutil

def procesos():
    print("Dime una palabra clave para encontrar el proceso:")
    clave = input()
    print("{:<10} {:<25}".format("PID", "Nombre del proceso"))
    encontrado = False

    for proceso in psutil.process_iter(['pid', 'name', 'memory_info']):
        try:
            pid = proceso.info['pid']
            nombre = proceso.info['name']
            memoria = proceso.info['memory_info'].rss / (1024 * 1024)
            if clave.lower() in nombre.lower():
                print("{:<10} {:<25} {:10.2f}".format(pid, nombre, memoria))
                encontrado = True
        except psutil.NoSuchProcess:
            pass

    if not encontrado:
        print(f"No hay procesos que contengan la palabra '{clave}'.")

    print("Dime el nombre del proceo para finalizarlo:")
    finalizar = input()
    proceso_finalizado = False

    for proceso in psutil.process_iter(['pid', 'name']):
        nombre = proceso.info['name']
        try:
            if finalizar.lower() in nombre.lower():
                proceso.terminate()
                proceso.wait()
                print("El proceso terminó exitosamente.")
                proceso_finalizado = True
                break
        except psutil.NoSuchProcess:
            print("no se pudo finalizar el proceso")
    if not proceso_finalizado:
        procesos("no se encontraron procesos coincidentes")
if __name__ == "__main__":
    procesos()