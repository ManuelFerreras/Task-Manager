function iniciarSesion() {
  let form = document.getElementById('formulario');
  let mail = document.getElementById('mail');
  let pass = document.getElementById('pass');

  let data = new FormData(form);
  let xhr = new XMLHttpRequest();

  if(mail.value != '' && validateEmail(mail) && pass.value.length > 7 && pass.value.match(/^[0-9a-z]+$/)) {
    xhr.open("post", "/loginForm", false)
    xhr.send(data);

    if (xhr.status == 200){
      let respuesta = JSON.parse(xhr.responseText);
      alert(respuesta.mensaje);

    } else{
      let respuesta = JSON.parse(xhr.responseText);
      alert("Error: "+respuesta.mensaje);
    }
  } else {
    alert('Complete los campos correctamente.')
  }
}

function registrarCuenta() {
  let form = document.getElementById('formulario');
  let mail = document.getElementById('mail');
  let pass = document.getElementById('pass');

  let data = new FormData(form);
  let xhr = new XMLHttpRequest();

  if(mail.value != '' && validateEmail(mail) && pass.value.length > 7 && pass.value.match(/^[0-9a-z]+$/)) {
    xhr.open("post", "/registerForm", false)
    xhr.send(data);

    if (xhr.status == 200){
      let respuesta = JSON.parse(xhr.responseText);
      alert(respuesta.mensaje);

    } else if(xhr.status == 409){
      let respuesta = JSON.parse(xhr.responseText);
      alert("Error: " + respuesta.mensaje);
    } 
  } else {
    alert('Complete los campos correctamente.')
  }
}

function validateEmail(mail) { 
    if (/^[a-zA-Z0-9.!#$%&'*+/=?^_`{|}~-]+@[a-zA-Z0-9-]+(?:\.[a-zA-Z0-9-]+)*$/.test(mail.value)){
        return (true)
    } else {
        return (false)
    }
}