$(document).ready(function () {
var url = 'http://' + document.domain + ':' + location.port;
var socket = io.connect(url + "/mcc");
	socket.on('connect', function() {
		socket.emit('last_dots');
	});

socket.on('lastMarkers', function (msg) {
		var json_packet = msg['json_data'];
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
i =0 
socket.on('packet', function (msg) {
	if (i==0){
		receive(msg);
		i=1;
		alert(i);
	}
	else{
		setTimeout(function(){
	  		receive(msg);
		}, 5000);
	}
});
function receive(msg){
	if (msg['json_data'] != 0){
		var json_packet = msg['json_data'];
                var json = JSON.parse(json_packet);
                json.forEach(function (item, i, json) {
                    j = json[i];
		    lat = j.lat;
		    lon = j.lon;
                    $('#id').html(j.id);
                    $('#numberOfFlight').html(j.numberOfFlight);
                    $('#datatime').html(j.datatime);
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
};

/*function sleep(ms) {
ms += new Date().getTime();
while (new Date() < ms){}
}*/


    

