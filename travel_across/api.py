from flask import request, redirect, Response, render_template, session, url_for
import os
from bson.objectid import ObjectId
from travel_across import app
from travel_across import ALLOWED_EXTENSIONS
import json
from travel_across.models.travelDetails import  TravelDetails
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


@app.route('/travelDetails/save_tdetails', methods=['POST'])
def save_travel_details():
    if request.method == 'POST':
        place = request.form.get('place',None)
        catchy_title = request.form.get('catchy_title', None)
        sub_title = request.form.get('sub_title',None)
        start_date = request.form.get('start_date', None)
        end_date = request.form.get('end_date', None)
        file = request.files['file']
        print(file)

        if place and catchy_title and sub_title and start_date and end_date and file:
            if file.filename == '':
                return 'No selected file'
            if file and allowed_file(file.filename):
                filename = secure_filename(file.filename)
                file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
                print(url_for('uploaded_file', filename=filename))
                return redirect(url_for('uploaded_file', filename=filename))
            t_details_object = {'place':place,'catchy_title':catchy_title,'sub_title':sub_title,'start_date':start_date,'end_date':end_date,'file':file}
            #td.saveTravelInfo(t_details_object)
            render_template('travel_details.html')