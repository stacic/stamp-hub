from app import app
from flask import render_template
from .models import Stamp


@app.route('/')
@app.route('/index')
def index():
	stamps = Stamp.query.all()

	return render_template('index.html', 
							stamps=stamps)