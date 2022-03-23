# from flask import Flask, request, jsonify
# from waitress import serve
# #from PIL import Image 
# #creating flask app
# app = Flask(__name__)

# @app.route('/', methods = ['GET'])
# def testFunction():
# 	#request from the front end
# 	request_data = request.get_json()
# 	print(request_data) 

# 	return jsonify({"Output":"THIS is the 3rd message"})

# if __name__ == '__main__':
# 	#serving the application using waitress
# 	# serve(app, host="127.0.0.1", port="8001", threads = 1)
# 	app.run(host="127.0.0.1", port=8001, debug = True)

from flask import Flask, request, render_template,jsonify
from waitress import serve
import urllib.request, json


app = Flask(__name__)



@app.route('/', methods =["GET", "POST"])
def gfg():
    if request.method == "POST":
        keyword = request.form.get("key")

        url = "https://api.tvmaze.com/search/shows?q="+keyword
        response = urllib.request.urlopen(url)
        data = response.read()
        dictionary1 = json.loads(data)
        dict2 = {}
        count = 0
        for i in dictionary1 :
            dict2[count] = i['show']['name']
            count += 1

        return render_template("my-form.html", output = dict2)

        # return jsonify({"Suggested Movies related to " + keyword + ' are ' : dict2})
    return render_template("my-form.html")

if __name__ == '__main__':
    app.run(host="127.0.0.1", port=8000, debug = True)
	# serve(app, host="127.0.0.1", port="8000", threads = 1)