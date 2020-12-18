from flask import Flask, render_template, url_for, request, redirect
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)


@app.route('/', methods=['POST', 'GET'])
def index():
    if request.method == 'POST':
        try:
            filter_cat = 2017
            return render_template('index.html', filter_cat)
        except:
            redirect('/')
    else:
        return render_template('index.html')


if __name__ == "__main__":
    app.run(debug=True)
