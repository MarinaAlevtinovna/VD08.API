from flask import Flask, render_template, jsonify
import requests

app = Flask(__name__)

# Функция для запроса случайной цитаты с API
def fetch_random_quote():
    response = requests.get("http://api.quotable.io/random")
    if response.status_code == 200:
        return response.json()
    else:
        return {"content": "Не удалось получить цитату", "author": "Неизвестно"}

# Роут для главной страницы, которая отображает цитату
@app.route("/")
def home():
    quote = fetch_random_quote()
    return render_template("quotable.html", quote=quote)

# API роут для получения новой цитаты через AJAX-запрос
@app.route("/api/quote")
def api_quote():
    quote = fetch_random_quote()
    return jsonify(quote)

if __name__ == "__main__":
    app.run(debug=True)