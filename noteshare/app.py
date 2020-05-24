import os
from flask import Flask, flash, request, redirect, url_for, render_template, request, jsonify, send_from_directory, abort
from flask_wtf import FlaskForm
from flask_sqlalchemy import SQLAlchemy
from wtforms import SelectField, StringField, FileField
from flask_uploads import UploadSet, configure_uploads, IMAGES, TEXT, DOCUMENTS, ARCHIVES
from flask_bootstrap import Bootstrap

app = Flask(__name__)
Bootstrap(app)

folders = UploadSet('folders', ('pdf',) + TEXT + IMAGES + ARCHIVES + DOCUMENTS, default_dest=lambda x: 'storage/misc')

app.config['UPLOAD_FOLDER'] =  './'
configure_uploads(app, folders)

app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024 #maximum size of the file
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db/finaldb.sqlite'
app.config['SECRET_KEY'] = 'secret'

db = SQLAlchemy(app)

class Courses(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	sem_name = db.Column(db.String(80)) # Monsoon19
	course_name = db.Column(db.String(80)) #Data Str and Algo

class CourseForm(FlaskForm):
	sem = SelectField('Year', choices=[(sem[0],sem[0]) for sem in sorted(set(Courses.query.with_entities(Courses.sem_name)), reverse=True) ] )
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

#		flash("ERROR")
	
	return render_template('upload.html', form=form)

@app.route('/', methods=['GET', 'POST'])
@app.route('/browse', methods = ['GET', 'POST'])
def browse():
	retdiv = []
		
	file_path = os.getcwd() +'/storage/'

	filedirs = os.listdir(file_path) #access all year dirs

	dirs=[]
	for each_yr in filedirs: #access all course dirs
		courses_in_yr = os.listdir(file_path + '/' +each_yr) 
		for each_course in courses_in_yr:
			dirs.append([each_yr, each_course])
	counter = 1
	for each_dir in dirs:
		all_files = os.listdir(file_path + '/' + each_dir[0] + '/' + each_dir[1]) #list of files in second tier dir
		xxtencion =  each_dir[0] + '/' + each_dir[1]
		for each_file in all_files:
			retdiv.append( ( each_dir[0], each_dir[1] ,str(url_for('browse') + '/' + xxtencion+ '/' +each_file), each_file, counter) )
			counter+=1

	return render_template('browse.html', filelist=retdiv)#, form=form

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
