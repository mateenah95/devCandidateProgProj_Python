from flask import Flask, render_template
from tableManager import getData

#creating flask application
app = Flask(__name__)

#declaring home/index route and view
@app.route('/')
def index():
    data = getData()
    return render_template('index.html', data=data)


