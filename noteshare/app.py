import os
from flask import Flask, flash, request, redirect, url_for, render_template, request, jsonify
from flask_wtf import FlaskForm
from flask_sqlalchemy import SQLAlchemy
from wtforms_sqlalchemy.fields import QuerySelectField
from wtforms import SelectField, StringField, FileField
from flask_uploads import UploadSet, configure_uploads, IMAGES, TEXT, DOCUMENTS, ARCHIVES

app = Flask(__name__)

folders = UploadSet('folders', ('pdf',) + TEXT + IMAGES + ARCHIVES + DOCUMENTS, default_dest=lambda x: 'storage/misc')

app.config['UPLOAD_FOLDER'] =  './'
configure_uploads(app, folders)

app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024 #maximum size of the file
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db/courses.sqlite3'
app.config['SECRET_KEY'] = 'secret'

db = SQLAlchemy(app)

class Courses(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	sem_id = db.Column(db.String(20), nullable=False) # M19 Might be redundant
	sem_name = db.Column(db.String(80)) # Monsoon19
	course_id = db.Column(db.String(20)) #DSA Might be redundant
	course_name = db.Column(db.String(80)) #Data Str and Algo

class CourseForm(FlaskForm):
	sem = SelectField('Year', choices=[(sem[0],sem[0]) for sem in set(Courses.query.with_entities(Courses.sem_name))])
	course = SelectField('Course', choices=[(course[0],course[0]) for course in set(Courses.query.with_entities(Courses.course_name))])
	upload_file = FileField()

@app.route('/upload', methods = ['GET', 'POST'])
def upload():
	form = CourseForm()

	if form.validate_on_submit():

		# customise file path in local directory according to the data entered
		file_path = '../'+ str(form.sem.data) + '/' + str(form.course.data)

		#store the file
		file_name = folders.save(form.upload_file.data, folder=file_path)

		flash("Saved!")

	else:
		flash("ERROR")

	# form.course.choices = [ () for course in Courses.query.filter_by(sem=form.sem).all() ]
	# for dynamic forms

	return render_template('upload.html', form=form)

@app.route('/browse', methos = ['GET', 'POST'])
def browse():
	pass

if __name__ == "__main__":
	app.run(debug=True)
