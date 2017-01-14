from flask import Flask, render_template

app = Flask(__name__)
app.template_folder = '../frontend'


@app.route("/")
def hello():
    return render_template('index.html')

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)
