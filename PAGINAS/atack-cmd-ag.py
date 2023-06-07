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
