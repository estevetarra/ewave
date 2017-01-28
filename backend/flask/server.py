# -*- coding: utf-8 -*-

import json
import os.path
import random
import re
import time

from flask import Flask, send_from_directory
from flask import request, abort
from flask import Flask, request, redirect, url_for, flash
from werkzeug.utils import secure_filename

UPLOAD_FOLDER = "./"
ALLOWED_EXTENSIONS = set(['txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'])


app = Flask(__name__)

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.secret_key = 'admin'


# Regular expression to only accept certain files
fileChecker = re.compile(r"(.*\.js|.*\.html|.*\.png|.*\.css|.*\.map)$")
domain = "ewave.com"
random.seed(7)

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


def root_dir():  # pragma: no cover
    return os.path.abspath(os.path.dirname(__file__))


@app.route('/')
def root():
    return send_from_directory(os.path.join(root_dir(), '../../frontend/'), "index.html")



@app.route('/<path:filename>')
def index(filename):
    if fileChecker.match(filename):
        return send_from_directory(os.path.join(root_dir(), '../../frontend/'), filename)
    abort(403)


@app.route('/send_qr',methods=['POST'])
def send_qr():
    app.config['UPLOAD_FOLDER'] = root_dir()
    if request.method == 'POST':
        # check if the post request has the file part
        if 'QRimage' not in request.files:
            flash('No file part')
            return redirect(request.url)
        file = request.files['QRimage']
        # if user does not select file, browser also
        # submit a empty part without filename
        if file.filename == '':
            flash('No selected file')
            return redirect(request.url)
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))

            millis = int(round(time.time() * 1000))
            return json.dumps({"time_frames": 1000,"data": ["#FF2B2B","#AFDACA","#EFDECD"], "time": millis})
            return redirect(url_for('uploaded_file',
                                    filename=filename))
    #inigo finds position
    #esteve calculates the sequence
    return json.dumps({"error": "something when wrong"})


@app.route('/set_scenario',methods=['POST'])
def join_room():
    return redirect("http://lmgtfy.com/?q=Esteve+rules+avisam", code=302)
    return json.dumps({"url": "http://lmgtfy.com/?q=Esteve+rules"})
    return json.dumps({"url": domain + 234567})


if __name__ == '__main__':
    app.run()