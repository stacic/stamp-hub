from app import app
from flask import send_file, jsonify
from .models import Stamp


@app.route('/')
@app.route('/index')
def index():
	"""Renders index"""
	return send_file('index.html')

@app.route('/stamp/api/v1.0/stamps', methods=['GET'])
def get_stamps():
	"""Return complete list of stamps as json"""
	stamps = Stamp.query.all()
	json_list=[stamp.serialize for stamp in stamps]

	return jsonify(json_list)