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
      addCookieItem(productoId, accion); //agrega el producto al carrito
    } else {
      //si no
      actualizarCarrito(productoId, accion); //llama a la funcion actualizarCarrito
    }
  });
}

function addCookieItem(productoId, accion) {
  console.log("Usuario no logueado"); //muestra en consola que el usuario no esta logueado

  if (accion == "add") {
    if (carrito[productoId] == undefined) {
      //si el producto no esta en el carrito
      carrito[productoId] = { cantidad: 1 }; //agrega el producto al carrito
    } else {
      carrito[productoId]["cantidad"] += 1; //si el producto ya esta en el carrito, aumenta la cantidad
    }
  }

  if (accion == "remove") {
    carrito[productoId]["cantidad"] -= 1; //si el producto ya esta en el carrito, disminuye la cantidad

    if (carrito[productoId]["cantidad"] <= 0) {
      console.log("Eliminar item"); //muestra en consola que se va a eliminar el item
      delete carrito[productoId]; //elimina el producto del carrito
    }
  }
  console.log("carrito:", carrito); //muestra en consola el carrito
  document.cookie = "carrito=" + JSON.stringify(carrito) + ";domain=;path=/";
  location.reload(); //recarga la pagina
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
