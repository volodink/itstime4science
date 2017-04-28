var markers = [];
var map;
console.log(123)
    <script type="text/javascript" charset="utf-8">
	  $(document).ready(function () {
var url = 'http://' + document.domain + ':' + location.port;
var socket = io.connect(url + "/mcc");
console.log(234)
socket.on('data', function (msg) {
  var numberOfFlight = msg['numberOfFlight'];
  var datatime = msg['datatime'];
  var lat = msg['lat'];
  var lon = msg['lon'];
  var alt = msg['alt'];
  var temp1 = msg['temp1'];
  var temp2 = msg['temp2'];
  var pressure1 = msg['pressure1'];
  var pressure2 = msg['pressure2'];
  var bat_crg = msg['bat_crg'];
  var bat_volt = msg['bat_volt'];
  var bat_temp = msg['bat_temp'];
  var vect_axel1x = msg['vect_axel1x'];
  var vect_axel1y = msg['vect_axel1y'];
  var vect_axel1z = msg['vect_axel1z'];
  var vect_axel2x = msg['vect_axel2x'];
  var vect_axel2y = msg['vect_axel2y'];
  var vect_axel2z = msg['vect_axel2z'];
  var ultraviolet1 = msg['ultraviolet1'];
  var ultraviolet2 = msg['ultraviolet2'];
  var infrared1 = msg['infrared1'];
  var infrared2 = msg['infrared2'];
  var hdop = msg['hdop'];
  var vdop = msg['vdop'];
  var sats = msg['sats'];
  var radiation = msg['radiation'];
  var dust = msg['dust'];
  var ozone = msg['ozone'];

  $('#numberOfFlight').text(numberOfFlight)
  $('#datatime').text(datatime)
  $('#lat').text(lat)
  $('#lon').text(lon)
  $('#alt').text(alt)
  $('#temp1').text(temp1)
  $('#temp2').text(temp2)
  $('#pressure1').text(pressure1)
  $('#pressure2').text(pressure2)
  $('#bat_crg').text(bat_crg)
  $('#bat_volt').text(bat_volt)
  $('#bat_temp').text(bat_temp)
  $('#vect_axel1x').text(vect_axel1x)
  $('#vect_axel1y').text(vect_axel1y)
  $('#vect_axel1z').text(vect_axel1z)
  $('#vect_axel2x').text(vect_axel2x)
  $('#vect_axel2y').text(vect_axel2y)
  $('#vect_axel2z').text(vect_axel2z)
  $('#ultraviolet1').text(ultraviolet1)
  $('#ultraviolet2').text(ultraviolet2)
  $('#infrared1').text(infrared1)
  $('#infrared2').text(infrared2)
  $('#hdop').text(hdop)
  $('#vdop').text(vdop)
  $('#sats').text(sats)
  $('#radiation').text(radiation)
  $('#dust').text(dust)
  $('#ozone').text(ozone)
});

socket.on('status', function (msg) {
  var datatime = msg['datatime'];
  var lat = msg['lat'];
  var lon = msg['lon'];
  var alt = msg['alt'];
  var temp1 = msg['temp1'];
  var temp2 = msg['temp2'];
  var pressure1 = msg['pressure1'];
  var pressure2 = msg['pressure2'];
  var bat_crg = msg['bat_crg'];
  var bat_volt = msg['bat_volt'];
  var bat_temp = msg['bat_temp'];
  var vect_axel1x = msg['vect_axel1x'];
  var vect_axel1y = msg['vect_axel1y'];
  var vect_axel1z = msg['vect_axel1z'];
  var vect_axel2x = msg['vect_axel2x'];
  var vect_axel2y = msg['vect_axel2y'];
  var vect_axel2z = msg['vect_axel2z'];
  var ultraviolet1 = msg['ultraviolet1'];
  var ultraviolet2 = msg['ultraviolet2'];
  var infrared1 = msg['infrared1'];
  var infrared2 = msg['infrared2'];
  var hdop = msg['hdop'];
  var vdop = msg['vdop'];
  var sats = msg['sats'];
  var radiation = msg['radiation'];
  var dust = msg['dust'];
  var ozone = msg['ozone'];

  $('#datatime').append(datatime)
  $('#lat').append(lat)
  $('#lon').append(lon)
  $('#alt').append(alt)
  $('#temp1').append(temp1)
  $('#temp2').append(temp2)
  $('#pressure1').append(pressure1)
  $('#pressure2').append(pressure2)
  $('#bat_crg').append(bat_crg)
  $('#bat_volt').append(bat_volt)
  $('#bat_temp').append(bat_temp)
  $('#vect_axel1x').append(vect_axel1x)
  $('#vect_axel1y').append(vect_axel1y)
  $('#vect_axel1z').append(vect_axel1z)
  $('#vect_axel2x').append(vect_axel2x)
  $('#vect_axel2y').append(vect_axel2y)
  $('#vect_axel2z').append(vect_axel2z)
  $('#ultraviolet1').append(ultraviolet1)
  $('#ultraviolet2').append(ultraviolet2)
  $('#infrared1').append(infrared1)
  $('#infrared2').append(infrared2)
  $('#hdop').append(hdop)
  $('#vdop').append(vdop)
  $('#sats').append(sats)
  $('#radiation').append(radiation)
  $('#dust').append(dust)
  $('#ozone').append(ozone)
});
var markers = [];
var map;

function getSomething(data) {
  var position = {lat: Number(data["lat"][count]), lng: Number(data["lon"][count])}
  addMarker(position, map);
}

function addMarker(location, map) {
  if ($("#follow").prop('checked'))
      map.setCenter(location);
  var marker = new google.maps.Marker({
      position: location,
      map: map,
      icon: "https://raw.githubusercontent.com/volodink/itstime4science/dev/web/frontend/static/img/title_icon.ico"
  });
}


function printData(data, sleep) {
  console.log(data)
  setInterval(function () {
      getSomething(data)

  }, sleep);
}


function initMap() {
  var myLatLng = {lat: 53.22544088, lng: 45.00208070};

  map = new google.maps.Map(document.getElementById('map'), {
      zoom: 11,
      center: myLatLng
  });

}

var count = 0;

function startAll() {
  printData(arr, 500);
}
});W
printData(arr, 500);
}




