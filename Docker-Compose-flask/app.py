from flask import Flask
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)

class Programming(Resource):
  	def get_languages(self):
	    return{ 'languages': ['C', 'C++', 'Java','Go','Nodejs'] }

api.add_resource(Programming, '/')

if __name__ == '__main__':
 	app.run(host='0.0.0.0', port=80, debug=True)
