from flask import Flask, render_template
from werkzeug.utils import secure_filename
UPLOAD_FOLDER = "./image"
ALLOWED_EXTENSIONS = { 'png', 'jpg', 'jpeg'}

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

app = Flask(__name__)
def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS
@app.route("/image",methods=["GET"])
def image_post():
    return render_template("image.html")


@app.route("/image",methods=["POST"])
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
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
    return render_template("upload.html")
@app.route("/upload",methods=["GET"])
def upload():
    return render_template("upload.html")
    
