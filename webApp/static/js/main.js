function getCookie(name) {
  const value = `; ${document.cookie}`;
  const parts = value.split(`; ${name}=`);
  if (parts.length === 2) return parts.pop().split(";").shift();
}

function select_all_checkboxes() {
  const options = document.querySelectorAll("input[type='checkbox']");
  options.forEach(function (option) {
    option.checked = true;
  });
}

function delete_tag() {
  const options = document.querySelectorAll("input[type='checkbox']");
  let at_least_one_selected = false;
  var selected_tags = new Array();
  options.forEach(function (option) {
    if (option.checked) {
      at_least_one_selected = true;
      // Agrupar las tags seleccionadas
      selected_tags.push(option.value);
    }
  });

  if (!at_least_one_selected) {
    alert("Debe seleccionar al menos un tag. Inténtelo de nuevo.");
  } else {
    // Crear un objeto XMLHttpRequest
    var xhr = new XMLHttpRequest();

    // Definir la URL y el método de la solicitud
    var url = "/delete_tag/";
    var method = "POST";

    // Convertir los datos a formato de cadena
    var jsonData = JSON.stringify(selected_tags);

    // Configurar la solicitud AJAX
    xhr.open(method, url, true);
    xhr.setRequestHeader("X-CSRFToken", getCookie("csrftoken"));

    // Enviar la solicitud con los datos
    xhr.send(jsonData);
    setTimeout(function () {
      location.reload();
    }, 100);
  }
}

function data_ordering(selected_filter) {
  // Crear un objeto XMLHttpRequest
  var xhr = new XMLHttpRequest();

  // Definir la URL y el método de la solicitud
  var url = "/data_ordering/";
  var method = "POST";

  // Convertir los datos a formato de cadena
  var jsonData = JSON.stringify(selected_filter);

  // Configurar la solicitud AJAX
  xhr.open(method, url, true);
  xhr.setRequestHeader("X-CSRFToken", getCookie("csrftoken"));

  // Enviar la solicitud con los datos
  xhr.send(jsonData);
  setTimeout(function () {
    location.reload();
  }, 100);
}

function update_data_tags() {
  // Crear un objeto XMLHttpRequest
  var xhr = new XMLHttpRequest();

  // Definir la URL y el método de la solicitud
  var url = "/update_data_tags/";
  var method = "POST";

  // Configurar la solicitud AJAX
  xhr.open(method, url, true);
  xhr.setRequestHeader("X-CSRFToken", getCookie("csrftoken"));
  xhr.onreadystatechange = function () {
    if (xhr.readyState === 4 && xhr.status === 200) {
      var response = JSON.parse(xhr.responseText);
      // Realiza acciones con la respuesta recibida desde Python
      setTimeout(function () {
        location.reload();
      }, 100);
    }
  };

  // Enviar la solicitud
  xhr.send();
}
