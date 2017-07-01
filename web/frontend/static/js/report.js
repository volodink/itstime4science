$(document).ready(function () {
    var url = 'http://' + document.domain + ':' + location.port;
    var socket = io.connect(url + "/report");

    socket.emit('event_report');
	socket.on('json_report', function (msg) {
		//console.log(msg['json_gprs']);
		var json_gprs = msg['json_gprs'];
		var json_aprs = msg['json_aprs'];
		var json_telemetry = msg['json_telemetry'];

		var datetime =[];
		var buf = [];
		var gprs_datetime = [];var gprs_temp1 = [];var gprs_temp2 = [];var gprs_pressure1 = [];var gprs_pressure2 = [];var gprs_bat_volt = [];var gprs_vect_axel1x = [];var gprs_vect_axel1y = [];var gprs_vect_axel1z = [];var gprs_hdop = [];var gprs_vdop = [];var gprs_sats = [];var gprs_radiation = [];
		var aprs_datetime = [];var aprs_temp1 = [];var aprs_pressure1 = [];
		var telemetry_datetime = [];var telemetry_temp1 = [];var telemetry_temp2 = [];var telemetry_pressure1 = [];var telemetry_pressure2 = [];var telemetry_bat_volt = [];var telemetry_vect_axel1x = [];var telemetry_vect_axel1y = [];var telemetry_vect_axel1z = [];var telemetry_hdop = [];var telemetry_vdop = [];var telemetry_sats = [];var telemetry_radiation = [];

		json = parsing_json(json_gprs)
		json.forEach(function (item, i, json) {
			j = json[i];
			gprs_temp1[i] = j.temp1;
            gprs_temp2[i] = j.temp2;
			gprs_pressure1[i] = j.pressure1;
			gprs_datetime[i]= j.datetime;
            gprs_pressure2[i]=j.pressure2;
            gprs_bat_volt[i]=j.bat_volt;
            gprs_vect_axel1x[i]=j.vect_axel1x;
            gprs_vect_axel1y [i]=j.vect_axel1y;
            gprs_vect_axel1z [i]=j.vect_axel1z;           
            gprs_hdop [i]=j.hdop;
            gprs_vdop [i]=j.vdop;
            gprs_sats [i]=j.sats;
            gprs_radiation [i]=j.radiation;
            
		})
        

		json = parsing_json(json_aprs)
		json.forEach(function (item, i, json) {
			j = json[i];
			aprs_temp1[i] = j.temp1;
			aprs_pressure1[i] = j.pressure1;
			aprs_datetime[i]= j.datetime;
		})

		json = parsing_json(json_telemetry)
		json.forEach(function (item, i, json) {
			j = json[i];
			telemetry_temp1[i] = j.temp1;
            telemetry_temp2[i] = j.temp2;
			telemetry_pressure1[i] = j.pressure1;
			telemetry_datetime[i]= j.datetime;
            telemetry_pressure2[i]=j.pressure2;
            telemetry_bat_volt[i]=j.bat_volt;
            telemetry_vect_axel1x[i]=j.vect_axel1x;
            telemetry_vect_axel1y [i]=j.vect_axel1y;
            telemetry_vect_axel1z [i]=j.vect_axel1z;
            telemetry_hdop [i]=j.hdop;
            telemetry_vdop [i]=j.vdop;
            telemetry_sats [i]=j.sats;
            telemetry_radiation [i]=j.radiation;


		})

		var gprs_list = [ gprs_datetime , gprs_temp1 , gprs_temp2 , gprs_pressure1 , gprs_pressure2 , gprs_bat_volt ,  gprs_vect_axel1x , gprs_vect_axel1y , gprs_vect_axel1z ,   gprs_hdop , gprs_vdop , gprs_sats , gprs_radiation ]
		var telemetry_list = [ telemetry_datetime , telemetry_temp1 , telemetry_temp2 , telemetry_pressure1 , telemetry_pressure2 , telemetry_bat_volt ,  telemetry_vect_axel1x , telemetry_vect_axel1y , telemetry_vect_axel1z ,   telemetry_hdop , telemetry_vdop , telemetry_sats , telemetry_radiation]
		var aprs_list = [ aprs_datetime , aprs_temp1 , aprs_pressure1]
        gprs_datetime = gprs_list[0], gprs_temp1 = gprs_list[1], gprs_temp2 = gprs_list[2], gprs_pressure1 = gprs_list[3], gprs_pressure2 = gprs_list[4], gprs_bat_volt = gprs_list[5],  gprs_vect_axel1x = gprs_list[6], gprs_vect_axel1y = gprs_list[7], gprs_vect_axel1z = gprs_list[8], gprs_hdop = gprs_list[9], gprs_vdop = gprs_list[10], gprs_sats = gprs_list[11], gprs_radiation = gprs_list[12];
        telemetry_datetime = telemetry_list[0], telemetry_temp1 = telemetry_list[1], telemetry_temp2 = telemetry_list[2], telemetry_pressure1 = telemetry_list[3], telemetry_pressure2 = telemetry_list[4], telemetry_bat_volt = telemetry_list[5], telemetry_vect_axel1x = telemetry_list[6], telemetry_vect_axel1y = telemetry_list[7], telemetry_vect_axel1z = telemetry_list[8], telemetry_hdop = telemetry_list[9], telemetry_vdop = telemetry_list[10], telemetry_sats = telemetry_list[11], telemetry_radiation = telemetry_list[12];
        aprs_datetime = aprs_list[0], aprs_temp1 =aprs_list[1], aprs_pressure1 = aprs_list[2];

		gprs_list.forEach(function (item, i, gprs_list) {
			gprs_list[i]=parsMas(item);
		})
        
        aprs_list.forEach(function (item, i, aprs_list) {
			aprs_list[i]=parsMas(item);
		})
        telemetry_list.forEach(function (item, i, telemetry_list) {
			telemetry_list[i]=parsMas(item);
		})


		var ctx = document.getElementById('chart').getContext('2d');
		var chart = new Chart(ctx, {
		    type: 'line',
		    data:  {labels: gprs_datetime,
			    datasets: [{fill: false,
			    label: "Температура 1 по данным гпрс",
			    backgroundColor: 'rgb(255, 135, 0)',
			    borderColor: 'rgb(255, 0, 0)',
			    data: gprs_temp1}]
		    },

		    options: {}
		});
		var ctx = document.getElementById('chart1').getContext('2d');
		var chart = new Chart(ctx, {
		    type: 'line',
	    	    data:  {labels: telemetry_datetime,
	    		    datasets: [{fill: false,
			    label: "Температура 1 по данным телеметрии",
			    backgroundColor: 'rgb(0, 200, 0)',
			    borderColor: 'rgb(0, 50, 0)',
			    data: telemetry_temp1}]
		    },
		    options: {}
		});
		var ctx = document.getElementById('chart2').getContext('2d');
		var chart = new Chart(ctx, {
		    type: 'line',
	    	    data:  {labels: aprs_datetime,
			    datasets: [{
			    fill: false,
			    label: "Температура 1 по данным апрс",
			    backgroundColor: 'rgb(0, 150, 255)',
			    borderColor: 'rgb(0, 0, 255)',
			    data: aprs_temp1}]
		    },
		    options: {}
		});

		var ctx = document.getElementById('chart3').getContext('2d');
		var chart = new Chart(ctx, {
		    type: 'line',
		    data:  {labels: gprs_datetime,
			    datasets: [{fill: false,
			    label: "Давление 1 по данным гпрс",
			    backgroundColor: 'rgb(255, 135, 0)',
			    borderColor: 'rgb(255, 0, 0)',
			    data: gprs_pressure1}]
		    },

		    options: {}
		});
		var ctx = document.getElementById('chart4').getContext('2d');
		var chart = new Chart(ctx, {
		    type: 'line',
	    	    data:  {labels: telemetry_datetime,
	    		    datasets: [{fill: false,
			    label: "Давление 1 по данным телеметрии",
			    backgroundColor: 'rgb(0, 200, 0)',
			    borderColor: 'rgb(0, 50, 0)',
			    data: telemetry_pressure1}]
		    },
		    options: {}
		});
		var ctx = document.getElementById('chart5').getContext('2d');
		var chart = new Chart(ctx, {
		    type: 'line',
	    	    data:  {labels: aprs_datetime,
			    datasets: [{
			    fill: false,
			    label: "Давление 1 по данным апрс",
			    backgroundColor: 'rgb(0, 150, 255)',
			    borderColor: 'rgb(0, 0, 255)',
			    data: aprs_pressure1}]
		    },
		    options: {}
		});
    var ctx = document.getElementById('chart6').getContext('2d');
		var chart = new Chart(ctx, {
		    type: 'line',
		    data:  {labels: gprs_datetime,
			    datasets: [{fill: false,
			    label: "Температура 2 по данным гпрс",
			    backgroundColor: 'rgb(255, 135, 0)',
			    borderColor: 'rgb(255, 0, 0)',
			    data: gprs_temp2}]
		    },

		    options: {}
		});
		var ctx = document.getElementById('chart7').getContext('2d');
		var chart = new Chart(ctx, {
		    type: 'line',
	    	    data:  {labels: telemetry_datetime,
	    		    datasets: [{fill: false,
			    label: "Температура 2 по данным телеметрии",
			    backgroundColor: 'rgb(0, 200, 0)',
			    borderColor: 'rgb(0, 50, 0)',
			    data: telemetry_temp2}]
		    },
		    options: {}
		});
		    var ctx = document.getElementById('chart8').getContext('2d');
		var chart = new Chart(ctx, {
		    type: 'line',
		    data:  {labels: gprs_datetime,
			    datasets: [{fill: false,
			    label: "Давление 2 по данным гпрс",
			    backgroundColor: 'rgb(255, 135, 0)',
			    borderColor: 'rgb(255, 0, 0)',
			    data: gprs_pressure2}]
		    },

		    options: {}
		});
		var ctx = document.getElementById('chart9').getContext('2d');
		var chart = new Chart(ctx, {
		    type: 'line',
	    	    data:  {labels: telemetry_datetime,
	    		    datasets: [{fill: false,
			    label: "Давление 2 по данным телеметрии",
			    backgroundColor: 'rgb(0, 200, 0)',
			    borderColor: 'rgb(0, 50, 0)',
			    data: telemetry_pressure2}]
		    },
		    options: {}
		});
		    var ctx = document.getElementById('chart10').getContext('2d');
		var chart = new Chart(ctx, {
		    type: 'line',
		    data:  {labels: gprs_datetime,
			    datasets: [{fill: false,
			    label: "Напряжение аккумулятора по данным гпрс",
			    backgroundColor: 'rgb(255, 135, 0)',
			    borderColor: 'rgb(255, 0, 0)',
			    data: gprs_bat_volt}]
		    },

		    options: {}
		});
		var ctx = document.getElementById('chart11').getContext('2d');
		var chart = new Chart(ctx, {
		    type: 'line',
	    	    data:  {labels: telemetry_datetime,
	    		    datasets: [{fill: false,
			    label: "Напряжение аккумулятора по данным телеметрии",
			    backgroundColor: 'rgb(0, 200, 0)',
			    borderColor: 'rgb(0, 50, 0)',
			    data: telemetry_bat_volt}]
		    },
		    options: {}
		});
		    var ctx = document.getElementById('chart12').getContext('2d');
		var chart = new Chart(ctx, {
		    type: 'line',
		    data:  {labels: gprs_datetime,
			    datasets: [{fill: false,
			    label: "Аксель x по данным гпрс",
			    backgroundColor: 'rgb(255, 135, 0)',
			    borderColor: 'rgb(255, 0, 0)',
			    data: gprs_vect_axel1x}]
		    },

		    options: {}
		});
		var ctx = document.getElementById('chart13').getContext('2d');
		var chart = new Chart(ctx, {
		    type: 'line',
	    	    data:  {labels: telemetry_datetime,
	    		    datasets: [{fill: false,
			    label: "Аксель x по данным телеметрии",
			    backgroundColor: 'rgb(0, 200, 0)',
			    borderColor: 'rgb(0, 50, 0)',
			    data: telemetry_vect_axel1x}]
		    },
		    options: {}
		});
		    var ctx = document.getElementById('chart14').getContext('2d');
		var chart = new Chart(ctx, {
		    type: 'line',
		    data:  {labels: gprs_datetime,
			    datasets: [{fill: false,
			    label: "Аксель y по данным гпрс",
			    backgroundColor: 'rgb(255, 135, 0)',
			    borderColor: 'rgb(255, 0, 0)',
			    data: gprs_vect_axel1y}]
		    },

		    options: {}
		});
		var ctx = document.getElementById('chart15').getContext('2d');
		var chart = new Chart(ctx, {
		    type: 'line',
	    	    data:  {labels: telemetry_datetime,
	    		    datasets: [{fill: false,
			    label: "Аксель y по данным телеметрии",
			    backgroundColor: 'rgb(0, 200, 0)',
			    borderColor: 'rgb(0, 50, 0)',
			    data: telemetry_vect_axel1y}]
		    },
		    options: {}
		});
				    var ctx = document.getElementById('chart16').getContext('2d');
		var chart = new Chart(ctx, {
		    type: 'line',
		    data:  {labels: gprs_datetime,
			    datasets: [{fill: false,
			    label: "Аксель z по данным гпрс",
			    backgroundColor: 'rgb(255, 135, 0)',
			    borderColor: 'rgb(255, 0, 0)',
			    data: gprs_vect_axel1z}]
		    },

		    options: {}
		});
		var ctx = document.getElementById('chart17').getContext('2d');
		var chart = new Chart(ctx, {
		    type: 'line',
	    	    data:  {labels: telemetry_datetime,
	    		    datasets: [{fill: false,
			    label: "Аксель z по данным телеметрии",
			    backgroundColor: 'rgb(0, 200, 0)',
			    borderColor: 'rgb(0, 50, 0)',
			    data: telemetry_vect_axel1z}]
		    },
		    options: {}
		});
		
		
		var ctx = document.getElementById('chart30').getContext('2d');
		var chart = new Chart(ctx, {
		    type: 'line',
		    data:  {labels: gprs_datetime,
			    datasets: [{fill: false,
			    label: "Радиация по данным гпрс",
			    backgroundColor: 'rgb(255, 135, 0)',
			    borderColor: 'rgb(255, 0, 0)',
			    data: gprs_radiation}]
		    },

		    options: {}
		});
		var ctx = document.getElementById('chart31').getContext('2d');
		var chart = new Chart(ctx, {
		    type: 'line',
	    	    data:  {labels: telemetry_datetime,
	    		    datasets: [{fill: false,
			    label: "Радиация по данным телеметрии",
			    backgroundColor: 'rgb(0, 200, 0)',
			    borderColor: 'rgb(0, 50, 0)',
			    data: telemetry_radiation}]
		    },
		    options: {}
		});
	});
	function parsMas(mas_input){
		var len = mas_input.length;
		var mas_out = [];
		if (mas_input.length >50){
			    console.log('длина больше 50');
			    var step = parseInt(len / 50);
			    var now = 0;
			    var i = 0;
			    //U can set counts of dots here
			    while (i < 50)
                    {

				        mas_out[i]= mas_input[now]
				        now = now + step;
				        i = i+1;
			        }
		return mas_out;
        }
        else{
		return mas_input;}
	};
	function parsing_json(json_data) {
			var json = JSON.parse(json_data);
			var json = JSON.parse(json);
			return json;
	}
	function replace_datetime(datetime, type_datetime,buf,i) {
		buf[i]= type_datetime[i].replace( /-/g, "" );
		buf[i]= buf[i].replace( / /g, "" );
		buf[i]= buf[i].replace( /:/g, "" );
		return buf;
	}

});
