from app import app
from flask import render_template, jsonify
from .models import Stamp


@app.route('/')
@app.route('/index')
def index():
	stamps = Stamp.query.all()

	return render_template('index.html', 
							stamps=stamps)

@app.route('/stamp/api/v1.0/stamps', methods=['GET'])
def get_stamps():
	stamps = Stamp.query.all()
	json_list=[stamp.serialize for stamp in stamps]

	return jsonify(json_list)