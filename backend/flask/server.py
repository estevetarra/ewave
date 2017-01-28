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


@app.route('/set_scenario')
def join_room():
    return json.dumps({"url": "google.com"})
    return json.dumps({"url": domain + 234567})


if __name__ == '__main__':
    app.run()