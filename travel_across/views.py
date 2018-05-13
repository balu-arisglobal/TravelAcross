from flask import send_from_directory, render_template, session, Response
import os
from travel_across import app
from models.travelDetails import TravelDetails


td= TravelDetails()



@app.route('/')
def home():
    return render_template('index.html')
