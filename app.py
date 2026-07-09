from flask import Flask, render_template, request

app = Flask(__name__)

# Ruta principal: Muestra el formulario de registro
@app.route('/')
def home():
    return render_template('index.html')

# Ruta de registro: Recibe los datos del formulario
@app.route('/registrar', methods=['POST'])
def registrar():
    username = request.form.get('username')
    # Aquí puedes añadir lógica para guardar el usuario en una base de datos más adelante
    
    # Redirige al usuario a tu WhatsApp con un mensaje predeterminado
    # Cambia 5351234567 por tu número real en formato internacional
    wa_link = f"https://wa.me/55998674?text=Hola, quiero activar mi cuenta. Mi usuario es: {username}"
    
    return f"""
    <h1>Registro casi listo, {username}!</h1>
    <p>Para activar tu cuenta, haz clic en el siguiente botón:</p>
    <a href='{wa_link}' style='padding: 10px; background: #25d366; color: white; text-decoration: none; border-radius: 5px;'>
        Activar por WhatsApp
    </a>
    """

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=10000)
    
