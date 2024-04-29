import requests

key = "chave_da_api"
lat = "lat"
lon = "lon"

try:
      response = requests.get(f"https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={key}&units=metric&lang=pt_br")
      dados = response.json()

      tempo = dados['weather'][0]['description']
      temperatura = dados['main']['temp']
      sensacao_termica = dados['main']['feels_like']
      temperatura_minima = dados['main']['temp_min']
      temperatura_maxima = dados['main']['temp_max']
      umidade = dados['main']['humidity']
      pais = dados['sys']['country']
      cidade = dados['name']

      print(f"Status Code: {response.status_code}\n"
            f"Reason: {response.reason}\n")

      print(f"País:{pais}.\n"
            f"Cidade:{cidade}.\n"
            f"Tempo:{tempo.title()}.\n"
            f"Temperatura:{round(temperatura)}°C.\n"
            f"Sensação Térmica:{round(sensacao_termica)}°C.\n"
            f"Temperatura Mínima:{round(temperatura_minima)}°C.\n"
            f"Temperatura Máxima:{round(temperatura_maxima)}°C.\n"
            f"Umidade:{umidade}%.")

except requests.RequestException as R:
      print(f"Ocorreu um problema de conexão: {R}.\nVerifique se sua internet está ok.\nCaso esteja ok, o problema pode ser no servidor.")

input("Pressione ENTER para sair.")