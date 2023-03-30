from flask import Flask
from flask import request
from flask import render_template
from flask import send_from_directory
from random import randint
from waitress import serve
app = Flask(__name__)

@app.route('/')
def hello_world():
    rand = str(randint(5, 198))
    qrimg = '/config/peer' + rand + '/peer' + rand + '.png'
    config = '/config/peer' + rand + '/peer' + rand + '.conf'
    return render_template("index.html", qr = qrimg, name = "lux-"+rand, conf = config, location = "New York")

@app.route('/config/<path:filename>')
def getimage(filename):
    return send_from_directory('/config/', filename)

if __name__ == "__main__":
    serve(app, host="0.0.0.0", port=5070)
