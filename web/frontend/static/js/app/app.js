function genData(count) {

	return data = {
		ts: tipoMap(0.0, 400.0, count),	
		lat: tipoMap(53.22544088, 54.0, count),
		lon: tipoMap(45.00208070, 45.5, count),
		alt: tipoMap(0.0, 30.0, count),
		bat: tipoMap(99.0, 45.0, count)
	};
}

// function tipoMap(start, stop, step) {
// 	var diff = (stop - start)/step;
// 	var finalArr = [];

// 	diffSum = 0;
// 	for(var i = 0; i < step; i++) {
// 		diffSum += diff;
// 		finalArr[i] = (start + diffSum).toFixed(4);
// 	}
// 	console.log("Gen:", finalArr);
// 	return finalArr;
// }


function tipoMap(start, stop, step) {

	finalArr = [];
	for( var i = 0; i < step; i++) {

		finalArr[i] = (start - (start - stop)*i/step).toFixed(3);
	}
	console.log(finalArr)
	return finalArr;
}

function getSomething(data, max_count) {

	$("#ts").html(data["ts"][count]);
	$("#lat").html(data["lat"][count]);
	$("#lon").html(data["lon"][count]);
	$("#alt").html(data["alt"][count]);
	$("#bat").html(data["bat"][count]);
	
	// marker = new google.maps.Marker({
	//     position: new google.maps.LatLng(data["lat"][count], data["lon"][count]),
	//     map: map
	// });
	count++;
	if(count == max_count){
		count = 0;
	}


}

function printData(data, sleep, max_count){
	// console.log(data);

	// for(var i = 0; i < 5; i++){
		console.log(data)
		setInterval(function(){
		    getSomething(data, max_count) 
		}, sleep);
	// }


		}

// Modal window 

$(document).ready(function () {
	$('#myModal').modal('show');
});


// Google Maps API

 var marker, i;

function initMap() {
  var myLatLng = {lat:  53.22544088, lng: 45.00208070};

  var map = new google.maps.Map(document.getElementById('map'), {
    zoom: 15,
    center: myLatLng
  });

  var marker = new google.maps.Marker({
    position: myLatLng,
    map: map,
    title: 'Hello World!'
  });
}




// Gen data

var count = 0;
var MAX_COUNT = 1000;

$(document).ready(function () {
	var arr = genData(MAX_COUNT);
	console.log(arr);
	printData(arr, 500, MAX_COUNT);
	
});

