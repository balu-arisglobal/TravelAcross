from flask import Flask

app = Flask("travelAcross", static_folder='./travel_across/static',  static_url_path='', template_folder='./travel_across/templates')

UPLOAD_FOLDER = './travel_across/static/images/uploadedImages'
TEAM_IMAGES_FOLDER = './travel_across/static/images/ourTeam'
ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg', 'gif'])

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['TEAM_IMAGES_FOLDER'] = TEAM_IMAGES_FOLDER



from travel_across import views, api