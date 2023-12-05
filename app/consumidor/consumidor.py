import requests

response = requests.get("http://main:5000/dados")
resultado = response.json()
print(f"Resultado obtido do servidor: {resultado}")
