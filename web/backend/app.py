from flask import Flask, render_template
import sys
import os
import content

sys.path.append(str(os.path.abspath(sys.argv[0])))

from itstime4science.params import Parser


app = Flask(__name__)
app.template_folder = '../frontend/templates/'
app.static_folder = "../frontend/static/"

data = content.getContent() # Новый контент можно добавить в файл
							# /web/backend/content.py

parser = Parser()
argv = parser.createParser()
namespace = argv.parse_args(sys.argv[1:])

@app.route("/")
def main():
    return render_template('index.html', data = data["main"], main = True)

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
    app.run(host='{}'.format(namespace.ip), port=namespace.port, debug=True)
