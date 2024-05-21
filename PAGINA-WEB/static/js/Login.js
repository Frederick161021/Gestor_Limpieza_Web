document.addEventListener("DOMContentLoaded", function(){
    var ingresarButton = document.getElementById("ingresarButton");

    ingresarButton.addEventListener("click", function(){
        var usuario = document.getElementById("usuario").value;
        var contraseña = document.getElementById("contrasena").value;

        if (usuario == ""){
            Swal.fire({
              icon: "error",
              title: "Se te olvida algo?",
              text: "Te hace falta digitar el nombre del usario!"
            });
        }
        else if (contraseña == ""){
            Swal.fire({
              icon: "error",
              title: "Se te olvida algo?",
              text: "Te hace falta digitar la contraseña!"
            });
        }
        else{
            
            var data = {usuario: usuario, contraseña: contraseña}
            
            $.ajax({
                url: '/Login',
                type: 'POST',
                contentType: 'application/json',
                data: JSON.stringify(data),
                success: function(response) {
                    console.log(response.rolId);
                    switch (response.rolId){
                        case 1: 
                        window.location = "menuAdmin";
                        break;
                        case 2: 
                        window.location = "menuJefe";
                        break;
                        case 3:
                            window.location = "actividadesPendientes";
                            break;
                        }
                        
                    },
                    error: function(xhr, status, error) {
                        Swal.fire({
                          icon: "error",
                          title: "Quien eres tu?",
                          text: "Verififca tus datos!"
                        });
                        
                        // console.error(xhr.responseText);
                }
            });

            // window.location ="menuJefe";

            // var xhr = new XMLHttpRequest();
            // xhr.open("POST", "/Login", true);
            // xhr.setRequestHeader("Content-Type", "application/json");
            // var data = JSON.stringify({"usuario": usuario, "contraseña":contraseña});
            // xhr.send(data);
        }
    });

});
     
