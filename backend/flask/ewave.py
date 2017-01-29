# -*- coding: utf-8 -*-

import json
import os.path
import random
import re
import time

import math
import QRRead


from flask import Flask, send_from_directory, request, abort, redirect, url_for, flash, Response

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
        str = os.path.join(app.config['UPLOAD_FOLDER'], "filename")
        return 'No file part ' + str
        str = pprint.pformat(request.environ, depth=5)
        print (str)
        return Response(str, mimetype="text/text")
        return 'No file part'
    else:
        file = request.files['file']
        # return json.dumps(file)
        # if user does not select file, browser also
        # submit a empty part without filename
        if file.filename == '':
            flash('No selected file')
            return 'No selected file'
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            str = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            
            file.save(str)
            res,data,pos = QRRead.getQRPosition(str)
            if res==0:
                return 'No QR found'
            
            pos=pos.tolist()
            
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
    x = min(seqImage["image_width"], x)
    y = min(seqImage["image_height"], y)

    x = int (max(0, x))
    y = int (max(0, y))

    l = []
    for i in range(len(seqImage)):
        l.append(seqImage[i][x][y])

    return l


if __name__ == '__main__':
    app.run(debug=True)