# -*- coding: utf-8 -*-

import json
import os.path
import random
import re
import time
import pymongo

from pymongo import MongoClient
from flask import Flask, send_from_directory, request, abort, redirect, url_for, flash, Response

import pprint

from werkzeug.utils import secure_filename

UPLOAD_FOLDER = "./../tmp_img/"
ALLOWED_EXTENSIONS = set(['txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'])

client = MongoClient()

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
    if 'file' not in request.files:
        str = pprint.pformat(request.environ, depth=5)
        print (str)
        return Response(str, mimetype="text/text")
        return 'No file part'
    else:
        file = request.files['file']
        # if user does not select file, browser also
        # submit a empty part without filename
        if file.filename == '':
            flash('No selected file')
            return 'No selected file'
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            millis = int(round(time.time() * 1000))
            db = client.database
            cl = db.colection
            scenario = cl.find_one({"name": "prova"})
            
            return json.dumps({"time_frames": 1000,"data": ["#FF2B2B","#AFDACA","#EFDECD"], "time": millis})
    return 'something went wrong'
    

@app.route('/set_scenario',methods=['POST'])
def set_scenario():
    db = client.database
    cl = db.colection
    cl.insert_one(request.get_json())
    return json.dumps(request.get_json())
    """
    qr_size = request.args.get('qr_size')
    qr_center_height = request.args.get('qr_center_height')
    qr_distance = request.args.get('qr_distance')
    image_width = request.args.get('image_width')
    image_height = request.args.get('image_height')
    room_x = request.args.get('room_x')
    room_y = request.args.get('room_y')
    time_frames = request.args.get('time_frames')
    data = request.args.get('data')
    json_store = {            
            "qr_size" : qr_size,
            "qr_center_height" : qr_size,
            "qr_distance" : qr_distance,
            "image_width" : image_width,
            "image_height" : image_height,
            "room_x" : room_x,
            "room_y" : room_y,
            "time_frames" : time_frames,
            "data" : data
    }    
    """
    return json.dumps(json_store)
    return json.dumps({"url": "http://lmgtfy.com/?q=Esteve+rules"})


if __name__ == '__main__':
    app.run(debug=True)