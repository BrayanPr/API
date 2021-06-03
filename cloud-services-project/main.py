from re import X
from bson.objectid import ObjectId
from flask import Flask, json, jsonify, request
from flask_restful import Api, Resource, reqparse, abort
from flask_pymongo import pymongo
from werkzeug.wrappers import response
import db_config as database

from res.badge import Badge
from res.badges import AllBadges


app=Flask(__name__)
api = Api(app)

@app.route('/all/adults/')
def get_adults():
    response = list(database.db.Badges.find({'age': {"$gte":18}}))

    for element in response:
        element["_id"] = str(element['_id'])
    return jsonify(response)

@app.route('/all/kids/')
def get_kids():
    response = list(database.db.Badges.find({'age': {"$lte":18}}))

    for element in response:
        element["_id"] = str(element['_id'])
    return jsonify(response)

@app.route('/all/filter/')
def get_name_and_age():
    response = list(database.db.Badges.find({'age': {"$gte":18}}, {'name':1, 'age':1}))
    
    for element in response:
        element["_id"] = str(element["_id"])
    return jsonify(response)

api.add_resource(Badge,'/new/','/<string:by>:<string:data>/')
api.add_resource(AllBadges,'/all/', '/delete/all/')

if __name__ == '__main__':
    app.run(load_dotenv=True)