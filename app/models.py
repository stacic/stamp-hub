"""This module defines the database models
"""

from app import db
from flask import current_app

import os

tags = db.Table('tags',
	db.Column('tag_id', db.Integer, db.ForeignKey('tag.id')),
	db.Column('stamp_id', db.Integer, db.ForeignKey('stamp.id'))
)

class Stamp(db.Model):
	"""This defines a database model for Stamps.

	A stamp is an image etched onto a metal plate. There may be multiple stamps per plate.

	Attributes:
		id(int): Primary key identifier.
		plate_number(str): Identifies the plate the stamp comes from
		image(str): Path to a picture of the stamp, relative to IMAGES_PATH
		tags(Tag): Many to Many relationship with the Tag model

	"""
	id = db.Column(db.Integer, primary_key=True)
	plate_number = db.Column(db.String(10), index=True, unique=False)
	image = db.Column(db.String(64), unique=True)
	tags = db.relationship('Tag',
							secondary=tags,
							backref=db.backref('tagged', lazy='dynamic'))

	def __repr__(self):
		return '<Stamp %r>' % (self.plate_number)

	def photo_img(self):
		return os.path.join(current_app.config['IMAGES_PATH'], self.image)

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
	"""This defines a database model for Tags.

	A tag is used to categorize Stamp objects.

	Attributes:
		id(int): Primary key identifier.
		name(str): Describes the tag.
	"""
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