import Flask, render_template_string, request, jsonify

app = Flask(__name__)

# Diccionario simple para usuarios
users = {}

@app.route('/')
def home():
    return "<h1>Sistema P2P en Línea</h1><p>Bienvenido. Registra tu usuario en /registrar</p>"

@app.route('/registrar', methods=['POST'])
def registrar():
    data = request.json
    username = data.get('username')
    users[username] = {"status": "pendiente", "creditos": 0}
    return jsonify({"mensaje": f"Usuario {username} registrado. Escríbenos a WhatsApp para activar."})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=10000)
