from typing import Any

from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def home() -> Any:
    return render_template('index.html')


@app.route('/remove_bg')
def remove_bg() -> Any:
    return render_template('remove_bg.html')


if __name__ == '__main__':
    # remove_background()
    app.run(debug=True)
