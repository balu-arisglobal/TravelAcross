from flask import send_from_directory, render_template, session, Response
import os
from travel_across import app
from models.travelDetails import TravelDetails


td= TravelDetails()


@app.route('/')
def home():
   blog_details = td.getAllTravelDetails()
   team_user_details = td.getTeamUsersInfo()
   return render_template('index.html', results=blog_details, team_info=team_user_details)
   #return render_template('travel_details.html')
