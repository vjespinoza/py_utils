import os
from typing import Any

from flask import Flask, render_template, request
from flask_dropzone import Dropzone

from app_functionalities.image_utilities import remove_background

app = Flask(__name__)
dropzone = Dropzone(app)


@app.route('/')
def home() -> Any:
    return render_template('index.html')


@app.route('/remove_bg')
def remove_bg() -> Any:
    return render_template('remove_bg.html')


@app.route('/uploads', methods=['GET', 'POST'])
def uploads() -> Any:
    if request.method == 'POST':
        f = request.files.get('file')
        f.save(os.path.join('../resources/img', f.filename))

    return render_template('uploads.html')


@app.route('/process_bg_removal')
def process_bg_removal() -> Any:
    remove_background()
    return ""


if __name__ == '__main__':
    # remove_background()
    app.run(debug=True)
