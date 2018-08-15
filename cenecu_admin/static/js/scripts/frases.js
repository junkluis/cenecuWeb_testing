
//Validación de campos

/* Para validar el formato de la imagen, solo admite .jpg, .jpeg y .png */
function validarFormatoImagen() {
    var extensionImagenes = /(.jpg|.jpeg|.png)$/i;
    var imagen = document.getElementById('img_frase');
    var archivo = imagen.value;
    if (!extensionImagenes.test(archivo)) {
        console.log(archivo);
        alert("El formato de la imagen no es válido.");
        document.getElementById("img_frase").value = "";        
    }
}

/* Para resetear */
function resetForm() {
    document.getElementById("nuevaFrase-form").reset();
} 

$(document).ready(function() {
    $("table#fraseTable").DataTable({
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