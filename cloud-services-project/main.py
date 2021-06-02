from re import X
from bson.objectid import ObjectId
from flask import Flask, json, jsonify, request
from flask_restful import Api, Resource, reqparse, abort
from flask_pymongo import pymongo
from werkzeug.wrappers import response
import db_config as database

app=Flask(__name__)
api = Api(app)

class Badge(Resource):

    def get(self,by,data):
        response = self.abort_if_not_exist(by,data)
        response['_id'] = str(response['_id'])
        return jsonify(response)

    def post(self):
        _id = str(database.db.Badges.insert_one({
                'header_img_url': request.json['header_img_url'],
                'profile_picture_url': request.json['profile_picture_url'],
                'name': request.json['name'],
                'age': request.json['age'],
                'city': request.json['city'],
                'followers': request.json['followers'],
                'likes': request.json['likes'],
                'post': request.json['post']
            }).inserted_id)

        return jsonify({"_id":_id})

    def put(self, by, data):
        response = self.abort_if_not_exist(by,data)
    
    def abort_if_not_exist(self,by,data):
        if by == "_id":
            response = database.db.Badges.find_one({"_id":ObjectId(data)})
        else:
            response = database.db.Badges.find_one({f"{by}":data})

        if response:
            return response
        else:
            abort(jsonify({"status":404, f"{by}":f"{data} not found"}))

api.add_resource(Badge,'/new/','/<string:by>:<string:data>/')

if __name__ == '__main__':
    app.run(load_dotenv=True)