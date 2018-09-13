import requests
import json
import time

# 180215006 - исходник
# программа будет работать бесконечно
n=0
while (n<1):
    # получить данные с биржи
    r = requests.get('https://api.exmo.com/v1/ticker/')
    # переводим данные во понятный программе формат
    obj = json.loads(r.text)
    # находим все валюты, перечисленные в файле
    #print(obj)

   
    # подождать три секунды и начать заново
    #time.sleep(3)
    n+=1

    with open("base.txt", "w") as file:
        file.write(r.text)  
