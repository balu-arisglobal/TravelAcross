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


@app.route('/travelDetails/save', methods=['POST'])
def save_travel_details():
    if request.method == 'POST':
        place = request.form.get('place',None)
        catchy_title = request.form.get('catchy_title', None)
        sub_title = request.form.get('sub_title',None)
        start_date = request.form.get('start_date', None)
        end_date = request.form.get('end_date', None)

        if place and catchy_title and sub_title:
            t_details_object = {'place':place,'catchy_title':catchy_title,'sub_title':sub_title,'start_date':start_date,'end_date':end_date}
            td.saveTravelInfo(t_details_object)
            allDetails = td.getAllTravelDetails()
            return render_template('travel_details.html', results=allDetails)