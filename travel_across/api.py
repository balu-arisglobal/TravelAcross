from flask import request, redirect, Response, render_template, session, url_for, send_from_directory
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

@app.route('/travelDetails/save', methods=['POST'])
def save_travel_details():
    if request.method == 'POST':
        place = request.form.get('place',None)
        catchy_title = request.form.get('catchy_title', None)
        sub_title = request.form.get('sub_title',None)
        start_date = request.form.get('start_date', None)
        end_date = request.form.get('end_date', None)
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
            image_url = url_for('uploaded_file',filename=filename)
            t_details_object = {'place': place, 'catchy_title': catchy_title, 'sub_title': sub_title,'start_date': start_date,'end_date': end_date, 'image_url':image_url}
            td.saveTravelInfo(t_details_object)
            allDetails = td.getAllTravelDetails()
            return render_template('travel_details.html', results=allDetails)


@app.route('/uploads/<filename>')
def uploaded_file(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'],filename)


@app.route('/travelDetails/save-user', methods=['POST'])
def save_user():
    if request.method == 'POST':
        pass
