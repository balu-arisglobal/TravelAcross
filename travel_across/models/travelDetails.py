from pymongo import MongoClient
from flask import session
import re
from bson.objectid import ObjectId
import json



class TravelDetails:

        def __init__(self):
            config = json.load(open("./config.json", "r"))
            client = MongoClient(config["mongod_host"], config["mongod_port"])
            self.db = client[config["mongod_dbName"]]

        def saveTravelInfo(self, travelDetails):
            self.db.travelDetails.insert(travelDetails)

        def getAllTravelDetails(self):
            allItems = self.db.travelDetails.find()
            if allItems.count() > 0:
                matches = []
                for item in allItems:
                    matches.append(item)
                return matches
            else:
                return ""
