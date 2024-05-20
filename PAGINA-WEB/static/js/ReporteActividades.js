document.addEventListener('DOMContentLoaded', function(){
    // Obtener el contexto del lienzo donde se dibujará la gráfica
    var ctx = document.getElementById('myPieChart').getContext('2d');

    // Datos para la gráfica de pastel
    var numEsperaConfirmacion = document.getElementById('numEsperaConfirmacion').innerText
    var numPendiente = document.getElementById('numPendiente').innerText
    var numFinalizado = document.getElementById('numFinalizado').innerText
    var numCancelado = document.getElementById('numCancelado').innerText

    console.log(numEsperaConfirmacion);
    var data = {
        labels: ['Espera de Confirmacion', 'Pendiente', 'Finalizada', 'Cancelada'],
        datasets: [{
            data: [numEsperaConfirmacion, numPendiente, numFinalizado, numCancelado],
            backgroundColor: ['#36A2EB', '#FFCE56', '#00913f','#FF6384'],
            hoverBackgroundColor: ['#36A2EB', '#FFCE56', '#00913f', '#FF6384']
        }]
    };

    // Crear la gráfica de pastel
    var myPieChart = new Chart(ctx, {
        type: 'pie',
        data: data,
        options: {
            responsive: true,
            plugins: {
                legend: {
                    position: 'top',
                },
                tooltip: {
                    callbacks: {
                        label: function(tooltipItem) {
                            return tooltipItem.label + ': ' + tooltipItem.raw;
                        }
                    }
                }
            }
        }
});
});