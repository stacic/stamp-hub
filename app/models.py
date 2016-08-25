from app import db

import os

tags = db.Table('tags',
	db.Column('tag_id', db.Integer, db.ForeignKey('tag.id')),
	db.Column('stamp_id', db.Integer, db.ForeignKey('stamp.id'))
)


IMAGES_PATH = '/static/stamp-images/'

class Stamp(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	plate_number = db.Column(db.String(10), index=True, unique=False)
	image = db.Column(db.String(64), unique=True)
	tags = db.relationship('Tag',
							secondary=tags,
							backref=db.backref('tagged', lazy='dynamic'))

	def __repr__(self):
		return '<Stamp %r>' % (self.plate_number)

	def photo_img(self):
		return os.path.join(IMAGES_PATH, self.image)

	@property
	def serialize(self):
		return {
			'id'			: self.id,
			'plate_number'	: self.plate_number,
			'image'			: self.photo_img(),
			'tags'			: self.serialize_tags
		}

	@property
	def serialize_tags(self):
		return [ tag.serialize for tag in self.tags ]

class Tag(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.String(30))

	def __repr__(self):
		return '<Tag %r>' % (self.name)

	@property
	def serialize(self):
		return {
			'id'	: self.id,
			'name'	: self.name
		}