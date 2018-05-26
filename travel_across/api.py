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
        if 'image1' not in request.files:
            return 'No file part'
        file = request.files['image1']
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
            blog_details = td.getAllTravelDetails()
            team_user_details = get_team_user_info()
            return render_template('index.html', results=blog_details, team_info=team_user_details )





@app.route('/saveTeamInfo', methods=['POST'])
def save_team_info():
    if request.method == 'POST':

        team_user_picture = request.form.get('profilePicUrl', None)
        team_user_name = request.form.get('name',None)
        team_user_designation = request.form.get('designation', None)
        team_user_about = request.form.get('about',None)
        team_user_fb = request.form.get('fblink', None)
        team_user_gplus = request.form.get('glink', None)
        team_user_linkedin = request.form.get('linkedinlink', None)
        team_user_instagram = request.form.get('instaLink', None)
        if team_user_name is None or team_user_designation is None or team_user_about is None or team_user_picture is None:
            return Response('One of the below field is empty (Name / desgination/ about / Profile Pic URL) ', mimetype='application/json')
        else:
            team_user_info = {'team_user_name': team_user_name,
                              'team_user_picture': team_user_picture,
                              'team_user_designation': team_user_designation,
                              'team_user_about': team_user_about,
                              'team_user_fb': team_user_fb,
                              'team_user_gplus':team_user_gplus,
                              'team_user_linkedin':team_user_linkedin,
                              'team_user_instagram':team_user_instagram
                              }
            td.saveTeamInfo(team_user_info)
            return Response('Saved.........', mimetype='application/json')




@app.route('/travelDetails/getTeamUserInf0', methods=['POST'])
def get_team_user_info():
     return td.getTeamUsersInfo()



@app.route('/travelDetails/save-user', methods=['POST'])
def save_user():
    if request.method == 'POST':
        pass



