# -*- coding: utf-8 -*-

import json
import os.path
import random
import re

from flask import Flask, send_from_directory
from flask import request, abort




app = Flask(__name__)

# Regular expression to only accept certain files
fileChecker = re.compile(r"(.*\.js|.*\.html|.*\.png|.*\.css|.*\.map)$")
domain = "ewave.com"
random.seed(7)


def root_dir():  # pragma: no cover
    return os.path.abspath(os.path.dirname(__file__))


@app.route('/')
def root():
    return send_from_directory(os.path.join(root_dir(), '../../frontend/user_screen'), "index.html")
    
@app.route('/master')
def master():
    return send_from_directory(os.path.join(root_dir(), '../../frontend/master_screen'), "main.html")


@app.route('/<path:filename>')
def index(filename):
    if fileChecker.match(filename):
        return send_from_directory(os.path.join(root_dir(), 'static'), filename)
    abort(403)


@app.route('/send_qr',methods=['POST'])
def send_qr():
    #inigo finds position
    #esteve calculates the sequence
    return json.dumps({"time_frames": 1000,"data": ["#FF2B2B","#AFDACA","#EFDECD"]})


@app.route('/set_scenario',methods=['POST'])
def join_room():
    return redirect("http://lmgtfy.com/?q=Esteve+rules+avisam", code=302)
    return json.dumps({"url": "http://lmgtfy.com/?q=Esteve+rules"})
    return json.dumps({"url": domain + 234567})


if __name__ == '__main__':
    app.run()