from flask import request, redirect, Response, render_template, session, url_for
import os
from bson.objectid import ObjectId
from travel_across import app
from travel_across import ALLOWED_EXTENSIONS
import json
from models.travelDetails import  TravelDetails
from werkzeug.utils import secure_filename

td = TravelDetails()

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


@app.route("/travelDetails/<requestType>", methods = ['POST','GET'])
def users(requestType):
    if requestType != None and requestType == "save":
        if 'file' not in request.files:
            return 'No file part'
        file = request.files['file']
        # if user does not select file, browser also
        # submit a empty part without filename
        if file.filename == '':
            return 'No selected file'
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            print(url_for('uploaded_file',filename=filename))
            return redirect(url_for('uploaded_file',filename=filename))
            #td.saveTravelInfo();