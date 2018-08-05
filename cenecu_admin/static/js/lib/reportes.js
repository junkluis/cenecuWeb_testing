lista_reporte=[]
lista_curso_numregistro = []

    setInterval(function() {
        jQuery.ajax({
            url: "/cenecu_admin/refresh",
            dataType: "json",
            type: 'GET',
            success: function (datos) {
                lista_reporte = datos.lista_reporte;
                lista_curso_numregistro = datos.lista_curso_numregistro
            },
            error: function(XMLHttpRequest, textStatus, errorThrown){
                console.log(errorThrown);
            }
        });
    var ctx = document.getElementById("grafico-usuarios-interes").getContext('2d');
                var i;
                var myChart = new Chart(ctx, {
                type: 'pie',
                data: {
                    for (i = 0; i < lista_reporte.length; i++) { 
                    labels: [ " i.keys "],
                    }
                   
                    datasets: [{
                        label: '# Usuarios Interesados',
                        data: [{% for d in lista_reporte %} {{d.values}}, {% endfor %}],
                        backgroundColor: [
                            'rgba(255, 99, 132, 0.2)',
                            'rgba(54, 162, 235, 0.2)',
                            'rgba(255, 206, 86, 0.2)',
                            'rgba(75, 192, 192, 0.2)',
                            'rgba(153, 102, 255, 0.2)',
                            'rgba(255, 159, 64, 0.2)'
                        ],
                        borderColor: [
                            'rgba(255,99,132,1)',
                            'rgba(54, 162, 235, 1)',
                            'rgba(255, 206, 86, 1)',
                            'rgba(75, 192, 192, 1)',
                            'rgba(153, 102, 255, 1)',
                            'rgba(255, 159, 64, 1)'
                        ],
                        borderWidth: 1
                    }]
                },
                 options: {
                    scales: {
                        yAxes: [{
                            display: false,
                            ticks: {
                                beginAtZero:true
                            }
                        }]
                        }
                    }
                }); 