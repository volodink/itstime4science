from flask import Flask, render_template
import sys
import os
import content

# get env variable to make dev version of website different
is_dev = os.getenv('DEV', 0)
print('Now in DEV={} mode.'.format(is_dev))

sys.path.append(str(os.path.abspath(sys.argv[0])))

from params import Parser


app = Flask(__name__)
app.template_folder = '../frontend/templates/'
app.static_folder = "../frontend/static/"

data = content.getContent() # Новый контент можно добавить в файл
							# /web/backend/content.py

namespace = Parser().createParser().parse_args(sys.argv[1:])

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


if __name__ == "__main__":
    app.run(host='{}'.format(namespace.ip), port=namespace.port, debug=True)
