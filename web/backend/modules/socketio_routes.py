

@socketio.on('my_event', namespace='/mcc')
def message(message):
        json_data = parsing.getData(mysql)
        mas = json.loads(json_data)
        if message['data'] != mas[0]['id']:
            emit('packet', {'json_data': json_data}, namespace='/mcc')
        else:
            emit('packet', {'json_data': 0}, namespace='/mcc')


@socketio.on('my_event2', namespace='/mcc')
def message():
    response = urllib.request.urlopen('https://api.aprs.fi/api/get?name=UB4FEU-11&what=loc&apikey=API_KEY&format=json')
    emit('aprs', {'response': response.read()}, namespace='/mcc')

@socketio.on('last_dots', namespace='/mcc')
def msg():
    #количество последних маркеров, которые будут показываться при загрузке страницы
    i = 10
    json_data = parsing.last_dots(mysql, i)
    emit('lastMarkers', {'json_data': json_data}, namespace='/mcc')
