
//Validación de campos

/* Para validar el formato en nombre de área */
function validarLetras(event) {
    var input = document.getElementsByClassName("letras").value;
    var key = event.key;
    var keyCode = event.keyCode;
    var expresion = /^[A-Za-záéíóúÁÉÍÓÚñÑ\s\.\',']+$/;
    if (!expresion.test(input+key)) {
        alert("Este campo permite solo permite letras.");
        event.preventDefault();
    }
}

/* Para validar el formato de la imagen, solo admite .jpg, .jpeg y .png */
function validarFormatoImagen() {
    var extensionImagenes = /(.jpg|.jpeg|.png)$/i;
    var imagen = document.getElementById("img_area");
    var archivo = imagen.value;
    if (!extensionImagenes.test(archivo)) {
        console.log(archivo);
        alert("El formato de la imagen no es válido.");
        document.getElementById("img_area").value = "";        
    }
}

/* Para resetear */
function resetForm(){
    document.getElementById("nuevoArea-form").reset();
}

$(document).ready(function() {
    $("table#areaTable").DataTable({
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