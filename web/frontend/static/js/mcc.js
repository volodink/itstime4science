$(document).ready(function () {
var markers_gprs = [];
var markers_aprs = [];
var markers_telem = [];

var url = 'http://' + document.domain + ':' + location.port;
var socket = io.connect(url + "/mcc");
	socket.on('connect', function() {
		socket.emit('last_dots');
	});

socket.on('lastMarkers', function (msg) {
		console.log(msg['gprs']);
		var gprs = msg['gprs'];
		var json = JSON.parse(gprs);
		json.forEach(function (item, i, json) {
			j = json[i];
			lat = j.lat;
			lon = j.lon;
			var position = {lat: parseFloat(lat), lng: parseFloat(lon)};
			addMarker(position,map,lat,lon,markers_gprs,'gprs');
		})

        console.log(msg['aprs']);
		var aprs = msg['aprs'];
		var json = JSON.parse(aprs);
		json.forEach(function (item, i, json) {
			j = json[i];
			lat = j.lat;
			lon = j.lon;
			var position = {lat: parseFloat(lat), lng: parseFloat(lon)};
			addMarker(position,map,lat,lon,markers_aprs,'aprs');
		})

        /*console.log(msg['telemetry']);
		var telemetry = msg['telemetry'];
		var json = JSON.parse(telemetry);
		json.forEach(function (item, i, json) {
			j = json[i];
			lat = j.lat;
			lon = j.lon;
			var position = {lat: parseFloat(lat), lng: parseFloat(lon)};
			addMarker(position,map,lat,lon,markers_telemetry,'telemetry');
		})*/

})
socket.emit('my_event',{data: 0});
k=0;
i =0;
socket.on('gprs', function (msg) {
	if (i==0){

		GPRS(msg,markers_gprs);
		i=1;
		 }
	else	{
			setTimeout(function(){
	  		GPRS(msg,markers_gprs);
			}, 5000);
		}

});
n=0
socket.emit('my_event2',{data: 0});
console.log('1')
socket.on('aprs', function (msg) {
    console.log('3')
	if (n==0){
		APRS(msg,markers_aprs);
		n=1;
	}	
	else	{
			setTimeout(function(){
	  		APRS(msg,markers_aprs);
			}, 300000);
		}
});


console.log(document.getElementById('telemetry'));
$("#telemetry").change(function(){
	if($("#telemetry").prop("checked")){changeMarkers(map,markers_telemetry)}
	else {changeMarkers(null,markers_telemetry)} });
$("#gprs").change(function(){
	if($("#gprs").prop("checked")){changeMarkers(map,markers_gprs)}
	else  {changeMarkers(null,markers_gprs)}});
$("#aprs").change(function(){
	if($("#aprs").prop("checked")) {changeMarkers(map,markers_aprs)}
	else {changeMarkers(null,markers_aprs)} });


function APRS(msg,markers_aprs){
    console.log(msg['json_data'])
	if (msg['json_data'] != 0){
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
				    $('#pressure1').html(j.pressure);

				    var mas = ['lat','lon','alt','temp1','pressure1','modul'];
					    for(var i = 0; i < mas.length; i++) {
					        console.log(mas[i])
						change_color(mas[i], j.status[mas[i]])
					    }
				    var position = {lat: parseFloat(lat), lng: parseFloat(lon)};
				    addMarker(position,map,lat,lon,markers_aprs,'aprs');
				    console.log("Данные aпрс есть, омномном");
                    change_data(msg['type'],k);

			})
	}    
	console.log("Данных апрс нема, хозяина");
	socket.emit('my_event2',{data: j.id});
}
function GPRS(msg,markers_gprs){
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
									    var mas = ['datetime','lat','lon','alt','temp1','temp2','pressure1','pressure2',
									    'bat_volt','bat_temp','vect_axel1x','vect_axel1y','vect_axel1z','vect_axel2x','vect_axel2y','vect_axel2z',
									    'ultraviolet1','ultraviolet2','infrared1','infrared2','hdop','vdop','sats','radiation','dust','ozone'];
	
												    for(var i = 0; i < mas.length; i++) {
													change_color(mas[i], j.status[mas[i]])
												    }
									    var position = {lat: parseFloat(lat), lng: parseFloat(lon)};
										
									    addMarker(position,map,lat,lon,markers_gprs,'gprs');
									    console.log("Данные гпрс есть, омномном");

									})
					}    
			console.log("Данных гпрс нема, хозяина");
			socket.emit('my_event',{data: j.id}); 	
	
};
});

function changeMarkers(map,mas) {
        for (var i = 0; i < mas.length; i++) {
          mas[i].setMap(map);
        }
}

function addMarker(location, map,lat,lon,massive,type){

	
	if ($("#follow").prop("checked")){map.setCenter(location)};

	if(type == 'gprs'){
		var marker = new google.maps.Marker({position: location,map: map,icon: "../static/img/icon.ico"});
	}
	if(type == 'aprs'){
		var marker = new google.maps.Marker({position: location,map: map,icon: "../static/img/icon1.png"});
	}
	if(type == 'telemetry'){
		var marker = new google.maps.Marker({position: location,map: map,icon: "../static/img/icon2.png"});
	}
	marker.setMap(map);
	if (!!massive[9]){
		el = massive.shift();
		el.setMap(null)
		massive.push(marker);
		var lastMarker = massive[massive.length - 1];
		lastMarker.setMap(map)

		}
	else{	
		massive.push(marker);
		marker.setMap(map)
		};
	marker.setMap(map);
	

};
