import requests

response = requests.get("http://main:5000/media")
mean = response.json()
print(f"Média de idades: {mean}")

response = requests.get("http://main:5000/media/house")
mean_house = response.json()
print(f"Análise da média de idade por tipos de moradia: {mean_house}")

response = requests.get("http://main:5000/credit/age")
creditByAge = response.json()
print(f"Análise do registro de inadimplência por idade: {creditByAge}")
