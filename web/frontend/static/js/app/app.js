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

// function sizeSlider() {
// 	size = document.getElementById("size").value;
// 	$("#slider").html(size);
// }

// while(true)
// 	sizeSlider();
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
	// sizeSlider();
	var position = {lat: Number(data["lat"][count]), lng: Number(data["lon"][count])}
	addMarker(position, map);
	// console.log(size);
	count++;
	if(count == max_count){
		count = 0;
	}
}

function addMarker(location, map) {
  // Add the marker at the clicked location, and add the next-available label
  // from the array of alphabetical characters.
	if($("#follow").prop('checked'))
 		 map.setCenter(location);
  var marker = new google.maps.Marker({
    position: location,
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
		    // console.log(size);
		}, sleep);
	// }


		}


function initMap() {
  var myLatLng = {lat:  53.22544088, lng: 45.00208070};

  	map = new google.maps.Map(document.getElementById('map'), {
    zoom: 11,
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




