import requests

url = "http://127.0.0.1:8000/update_data_tags"

# Realizar la solicitud y obtener la respuesta
response = requests.get(url)

print(response)
