from flask import render_template

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
    return render_template('mcc.html', is_dev=is_dev, panel_tags=content.panel_tags, communication_channel_panel=content.communication_channel_panel)