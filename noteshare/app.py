import os
from flask import Flask, flash, request, redirect, url_for, render_template, request, jsonify
from flask_wtf import FlaskForm
from wtforms import SelectField, StringField, FileField
from werkzeug.utils import secure_filename

UPLOAD_FOLDER = '/path/to/the/uploads'
ALLOWED_EXTENSIONS = {'zip', 'gz', 'pdf', 'png', 'jpg', 'jpeg'}

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024
app.config['SECRET_KEY'] = 'secret'

class CourseForm(FlaskForm):
	#create a db to handle the courses and semesters
	sem = SelectField('Semester', choices=[('M19', 'Monsoon19'), ('S19', 'Spring19')])
	course = SelectField('Course', choices=[('A', 'Course A'), ('B', 'Course B')])

@app.route('/upload', methods = ['GET', 'POST'])
def formdisp():
	form = CourseForm()

	#ignore the next line completely please
	# form.city.choices = [(city.id, city.name) for city in City.query.filter_by(state='CA').all()] 
	#this is for when we have implemented db

	return render_template('upload.html', form=form)


if __name__ == "__main__":
	app.run(debug=True)
	


