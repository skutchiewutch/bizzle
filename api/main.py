from flask import Flask
from flask_restful import Api, Resource
from twitter.twitter import Twitter

app = Flask(__name__)
api = Api(app)

@app.route('/api/test')
def get_test():
    return 'TEST PAGE: API RUNNING'

@app.route('/')
def home():
    return 'Meantweets Flask homepage'


class MeanTweetsApi(Resource):
    def get(self, handle):
        return Twitter(handle).data


api.add_resource(MeanTweetsApi, "/meantweet/<string:handle>")
#format: "/meantweet/<string:handle>/<int:num>/"

if __name__ == "__main__":
    app.run(debug=False, host='0.0.0.0')
