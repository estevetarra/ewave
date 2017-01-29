# -*- coding: utf-8 -*-

import json
import os.path
import random
import re
import time

import math
import QRRead


from flask import Flask, send_from_directory, request, abort, redirect, url_for, flash, Response

from flask import jsonify

class InvalidUsage(Exception):
    status_code = 400

    def __init__(self, message, status_code=None, payload=None):
        Exception.__init__(self)
        self.message = message
        if status_code is not None:
            self.status_code = status_code
        self.payload = payload

    def to_dict(self):
        rv = dict(self.payload or ())
        rv['message'] = self.message
        return rv
        
        
def handle_invalid_usage(error):
    response = jsonify(error.to_dict())
    response.status_code = error.status_code
    return response

import pprint

from werkzeug.utils import secure_filename

UPLOAD_FOLDER = "/var/www/ewave/backend/tmp_img"
ALLOWED_EXTENSIONS = set(['txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'])



app = Flask(__name__)

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.secret_key = 'admin'


# Regular expression to only accept certain files
fileChecker = re.compile(r"(.*\.js|.*\.html|.*\.png|.*\.css|.*\.map|.*\.jpg|.*\.jpeg)$")
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
        raise InvalidUsage('There is no file', status_code=410)
    else:
        file = request.files['file']
        # return json.dumps(file)
        # if user does not select file, browser also
        # submit a empty part without filename
        if file.filename == '':
            flash('No selected file')
            raise InvalidUsage('No selected files', status_code=410)
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            str = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            
            file.save(str)
            res,data,pos = QRRead.getQRPosition(str)
            if res==0:
                raise InvalidUsage('No QR found', status_code=410)
            
            pos=pos.tolist()
            
            text_file = open("/var/www/ewave/backend/tmp_img/debug_pos.txt", "w")
            text_file.write(json.dumps(pos))
            text_file.close()
            
            
            text_file = open("/var/www/ewave/backend/tmp_img/output.txt", "r")
            scenario = json.load(text_file)

            scenario['time_frames'] = int(scenario['time_frames'])
            scenario["qr_size"] = float(scenario["qr_size"])
            scenario["room_x"] = float(scenario["room_x"])
            scenario["room_y"] = float(scenario["room_y"])
            scenario["qr_distance"] = float(scenario["qr_distance"])
            scenario["image_width"] = int(scenario["image_width"])
            scenario["image_height"] = int(scenario["image_height"])
            
            text_file.close()
            par = {}
            par['x'] = pos[0]
            par['y'] = pos[2]
            marcret = getColorSequence(scenario,par)
            
            millis = int(round(time.time() * 1000))
            return json.dumps({"time_frames": scenario['time_frames'],"data": marcret, "time": millis})
    return 'something went wrong'
    

@app.route('/set_scenario',methods=['POST'])
def set_scenario():
    text_file = open("/var/www/ewave/backend/tmp_img/output.txt", "w")
    text_file.write(json.dumps(request.get_json()))
    text_file.close()
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

def getColorSequence(seqImage, posFromQr):
    #Get position from bottom right corner of the room
    x = posFromQr["x"] * seqImage["qr_size"] + (seqImage["room_x"] - seqImage["qr_size"])/2
    y = posFromQr["y"] * seqImage["qr_size"] - seqImage["qr_distance"]
    
    #Scale the results to the image boundaries
    x = x / seqImage["room_x"] * seqImage["image_width"]
    y = y / seqImage["room_y"] * seqImage["image_height"]
    
    #Adjust the position of the (0,0) (upper left) and round the results
    x = seqImage["image_width"] - math.ceil(x)
    y = seqImage["image_height"] - math.ceil(y)

    #Fit the results inside the area
    x = min(seqImage["image_width"]-1, x)
    y = min(seqImage["image_height"]-1, y)

    x = int (max(0, x))
    y = int (max(0, y))

    l = []
    for i in range(len(seqImage["data"])):
        l.append(seqImage["data"][i][y][x])

    return l


if __name__ == '__main__':
    app.run(processes=3)