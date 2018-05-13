from flask import Flask

app = Flask("travelAcross", static_folder='./travel_across/static',  static_url_path='', template_folder='./travel_across/templates')

UPLOAD_FOLDER = '/travel_across/images/uploadedImages'
ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg', 'gif'])

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER


from travel_across import views, api