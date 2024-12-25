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
    <title>Моя первая страница</title>
</head>
<body>
    <h1>Привет, мир!</h1>
    <p>Это моя первая HTML-страница.</p>
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
