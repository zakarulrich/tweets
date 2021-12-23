# pylint: disable=missing-docstring

from os import abort
from app.models import Tweet
from flask_restx import Namespace, Resource, fields
from app.db import tweet_repository

api = Namespace('tweets')

tweet = api.model('Tweet', {
    'id': fields.Integer,
    'text': fields.String,
    'created_at': fields.DateTime
})


@api.route('/<int:id>')
@api.response(404, 'Tweet not found')
class TweetResource(Resource):
    @api.marshal_with(tweet)
    def get(self, id):
        tweet = tweet_repository.get(id)
        if tweet is None:
            api.abort(404)
        else:
            return tweet

    @api.marshal_with(tweet)
    def patch(self, id):
        tweet = tweet_repository.get(int(id))
        if(tweet is None):
            abort(404)

        tweet.text = api.payload['text']
        return None, 204

    @api.marshal_with(tweet)
    def delete(self, id):
        tweet = tweet_repository.remove(int(id))
        if(tweet is None):
            abort(404)

        return None, 204
