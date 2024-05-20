document.addEventListener('DOMContentLoaded', function(){
    var btnGuardarAsignaccion = document.getElementById('btnGuardarAsignacion');

    btnGuardarAsignaccion.addEventListener('click', function(){
        var txtDescripcion = document.getElementById('descripcion').value;
        var txtfecha = document.getElementById('fechaAgendada').value;
        var coloniaId = document.getElementById('seleccionarColonia').value;
        var cuadrillaId = document.getElementById('seleccionarCuadrilla').value;
        
        if(txtDescripcion != "" && txtfecha != "" && coloniaId != "" && cuadrillaId != ""){
            console.log(descripcion);
            var data = {descripcion: txtDescripcion, fecha: txtfecha, cuadrillaId: cuadrillaId, coloniaId: coloniaId}

            $.ajax({
                url: '/crearActividad',
                type: 'POST',
                contentType: 'application/json',
                data: JSON.stringify(data),
                success: function(response) {
                    if(response.respuesta != 0){
                        Swal.fire({
                            icon: "success",
                            title: "Actividad ha sido asignada!",
                            text: "Se ha avisado al jefe de la cuadrilla!"
                        }).then((result)=>{
                            document.getElementById('descripcion').value = "";
                            document.getElementById('fechaAgendada').value = "";
                        });
                    }
                    else{
                        Swal.fire({
                            icon: "error",
                            title: "Eror al asignar la Actividad!",
                            text: "No se pudo asignar la actividad!"
                          });
                    }
                },
                error: function(xhr, status, error) {
                }
            });
        }else{
            swal.fire({
                icon: "error",
                title: "Se te olvida algo?",
                text: "Asegurate de haber llenado todos los campos!"
              });
        }
    });
});