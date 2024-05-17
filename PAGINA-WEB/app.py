from flask import Flask, render_template,  request, redirect, url_for, jsonify
from model.package_model.Persona import Persona
from model.package_model.Administrador import Administrador
from model.package_model.UsuarioDTO import UsuarioDTO

app = Flask(__name__)
app.config['secret_key'] = ['123']


@app.route('/')
@app.route('/login')
def login ():
    return render_template('Login.html')


@app.route('/Login', methods = ['POST'])
def loginComprobar():
    data = request.json
    usuario = data.get('usuario')
    contraseña  = data.get('contraseña')
    print ("usuario: " + usuario + "\ncontrsaña: " + contraseña)
    persona = Persona()
    user = persona.getUsuario(usuario, contraseña)
    user = user[0]
    print(user)
    print(len(user))
    if len(user) > 0:
        return jsonify({'rolId': user[1]}), 200
    else: 
        return jsonify({"rolId": 0}), 401
    

@app.route('/menuAdmin', methods = ['GET', 'POST'])
def menuAdmin():
    return render_template('MenuAdmin.html')


@app.route('/menuJefe', methods = ['GET', 'POST'])
def menuJefe():
    return render_template('MenuJefe.html')


@app.route('/actividadesPendientes', methods = ['GET','POST'])
def actividadesPendientes():
    persona = Persona()
    usuario = UsuarioDTO()

    actividadesPendientes = persona.getActiviadesPorEstatus(2, usuario.getPersonaId())

    print(actividadesPendientes)
    
    return render_template('ActividadesPendientes.html', actividadesPendientes = actividadesPendientes, rolId = usuario.getRolId())

@app.route('/gestionUsuarios', methods=['GET', 'POST'])
def gestionUsuarios():
    return render_template('GestionUsuarios.html')

@app.route('/agregarUsuario', methods=['POST'])
def agregarUsuario():
    data = request.json

    id = data.get('id')
    rolId = data.get('rolId')
    nombre = data.get('nombre')
    apellidoPaterno = data.get('apellidoPaterno')
    apellidoMaterno = data.get('apellidoMaterno')
    nombreUsuario = data.get('usuario')
    contraseña = data.get('contraseña')
    email = data.get('email')
    telefono = data.get('telefono')
    admin = Administrador()

    respuesta = admin.agregarPersona(id, rolId, nombre, apellidoPaterno, apellidoMaterno, nombreUsuario, contraseña, email, telefono)

    if respuesta != 0:
        return jsonify({'respuesta': 1}), 200
    else: 
        return jsonify({"respuesta": 0}), 401

@app.route('/buscarUsuario', methods=['POST'])
def buscarUsuario():
    data = request.json

    id = data.get('id')

    admin = Administrador()
    usuario = admin.buscarPersona(id)

    if not usuario:
        return jsonify({"usuario": None}), 401
    else: 
        return jsonify({'usuario': usuario}), 200

@app.route('/actualizarUsuario', methods=['PosT'])
def actualizarUsuario():
    data = request.json
    id = data.get('id')
    rolId = data.get('rolId')
    nombre = data.get('nombre')
    apellidoPaterno = data.get('apellidoPaterno')
    apellidoMaterno = data.get('apellidoMaterno')
    nombreUsuario = data.get('usuario')
    contraseña = data.get('contraseña')
    email = data.get('email')
    telefono = data.get('telefono')

    admin = Administrador()
    respuesta = admin.actualizarPersona(id, rolId, nombre, apellidoPaterno, apellidoMaterno, nombreUsuario, contraseña, email, telefono)
    
    if respuesta != 0:
        return jsonify({'respuesta': 1}), 200
    else: 
        return jsonify({"respuesta": 0}), 401

@app.route('/eliminarUsuario', methods=['POST'])
def elimiarUsuario():
    data = request.json
    id = data.get('id')
    admin = Administrador()
    respuesta = admin.eliminarPersona(id)
    return render_template('VerUsuarios.html', respuesta = respuesta)

@app.route('/usuarios', methods=['GET'])
def usuarios():
    admin = Administrador()
    usuarios = admin.getUsuarios()
    return render_template('VerUsuarios.html', usuarios = usuarios)


@app.route('/gestionColonias', methods = ['GET', 'POST'])
def gestionColonias():
    return render_template('GestionColonias.html')

@app.route('/colonias', methods = ['GET'])
def colonias():
    return render_template('VerColonias.html')

@app.route('/cerrarSeccion', methods=['GET'])
def cerrarSeccion():
    usuario = UsuarioDTO()
    usuario.cerroSesion()
    print("si estoy xd")
    return jsonify({"status": "success"}), 200

if __name__ == '__main__':
    app.run(debug = True, port = 5000)