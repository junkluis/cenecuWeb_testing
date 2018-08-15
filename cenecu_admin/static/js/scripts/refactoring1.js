
//Refactoring

/* Para validar el formato en descripción */
function validarLetrasNumeros(event) {
    var input = document.getElementById("descripcion").value;
    var key = event.key;            // Obtengo la tecla que presiono
    var keyCode = event.keyCode;    // Obtengo el codigo de la tecla
    expresion = /([A-Za-záéíóúÁÉÍÓÚñÑ´]+)/;
    expresion2 = /[A-Za-z0-9áéíóúÁÉÍÓÚñÑ´\s\.\',']+$/;
    if (expresion.test(input+key) == true && 
      expresion2.test(input+key) == true) {
        console.log("correcto");
    } else if(input.length > 255) {
        console.log("");
    } else {
        alert("- El primer caracter deber ser una letra." +
        "\n- Este campo permite solo permite letras y números.");
        event.preventDefault();
    }
}
