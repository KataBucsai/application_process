import os
from importlib.machinery import SourceFileLoader
current_file_path = os.path.dirname(os.path.abspath(__file__))

sql_connection = SourceFileLoader("sql_connection", current_file_path + "/connection/sql_connection.py").load_module()


def query_mentors_name():
    result = sql_connection.handle_db_queries("""SELECT first_name, last_name FROM mentors; """)
    return result


def query_nicknames_from_miskolc():
    result = sql_connection.handle_db_queries("""SELECT nick_name FROM mentors WHERE city='Miskolc'; """)
    return result


def query_carols_data():
    result = sql_connection.handle_db_queries("""SELECT first_name, last_name, phone_number 
                               FROM applicants WHERE first_name='Carol'; """)
    final_result = [((result[0][0] + " " + result[0][1]), result[0][2])]
    return final_result


def query_aduni_students_data():
    result = sql_connection.handle_db_queries("""SELECT first_name, last_name, phone_number 
                               FROM applicants WHERE email 
                               LIKE '%@adipiscingenimmi.edu'; """)
    final_result = [((result[0][0] + " " + result[0][1]), result[0][2])]
    return final_result


def query_new_applicant():
    sql_connection.handle_db_queries("""INSERT INTO applicants (first_name, last_name, phone_number, email, application_code)
                      VALUES ('Markus', 'Schaffarzyk','003620/725-2666', 'djnovus@groovecoverage.com', 54823);""")
    result = sql_connection.handle_db_queries("""SELECT * FROM applicants 
                               WHERE application_code=54823; """)
    return result


def query_update_phonenumber():
    sql_connection.handle_db_queries("""UPDATE applicants SET phone_number='003670/223-7459' 
                      WHERE first_name='Jemima' AND last_name='Foreman';""")
    result = sql_connection.handle_db_queries("""SELECT * FROM applicants 
                               WHERE first_name='Jemima' AND last_name='Foreman';""")
    return result


def query_delete_applicants():
    sql_connection.handle_db_queries("""DELETE FROM applicants WHERE email LIKE '%@mauriseu.net';""")
    result = sql_connection.handle_db_queries("""SELECT * FROM applicants; """)
    return result


def query_mentors():
    result = sql_connection.handle_db_queries("""SELECT mentors.first_name, mentors.last_name,
                               schools.name, schools.country FROM mentors JOIN schools
                               ON mentors.city = schools.city ORDER BY mentors.id;""")
    return result


def query_all_school():
    result = sql_connection.handle_db_queries("""SELECT mentors.first_name, mentors.last_name,
                               schools.name, schools.country FROM mentors RIGHT JOIN schools
                               ON mentors.city = schools.city ORDER BY mentors.id;""")
    return result


def query_mentors_by_country():
    result = sql_connection.handle_db_queries("""SELECT schools.country, COUNT(mentors.id) as CountOfMentors
                                              FROM schools LEFT JOIN mentors ON schools.city = mentors.city
                                              GROUP BY schools.country ORDER BY schools.country;""")
    return result


def query_contacts():
    result = sql_connection.handle_db_queries("""SELECT schools.name, mentors.first_name, mentors.last_name
                                              FROM schools LEFT JOIN mentors ON schools.contact_person = mentors.id
                                              ORDER BY schools.name ; """)
    return result


def query_applicants():
    result = sql_connection.handle_db_queries("""SELECT applicants.first_name, applicants.application_code,
                                              applicants_mentors.creation_date FROM applicants 
                                              JOIN applicants_mentors ON applicants.id = applicants_mentors.applicant_id
                                              WHERE creation_date > '2016-01-01'; """)
    return result


def query_applicants_and_mentors():
    result = sql_connection.handle_db_queries("""SELECT applicants.first_name, applicants.application_code,
                                              mentors.first_name, mentors.last_name FROM ((applicants 
                                              LEFT JOIN applicants_mentors ON applicants.id = applicants_mentors.applicant_id)
                                              LEFT JOIN mentors ON applicants_mentors.mentor_id = mentors.id);""")
    return result