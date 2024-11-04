import asyncio
import subprocess
import time
def muestraSincrono():
    try:
        comienzo = time.time()
        subprocess.run(['notepad.exe'])
        final = time.time()
        return final - comienzo
    except subprocess.CalledProcessError as e:
        print(e.output)

async def muestraAsincrono():
            try:
                comienzo = time.time()
                await asyncio.create_subprocess_exec('notepad.exe')
                final = time.time()
                return final - comienzo
            except subprocess.CalledProcessError as e:
                print(e.output)

async def main():
    print("Elige 1 para ejecución sincrona o 2 para asincrona")
    opcion = input()
    if opcion == '1':
        muestraSincrono()
    elif opcion == '2':
        await muestraAsincrono()

asyncio.run(main())