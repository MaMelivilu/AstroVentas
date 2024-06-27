function iniciarMap(){
    var coord = {lat:-13.1627417 ,lng:-72.5450528};
    var map = new google.maps.Map(document.getElementById('map'),{
        zoom: 10,
        center: coord
    });
    var marker = new google.maps.Marker({
        position: coord,
        map: map
    })
}