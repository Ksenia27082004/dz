from flask import Flask, render_template_string
import os

app = Flask(__name__)

# HTML-код вашей страницы
html_content = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Новогодняя страница</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            text-align: center;
            background-color: #f0f8ff;
            background-image: url('https://avatars.mds.yandex.net/i?id=8940dbdff44af45dedb4331cae58846da331a3f0-8187583-images-thumbs&n=13');
            background-size: cover;
            background-repeat: no-repeat;
            color: #333;
        }
        h1 {
            color: #d32f2f;
        }
        button {
            margin: 10px;
            padding: 10px 20px;
            font-size: 16px;
            background-color: #4caf50;
            color: white;
            border: none;
            border-radius: 5px;
            cursor: pointer;
        }
        button:hover {
            background-color: #45a049;
        }
    </style>
</head>
<body>
    <h1>Добро пожаловать!</h1>
    <p>До Нового года осталось: 4 дня!</p>
    <img src="https://avatars.mds.yandex.net/i?id=ae398961a8d5ca648040e8067d4b41b88012ad7a-9148772-images-thumbs&n=13" alt="Елка">
    <p>Нажмите на кнопку, чтобы узнать про подарки!</p>
    <button onclick="alert('С Новым годом! Желаем счастья и здоровья!')">Про подарки</button>
    <button onclick="alert('2025 год будет успешным!')">Узнать про 2025</button>
</body>
</html>
"""

@app.route('/')
def home():
    # Рендерим HTML-страницу
    return render_template_string(html_content)

if __name__ == '__main__':
    # Указываем хост и порт
    port = int(os.environ.get('PORT', 5000))  # Используем порт из переменной окружения или 5000 по умолчанию
    app.run(host='0.0.0.0', port=port, debug=True)
