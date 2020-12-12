
let url = "http://127.0.0.1:8000/api/DetallePlanes/?format=json"
$.get (url, function(respuesta){

    console.log(respuesta)
}, "jason" )