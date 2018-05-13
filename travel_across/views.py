from flask import send_from_directory, render_template, session, Response
import os
from travel_across import app
from travel_across.models.travelDetails import TravelDetails


td= TravelDetails()


@app.route('/')
def home():
   return render_template('travel_details.html')
