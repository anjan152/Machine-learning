from flask import Flask, render_template,request,flash,redirect
import os
from werkzeug.utils import secure_filename
from ml_model import classify_flower
UPLOAD_FOLDER = "./image"
ALLOWED_EXTENSIONS = { 'png', 'jpg', 'jpeg'}

app = Flask(__name__)
app.config['SECRET_KEY'] = 'the malayalam'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER


def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS
@app.route("/",methods=["GET"])
def image_post():
    return render_template("image.html")
@app.route("/",methods=["POST"])
def upload_post():
    if 'file' not in request.files:
        flash('No file part')
        return redirect(request.url)
    file = request.files['file']
    # If the user does not select a file, the browser submits an
    # empty file without a filename.
    if file.filename == '':
        flash('No selected file')
        return redirect(request.url)
    flower = None
    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)
        flower_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        file.save(flower_path)
        flower = classify_flower(flower_path)
    return render_template("image.html",flower = flower)


