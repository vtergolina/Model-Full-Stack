import json
from flask import request, jsonify, Blueprint
import sys
from flask_cors import CORS
import flask
import os
import service

sys.path.append(os.getcwd())

# Create Blueprint
MODEL_APP = Blueprint('MODEL_APP', __name__)

# Get all data from database
@MODEL_APP.route("/MODEL_APP/get_all", methods=["GET", "POST"])
def get_all():
	if request.method == 'POST':
		args = request.get_json()
		return jsonify(service.get_all(args))

# ------------------------------------------------------------- #
# Create App
# ------------------------------------------------------------- #

def prepare_server():
    if sys.platform in ["win32", "darwin"]:
        server = r"http://127.0.0.1:4200"
    else:
        server = os.environ['BACKEND_URI']
        redirect_uri = os.environ['BACKEND_REDIRECT_URI']
        front_end_url = os.environ['FRONTEND_REDIRECT_URI']

    app = flask.Flask(__name__)
    app.config["DEBUG"] = True
    CORS(app)

    app.register_blueprint(MODEL_APP)

app = prepare_server()

# Function that intercepts endpoints
if __name__ == "__main__":
    if sys.platform in ["win32", "darwin"]:
        app.run(host='0.0.0.0', port=4200, threaded=True)
    else:
        app.run(host='0.0.0.0', port=8080, threaded=True)
           


