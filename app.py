from flask import Flask, render_template, request
import requests

app = Flask(__name__)

# PEGA AQUÍ LA URL QUE COPIASTE DE GOOGLE SCRIPT
GOOGLE_SCRIPT_URL = "https://script.google.com/macros/s/AKfycbzWOrDS82UGQJJfC-e3sWX751qdiMkZlWoJEgqntQroFgJNUh73o5FCfdbedkrrVTcP/exec"

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/registrar', methods=['POST'])
def registrar():
    username = request.form.get('username')
    # Envía los datos a Google Sheets
    requests.post(GOOGLE_SCRIPT_URL, json={"username": username})
    
    wa_link = f"https://wa.me/5351234567?text=Hola, quiero activar mi usuario: {username}"
    return f"<h1>Registrado, {username}!</h1><a href='{wa_link}'>Click aquí para activar por WhatsApp</a>"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=10000)
