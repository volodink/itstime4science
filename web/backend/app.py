from flask import Flask, render_template
from flask.ext.mysql import MySQL
import sys
import os
import config
import parsing
import content
from flask_socketio import SocketIO
from flask_socketio import send, emit


app = config.app_config()
socketio=config.my_socket()
mysql = MySQL(app)


is_dev = int(os.getenv("DEV", "0"))
sys.path.append(str(os.path.abspath(sys.argv[0])))



data = content.getContent()

@app.route("/")
def main():
    return render_template('index.html', is_dev=is_dev, data = data["main"], main = True)

@app.route("/copter")
def copter():
    return render_template('index.html', is_dev=is_dev, data = data["copter"])

@app.route("/satellite")
def satellite():
    return render_template('index.html', is_dev=is_dev, data = data["satellite"])

@app.route("/mcc")
def mcc():
    return render_template('mcc.html', is_dev=is_dev)

@socketio.on('connected',namespace='/mcc')
def connected():
    json_data = parsing.getData()
    socketio.emit('json_data', {'json_data': json_data}, namespace='/mcc')



if __name__ == "__main__":
    mysql.init_app(app)
    if is_dev == 1:
        socketio.run(app, host='0.0.0.0', debug=True)
    else:
        socketio.run(app, host='0.0.0.0',)
