import os
from flask import Flask, flash, request, redirect, url_for, render_template, request, jsonify
from flask_wtf import FlaskForm
from wtforms import SelectField, StringField, FileField
from flask_uploads import UploadSet, configure_uploads, IMAGES, TEXT, DOCUMENTS, ARCHIVES

app = Flask(__name__)

folders = UploadSet('folders', ('pdf',) + TEXT + IMAGES + ARCHIVES + DOCUMENTS, default_dest=lambda x: 'storage/misc')

app.config['UPLOAD_FOLDER'] =  './'
configure_uploads(app, folders)

app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024 #maximum size of the file
app.config['SECRET_KEY'] = 'secret'

class CourseForm(FlaskForm):
	#create a db to handle the courses, years and semesters
	sem = SelectField('Year', choices=[('M19', 'Monsoon19'), ('S19', 'Spring19')])
	course = SelectField('Course', choices=[('A', 'Course A'), ('B', 'Course B')])
	upload_file = FileField()

@app.route('/upload', methods = ['GET', 'POST'])
def formdisp():
	form = CourseForm()

	if form.validate_on_submit():

		# customise file path in local directory according to the 
		# data entered
		file_path = '../'+ str(form.sem.data) + '/' + str(form.course.data)

		#store the file
		file_name = folders.save(form.upload_file.data, folder=file_path)

		flash("Saved!")

	else:
		flash("ERROR")

	# form.city.choices = [(city.id, city.name) for city in City.query.filter_by(state='CA').all()] 
	#this is for when we have implemented db

	return render_template('upload.html', form=form)


if __name__ == "__main__":
	app.run(debug=True)
