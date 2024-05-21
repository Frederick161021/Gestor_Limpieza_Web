document.addEventListener('DOMContentLoaded', function(){
    var form = document.getElementById('uploadForm');
    form.addEventListener('submit', function(event){
        event.preventDefault();
        var imagen = document.getElementById('image').value.split('\\').pop();
        var comentarios = document.getElementById('comment').value;
        
        var data = {imagen: imagen, comentarios: comentarios}
        $.ajax({
            url: '/finalizarActividad',
            type: 'POST',
            contentType: 'application/json',
            data: JSON.stringify(data),
            success: function(response) {
                Swal.fire({
                    title: "Actividad finalizada!",
                    text: "La actividad se finalizo correctamente!",
                    icon: "success"
                  }).then((result)=>{
                    window.location = "actividadesPendientes";
                  });
            },
            error: function(xhr, status, error) {
                Swal.fire({
                    icon: "error",
                    title: "Eror al terminar Actividad!",
                    text: "No se pudo terminar la actividad!"
                  });
                // console.error(xhr.responseText);
            }
        });
    });

});