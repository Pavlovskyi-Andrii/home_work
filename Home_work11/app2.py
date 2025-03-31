import flask  # Добавь этот импорт
import requests

from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return 'Привет, мен!'

if __name__ == '__main__':
    app.run(debug=True)

response = requests.get("http://127.0.0.1:5000/users")  # Используй requests, а не request

print(response.status_code)  # Выведет HTTP-статус
print("1. Получение всех существующих пользователей:")
print(response.json())  # Выведет данные пользователей
