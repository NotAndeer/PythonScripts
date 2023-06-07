import socket
import os

def verificar_puertos(host, puertos):
    resultados = []

    for puerto in puertos:
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.settimeout(5)
            resultado = s.connect_ex((host, puerto))

            if resultado == 0:
                resultados.append(f"El puerto {puerto} en el host {host} está abierto.")
            else:
                resultados.append(f"El puerto {puerto} en el host {host} está cerrado o inaccesible.")

            s.close()
        except socket.error as e:
            resultados.append(f"Ocurrió un error al verificar el puerto {puerto}: {e}")

    # Ruta y nombre de archivo en el escritorio
    escritorio = os.path.join(os.path.join(os.environ['USERPROFILE']), 'Desktop')
    archivo_resultados = os.path.join(escritorio, 'resultados_puertos.txt')

    # Guardar los resultados en un archivo de texto
    with open(archivo_resultados, 'w') as archivo:
        archivo.write('\n'.join(resultados))

    print(f"Se ha generado el archivo {archivo_resultados} en el escritorio.")

# Ejemplo de uso
host = 'localhost'
puertos = [20, 21, 22, 23, 25, 53, 80, 110, 143, 443, 3306, 5432, 5900, 8080, 8888, 9000, 9090, 3389, 8443, 993, 995, 1521, 1433, 1723, 389, 465, 587, 993, 995, 2049, 3389, 5900, 6379, 27017, 27018, 27019, 9200, 9300, 11211]

verificar_puertos(host, puertos)
