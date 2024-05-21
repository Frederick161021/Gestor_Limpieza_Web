from flask import Flask, render_template,  request, redirect, url_for, jsonify
from model.package_model.Persona import Persona
from model.package_model.Administrador import Administrador
from model.package_model.Colonia import Colonia
from model.package_model.Cuadrilla import Cuadrilla
from model.package_model.Actividad import Actividad
from model.package_model.JefeCuadrilla import JefeCuadrilla
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
    print(usuario)
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

@app.route('/buscarPorNombreColonia', methods = ['POST'])
def buscarPorNombreColonia():
    data = request.json
    nombreColonia = data.get('nombreColonia')
    col = Colonia()
    colonias = col.getColoniasPorNombre(nombreColonia)
    # return render_template('/GestionColonias.html', colonias = colonias)
    colonias_list = [list(colonia) for colonia in colonias]  
    return jsonify(colonias=colonias_list)

@app.route('/agregarColonia', methods = ['POST'])
def agregarColonia():
    data = request.json
    coloniaId = data.get('coloniaId')
    col = Colonia()

    resultado = col.agregarColonia(coloniaId)
    return jsonify( resultado = resultado)

@app.route('/colonias', methods = ['GET'])
def colonias():
    col = Colonia()
    colonias = col.buscarColonias()
    return render_template('VerColonias.html', colonias = colonias)

@app.route('/gestionCuadrillas', methods = ['GET'])
def gestionCuadrillas():
    cuadrilla = Cuadrilla()
    jefes = cuadrilla.getJefeSinCuadrilla()
    trabajadores = cuadrilla.getTrabajadoresSinCuadrilla()
    return render_template('GestionCuadrillas.html', jefes = jefes, trabajadores = trabajadores)

@app.route('/agregarJefeCuadrilla', methods=['POST'])
def agregarJefeCuadrilla():
    data = request.json
    jefeId = data.get('jefeId')
    cuadrillaId = data.get('cuadrillaId')
    cuadrilla = Cuadrilla()
    resultado = cuadrilla.agregarTrabajadorACuadrilla(jefeId, cuadrillaId)
    return jsonify({"resultado": resultado})

@app.route('/agregarTrabajadorCuadrilla', methods=['POST'])
def agregarTrabajadorCuadrilla():
    data = request.json
    trabajadorId = data.get('trabajadorId')
    cuadrillaId = data.get('cuadrillaId')
    cuadrilla = Cuadrilla()
    resultado = cuadrilla.agregarTrabajadorACuadrilla(trabajadorId, cuadrillaId)
    return jsonify({"resultado": resultado})

@app.route('/eliminarTrabajadorCuadrilla', methods=['POST'])
def eliminarTrabajadorCuadrilla():
    data = request.json
    trabajadorId = data.get('trabajadorId')
    cuadrillaId = data.get('cuadrillaId')
    cuadrilla = Cuadrilla()
    resultado = cuadrilla.eliminarTrabajadorACuadrilla(trabajadorId, cuadrillaId)
    return jsonify({"resultado": resultado})

@app.route('/crearCuadrilla', methods=['POST'])
def crearCuadrilla():
    data = request.json
    nombreCuadrilla = data.get('nombreCuadrilla')
    cuadrilla = Cuadrilla()
    resultado = cuadrilla.crearCuadrilla(nombreCuadrilla)
    id = cuadrilla.getCuadrillaId(nombreCuadrilla)
    return jsonify({'resultado': resultado, 'id':id})


@app.route('/consultarCuadrilla', methods=['POST'])
def consultarCuadrilla():
    data = request.json
    cuadrillaId = data.get('cuadrillaId')
    cuadrilla = Cuadrilla()
    nombreCuadrilla = cuadrilla.getNombreCuadrilla(cuadrillaId)
    empleados = cuadrilla.getEmpleadosCuadrilla(cuadrillaId)
    return jsonify({'nombreCuadrilla': nombreCuadrilla, 'empleados': empleados})


@app.route('/actualizarCuadrilla', methods=['POST'])
def actualizarCuadrilla():
    data = request.json
    cuadrillaId = data.get('cuadrillaId')
    nombreCuadrilla = data.get('nombreCuadrilla')
    cuadrilla = Cuadrilla()
    resultado = cuadrilla.actualizarCuadrilla(cuadrillaId, nombreCuadrilla)
    return jsonify({'resultado': resultado})


@app.route('/eliminarCuadrilla', methods=['POST'])
def eliminarCuadrilla():
    data = request.json
    cuadrillaId = data.get('cuadrillaId')
    cuadrilla = Cuadrilla()
    resultado = cuadrilla.eliminarCuadrilla(cuadrillaId)
    return jsonify({'resultado': resultado})


@app.route('/cuadrillas', methods = ['GET'])
def cuadrillas():
    cuadrilla = Cuadrilla()
    cuadrillas = cuadrilla.getCuadrillas()
    trabajadores = cuadrilla.getTrabajadoresCuadrillas()
    return render_template('VerCuadrillas.html', cuadrillas = cuadrillas, trabajadores = trabajadores)

@app.route('/gestionActividades', methods=['GET','POST'])
def gestionActividades():
    actividad = Actividad()
    cuadrillas = actividad.obtenerCudrillasNombre()
    colonias = actividad.obetenerColoniasNombre()
    return render_template('GestionActividades.html', cuadrillas = cuadrillas, colonias = colonias)

@app.route('/crearActividad', methods=['POST'])
def crearActividad():
    data = request.json
    descripcion = data.get('descripcion')
    fecha = data.get('fecha')
    cuadrillaId = data.get('cuadrillaId')
    coloniaId = data.get('coloniaId')
    print(descripcion)
    print(fecha)
    print(cuadrillaId)
    print(coloniaId)

    actividad = Actividad()
    respuesta = actividad.agregarActividad(descripcion, fecha, cuadrillaId, coloniaId)
    return jsonify({'respuesta': respuesta})

@app.route('/actividades', methods=['GET'])
def actividades():
    actividad = Actividad()
    actividades = actividad.obtenerActvidades()
    return render_template('VerAsignaciones.html', actividades = actividades)

@app.route('/reporteActividades', methods=['GET', 'POST'])
def reporteActividades():
    actividad = Actividad()
    actividades = actividad.reporteActividades()
    numEsperaConfirmacion = actividad.countEstatusActividad(1)
    numPendiente = actividad.countEstatusActividad(2)
    numFinalizado = actividad.countEstatusActividad(3)
    numCancelado = actividad.countEstatusActividad(4)
    return render_template('ReporteActividades.html', actividades = actividades, numEsperaConfirmacion = numEsperaConfirmacion, numPendiente = numPendiente, numFinalizado = numFinalizado, numCancelado = numCancelado)

@app.route('/activiadesAceptar', methods=['GET', 'POST'])
def actividadesAceptar():
    jefe = JefeCuadrilla()
    actividades = jefe.obtenerActiviadesPendientesAceptar()
    return render_template('ActividadesAceptar.html', actividades = actividades)

@app.route('/actualizarEstatusActividades', methods=['POST'])
def actuliazarEstatusActividades():
    data = request.json
    actividadId = data.get('actividadId')
    estatus = data.get('estatus')
    jefe = JefeCuadrilla()
    respuesta = jefe.actualizarEstatusActiviades(actividadId, estatus)
    mensaje = jefe.notificarCuadrilla(actividadId)
    return jsonify({'respuesta': respuesta, 'mensaje': mensaje})


@app.route('/actividadesCompletas', methods=['GET'])
def actividadesCompletas():
    print('estas aqui xd')
    usuario = UsuarioDTO()
    personaId = usuario.getPersonaId()
    print(personaId)
    persona = Persona()
    actividades = persona.getActiviadesPorEstatus(3, personaId)
    print(persona)
    return render_template('ActividadesCompletas.html', actividades = actividades)

@app.route('/setActividadId', methods=['POST'])
def setActividadId():
    data = request.json
    actividadId = data.get('actividadId')
    usuario = UsuarioDTO()
    usuario.setActividadId(actividadId)
    return jsonify({'respuesta': 1})

@app.route('/terminarActividad', methods=['GET'])
def terminarActividad():
    return render_template('TerminarActividad.html')

@app.route('/finalizarActividad', methods=['POST'])
def finalizarActividad():
    data = request.json
    comentarios = data.get('comentarios')
    imagen = data.get('imagen')

    jefe = JefeCuadrilla()
    respuesta = jefe.terminarActividad(comentarios, imagen)
    return jsonify({'respuesa': respuesta})


@app.route('/cerrarSeccion', methods=['GET'])
def cerrarSeccion():
    usuario = UsuarioDTO()
    usuario.cerroSesion()
    return jsonify({"status": "success"}), 200

if __name__ == '__main__':
    app.run(debug = True, port = 5000)