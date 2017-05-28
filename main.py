from flask import Flask, render_template, request, redirect
import os
from importlib.machinery import SourceFileLoader
current_file_path = os.path.dirname(os.path.abspath(__file__))

data_manager = SourceFileLoader("data_manager", current_file_path + "data_manager.py").load_module()


app = Flask(__name__)


@app.route('/')
def index():
   pass


@app.route('/mentors')
def index():
   pass


@app.route('/all-school')
def index():
   pass


@app.route('/mentors-by-country')
def index():
   pass


@app.route('/contacs')
def index():
   pass


@app.route('/applicants')
def index():
   pass


@app.route('/applicants-and-mentors')
def index():
   pass


if __name__ == '__main__':
    app.run(debug=True)