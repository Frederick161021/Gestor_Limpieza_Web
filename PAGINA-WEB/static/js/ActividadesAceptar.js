window.addEventListener('pageshow', function(event) {
    if (event.persisted) {
        window.location.reload();
    }
});
document.addEventListener('DOMContentLoaded', function(){
    var btnAceptar = document.querySelectorAll('.aceptar-button');
    var btnRechazar = document.querySelectorAll('.rechazar-button');

    btnAceptar.forEach(function(button) {
        button.addEventListener('click', function(){
            var actividadId = button.value;
            var data = {actividadId: actividadId, estatus: 2}
            $.ajax({
                url: '/actualizarEstatusActividades',
                type: 'POST',
                contentType: 'application/json',
                data: JSON.stringify(data),
                success: function(response) {
                    Swal.fire({
                        title: "Actividad aceptada!",
                        text: "Se ah aceptado eh iformado a todos tus empleados!",
                        icon: "success"
                      }).then((result)=>{
                        window.location.reload();
                      });
                },
                    error: function(xhr, status, error) {
                        Swal.fire({
                            icon: "error",
                            title: "Eror al aceptar Actividad!",
                            text: "No se pudo aceptar la actividad!"
                          });
                        // console.error(xhr.responseText);
                    }
                });
            });
        });
        
        btnRechazar.forEach(function(button) {
            button.addEventListener('click', function(){
                var actividadId = button.value;
                var data = {actividadId: actividadId, estatus: 4};
                $.ajax({
                    url: '/actualizarEstatusActividades',
                    type: 'POST',
                    contentType: 'application/json',
                    data: JSON.stringify(data),
                    success: function(response) {
                        Swal.fire({
                            title: "Actividad rechazada!",
                            text: "Se ha rechazado la actividad!",
                            icon: "success"
                          }).then((result)=>{
                            window.location.reload();
                          });
                    },
                        error: function(xhr, status, error) {
                            Swal.fire({
                                icon: "error",
                                title: "Eror al rechazar la Actividad!",
                                text: "No se pudo rechazar la actividad!"
                              });
                            // console.error(xhr.responseText);
                        }
                    });
        });
    });
});