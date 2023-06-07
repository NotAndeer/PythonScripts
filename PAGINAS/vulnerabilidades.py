import requests

target_url = "http://www.example.com"

# Ejemplo de verificación de vulnerabilidades
def verificar_vulnerabilidades(url):
    response = requests.get(url)
    
    if response.status_code == 200:
        # Aquí puedes agregar lógica para analizar la respuesta y buscar vulnerabilidades específicas
        print("¡Vulnerabilidades verificadas con éxito!")
    else:
        print("No se pudo acceder al sitio web.")

# Llamada a la función para verificar vulnerabilidades en el objetivo
verificar_vulnerabilidades(target_url)