
//Validación de campos

$(document).ready(function() {
    $("table#anuncioTable").DataTable({
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

/* Para validar el formato en descripción de anuncios publicitarios */
function validarLetrasNumeros(event) {
    var input = document.getElementById("descripcion").value;
    var key = event.key;            // Obtengo la tecla que presiono
    var keyCode = event.keyCode;    // Obtengo el codigo de la tecla
    expresion = /([A-Za-záéíóúÁÉÍÓÚñÑ´]+)/;
    expresion2 = /[A-Za-z0-9áéíóúÁÉÍÓÚñÑ´\s\.\','\'%']+$/;
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

/* Para resetear */
function resetForm() {  
    document.getElementById("nuevoAnuncio-form").reset();
}

/* Para validar el formato de la imagen, solo admite .jpg, .jpeg y .png */
function validarFormatoImagen() {
    var extensionImagenes = /(.jpg|.jpeg|.png)$/i;
    var imagen = document.getElementById("img_anuncio");
    var archivo = imagen.value;
    if (!extensionImagenes.test(archivo)) {
        console.log(archivo);
        alert("El formato de la imagen no es válido.");
        document.getElementById("img_anuncio").value = "";
    }
}

/* Para obtener la fecha del sistema, colocarla en el input y en min */
function fechaDelSistema(_id) {
    var _dat = document.querySelector(_id);
    var hoy = new Date(),
          d = hoy.getDate(),
          m = hoy.getMonth()+1, 
          y = hoy.getFullYear(),
          data;
    if (d < 10) {
        d = "0" + d;
    }
    if (m < 10) {
        m = "0" + m;
    }
    var fechaActual = y + "-" + m + "-" + d;
    _dat.value = fechaActual;
}

fechaDelSistema("#fecha_limite");
var pc = document.getElementById("fecha_limite").value;
document.getElementById("fecha_limite").min = pc;