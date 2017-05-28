import os
from importlib.machinery import SourceFileLoader
current_file_path = os.path.dirname(os.path.abspath(__file__))

query_handler = SourceFileLoader("query_handler", current_file_path + "/query_handler.py").load_module()


def index_data():
    menu_list = [["mentors", "Mentors and schools"], ["all-school", "All school"],
                 ["mentors-by-country", "Mentors by country"], ["contacts", "Contacts"],
                 ["applicants", "Applicants"], ["applicants-and-mentors", "Applicants and mentors"]]
    return menu_list


def mentors_data():
    result = query_handler.query_mentors()
    return result


def all_school_data():
    result = query_handler.query_all_school()
    return result


def mentors_by_country_data():
    result = query_handler.query_mentors_by_country()
    return result


def contacts_data():
    result = query_handler.query_contacts()
    return result


def applicants_data():
    result = query_handler.query_applicants()
    return result


def applicants_and_mentors_data():
    result = query_handler.query_applicants_and_mentors()
    return result
