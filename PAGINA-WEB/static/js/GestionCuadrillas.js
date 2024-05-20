document.addEventListener('DOMContentLoaded', function(){
    var agregarJefe = document.getElementById('agregarJefe');
    var agregarTrabajador = document.getElementById('agregarTrabajador');
    var eliminarTrabajador = document.getElementById('eliminarTrabajador');
    var agregarCuadrilla = document.getElementById('guardarCuadrilla');
    var consultarCuadrilla = document.getElementById('consultarCuadrilla');
    var actualizarCuadrilla = document.getElementById('actualizarCuadrilla');
    var eliminarCuadrilla = document.getElementById('eliminarCuadrilla');

    agregarJefe.addEventListener('click', function(){
        cuadrillaId = document.getElementById('idCuadrilla').value

        jefe = document.getElementById('jefeCuadrilla');
        jefeId = jefe.value;
        
        if(cuadrillaId != ""){
            if(jefeId != 0 || jefeId != ""){
                jefeNombre = jefe.options[jefe.selectedIndex].text;
                
                data = {jefeId: jefeId, cuadrillaId: cuadrillaId}

                $.ajax({
                    url: '/agregarJefeCuadrilla',
                    type: 'POST',
                    contentType: 'application/json',
                    data: JSON.stringify(data),
                    success: function(response) {
                        if(response.respuesta != 0){
                            lista = document.getElementById('cuadrilla');
                            listaTrabajadores = lista.value;
                            lista.value = listaTrabajadores + "\n" + jefeId + "-" + jefeNombre + "(Jefe)";
                
                            var selectedIndex = jefe.selectedIndex;
                            if (selectedIndex !== -1) { 
                                jefe.remove(selectedIndex);
                            }
                            Swal.fire({
                                title: "Jefe de cuadrilla Agregado!",
                                text: "Jefe de cuadrilla  agregado correctamente a la cuadrilla!",
                                icon: "success"
                            });
                        }
                        else{
                            Swal.fire({
                                icon: "error",
                                title: "Eror al agragar jefe!",
                                text: "No se pudo agragar correctamente al Jefe en la cuadrilla!"
                              });
                        }
                    },
                    error: function(xhr, status, error) {
                        Swal.fire({
                            icon: "error",
                            title: "Eror al agragar el jefe!",
                            text: "No se pudo agragar correctamente al jefe en la cuadrilla!"
                          });
                        // console.error(xhr.responseText);
                        }
                    });

            }
            else{
                Swal.fire({
                    icon: "error",
                    title: "No hay jefes para seleccionar!",
                    text: "Agrega un jefe primero!"
                  });
            }
        }
        else{
            Swal.fire({
                icon: "error",
                title: "Se te olvida algo?",
                text: "Digita un ID de una cuadrilla!"
              });
        }

    });
    

    agregarTrabajador.addEventListener('click', function(){
        cuadrillaId = document.getElementById('idCuadrilla').value

        trabajador = document.getElementById('miembrosDisponibles');
        trabajadorId = trabajador.value;
        
        if(cuadrillaId != ""){
            if(trabajadorId != 0 || trabajadorId != ""){
                trabajadorNombre = trabajador.options[trabajador.selectedIndex].text;
                
                data = {trabajadorId: trabajadorId, cuadrillaId: cuadrillaId}

                $.ajax({
                    url: '/agregarTrabajadorCuadrilla',
                    type: 'POST',
                    contentType: 'application/json',
                    data: JSON.stringify(data),
                    success: function(response) {
                        if(response.respuesta != 0){
                            lista = document.getElementById('cuadrilla');
                            listaTrabajadores = lista.value;
                            lista.value = listaTrabajadores + "\n" + trabajadorId + "-" + trabajadorNombre;
                
                            var selectedIndex = trabajador.selectedIndex;
                            if (selectedIndex !== -1) { 
                                trabajador.remove(selectedIndex);
                            }
                            Swal.fire({
                                title: "Trabajador Agregado!",
                                text: "Trabajador agregado correctamente a la cuadrilla!",
                                icon: "success"
                            });
                        }
                        else{
                            Swal.fire({
                                icon: "error",
                                title: "Eror al agragar el trabajador!",
                                text: "No se pudo agragar correctamente al trabajador en la cuadrilla!"
                              });
                        }
                    },
                    error: function(xhr, status, error) {
                        Swal.fire({
                            icon: "error",
                            title: "Eror al agragar el trabajador!",
                            text: "No se pudo agragar correctamente al trabajador en la cuadrilla!"
                          });
                        // console.error(xhr.responseText);
                        }
                    });

            }
            else{
                Swal.fire({
                    icon: "error",
                    title: "No hay trajadores para seleccionar!",
                    text: "Agrega un trabajador primero!"
                  });
            }
        }
        else{
            Swal.fire({
                icon: "error",
                title: "Se te olvida algo?",
                text: "Digita un ID de una cuadrilla!"
              });
        }

    });


    eliminarTrabajador.addEventListener('click', function(){
        cuadrillaId = document.getElementById('idCuadrilla').value

        trabajador = document.getElementById('idTrabajadorEliminar');
        trabajadorId = trabajador.value;
        
        if(cuadrillaId != ""){
            if(trabajadorId != ""){
                
                data = {trabajadorId: trabajadorId, cuadrillaId: cuadrillaId}

                $.ajax({
                    url: '/eliminarTrabajadorCuadrilla',
                    type: 'POST',
                    contentType: 'application/json',
                    data: JSON.stringify(data),
                    success: function(response) {
                        if(response.respuesta != 0){
                            Swal.fire({
                                title: "Trabajador Eliminado!",
                                text: "Trabajador eliminado correctamente a la cuadrilla!",
                                icon: "success"
                            }).then((result) => {
                                if (result.isConfirmed) {
                                        window.location = 'gestionCuadrillas';
                                    }
                            });
                        }
                        else{
                            Swal.fire({
                                icon: "error",
                                title: "Eror al eliminar el trabajador!",
                                text: "No se pudo eliminar correctamente al trabajador en la cuadrilla!"
                              });
                            }
                        },
                        error: function(xhr, status, error) {
                            Swal.fire({
                                icon: "error",
                                title: "Eror al eliminar el trabajador!",
                                text: "No se pudo eliminar correctamente al trabajador en la cuadrilla!"
                              });
                            // console.error(xhr.responseText);
                        }
                    });

            }
            else{
                Swal.fire({
                    icon: "error",
                    title: "Se te olvida algo?",
                    text: "Digita el ID de un trabajador primero!"
                  });
            }
        }
        else{
            Swal.fire({
                icon: "error",
                title: "Se te olvida algo?",
                text: "Digita un ID de una cuadrilla!"
              });
        }

    });


    agregarCuadrilla.addEventListener('click', function(){
        nombreCuadrilla = document.getElementById('nombreCuadrilla').value
        
        if(nombreCuadrilla != ""){
                
                data = {nombreCuadrilla: nombreCuadrilla}

                $.ajax({
                    url: '/crearCuadrilla',
                    type: 'POST',
                    contentType: 'application/json',
                    data: JSON.stringify(data),
                    success: function(response) {
                        if(response.respuesta != 0){
                            Swal.fire({
                                title: "Se ha creado la cuadrilla!",
                                text: "La cuadrilla se ha creado de manera exitosa!",
                                icon: "success"
                            }).then((result) => {
                                if (result.isConfirmed) {
                                        document.getElementById('idCuadrilla').value =  response.id;
                                    }
                            });
                        }
                        else{
                            Swal.fire({
                                icon: "error",
                                title: "Error al crear la cuadrilla!",
                                text: "No se pudo crear la cuadrilla!"
                              });
                            }
                        },
                        error: function(xhr, status, error) {
                            Swal.fire({
                                icon: "error",
                                title: "Error al crear la cuadrilla!",
                                text: "No se pudo crear la cuadrilla!"
                              });
                            // console.error(xhr.responseText);
                        }
                    });
        }
        else{
            Swal.fire({
                icon: "error",
                title: "Se te olvida algo?",
                text: "Digita un nombre para la cuadrilla!"
              });
        }

    });

    actualizarCuadrilla.addEventListener('click', function(){
        cuadrillaId = document.getElementById('idCuadrilla').value
        nombreCuadrilla = document.getElementById('nombreCuadrilla').value
        
        if(nombreCuadrilla != ""){
            if(nombreCuadrilla != ""){
                data = {cuadrillaId: cuadrillaId, nombreCuadrilla: nombreCuadrilla}

                $.ajax({
                    url: '/actualizarCuadrilla',
                    type: 'POST',
                    contentType: 'application/json',
                    data: JSON.stringify(data),
                    success: function(response) {
                        if(response.respuesta != 0){
                            Swal.fire({
                                title: "Se ha actualizado la cuadrilla!",
                                text: "La cuadrilla se ha actualizado de manera exitosa!",
                                icon: "success"
                            }).then((result) => {
                                if (result.isConfirmed) {
                                        document.getElementById('idCuadrilla').value =  "";
                                        document.getElementById('nombreCuadrilla').value = "";
                                        document.getElementById('cuadrilla').value = ""
                                    }
                            });
                        }
                        else{
                            Swal.fire({
                                icon: "error",
                                title: "Error al actualizar la cuadrilla!",
                                text: "No se pudo actualizar la cuadrilla!"
                              });
                            }
                        },
                        error: function(xhr, status, error) {
                            Swal.fire({
                                icon: "error",
                                title: "Error al actualizar la cuadrilla!",
                                text: "No se pudo actualizar la cuadrilla!"
                              });
                            // console.error(xhr.responseText);
                        }
                    });
            }
            else{
                Swal.fire({
                    icon: "error",
                    title: "Se te olvida algo?",
                    text: "Digita un nombre para la cuadrilla!"
                  });
            }
        }
        else{
            Swal.fire({
                icon: "error",
                title: "Se te olvida algo?",
                text: "Digita el ID de la cuadrilla!"
              });
        }

    });

    consultarCuadrilla.addEventListener('click', function(){
        cuadrillaId = document.getElementById('idCuadrilla').value;
        
        if(cuadrillaId != ""){
                data = {cuadrillaId: cuadrillaId}

                $.ajax({
                    url: '/consultarCuadrilla',
                    type: 'POST',
                    contentType: 'application/json',
                    data: JSON.stringify(data),
                    success: function(response) {
                        if(response.nombreCuadrilla != null){
                            document.getElementById('nombreCuadrilla').value = response.nombreCuadrilla;
                            if(response.empleados != null){
                                var cuadrilla = "";
                                response.empleados.forEach(empleado => {
                                    if(empleado[0] == 2){
                                        cuadrilla += empleado[1] + "-" + empleado[2] + "(feje)\n";
                                    }
                                    else{
                                        cuadrilla += empleado[1] + "-" + empleado[2] + "\n";
                                    }
                                });
                                
                                document.getElementById('cuadrilla').value = cuadrilla; 
                            }
                        }
                        else{
                            Swal.fire({
                                icon: "error",
                                title: "Error al consultar la cuadrilla!",
                                text: "No se pudo consultar los datos la cuadrilla!"
                              });
                        }
                    },
                        error: function(xhr, status, error) {
                            Swal.fire({
                                icon: "error",
                                title: "Error al consultar la cuadrilla!",
                                text: "No se pudo consultar los datos la cuadrilla!"
                              });
                            // console.error(xhr.responseText);
                        }
                    });
        }
        else{
            Swal.fire({
                icon: "error",
                title: "Se te olvida algo?",
                text: "Digita el ID de la cuadrilla!"
              });
        }

    });
    

    eliminarCuadrilla.addEventListener('click', function(){
        cuadrillaId = document.getElementById('idCuadrilla').value;
        
        if(cuadrillaId != ""){
                data = {cuadrillaId: cuadrillaId}

                $.ajax({
                    url: '/eliminarCuadrilla',
                    type: 'POST',
                    contentType: 'application/json',
                    data: JSON.stringify(data),
                    success: function(response) {
                            if(response.resultado == 1){
                                swal.fire({
                                    icon: "success",
                                    title: "Se ha eliminado la cuadrilla!",
                                    text: "Se elimino la cuadrilla exitosamente!"
                                }).then((result) =>{
                                    document.getElementById('idCuadrilla').value = "";
                                    document.getElementById('nombreCuadrilla').value = "";
                                    document.getElementById('cuadrilla').value = "";
                                });
                            }
                            else{
                                Swal.fire({
                                    icon: "error",
                                    title: "Error al eliminar la cuadrilla!",
                                    text: "No se pudo eliminar la cuadrilla!"
                                  });
                            }
                        },
                        error: function(xhr, status, error) {
                            Swal.fire({
                                icon: "error",
                                title: "Error al eliminar la cuadrilla!",
                                text: "No se pudo eliminar la cuadrilla!"
                              });
                            // console.error(xhr.responseText);
                        }
                    });
        }
        else{
            Swal.fire({
                icon: "error",
                title: "Se te olvida algo?",
                text: "Digita el ID de la cuadrilla!"
              });
        }

    });
});