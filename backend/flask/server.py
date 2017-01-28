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
    return send_from_directory(os.path.join(root_dir(), '../../frontend/'), "user_index.html")



@app.route('/<path:filename>')
def index(filename):
    if fileChecker.match(filename):
        return send_from_directory(os.path.join(root_dir(), '../../frontend/'), filename)
    abort(403)


@app.route('/send_qr',methods=['POST'])
def send_qr():
    millis = int(round(time.time() * 1000))
    return json.dumps({"time_frames": 1000,"data": ["#FF2B2B","#AFDACA","#EFDECD"], "time": millis})
    

@app.route('/set_scenario',methods=['POST'])
def join_room():
    return json.dumps({"url": "http://lmgtfy.com/?q=Esteve+rules"})


if __name__ == '__main__':
    app.run()