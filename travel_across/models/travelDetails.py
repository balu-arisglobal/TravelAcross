from pymongo import MongoClient
from flask import session
import re
import jwt
from bson.objectid import ObjectId
import json



class TravelDetails:

        def __init__(self):
            config = json.load(open("./config.json", "r"))
            client = MongoClient(config["mongod_host"], config["mongod_port"])
            self.db = client[config["mongod_dbName"]]

