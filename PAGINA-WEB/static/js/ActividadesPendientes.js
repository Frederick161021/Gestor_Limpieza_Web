window.addEventListener('pageshow', function(event) {
    if (event.persisted) {
        window.location.reload();
    }
});
document.addEventListener('DOMContentLoaded', function(){
    var botonSalir = document.getElementById('btnSalir');

    botonSalir.addEventListener('click', function(){
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
                success: function(response) {
                    console.log('Cerró sesión con éxito:', response);
                    window.location = 'login';
                },
                error: function(xhr, status, error) {
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
});