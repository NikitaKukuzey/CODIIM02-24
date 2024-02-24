import requests
import uuid
import json

menu = {    'apple_pie': 'яблочный пирог',
    'caesar_salad': 'салат "Цезарь"',    'caprese_salad': 'салат "Капрезе"',
    'carrot_cake': 'морковный пирог',    'cheesecake': 'чизкейк',
    'chicken_curry': 'куриное карри',    'chocolate_cake': 'шоколадный пирог',
    'chocolate_mousse': 'шоколадный мусс',    'donuts': 'пончики',
    'dumplings': 'пельмени',    'eggs_benedict': 'яичница по-бенедиктински',
    'greek_salad': 'греческий салат',    'lasagna': 'лазанья',
    'pancakes': 'блины',    'panna_cotta': 'панна котта',
    'peking_duck': 'утка по-пекински',    'pizza': 'пицца',
    'ramen': 'рамен',    'risotto': 'ризотто',
    'waffles': 'вафли'}
def gigachat(predicted_class):

    url = "https://ngw.devices.sberbank.ru:9443/api/v2/oauth"
    from requests.auth import HTTPBasicAuth

    # basic = HTTPBasicAuth('a3708278-56f2-4c95-ae35-0be5438c01a8', '')
    payload = 'scope=GIGACHAT_API_PERS'
    headers = {
        'Content-Type': 'application/x-www-form-urlencoded',
        'Accept': 'application/json',
        'RqUID': str(uuid.uuid4()),
        'Authorization': 'Basic ZGE2YmZhM2EtMTVmNC00MjY3LTgxNWMtODU5NzNmMGJiMmYzOmEzNzA4Mjc4LTU2ZjItNGM5NS1hZTM1LTBiZTU0MzhjMDFhOA=='
    }

    response = requests.post(url, headers=headers, data=payload, verify=False)

    token = response.json()['access_token']

    url = "https://gigachat.devices.sberbank.ru/api/v1/chat/completions"

    payload = json.dumps({
        "model": "GigaChat:latest",
        "messages": [
            {
                "role": "user",
                "content": "Напиши рецепт с ингридиентами и пошаговой инструкцией для " + menu[predicted_class]
            }
        ],
        "temperature": 1,
        "top_p": 0.1,
        "n": 1,
        "stream": False,
        "max_tokens": 512,
        "repetition_penalty": 1
    })
    headers = {
        'Content-Type': 'application/json',
        'Accept': 'application/json',
        'Authorization': 'Bearer ' + token
    }

    response = requests.request("POST", url, headers=headers, data=payload, verify=False)

    return (json.loads(response.text)["choices"][0]["message"]["content"])