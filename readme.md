# Currency openexchangerates.org
Программа для вывода курса валют с сайта openexchangerates.org через API
_________________________________________
Программа написана на Python с использованием:
- requests (направление http-запроса на сервер)
- datetime (форматирует врмея из формата UNIX в человеческий формат)

## Как запустить программу:
1) Клонируйте репозитроий с программой:
```
git clone https://github.com/LyovochkinPavel/Currency-openexchangerates.org
```
2) В созданной директории установите виртуальное окружение, активируйте его и установите необходимые зависимости:
```
python -m venv venv

. venv\Scrippts\activate

pip install -r requirements.txt
```
3) Зарегистрироваться на сайте openexchangerates.org для получения API ключа

4) Откройте файл main.py и в строчке 7 укажите API ключ
```
api_key = "xxxxxxxxxxxxxxxxxxxx"
```
5) Запустите код

## Как работает программа:
Программа получает данные в формате JSON посредством обращения к API и выводит стоимость 1 доллара в рублях с указанием даты последнего изменения курса на сайте

Если необходимо поменять отслеживаемые валюты, то необходимо внести изменения в стрчоках 4 и 5

```
from_valute = "USD"  # валюта, стоимость которой мы хотим узнать
to_valute = "RUB"  # валюта, цену которую просят за первую валюту
```