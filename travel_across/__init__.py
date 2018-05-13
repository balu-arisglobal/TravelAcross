from flask import Flask

app = Flask("travelAcross", static_folder='./travel_across/static',  static_url_path='', template_folder='./travel_across/templates')


from travel_across import views, api