from flask import Flask, render_template
import params
import sys

sys.path.append("../../utils/data-emulator")

import content

app = Flask(__name__)
app.template_folder = '../frontend/templates/'
app.static_folder = "../frontend/static/"

data = content.getContent() # Новый контент можно добавить в файл
							# /web/backend/content.py


Parser = params.Parser()
gen = telemetrySenderEmulator.generateData()
argv = Parser.createParser()
host = ip_and_port.ip
port = int(ip_and_port.port)
addr = (host, port)

@app.route("/")
def main():
    return render_template('index.html', data = data["main"])

@app.route("/copter")
def copter():
    return render_template('index.html', data = data["copter"])

@app.route("/satellite")
def satellite():
    return render_template('index.html', data = data["satellite"])

@app.route("/mcc")
def mcc():
    return render_template('coming_soon.html')


if __name__ == "__main__":
    app.run(host='{}'.format(host), port=port, debug=True)
