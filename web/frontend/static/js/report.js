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
		var gprs_datetime = [];var gprs_temp1 = [];var gprs_temp2 = [];var gprs_pressure1 = [];var gprs_pressure2 = [];var gprs_bat_volt = [];var gprs_vect_axel1x = [];var gprs_vect_axel1y = [];var gprs_vect_axel1z = [];var gprs_vect_axel2x = [];var gprs_vect_axel2y = [];var gprs_vect_axel2z = [];var gprs_ultraviolet1 = [];var gprs_ultraviolet2 = [];var gprs_infrared1 = [];var gprs_infrared2 = [];var gprs_hdop = [];var gprs_vdop = [];var gprs_sats = [];var gprs_radiation = [];var gprs_dust = [];var gprs_ozone = [];
		var aprs_datetime = [];var aprs_temp1 = [];var aprs_pressure1 = [];
		var telemetry_datetime = [];var telemetry_temp1 = [];var telemetry_temp2 = [];var telemetry_pressure1 = [];var telemetry_pressure2 = [];var telemetry_bat_volt = [];var telemetry_vect_axel1x = [];var telemetry_vect_axel1y = [];var telemetry_vect_axel1z = [];var telemetry_vect_axel2x = [];var telemetry_vect_axel2y = [];var telemetry_vect_axel2z = [];var telemetry_ultraviolet1 = [];var telemetry_ultraviolet2 = [];var telemetry_infrared1 = [];var telemetry_infrared2 = [];var telemetry_hdop = [];var telemetry_vdop = [];var telemetry_sats = [];var telemetry_radiation = [];var telemetry_dust = [];var telemetry_ozone = [];

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
            gprs_ultraviolet1 [i]=j.ultraviolet1;
            gprs_ultraviolet2 [i]=j.ultraviolet2;
            gprs_infrared1 [i]=j.infrared1;
            gprs_infrared2 [i]=j.infrared2;
            gprs_hdop [i]=j.hdop;
            gprs_vdop [i]=j.vdop;
            gprs_sats [i]=j.sats;
            gprs_radiation [i]=j.radiation;
            gprs_dust [i]=j.dust ;
            gprs_ozone [i]=j.ozone;


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
            telemetry_ultraviolet1 [i]=j.ultraviolet1;
            telemetry_ultraviolet2 [i]=j.ultraviolet2;
            telemetry_infrared1 [i]=j.infrared1;
            telemetry_infrared2 [i]=j.infrared2;
            telemetry_hdop [i]=j.hdop;
            telemetry_vdop [i]=j.vdop;
            telemetry_sats [i]=j.sats;
            telemetry_radiation [i]=j.radiation;
            telemetry_dust [i]=j.dust ;
            telemetry_ozone [i]=j.ozone;

		})

		var gprs_list = [ gprs_datetime , gprs_temp1 , gprs_temp2 , gprs_pressure1 , gprs_pressure2 , gprs_bat_volt ,  gprs_vect_axel1x , gprs_vect_axel1y , gprs_vect_axel1z , gprs_ultraviolet1 , gprs_ultraviolet2 , gprs_infrared1 , gprs_infrared2 , gprs_hdop , gprs_vdop , gprs_sats , gprs_radiation , gprs_dust , gprs_ozone]
		var telemetry_list = [ telemetry_datetime , telemetry_temp1 , telemetry_temp2 , telemetry_pressure1 , telemetry_pressure2 , telemetry_bat_volt ,  telemetry_vect_axel1x , telemetry_vect_axel1y , telemetry_vect_axel1z , telemetry_ultraviolet1 , telemetry_ultraviolet2 , telemetry_infrared1 , telemetry_infrared2 , telemetry_hdop , telemetry_vdop , telemetry_sats , telemetry_radiation , telemetry_dust , telemetry_ozone]
		var aprs_list = [ aprs_datetime , aprs_temp1 , aprs_pressure1]
        gprs_datetime = gprs_list[0], gprs_temp1 = gprs_list[1], gprs_temp2 = gprs_list[2], gprs_pressure1 = gprs_list[3], gprs_pressure2 = gprs_list[4], gprs_bat_volt = gprs_list[5],  gprs_vect_axel1x = gprs_list[6], gprs_vect_axel1y = gprs_list[7], gprs_vect_axel1z = gprs_list[8], gprs_ultraviolet1 = gprs_list[9], gprs_ultraviolet2 = gprs_list[10], gprs_infrared1 = gprs_list[11], gprs_infrared2 = gprs_list[12], gprs_hdop = gprs_list[13], gprs_vdop = gprs_list[14], gprs_sats = gprs_list[15], gprs_radiation = gprs_list[16], gprs_dust = gprs_list[17], gprs_ozone = gprs_list[18];
        telemetry_datetime = telemetry_list[0], telemetry_temp1 = telemetry_list[1], telemetry_temp2 = telemetry_list[2], telemetry_pressure1 = telemetry_list[3], telemetry_pressure2 = telemetry_list[4], telemetry_bat_volt = telemetry_list[5], telemetry_vect_axel1x = telemetry_list[6], telemetry_vect_axel1y = telemetry_list[7], telemetry_vect_axel1z = telemetry_list[8], telemetry_ultraviolet1 = telemetry_list[9], telemetry_ultraviolet2 = telemetry_list[10], telemetry_infrared1 = telemetry_list[11], telemetry_infrared2 = telemetry_list[12], telemetry_hdop = telemetry_list[13], telemetry_vdop = telemetry_list[14], telemetry_sats = telemetry_list[15], telemetry_radiation = telemetry_list[16], telemetry_dust = telemetry_list[17], telemetry_ozone = telemetry_list[18];
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
		var ctx = document.getElementById('chart18').getContext('2d');
		var chart = new Chart(ctx, {
		    type: 'line',
		    data:  {labels: gprs_datetime,
			    datasets: [{fill: false,
			    label: "Ультрафиолет 1 по данным гпрс",
			    backgroundColor: 'rgb(255, 135, 0)',
			    borderColor: 'rgb(255, 0, 0)',
			    data: gprs_ultraviolet1}]
		    },

		    options: {}
		});
		var ctx = document.getElementById('chart19').getContext('2d');
		var chart = new Chart(ctx, {
		    type: 'line',
	    	    data:  {labels: telemetry_datetime,
	    		    datasets: [{fill: false,
			    label: "Ультрафиолет 1 по данным телеметрии",
			    backgroundColor: 'rgb(0, 200, 0)',
			    borderColor: 'rgb(0, 50, 0)',
			    data: telemetry_ultraviolet1}]
		    },
		    options: {}
		});
				    var ctx = document.getElementById('chart20').getContext('2d');
		var chart = new Chart(ctx, {
		    type: 'line',
		    data:  {labels: gprs_datetime,
			    datasets: [{fill: false,
			    label: "Ультрафиолет 2 по данным гпрс",
			    backgroundColor: 'rgb(255, 135, 0)',
			    borderColor: 'rgb(255, 0, 0)',
			    data: gprs_ultraviolet2}]
		    },

		    options: {}
		});
		var ctx = document.getElementById('chart21').getContext('2d');
		var chart = new Chart(ctx, {
		    type: 'line',
	    	    data:  {labels: telemetry_datetime,
	    		    datasets: [{fill: false,
			    label: "Ультрафиолет 2 по данным телеметрии",
			    backgroundColor: 'rgb(0, 200, 0)',
			    borderColor: 'rgb(0, 50, 0)',
			    data: telemetry_ultraviolet2}]
		    },
		    options: {}
		});
				    var ctx = document.getElementById('chart22').getContext('2d');
		var chart = new Chart(ctx, {
		    type: 'line',
		    data:  {labels: gprs_datetime,
			    datasets: [{fill: false,
			    label: "Инфракрасное  изл. 1 по данным гпрс",
			    backgroundColor: 'rgb(255, 135, 0)',
			    borderColor: 'rgb(255, 0, 0)',
			    data: gprs_infrared1}]
		    },

		    options: {}
		});
		var ctx = document.getElementById('chart23').getContext('2d');
		var chart = new Chart(ctx, {
		    type: 'line',
	    	    data:  {labels: telemetry_datetime,
	    		    datasets: [{fill: false,
			    label: "Инфракрасное  изл. 1 по данным телеметрии",
			    backgroundColor: 'rgb(0, 200, 0)',
			    borderColor: 'rgb(0, 50, 0)',
			    data: telemetry_infrared1}]
		    },
		    options: {}
		});
						    var ctx = document.getElementById('chart24').getContext('2d');
		var chart = new Chart(ctx, {
		    type: 'line',
		    data:  {labels: gprs_datetime,
			    datasets: [{fill: false,
			    label: "Инфракрасное  изл. 2 по данным гпрс",
			    backgroundColor: 'rgb(255, 135, 0)',
			    borderColor: 'rgb(255, 0, 0)',
			    data: gprs_infrared2}]
		    },

		    options: {}
		});
		var ctx = document.getElementById('chart25').getContext('2d');
		var chart = new Chart(ctx, {
		    type: 'line',
	    	    data:  {labels: telemetry_datetime,
	    		    datasets: [{fill: false,
			    label: "Инфракрасное  изл. 2 по данным телеметрии",
			    backgroundColor: 'rgb(0, 200, 0)',
			    borderColor: 'rgb(0, 50, 0)',
			    data: telemetry_infrared2}]
		    },
		    options: {}
		});
						    var ctx = document.getElementById('chart26').getContext('2d');
		var chart = new Chart(ctx, {
		    type: 'line',
		    data:  {labels: gprs_datetime,
			    datasets: [{fill: false,
			    label: "Количество пыли по данным гпрс",
			    backgroundColor: 'rgb(255, 135, 0)',
			    borderColor: 'rgb(255, 0, 0)',
			    data: gprs_dust}]
		    },

		    options: {}
		});
		var ctx = document.getElementById('chart27').getContext('2d');
		var chart = new Chart(ctx, {
		    type: 'line',
	    	    data:  {labels: telemetry_datetime,
	    		    datasets: [{fill: false,
			    label: "Количество пыли по данным телеметрии",
			    backgroundColor: 'rgb(0, 200, 0)',
			    borderColor: 'rgb(0, 50, 0)',
			    data: telemetry_dust}]
		    },
		    options: {}
		});
        var ctx = document.getElementById('chart28').getContext('2d');
		var chart = new Chart(ctx, {
		    type: 'line',
		    data:  {labels: gprs_datetime,
			    datasets: [{fill: false,
			    label: "Озон по данным гпрс",
			    backgroundColor: 'rgb(255, 135, 0)',
			    borderColor: 'rgb(255, 0, 0)',
			    data: gprs_ozone}]
		    },

		    options: {}
		});
		var ctx = document.getElementById('chart29').getContext('2d');
		var chart = new Chart(ctx, {
		    type: 'line',
	    	    data:  {labels: telemetry_datetime,
	    		    datasets: [{fill: false,
			    label: "Озон по данным телеметрии",
			    backgroundColor: 'rgb(0, 200, 0)',
			    borderColor: 'rgb(0, 50, 0)',
			    data: telemetry_ozone}]
		    },
		    options: {}
		});        var ctx = document.getElementById('chart30').getContext('2d');
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
