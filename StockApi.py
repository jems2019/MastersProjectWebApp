from flask import Flask
from flask import render_template, request

app = Flask(__name__)

# setting the route for the project
# rendering the home page


@app.route('/')
def index():
    return render_template('Index.html')


@app.route('/StockApiImplementation/')
def homepage():
    return render_template('Index.html')

