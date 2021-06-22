from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
import logging
import os
from werkzeug.utils import secure_filename
from os import listdir
from os.path import isfile, join

app = Flask(__name__)
app.config['UPLOAD_PATH'] = 'tmp'


@app.route('/')
def hello_world():
    return render_template("index.html")


@app.route('/uploader', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        f = request.files['file']
        filename = secure_filename(f.filename)
        # f.save(os.path.join("tmp", filename))
        print(os.path.join(app.config['UPLOAD_PATH'], filename))
        f.save(os.path.join(app.config['UPLOAD_PATH'], filename))
        # f.save(secure_filename(f.filename))
        print("success msg")
        print(os.path)
        print("something new here")

        onlyfiles = os.listdir(app.config['UPLOAD_PATH'])
        return render_template("page2.html")


@app.route('/user')
def user():
    return 'This is the user page'


if __name__ == "__main__":
    app.run(debug=True, port=8000)




@app.route('/filelist')
def get_files():
    print(os.path)
    print("something new here")
    mypath = os.path.dirname("tmp")
    onlyfiles = [f for f in listdir(mypath) if isfile(join(mypath, f))]
    return onlyfiles
