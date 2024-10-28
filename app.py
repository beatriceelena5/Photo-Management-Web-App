from flask import Flask, render_template, request, redirect, url_for, session, flash
from werkzeug.utils import secure_filename
from PIL import Image
from urllib.parse import quote
import os
import json

app = Flask(__name__)
app.secret_key = 'very_secret_key'
app.config['UPLOAD_FOLDER'] = 'static/uploads/'
app.config['ALLOWED_EXTENSIONS'] = {'png', 'jpg', 'jpeg', 'gif'}

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in app.config['ALLOWED_EXTENSIONS']

def create_thumbnail(image_path):
    try:
        with Image.open(image_path) as img:
            img.thumbnail((150, 150))  
            thumbnail_path = f"{image_path.rsplit('.', 1)[0]}.thumb.{image_path.rsplit('.', 1)[1]}"
            img.save(thumbnail_path)
            print(f"Thumbnail created at: {thumbnail_path}") 
    except Exception as e:
        print(f"Error creating thumbnail: {e}")


@app.route('/')
def index():
    categories = ['natura', 'urban', 'portrete', 'abstract']
    images_by_category = {}
    for category in categories:
        metadata_path = os.path.join('metadata', f'{category}.json')
        try:
            with open(metadata_path, 'r') as file:
                images_by_category[category] = json.load(file)
        except FileNotFoundError:
            images_by_category[category] = []

    return render_template('index.html', images_by_category=images_by_category, categories=categories)


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        if username == "admin" and password == "password":
            session['logged_in'] = True
            flash('Successfully logged in.')
            return redirect(url_for('index'))
        else:
            flash('Invalid username or password.')
            return render_template('login.html')
    return render_template('login.html')


@app.route('/upload', methods=['GET', 'POST'])
def upload():
    if not session.get('logged_in'):
        return redirect(url_for('login'))

    if request.method == 'POST':
        file = request.files['image']
        name = request.form.get('name', 'No Name')
        description = request.form.get('description', 'No Description')
        category = request.form.get('category')

        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            category_path = os.path.join(app.config['UPLOAD_FOLDER'], category)
            if not os.path.exists(category_path):
                os.makedirs(category_path)
            file_path = os.path.join(category_path, filename)

            metadata_dir = os.path.join('metadata')
            if not os.path.exists(metadata_dir):
                os.makedirs(metadata_dir)

            file.save(file_path)
            create_thumbnail(file_path)

            metadata_path = os.path.join(metadata_dir, f'{category}.json')
            try:
                if not os.path.exists(metadata_path):
                    with open(metadata_path, 'w') as f:
                        json.dump([], f)

                with open(metadata_path, 'r+') as f:
                    metadata = json.load(f)
                    metadata.append({'filename': filename, 'name': name, 'description': description})
                    f.seek(0)
                    json.dump(metadata, f)

                flash('File successfully uploaded and metadata saved.')
            except Exception as e:
                flash(f'Failed to save file: {e}', 'error')

            return redirect(url_for('index'))
        else:
            flash('Invalid file type.', 'error')

    return render_template('upload.html')

@app.route('/delete/<category>/<filename>', methods=['GET', 'POST'])
def delete_image(category, filename):
	print("Category:", category)
	print("Filename:", filename)
	if not session.get('logged_in'):
		flash('You need to be logged in to delete images.', 'error')
		return redirect(url_for('index'))

	image_path = os.path.join(app.config['UPLOAD_FOLDER'], category, filename)
	if os.path.exists(image_path):
		os.remove(image_path) 

		metadata_path = os.path.join('metadata', f'{category}.json')
		try:
			with open(metadata_path, 'r+') as file:
				images = json.load(file)
				images = [img for img in images if img['filename'] != filename]
				file.seek(0)
				file.truncate()
				json.dump(images, file)
			flash('Image successfully deleted.')
		except Exception as e:
			flash(f'Failed to update metadata: {e}', 'error')
	else:
		flash('File does not exist.', 'error')

	return redirect(url_for('index'))



@app.route('/logout')
def logout():
    session.clear()  
    flash('Ai fost deconectat cu succes.')
    return redirect(url_for('index'))


@app.route('/about')
def about():
    return render_template('about.html')