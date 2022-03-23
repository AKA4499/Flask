from flask import Flask, request, jsonify
from waitress import serve
#from PIL import Image 
#creating flask app
app = Flask(__name__)

@app.route('/', methods = ['GET'])
def testFunction():
	#request from the front end
	request_data = request.get_json()
	print(request_data) 

	return jsonify({"Output":"THIS is the 3rd message"})

if __name__ == '__main__':
	#serving the application using waitress
	# serve(app, host="127.0.0.1", port="8001", threads = 1)
	app.run(host="127.0.0.1", port=8001, debug = True)