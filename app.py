from flask import Flask, render_template, request
import requests

app = Flask(__name__)

# PEGA AQUÍ LA URL QUE COPIASTE DE GOOGLE SCRIPT
GOOGLE_SCRIPT_URL = "https://script.google.com/macros/s/AKfycbwO1RH1mb8adDdz4gE0H0FWyxKKMbZE9hJIi62zvYYPZ2Ndi-HFxy0__0-78VD3W-bE/exec"

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
