import requests


# API clima
CLIMA_URL = "https://api.open-meteo.com/v1/forecast?latitude=52.52&longitude=13.41&hourly=temperature_2m"

# Obtener usuarios
def obtener_usuarios_api():
    response = requests.get(API_URL, timeout=10)

    if response.status_code == 200:
        return response.json()
    else:
        return []

# Obtener clima
def obtener_clima_api():
    response = requests.get(CLIMA_URL, timeout=10)

    if response.status_code == 200:
        return response.json()
    else:
        return {}