import subprocess

url = "https://www.youtube.com/"  # Reemplaza esta URL por la que desees abrir

# Define el número de aperturas y el límite deseado
num_aperturas = 5  # Puedes ajustar este valor según tus preferencias
limite_aperturas = 10  # El cmd se cerrará después de alcanzar este límite

for _ in range(num_aperturas):
    subprocess.Popen(["start", url], shell=True)

    limite_aperturas -= 1
    if limite_aperturas == 0:
        break

def change_ipv4():
    # Comando para liberar la dirección IP
    release_cmd = 'ipconfig /release'
    # Comando para renovar la dirección IP
    renew_cmd = 'ipconfig /renew'

    try:
        # Liberar la dirección IP actual
        subprocess.run(release_cmd, shell=True, check=True)
        # Renovar la dirección IP
        subprocess.run(renew_cmd, shell=True, check=True)
        print("La dirección IP de IPv4 ha sido cambiada correctamente.")
    except subprocess.CalledProcessError as e:
        print("Se produjo un error al cambiar la dirección IP de IPv4:", e)

change_ipv4()
