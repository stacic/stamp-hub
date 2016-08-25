from app import app
from flask import render_template


@app.route('/')
@app.route('/index')
def index():
	stamps = [
		{
			'id': 1,
			'plate_number': 'bm-412',
			'image': '/static/stamp-images/bm-412-0.jpg',
			'tags': ['baseball', 'sports']
		},
		{
			'id': 2,
			'plate_number': 'bm-412',
			'image': '/static/stamp-images/bm-412-1.jpg',
			'tags': ['buildings', 'skyline']
		},
		{
			'id': 3,
			'plate_number': 'bm-412',
			'image': '/static/stamp-images/bm-412-2.jpg',
			'tags': ['seahorse']
		}

	]

	return render_template('index.html', 
							stamps=stamps)