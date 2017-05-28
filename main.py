from flask import Flask, render_template, request, redirect
import os
from importlib.machinery import SourceFileLoader
current_file_path = os.path.dirname(os.path.abspath(__file__))

data_manager = SourceFileLoader("data_manager", current_file_path + "/data_manager.py").load_module()


app = Flask(__name__)


@app.route('/')
def index():
    menu_list = data_manager.index_data()
    return render_template('index.html', menu_list=menu_list)


@app.route('/mentors')
def mentors():
    title = "Mentors and schools"
    columns = ["First name", "Last name", "School name", "Country"]
    result = data_manager.mentors_data()
    return render_template('result.html', title=title, result=result, columns=columns)


@app.route('/all-school')
def all_school():
    title = "All school"
    columns = ["First name", "Last name", "School name", "Country"]
    result = data_manager.all_school_data()
    return render_template('result.html', title=title, result=result, columns=columns)


@app.route('/mentors-by-country')
def mentors_by_country():
    title = "Mentors"
    columns = ["Country", "Count of mentors"]
    result = data_manager.mentors_by_country_data()
    return render_template('result.html', title=title, result=result, columns=columns)


@app.route('/contacts')
def contacts():
    title = "Contacts"
    columns = ["School name", "First name", "Last name"]
    result = data_manager.contacts_data()
    return render_template('result.html', title=title, result=result, columns=columns)


@app.route('/applicants')
def applicants():
    title = "Applicants"
    columns = ["First name", "Application code", "Date"]
    result = data_manager.applicants_data()
    return render_template('result.html', title=title, result=result, columns=columns)


@app.route('/applicants-and-mentors')
def applicants_and_mentors():
    title = "Applicants and mentors"
    columns = ["Applicant's first name", "Application code", "Mentor's first name", "Mentor's last name"]
    result = data_manager.applicants_and_mentors_data()
    return render_template('result.html', title=title, result=result, columns=columns)


if __name__ == '__main__':
    app.run(debug=True)