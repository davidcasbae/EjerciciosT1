import subprocess

proceso1 = subprocess.Popen('ftp', shell=True,stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
comandos = [b"verbose\n",
            b"open test.rebex.net\n",
            b"demo\n",
            b"password\n",
            b"get readme.txt\n"]

for cmd in comandos:
    proceso1.stdin.write(cmd)

respuesta = proceso1.communicate(timeout=5)[0]
print(respuesta.decode("cp850", "ignore"))