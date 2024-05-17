window.addEventListener('pageshow', function(event) {
    if (event.persisted) {
        window.location.reload();
    }
});
document.addEventListener('DOMContentLoaded', function(){
    document.getElementById('tabla').style.visibility = 'hidden';

    var btnBuscarColonia = document.getElementById('btnConsultar');
    var btnAgregar = document.getElementById('btnAgregar');

    btnBuscarColonia.addEventListener('click', function(){
        var nombreColonia = document.getElementById('nombreColonia').value;
        if(nombreColonia != ""){
            var data = {nombreColonia: nombreColonia}
            
            $.ajax({
                url: '/buscarPorNombreColonia',
                type: 'POST',
                contentType: 'application/json',
                data: JSON.stringify(data),
                success: function(response) {
                    if(response.colonias.length != 0){
                        actualizarTabla(response.colonias);
                    }
                    else{
                        Swal.fire({
                            icon: "error",
                            title: "Eror al buscar las colonias!",
                            text: "No se encontro ninguna colonia!"
                          });
                          document.getElementById('tabla').style.visibility = 'Hidden';
                    }
                },
                error: function(xhr, status, error) {
                }
            });
        }
        else{
            Swal.fire({
                icon: "error",
                title: "Se te olvida algo?",
                text: "Te hace falta digitar el nombre de la colonia!"
              });
        }
    });

    function actualizarTabla(colonias) {
        var tbody = document.querySelector('table tbody');
        tbody.innerHTML = '';  // Limpia el contenido existente

        colonias.forEach(function(colonia) {
            var tr = document.createElement('tr');
            colonia.forEach(function(campo) {
                var td = document.createElement('td');
                td.textContent = campo;
                tr.appendChild(td);
            });
            tbody.appendChild(tr);
        });
        
        document.getElementById('tabla').style.visibility = 'visible';
        document.getElementById('noColonias').style.visibility = 'hidden';
    }

    btnAgregar.addEventListener('click', function(){
        var idColonia = document.getElementById('idColonia').value;

        if(idColonia != ""){
            var data = {coloniaId: idColonia}
            
            $.ajax({
                url: '/agregarColonia',
                type: 'POST',
                contentType: 'application/json',
                data: JSON.stringify(data),
                success: function(response) {
                    if(response.resultado != 0){
                        Swal.fire({
                            title: "Colonia Agregada!",
                            text: "La colonia ha sido agregada a las opciones disponibles!",
                            icon: "success"
                          });
                    }
                    else{
                        Swal.fire({
                            icon: "error",
                            title: "Eror al agregar la colonia!",
                            text: "No se agregar la colonia!"
                          });
                          document.getElementById('tabla').style.visibility = 'Hidden';
                    }
                },
                error: function(xhr, status, error) {
                    Swal.fire({
                        icon: "error",
                        title: "Eror al agregar la colonia!",
                        text: "No se agregar la colonia!"
                      });
                      document.getElementById('tabla').style.visibility = 'Hidden';
                }
            });
        }
        else{
            Swal.fire({
                icon: "error",
                title: "Se te olvida algo?",
                text: "Te hace falta digitar el id de la colonia!"
              });
        }
    });


});