import geocoder

def obtener_coordenadas():
    g = geocoder.ip('me')
    if g.latlng:
        latitud, longitud = g.latlng
        return latitud, longitud
    else:
        return None

coordenadas = obtener_coordenadas()

if coordenadas:
    latitud, longitud = coordenadas
    print(f"Tus coordenadas son: Latitud = {latitud}, Longitud = {longitud}")
else:
    print("No se pudieron obtener las coordenadas.")