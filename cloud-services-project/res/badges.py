from flask_restful import Resource


from flask import jsonify, request
from flask_restful import Resource, abort
from flask_pymongo import pymongo
from bson.json_util import dumps, ObjectId
from pymongo import results
from werkzeug.wrappers import response
import db_config as database

class AllBadges(Resource):
    def get(self):
        response = list(database.db.Badges.find())
        for doc in response:
            doc['_id'] = str(doc['_id'])

        return jsonify(response)

    def post(self):
        _ids = list(database.db.Badge.insert_many([
            {
                'header_img_url': request.json[0]['header_img_url'],
                'profile_picture_url': request.json[0]['profile_picture_url'],
                'name': request.json[0]['name'],
                'age': request.json[0]['age'],
                'city': request.json[0]['city'],
                'followers': request.json[0]['followers'],
                'likes': request.json[0]['likes'],
                'post': request.json[0]['post'],
                'posts': request.json[0]['posts']
            },
            {
                'header_img_url': request.json[1]['header_img_url'],
                'profile_picture_url': request.json[1]['profile_picture_url'],
                'name': request.json[1]['name'],
                'age': request.json[1]['age'],
                'city': request.json[1]['city'],
                'followers': request.json[1]['followers'],
                'likes': request.json[1]['likes'],
                'post': request.json[1]['post'],
                'posts': request.json[1]['posts']
            },
            {
                'header_img_url': request.json[2]['header_img_url'],
                'profile_picture_url': request.json[2]['profile_picture_url'],
                'name': request.json[2]['name'],
                'age': request.json[2]['age'],
                'city': request.json[2]['city'],
                'followers': request.json[2]['followers'],
                'likes': request.json[2]['likes'],
                'post': request.json[2]['post'],
                'posts': request.json[2]['posts']
            }
        ]).inserted_ids) 

        results = []

        for _id in _ids:
            results.append(str(_id))

        return jsonify({'inserted_ids': results})
    def delete(self):
        return database.db.Badges.delete_many({}).deleted_count