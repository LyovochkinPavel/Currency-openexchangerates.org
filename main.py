import requests  # библиотека для работы с запросами
from datetime import datetime  # форматирует врмея из формата UNIX в человеческий формат

from_valute = "USD"  # валюта, стоимость которой мы хотим узнать
to_valute = "RUB"  # валюта, цену которую просят за первую валюту

api_key = "xxxxxxxxxxxxxxxxxxxx"  # API-ключ, который можно получить бесплатно на сайте openexchangerates.org

request_link = f"https://openexchangerates.org/api/latest.json?app_id={api_key}&base={from_valute}&symbols={to_valute}"  # формируем запрос

data = requests.get(request_link).json()  # получаем результат в формате JSON

date_print = datetime.fromtimestamp(data['timestamp']).strftime('%d.%m.%Y %H:%M:%S')  # форматируем дату из фората UNIX в человеческий формат

human_price = "%.2f" % data['rates'][to_valute]  # округляем результат стоиомсти до 2 знаков после запятой

print (f"1 {from_valute} на {date_print} стоит {human_price} {to_valute}")  # выводим результат в консоль