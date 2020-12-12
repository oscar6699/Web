function iniciarMap(){
    var coord = {lat:-33.363603 ,lng:-70.677856};
    var map = new google.maps.Map(document.getElementById('map'),{
        zoom: 15, center: coord

    },);
}

