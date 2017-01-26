var markers = [];
var map;

function genData(count) {

	return data = {
		ts: tipoMap(0, 10000, count),	
		lat: tipoMap(53.22544088, 58.0, count),
		lon: tipoMap(45.00208070, 45.9, count),
		alt: tipoMap(0.0, 30.0, count),
		bat: tipoMap(99.0, 45.0, count)
	};
}

function tipoMap(start, stop, step) {

	finalArr = [];
	for( var i = 0; i < step; i++) {

		finalArr[i] = (start - (start - stop)*i/step).toFixed(3);
	}
	console.log(finalArr)
	return finalArr;
}

function getSomething(data, max_count) {
	// var neighborhoods = [
	// 	{lat: 52.511, lng: 13.447},
	// 	{lat: 52.549, lng: 13.422},
	//   	{lat: 52.497, lng: 13.396},
	//   	{lat: 52.517, lng: 13.394}
	// ];


	$("#ts").html(data["ts"][count]);
	$("#lat").html(data["lat"][count]);
	$("#lon").html(data["lon"][count]);
	$("#alt").html(data["alt"][count]);
	$("#bat").html(data["bat"][count]);

	var position = {lat: Number(data["lat"][count]), lng: Number(data["lon"][count])}
	// console.log(position)
	addMarker(position, map);
	
	// marker = new google.maps.Marker({
	//     position: new google.maps.LatLng(data["lat"][count], data["lon"][count]),
	//     map: map
	// });
	count++;
	if(count == max_count){
		marker.setMap(null);
		count = 0;
	}
}

function addMarker(location, map) {
  // Add the marker at the clicked location, and add the next-available label
  // from the array of alphabetical characters.
  console.log(location);
  var marker = new google.maps.Marker({
    position: location,
    // label: labels[labelIndex++ % labels.length],
    map: map,
    icon: "https://raw.githubusercontent.com/volodink/itstime4science/dev/web/frontend/static/img/title_icon.ico"
  });
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


function initMap() {
  var myLatLng = {lat:  53.22544088, lng: 45.00208070};

  	map = new google.maps.Map(document.getElementById('map'), {
    zoom: 8,
    center: myLatLng
  });

}


$(document).ready(function () {
	$('#myModal').modal('show');
	$('#startDemo').bind('click', startAll);
});

// Gen data

var count = 0;
var MAX_COUNT = 1000;

// $(document).ready(function () {
// 	 $('#startDemo').bind('click', 
//  	var arr = genData(MAX_COUNT);
// 	console.log(arr);
// 	printData(arr, 500, MAX_COUNT);
// );
	
// });

function startAll() {
	var arr = genData(MAX_COUNT);
	console.log(arr);
	printData(arr, 500, MAX_COUNT);
}



// $(document).ready(function () {
// 	var arr = genData(MAX_COUNT);
// 	console.log(arr);
// 	printData(arr, 500, MAX_COUNT);
	
// });




