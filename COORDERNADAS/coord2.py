import requests

def obtener_coordenadas():
    url = 'https://ipinfo.io/json'
    try:
        response = requests.get(url)
        data = response.json()
        if 'loc' in data:
            latitud, longitud = data['loc'].split(',')
            return latitud, longitud
        else:
            return None
    except requests.exceptions.RequestException as e:
        print(f"Error al obtener las coordenadas: {e}")
        return None

coordenadas = obtener_coordenadas()

if coordenadas:
    latitud, longitud = coordenadas
    print(f"Tus coordenadas son: Latitud = {latitud}, Longitud = {longitud}")
else:
    print("No se pudieron obtener las coordenadas.")