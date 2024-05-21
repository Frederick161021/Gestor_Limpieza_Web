window.addEventListener('pageshow', function (event) {
  if (event.persisted) {
    window.location.reload();
  }
});
document.addEventListener('DOMContentLoaded', function () {
  var botonSalir = document.getElementById('btnSalir');
  var btnTerminar = document.querySelectorAll('#terminar');
  console.log(btnTerminar);

  if(botonSalir != null){
    botonSalir.addEventListener('click', function () {
      Swal.fire({
        title: "Seguro que quieres salir?",
        showDenyButton: false,
        showCancelButton: true,
        confirmButtonText: "Salir"
      }).then((result) => {
        /* Read more about isConfirmed, isDenied below */
        if (result.isConfirmed) {
          Swal.fire("Adios", "", "Nos vemos pronto!");
          $.ajax({
            url: '/cerrarSeccion',
            type: 'GET',
            contentType: 'application/json',
            success: function (response) {
              console.log('Cerró sesión con éxito:', response);
              window.location = 'login';
            },
            error: function (xhr, status, error) {
              Swal.fire({
                icon: "error",
                title: "Se te olvida algo?",
                text: "Te hace falta digitar la contraseña!"
              });
              console.error('Error:', xhr.responseText);
            }
          });
        }
      });
    });
  }

  btnTerminar.forEach(function(boton){
    boton.addEventListener('click', function(){
        var actividadId = boton.value;
        var data = {actividadId: actividadId}
        $.ajax({
          url: '/setActividadId',
          type: 'POST',
          contentType: 'application/json',
          data: JSON.stringify(data),
          success: function(response) {
            window.location = "terminarActividad";
          },
              error: function(xhr, status, error) {
                  Swal.fire({
                      icon: "error",
                      title: "Se ha producido un erro Error!",
                      text: "No se pudo terminar la actividad!"
                    });
                  // console.error(xhr.responseText);
              }
          });
    });
  });
});