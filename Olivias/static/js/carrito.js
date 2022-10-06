var actualizarBtns = document.getElementsByClassName("actualizar-carrito"); //obtiene todos los botones con la clase actualizar-carrito

for (var i = 0; i < actualizarBtns.length; i++) {
  //recorre todos los botones
  actualizarBtns[i].addEventListener("click", function () {
    //agrega un evento click a cada boton
    var productoId = this.dataset.producto; //obtiene el id del producto
    var accion = this.dataset.accion; //obtiene el tipo de accion
    console.log("productoId:", productoId, "accion:", accion); //muestra en consola el id del producto y la accion

    console.log("USER:", user); //muestra en consola el usuario
    if (user === "AnonymousUser") {
      //si el usuario es anonimo
      console.log("No estas logueado"); //muestra en consola que no esta logueado
    } else {
      //si no
      actualizarCarrito(productoId, accion); //llama a la funcion actualizarCarrito
    }
  });
}

function actualizarCarrito(productoId, accion) {
  console.log("Usuario logueado, enviando datos..."); //muestra en consola que el usuario esta logueado

  var url = "/actualizar_item/"; //url de la vista actualizar_item

  fetch(url, {
    //envia los datos a la vista
    method: "POST", //metodo POST
    headers: {
      "Content-Type": "application/json", //tipo de contenido JSON
      "X-CSRFToken": csrftoken, //token de seguridad
    },
    body: JSON.stringify({ productoId: productoId, accion: accion }), //envia el id del producto y la accion
  })
    //recibe la respuesta
    .then((response) => {
      return response.json(); //convierte la respuesta a JSON
    })
    //recibe los datos
    .then((data) => {
      console.log("data:", data); //muestra en consola los datos
      location.reload(); //recarga la pagina
    });
}
