from flask import Flask, render_template
import params
import sys

sys.path.append("../../utils/data-emulator")

app = Flask(__name__)

app.template_folder = '../frontend'
app.static_folder = "../frontend/static/"

Parser = params.Parser()
gen = telemetrySenderEmulator.generateData()
argv = Parser.createParser()
host = ip_and_port.ip
port = int(ip_and_port.port)
addr = (host, port)
@app.route("/")
def hello():
    return render_template('index.html')
@app.route("/about.html")
def about():
    return render_template('index.html', name=about)

if __name__ == "__main__":
    app.run(host='{}'.format(host), port=port, debug=True)
