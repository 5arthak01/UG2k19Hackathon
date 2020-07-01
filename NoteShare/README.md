# NoteShare 

Notes sharing and QP archive web-app.
Allows images, text files, archives and PDFs as uploads and stores them. 
A simple, easy-to-use solution to repetitive, redundant requests for notes and previous year papers on whatsapp groups.

## Implementation
Flask based back-end with JavaScript front-end.
Jinja2 and Bootstrap used with HTML5.
SQLite as DBMS.

## Requirements
Flask
```
pip install Flask
```
SQlite
```
$tar xvfz sqlite-autoconf-3071502.tar.gz
$cd sqlite-autoconf-3071502
$./configure --prefix=/usr/local
$make
$make install
```
Werkzeug
```
pip install Werkzeug
```
FLask-Uploads
```
pip install Flask-Uploads
```
Flask-SQLAlchemy
```
pip install flask-sqlalchemy
```
Flask-WTF
```
pip install Flask-WTF
```
WTForms
```
pip install WTForms
```
Flask-Bootstrap
```
pip install Flask-Bootstrap
```
MDBootstrap
Refer:
https://mdbootstrap.com/docs/jquery/getting-started/download/
Note- the free install is sufficient for this app.

## License
[MIT](https://choosealicense.com/licenses/mit/)
