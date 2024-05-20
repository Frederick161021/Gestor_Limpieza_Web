window.addEventListener('pageshow', function(event) {
    if (event.persisted) {
        window.location.reload();
    }
});

document.addEventListener('DOMContentLoaded', function(){
    var lblId;
    var selectRolId;
    var lblNombre;
    var lblApellidoPaterno;
    var lblApellidoMaterno;
    var lblUsuario;
    var lblTelefono;
    var lblCorreo;
    var lblContraseña;


    var btnAgregar = document.getElementById('btnAgregar');
    var btnBuscar = document.getElementById('btnBuscar');
    var btnActualizar = document.getElementById('btnActualizar');
    var btnEliminar = document.getElementById('btnEliminar');


    btnAgregar.addEventListener('click', function () {
        lblId = document.getElementById('id').value;
        var selectElement = document.getElementById('tipo-usuario');
        selectRolId = selectElement.value;
        lblNombre = document.getElementById('nombre').value;
        lblApellidoPaterno = document.getElementById('apellido-paterno').value;
        lblApellidoMaterno = document.getElementById('apellido-materno').value;
        lblUsuario = document.getElementById('usuario').value;
        lblTelefono = document.getElementById('telefono').value;
        lblCorreo = document.getElementById('correo').value;
        lblContraseña = document.getElementById('contrasena').value;
       
        if (formularioCompleto()){
            
            var data = {id: lblId, rolId: selectRolId, nombre: lblNombre, apellidoPaterno: lblApellidoPaterno, apellidoMaterno: lblApellidoMaterno, usuario: lblUsuario, contraseña: lblContraseña, email: lblCorreo, telefono: lblTelefono}
            
            $.ajax({
                url: '/agregarUsuario',
                type: 'POST',
                contentType: 'application/json',
                data: JSON.stringify(data),
                success: function(response) {
                    Swal.fire({
                        title: "Usuario Agregado!",
                        text: "Usuario agregado correctamente!",
                        icon: "success"
                      });
                },
                    error: function(xhr, status, error) {
                        Swal.fire({
                            icon: "error",
                            title: "Eror al agragar usuario!",
                            text: "No se pudo agragar correctamente al usuario!"
                          });
                        // console.error(xhr.responseText);
                    }
                });
            limpiarForm();
        }
    });


    btnBuscar.addEventListener('click', function () {
        lblId = document.getElementById('id').value;

        if(tieneId){
            var data = {id: lblId}
            
            $.ajax({
                url: '/buscarUsuario',
                type: 'POST',
                contentType: 'application/json',
                data: JSON.stringify(data),
                success: function(response) {
                    if (response['usuario'][1] == 1){
                        selectElement = document.getElementById('tipo-usuario');
                        selectElement.value = "1";
                    }
                    else if(response['usuario'][1] == 2){
                        var selectElement = document.getElementById('tipo-usuario');
                        selectElement.value = "2";
                    }
                    else if (response['usuario'][1] == 3){
                        var selectElement = document.getElementById('tipo-usuario');
                        selectElement.value = "3";
                    }

                    
                    document.getElementById('nombre').value= response['usuario'][2];
                    document.getElementById('apellido-paterno').value = response['usuario'][3];
                    document.getElementById('apellido-materno').value = response['usuario'][4];
                    document.getElementById('usuario').value = response['usuario'][5];
                    document.getElementById('contrasena').value = response['usuario'][6];
                    document.getElementById('correo').value = response['usuario'][7];
                    document.getElementById('telefono').value = response['usuario'][8];
                },
                error: function(xhr, status, error) {
                    Swal.fire({
                        icon: "error",
                        title: "Eror al buscar usuario!",
                        text: "No existe usuario!"
                      });
                    // console.error(xhr.responseText);
                }
            });
        }
    });


    btnActualizar.addEventListener('click', function () {
        lblId = document.getElementById('id').value;
        var selectElement = document.getElementById('tipo-usuario');
        selectRolId = selectElement.value;
        lblNombre = document.getElementById('nombre').value;
        lblApellidoPaterno = document.getElementById('apellido-paterno').value;
        lblApellidoMaterno = document.getElementById('apellido-materno').value;
        lblUsuario = document.getElementById('usuario').value;
        lblTelefono = document.getElementById('telefono').value;
        lblCorreo = document.getElementById('correo').value;
        lblContraseña = document.getElementById('contrasena').value;

        if(formularioCompleto()){
            var data = {id: lblId, rolId: selectRolId, nombre: lblNombre, apellidoPaterno: lblApellidoPaterno, apellidoMaterno: lblApellidoMaterno, usuario: lblUsuario, contraseña: lblContraseña, email: lblCorreo, telefono: lblTelefono}
            
            $.ajax({
                url: '/actualizarUsuario',
                type: 'POST',
                contentType: 'application/json',
                data: JSON.stringify(data),
                success: function(response) {
                    Swal.fire({
                        title: "Usuario Actualizado!",
                        text: "Usuario actualizado correctamente!",
                        icon: "success"
                      });
                },
                error: function(xhr, status, error) {
                    Swal.fire({
                        icon: "error",
                        title: "Eror al actualizar usuario!",
                        text: "No se pudo actualizar los datos del usuario!"
                      });
                    // console.error(xhr.responseText);
                }
            });
            limpiarForm();
        }
    });

    btnEliminar.addEventListener('click', function () {
        lblId = document.getElementById('id').value;
        if(tieneId){
            var data = {id: lblId}
            
            $.ajax({
                url: '/eliminarUsuario',
                type: 'POST',
                contentType: 'application/json',
                data: JSON.stringify(data),
                success: function(response) {
                    Swal.fire({
                        title: "Usuario Eliminado!",
                        text: "Usuario eliminado correctamente!",
                        icon: "success"
                      });
                },
                error: function(xhr, status, error) {
                    Swal.fire({
                        icon: "error",
                        title: "Eror al eliminar usuario!",
                        text: "No se pudo eliminar el usuario!"
                      });
                    // console.error(xhr.responseText);
                }
            });
            limpiarForm();
        }
    });

    function limpiarForm(){
        document.getElementById('id').value = "";
        document.getElementById('nombre').value = "";
        document.getElementById('apellido-paterno').value = "";
        document.getElementById('apellido-materno').value = "";
        document.getElementById('usuario').value = "";
        document.getElementById('contrasena').value = "";
        document.getElementById('correo').value = "";
        document.getElementById('telefono').value = "";
    }

    function formularioCompleto(){
        if (
        document.getElementById('id').value == "" ||
        document.getElementById('nombre').value == "" ||
        document.getElementById('apellido-paterno').value == "" ||
        document.getElementById('apellido-materno').value == "" ||
        document.getElementById('usuario').value == "" ||
        document.getElementById('contrasena').value == "" ||
        document.getElementById('correo').value == "" ||
        document.getElementById('telefono').value == "" 
        )
        {
            Swal.fire({
                icon: "error",
                title: "Se te olvida algo?",
                text: "Tienes que llenar todos los datos!"
              });
              return false;
        }
        else{
            return true;
        }
    }

    function tieneId(){
        if (lblId.value == "")
        {
            Swal.fire({
                icon: "error",
                title: "Se te olvida algo?",
                text: "Tienes que proporcionar un id!"
              });
              return false;
        }
        return true;
    }
    
});
