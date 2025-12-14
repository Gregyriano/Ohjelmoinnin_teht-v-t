import requests
import json

API_key = "23d6955977dbb0ff49f929d39a6e473e"

lang = "fi"
#Lang_rus = "ru"
city_name = input("Kirjoita kaupungin nimi: ")
pyyntö = f"https://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={API_key}&units=metric&lang={lang}"
#pyyntö1 = f"https://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={API_key}&units=metric&lang={Lang_rus}"

try:
    vastaus = requests.get(pyyntö)
#    vastaus1 = requests.get(pyyntö1)
    if vastaus.status_code == 200: #and vastaus1.status_code==200:
        json_vastaus = vastaus.json()
#        json_vastaus1 = vastaus1.json()
        print(json.dumps(json_vastaus, indent = 2))
#        print(json.dumps(json_vastaus1, indent = 2))
#        print(json_vastaus["weather"])
#        print(json_vastaus["main"]["temp"])
#        print(json_vastaus1)
        lämp = json_vastaus["main"]["temp"]
        sää_paikassa = json_vastaus["weather"][0]["description"]
        print(f"Sää kohteessa {city_name} on {sää_paikassa} ja lämpötila on {lämp:.0f} astetta")
except requests.exceptions.RequestException as e:
    print(e)
    print ("Hakua ei voitu suorittaa.")