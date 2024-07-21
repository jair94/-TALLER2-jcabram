from flask import Flask, jsonify, render_template
from models.huron import Huron
from models.boa_Constrictor import Boa_Constrictor
from models.perro import Perro
from models.gato import Gato
from models.guarderia import Guarderia

app = Flask(__name__)

# Instancia de la guardería
guarderia = Guarderia()

# Endpoint para obtener cómo hace un Huron
@app.route('/huron', methods=['GET'])
def obtener_huron():
    huron = guarderia.huron1  # Puedes cambiar a huron2 si prefieres
    respuesta = {
        "nombre": huron.obtener_nombre(),
        "sonido": huron.hacer_sonido(),
        "descripcion": str(huron)
    }
    return jsonify(respuesta)

@app.route('/hurones', methods=['GET'])
def vista_huron():
    huron = guarderia.huron1
    return render_template('huron.html', nombre=huron.obtener_nombre(), sonido=huron.hacer_sonido(), descripcion=str(huron))

# Endpoint para obtener cómo hace una Boa Constrictor
@app.route('/boa', methods=['GET'])
def obtener_boa():
    boa = guarderia.boa1  # Puedes cambiar a boa2 si prefieres
    respuesta = {
        "nombre": boa.obtener_nombre(),
        "sonido": boa.hacer_sonido(),
        "descripcion": str(boa)
    }
    return jsonify(respuesta)

@app.route('/boas', methods=['GET'])
def vista_boa():
    boa = guarderia.boa1
    return render_template('boa.html', nombre=boa.obtener_nombre(), sonido=boa.hacer_sonido(), descripcion=str(boa))

# Endpoint para obtener cómo hace un Perro
@app.route('/perro', methods=['GET'])
def obtener_perro():
    perro = guarderia.perro1
    respuesta = {
        "nombre": perro.obtener_nombre(),
        "sonido": perro.hacer_sonido(),
        "descripcion": str(perro)
    }
    return jsonify(respuesta)

@app.route('/perros', methods=['GET'])
def vista_perro():
    perro = guarderia.perro1
    return render_template('perro.html', nombre=perro.obtener_nombre(), sonido=perro.hacer_sonido(), descripcion=str(perro))

# Endpoint para obtener cómo hace un Gato
@app.route('/gato', methods=['GET'])
def obtener_gato():
    gato = guarderia.gato1
    respuesta = {
        "nombre": gato.obtener_nombre(),
        "sonido": gato.hacer_sonido(),
        "descripcion": str(gato)
    }
    return jsonify(respuesta)

@app.route('/gatos', methods=['GET'])
def vista_gato():
    gato = guarderia.gato1
    return render_template('gato.html', nombre=gato.obtener_nombre(), sonido=gato.hacer_sonido(), descripcion=str(gato))

@app.route('/')
def home():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
