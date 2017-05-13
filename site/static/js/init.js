(function($){
  $(function(){

    $('.button-collapse').sideNav();
    $('.parallax').parallax();
    var mymap = L.map('mapid').setView([46.247377, 1.504289], 13);
    var fistIcon = L.icon({
        iconUrl: 'static/leaflet/images/fist.png',
        shadowUrl: 'static/leaflet/images/fist-shadow.png',

        iconSize:     [41, 59], // size of the icon
        shadowSize:   [82, 63], // size of the shadow
        iconAnchor:   [20, 59], // point of the icon which will correspond to marker's location
        shadowAnchor: [20, 59],  // the same for the shadow
        popupAnchor:  [-3, -76] // point from which the popup should open relative to the iconAnchor
    });
    L.tileLayer('https://api.tiles.mapbox.com/v4/{id}/{z}/{x}/{y}.png?access_token=pk.eyJ1IjoibWFwYm94IiwiYSI6ImNpejY4NXVycTA2emYycXBndHRqcmZ3N3gifQ.rJcFIG214AriISLbB6B5aw', {
      maxZoom: 18,
      attribution: 'Map data &copy; <a href="http://openstreetmap.org">OpenStreetMap</a> contributors, ' +
        '<a href="http://creativecommons.org/licenses/by-sa/2.0/">CC-BY-SA</a>, ' +
        'Imagery © <a href="http://mapbox.com">Mapbox</a>',
      id: 'mapbox.streets'
    }).addTo(mymap);

    L.marker([46.247377, 1.504289], {icon: fistIcon}).addTo(mymap);



  }); // end of document ready
})(jQuery); // end of jQuery name space
