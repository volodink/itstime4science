ymaps.ready(init);
    var myMap;

    function init(){     
        myMap = new ymaps.Map("map", {
            center: [53.22544088, 45.00208070],
            zoom: 17
        });
        myPlacemark = new ymaps.Placemark([53.22553745, 45.00223627], { 
            hintContent: 'Мы тут!', 
            balloonContentHeader: 'Лаборатория ВВиВС' ,
            balloonContentBody: 'улица Гагарина, 13Б<br>ПензГТУ (Корпус №2)<br>Кабинет: №316',
            balloonContentFooter: 'Здесь творится магия :)'
        });

        myMap.geoObjects.add(myPlacemark);