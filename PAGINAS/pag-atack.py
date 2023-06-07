import requests
import threading

def send_request():
    while True:
        try:
            # Envia una solicitud GET a la página objetivo
            response = requests.get("...")
            # Puedes personalizar las solicitudes y parámetros según tus necesidades
            # También podrías utilizar otros métodos HTTP como POST o HEAD
            print("Solicitud enviada:", response.status_code)
        except:
            print("Error al enviar solicitud.")

# Configura el número de hilos para enviar solicitudes simultáneas
num_threads = 10

# Crea y ejecuta los hilos
for _ in range(num_threads):
    thread = threading.Thread(target=send_request)
    thread.start()
