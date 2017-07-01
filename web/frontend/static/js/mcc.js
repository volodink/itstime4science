$(document).ready(function () {
var markers_gprs = [];
var markers_aprs = [];
var markers_telemetry = [];

var url = 'http://' + document.domain + ':' + location.port;
var socket = io.connect(url + "/mcc");
	socket.on('connect', function() {
		socket.emit('last_dots');
	});

socket.on('lastMarkers', function (msg) {

		var gprs = msg['gprs'];
        if (gprs != 'Nan'){
		    var json = JSON.parse(gprs);
		    json.forEach(function (item, i, json) {
			    j = json[i];
			    lat = j.lat;
			    lon = j.lon;
			    var position = {lat: parseFloat(lat), lng: parseFloat(lon)};
			    addMarker(position,map,lat,lon,markers_gprs,'gprs');
		    })
        }
        
		var aprs = msg['aprs'];
        if (aprs != 'Nan'){		
            var json = JSON.parse(aprs);
		    json.forEach(function (item, i, json) {
			    j = json[i];
			    lat = j.lat;
			    lon = j.lon;
			    var position = {lat: parseFloat(lat), lng: parseFloat(lon)};
			    addMarker(position,map,lat,lon,markers_aprs,'aprs');
		    })
        }
		var telemetry = msg['telemetry'];
        if (telemetry != 'Nan'){
		    var json = JSON.parse(telemetry);

		    json.forEach(function (item, i, json) {
			    j = json[i];
			    lat = j.lat;
			    lon = j.lon;
			    var position = {lat: parseFloat(lat), lng: parseFloat(lon)};
			    addMarker(position,map,lat,lon,markers_telemetry,'telemetry');
		    })
        }
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
socket.on('aprs', function (msg) {
	if (n==0){
		APRS(msg,markers_aprs);
		n=1;
	}	
	else	{
			setTimeout(function(){
	  		APRS(msg,markers_aprs);
			}, 60000);
		}
});

g=0
socket.emit('my_event3',{data: 0});

socket.on('telemetry', function (msg) {
    console.log(msg['json_data'])
	if (g==0){
  		TELEMETRY(msg,markers_telemetry);
		g=1;
	}	
	else	{
			setTimeout(function(){
	  		TELEMETRY(msg,markers_telemetry);
			}, 10000);
		}
});


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

	if (msg['json_data'] != 0){
	    if (msg['json_data'] != 'nothing'){
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
				        $('#pressure1').html(j.pressure);

                        change_data(msg['type'],k);
				        var position = {lat: parseFloat(lat), lng: parseFloat(lon)};
				        addMarker(position,map,lat,lon,markers_aprs,'aprs');
				        console.log("Данные aпрс есть, омномном");
                        socket.emit('my_even2',{data: j.id});

			    })
          }
            else {console.log("Данных апрс в базе данных нет, хозяина");
                                socket.emit('my_event2',{data: 0});}
	}   
    else{
        console.log("Данных апрс нема, хозяина");
        socket.emit('my_event2',{data: j.id});
    } 
	
}
function GPRS(msg,markers_gprs){
					if (msg['json_data'] != 0){
                                    	    if (msg['json_data'] != 'nothing'){
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
									                                            $('#vect_axel1x').html(j.vect_axel1x);
									                                            $('#vect_axel1y').html(j.vect_axel1y);
									                                            $('#vect_axel1z').html(j.vect_axel1z);
									                                            $('#hdop').html(j.hdop);
									                                            $('#vdop').html(j.vdop);
									                                            $('#sats').html(j.sats);
									                                            $('#radiation').html(j.radiation);
                                                                                change_data(msg['type'],k);
									                                            var position = {lat: parseFloat(lat), lng: parseFloat(lon)};
										
									                                            addMarker(position,map,lat,lon,markers_gprs,'gprs');
									                                            console.log("Данные гпрс есть, омномном");
                                                                                socket.emit('my_event',{data: j.id});
									                                        })
                                            }
                                            else {console.log("Данных гпрс в базе данных нет, хозяина");
                                                socket.emit('my_event',{data: 0});}
					}    
			        console.log("Данных гпрс нема, хозяина");
                    socket.emit('my_event',{data: j.id});

	
                            };
function TELEMETRY(msg,markers_telemetry){

					if (msg['json_data'] != 0){     
                	    if (msg['json_data'] != 'nothing'){
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
									        $('#vect_axel1x').html(j.vect_axel1x);
									        $('#vect_axel1y').html(j.vect_axel1y);
									        $('#vect_axel1z').html(j.vect_axel1z);
									        $('#hdop').html(j.hdop);
									        $('#vdop').html(j.vdop);
									        $('#sats').html(j.sats);
									        $('#radiation').html(j.radiation);
									        
                                            change_data(msg['type'],k);
									        var position = {lat: parseFloat(lat), lng: parseFloat(lon)};
										
									        addMarker(position,map,lat,lon,markers_telemetry,'telemetry');
									        console.log("Данные телеметрии есть, омномном");

                                            socket.emit('my_event3',{data: j.id});}
        
									    })
                        }
                        else {console.log("Данных телеметрии в базе данных нет, хозяина");
                                socket.emit('my_event3',{data: 0});}
					}    
			        else {console.log("Данных телеметрии нема, хозяина");
                            socket.emit('my_event3',{data: j.id});}

			 	
	
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
