$(document).ready(function () {
var url = 'http://' + document.domain + ':' + location.port;
var socket = io.connect(url + "/mcc");
	socket.on('connect', function() {
		socket.emit('last_dots');
	});

socket.on('lastMarkers', function (msg) {
		var json_packet = msg['json_data'];
		console.log(json_packet);
		var json = JSON.parse(json_packet);
		json.forEach(function (item, i, json) {
			j = json[i];
			lat = j.lat;
			lon = j.lon;
			var position = {lat: parseFloat(lat), lng: parseFloat(lon)};
			addMarker(position,map,lat,lon); 

	})
})
socket.emit('my_event',{data: 0});
n=0
socket.emit('my_event2',{data: 0});
/*socket.on('aprs', function (msg) {
	alert('APRS');
	if (n==0){
		var markers = [];
		APRS(msg,markers);
		n=1;
	}	
	else	{
			setTimeout(function(){
	  		APRS(msg,markers);
			}, 300000);
		}
});*/

k=0;
i =0; 
socket.on('gprs', function (msg) {
	if (i==0){
		var markers = [];
		GPRS(msg,markers);
		i=1;
		 }
	else	{
			setTimeout(function(){
	  		GPRS(msg,markers);
			}, 5000);
		}	
			
});
function APRS(msg){
					if (msg['json_data'] != 0){
						change_data(msg['type'],k);
						var json_packet = msg['json_data'];
						var json = JSON.parse(json_packet);
								json.forEach(function (item, i, json) {
									    j = json[i];
									    lat = j.lat;
									    lon = j.lon;
									    $('#id').html(j.id);
									    $('#numberOfFlight').html(j.numberOfFlight);
									    $('#datetime').html(j.datetime);
									    $('#temp1').html(j.temp1);
									    $('#lat').html(j.lat);
									    $('#lon').html(j.lon);
									    $('#alt').html(j.alt);
									    $('#vect_axel1x').html(j.vect_axel1x);
									    $('#vect_axel1y').html(j.vect_axel1y);
									    $('#vect_axel1z').html(j.vect_axel1z);
									    var mas = ['datetime','lat','temp1','vect_axel1x'];
										    for(var i = 0; i < mas.length; i++) {
											change_color(mas[i], j.status[mas[i]])
										    }
									    var position = {lat: parseFloat(lat), lng: parseFloat(lon)};
									    addMarker(position,map,lat,lon);
									    console.log("Данные есть, омномном");
								})
					}    
					console.log("Данных нема, хозяина");
					socket.emit('my_event2',{data: j.id});
}
function GPRS(msg){
					if (msg['json_data'] != 0){
						change_data(msg['type'],k);
						var json_packet = msg['json_data'];
						var json = JSON.parse(json_packet);
									json.forEach(function (item, i, json) {
									    j = json[i];
									    lat = j.lat;
									    lon = j.lon;
									    $('#id').html(j.id);
									    $('#numberOfFlight').html(j.numberOfFlight);
									    $('#datetime').html(j.datetime);
									    $('#lat').html(j.lat);
									    $('#lon').html(j.lon);
									    $('#alt').html(j.alt);
									    $('#temp1').html(j.temp1);
									    $('#temp2').html(j.temp2);
									    $('#pressure1').html(j.pressure1);
									    $('#pressure2').html(j.pressure2);
									    $('#bat_crg').html(j.bat_crg);
									    $('#bat_volt').html(j.bat_volt);
									    $('#bat_temp').html(j.bat_temp);
									    $('#vect_axel1x').html(j.vect_axel1x);
									    $('#vect_axel1y').html(j.vect_axel1y);
									    $('#vect_axel1z').html(j.vect_axel1z);
									    $('#vect_axel2x').html(j.vect_axel2x);
									    $('#vect_axel2y').html(j.vect_axel2y);
									    $('#vect_axel2z').html(j.vect_axel2z);
									    $('#ultraviolet1').html(j.ultraviolet1);
									    $('#ultraviolet2').html(j.ultraviolet2);
									    $('#infrared1').html(j.infrared1);
									    $('#infrared2').html(j.infrared2);
									    $('#hdop').html(j.hdop);
									    $('#vdop').html(j.vdop);
									    $('#sats').html(j.sats);
									    $('#radiation').html(j.radiation);
									    $('#dust').html(j.dust);
									    $('#ozone').html(j.ozone);
									    var mas = ['datetime','lat','lon','alt','temp1','temp2','pressure1','pressure2','bat_crg',
									    'bat_volt','bat_temp','vect_axel1x','vect_axel1y','vect_axel1z','vect_axel2x','vect_axel2y','vect_axel2z',
									    'ultraviolet1','ultraviolet2','infrared1','infrared2','hdop','vdop','sats','radiation','dust','ozone'];
	
												    for(var i = 0; i < mas.length; i++) {
													change_color(mas[i], j.status[mas[i]])
												    }
									    var position = {lat: parseFloat(lat), lng: parseFloat(lon)};
									    addMarker(position,map,lat,lon);
									    console.log("Данные есть, омномном");
									})
					}    
			console.log("Данных нема, хозяина");
			socket.emit('my_event',{data: j.id}); 	
	
};
});


function addMarker(location, map,lat,lon){

	var marker = new google.maps.Marker({
	position: location,
	map: map,
	icon: "https://raw.githubusercontent.com/volodink/itstime4science/dev/web/frontend/static/img/title_icon.ico"
	});
	marker.setMap(map);
	if (!!markers[9]){
		el = markers.shift();
		el.setMap(null)
		markers.push(marker);
		console.log(markers);
		var lastMarker = markers[markers.length - 1];
		lastMarker.setMap(map)
		console.log("10 маркеров");
		}
	else{	console.log("Маркеров меньше 10");
		markers.push(marker);
		console.log(markers);
		marker.setMap(map)
		};
	marker.setMap(map);
};

