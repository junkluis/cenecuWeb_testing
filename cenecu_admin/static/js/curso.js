function validarIngresos() {
    //Validar nombre curso
    console.log("johan estuvo aqui");
    var nombre = document.getElementById('nombreCurso').value;
    var descripcion = document.getElementById('descripcion').value;
    var area = document.getElementById('area').selectedIndex;
    var pensum = document.getElementById('pensum');
    var filePensum = pensum.value;
    var duracion = document.getElementById('duracion');
    var tipoDuracion = document.getElementById('tipoDuracion').selectedIndex;
    var costo = document.getElementById('costo').value;
    var profesor = document.getElementById('profesor').selectedIndex;
    var imagen = document.getElementById('imagen');
    var fileImagen = document.getElementById('imagen');
    var estado = document.getElementById('estado').selectedIndex;
    var extensionImagenes = /(.jpg|.jpeg|.png)$/i;
    var extensionArchivo = /(.pdf|)$/i;

    if ( /^[a-zA-Z]/.test(nombre)== false || /^\s+$/.test(nombre)){
        alert("Ingresa un nombre valido");
        return false;
    }
    if ( /^[a-zA-Z])/.test(descripcion) ||/^\s+$/.test(descripcion)){
        alert("Ingresa una descripcion valida");
        return false;
    }
    if ( area == "" || area == null){
    	alert("Debe seleccionar un area");
    	return false;
    }

    if(!extensionArchivo.exec(filePensum)){
    	alert("El formato del pensum debe ser PDF");
    }

    if (duracion =="" || area == null){
    	alert("Ingresa duracion para el curso");
    	return false;
    }

    if (tipoDuracion == "" || tipoDuracion == null){ 
    	alert("Ingrese tipo de duracion");
    	return false;

    }

    if (profesor == "" || tipoDuracion == null){ 
    	alert("Seleccione un profesor");
    	return false;

    }

    if (!extensionImagenes.exec(fileImagen)){
    	alert("El formato de la imagen no es valido");
    	return false;
    }


    return true;

}
