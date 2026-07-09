from flask import Flask, render_template, request
import json
import os

app = Flask(__name__)
DB_FILE = 'usuarios.json'

def cargar_usuarios():
    if not os.path.exists(DB_FILE): return {}
    with open(DB_FILE, 'r') as f: return json.load(f)

def guardar_usuario(username):
    usuarios = cargar_usuarios()
    usuarios[username] = {"status": "pendiente", "creditos": 0}
    with open(DB_FILE, 'w') as f: json.dump(usuarios, f)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/registrar', methods=['POST'])
def registrar():
    username = request.form.get('username')
    guardar_usuario(username)
    wa_link = f"https://wa.me/5351234567?text=Hola, quiero activar mi usuario: {username}"
    return f"<h1>Registrado, {username}!</h1><a href='{wa_link}'>Click aquí para activar por WhatsApp</a>"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=10000)
    
    
