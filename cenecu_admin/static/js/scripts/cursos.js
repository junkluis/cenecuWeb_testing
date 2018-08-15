
//Validación de campos

/* Para validar el formato de nombre de curso */
function validarLetrasNumerosNombre(event) {
    var input = document.getElementById("nombreCurso").value;
    var key = event.key;            // Obtengo la tecla que presiono
    var keyCode = event.keyCode;    // Obtengo el codigo de la tecla
    expresion = /([A-Za-záéíóúÁÉÍÓÚñÑ´]+)/;
    expresion2 = /[A-Za-z0-9áéíóúÁÉÍÓÚñÑ´\s\.\',']+$/;
    if (expresion.test(input+key) == true && 
      expresion2.test(input+key) == true) {
        console.log("correcto");
    } else if (input.length > 255) {
        console.log("");
    } else {
        alert("- El primer caracter deber ser una letra." +
        "\n- Este campo permite solo permite letras y números.");
        event.preventDefault();
    }
}

/* Para validar el formato del pensum, solo admite .pdf */
function validarFormatoArchivo() {
    var extensionArchivo = /(.pdf)$/i;
    var pensum = document.getElementById("pensum");
    var filePensum = pensum.value;
    if (!extensionArchivo.test(filePensum)) {
        console.log(filePensum);
        alert("El formato del pensum debe ser PDF.");
        document.getElementById("pensum").value = "";            
    }
}

/* Para validar el formato de la imagen, solo admite .jpg, .jpeg y .png */
function validarFormatoImagen() {
    var extensionImagenes = /(.jpg|.jpeg|.png)$/i;
    var imagen = document.getElementById("imagen");
    var fileImagen = imagen.value;
    if (!extensionImagenes.test(fileImagen)) {
        console.log(fileImagen);
        alert("El formato de la imagen no es válido.");
        document.getElementById("imagen").value = "";            
    }
}

function validarHoras() {
    var inputHoraInicio = document.getElementById("hora-inicio").value.split(":");
    console.log(inputHoraInicio);
    var inputHoraFin = document.getElementById("hora-fin").value.split(":");
    var horaInicio = inputHoraInicio[0];
    var minInicio = inputHoraInicio[1];
    var horaFin = inputHoraFin[0];
    var minFin = inputHoraFin[1];
    if ( parseInt(horaFin) < parseInt(horaInicio)) {
        alert("La hora ingresada no es valida");
        document.getElementById("hora-fin").value = "";
    }
}

/* Para validar el costo de cursos */
function validarCosto(event) {
    var input = document.getElementsById("costo").value;
    var key = event.key;            // Obtengo la tecla que presiono
    var keyCode = event.keyCode;    // Obtengo el codigo de la tecla
    expresion = /^[0-9]+[0-9\.]+$/;
    if (!expresion.test(input+key)) {
        alert("Este campo solo permite números");
        event.preventDefault();
    }
}

/* Para resetear */
function resetForm() {
    document.getElementById("nuevoCurso-form").reset();
}

$(document).ready(function() {
    $("table#cursoTable").DataTable({
      "ordering": false,
    });
});

$(".delete").on("click", function (e) {
    e.preventDefault();
    var choice = confirm($(this).attr("data-confirm"));
    if (choice) {
        window.location.href = $(this).attr("href");
    }
});