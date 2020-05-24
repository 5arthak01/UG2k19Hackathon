import os
from flask import Flask, flash, request, redirect, url_for, render_template, request, jsonify, send_from_directory, abort
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
	sem_id = db.Column(db.String(20), nullable=False) # M19 redundant
	sem_name = db.Column(db.String(80)) # Monsoon19
	course_id = db.Column(db.String(20)) #DSA redundant
	course_name = db.Column(db.String(80)) #Data Str and Algo

class CourseForm(FlaskForm):
	sem = SelectField('Year', choices=[(sem[0],sem[0]) for sem in sorted(set(Courses.query.with_entities(Courses.sem_name))) ] )
	course = SelectField('Course', choices=[])
	info = SelectField('Info', choices=[('Notes','Notes'), ('End-sem', 'End-sem'), ('Mid-sem', 'Mid-sem'), ('Quiz', 'Quiz'), ('Miscellaneous', 'Miscellaneous')])
	upload_file = FileField()

@app.route('/', methods=['GET', 'POST'])
def home():
	redirect(url_for('browse'))

@app.route('/upload', methods = ['GET', 'POST'])
def upload():
	form = CourseForm()
	form.course.choices = [ (course.course_name, course.course_name) for course in Courses.query.filter_by(sem_name='Monsoon19').all() ]

	if form.validate_on_submit():

		# customise file path in local directory according to the data entered
		file_path = '../'+ str(form.sem.data) + '/' + str(form.course.data)

		#store the file
		file_name = folders.save(form.upload_file.data, folder=file_path)

		flash("Saved!")

#		flash("ERROR")
	
	return render_template('upload.html', form=form)

@app.route('/browse', methods = ['GET', 'POST'])
def browse():
	form = CourseForm()
	form.course.choices = [ (course.course_name, course.course_name) for course in Courses.query.filter_by(sem_name='Monsoon19').all() ]

	retdiv = []

	if form.validate_on_submit():

		# customise file path in local directory according to the data entered
		xxtencion =  str(form.sem.data) + '/' + str(form.course.data)
		file_path = os.getcwd() +'/storage/' + xxtencion

		files = os.listdir(file_path)

		for each_file in files:
			
			retdiv.append( ( str(url_for('browse') + '/' + xxtencion+ '/' +each_file), each_file) )

	# form.course.choices = [ () for course in Courses.query.filter_by(sem=form.sem).all() ]
	# for dynamic forms

	print(retdiv)

	return render_template('browse.html', form=form, filelist=retdiv)

@app.route('/browse/<sem>/<course>/<filename>', methods = ['GET', 'POST'])
def filedisp(sem, course, filename):
	try:
		xxtencion = '/storage/' + sem + '/' + course
		file_path = os.getcwd() + xxtencion
		return send_from_directory(file_path, filename)
	except FileNotFoundError:
		abort(404)

@app.route('/course/<sem>')
def course(sem):
	courses = Courses.query.filter_by(sem_name=sem).all()

	courseArray = []

	for course in courses:
		courseObj = {}
		courseObj['name'] = course.course_name
		courseArray.append(courseObj)
	
	return jsonify({'courses' : courseArray})

if __name__ == "__main__":
	app.run(debug=True)
