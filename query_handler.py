from importlib.machinery import SourceFileLoader
current_file_path = os.path.dirname(os.path.abspath(__file__))

handle_db_queries = SourceFileLoader("sql_connection", current_file_path + "connection/sql_connection.py").load_module()


def query_mentors_name():
    result = handle_db_queries("""SELECT first_name, last_name FROM mentors; """)
    return result


def query_nicknames_from_miskolc():
    result = handle_db_queries("""SELECT nick_name FROM mentors WHERE city='Miskolc'; """)
    return result


def query_carols_data():
    result = handle_db_queries("""SELECT first_name, last_name, phone_number 
                               FROM applicants WHERE first_name='Carol'; """)
    final_result = [((result[0][0] + " " + result[0][1]), result[0][2])]
    return final_result


def query_aduni_students_data():
    result = handle_db_queries("""SELECT first_name, last_name, phone_number 
                               FROM applicants WHERE email 
                               LIKE '%@adipiscingenimmi.edu'; """)
    final_result = [((result[0][0] + " " + result[0][1]), result[0][2])]
    return final_result


def query_new_applicant():
    handle_db_queries("""INSERT INTO applicants (first_name, last_name, phone_number, email, application_code)
                      VALUES ('Markus', 'Schaffarzyk','003620/725-2666', 'djnovus@groovecoverage.com', 54823);""")
    result = handle_db_queries("""SELECT * FROM applicants 
                               WHERE application_code=54823; """)
    return result


def query_update_phonenumber():
    handle_db_queries("""UPDATE applicants SET phone_number='003670/223-7459' 
                      WHERE first_name='Jemima' AND last_name='Foreman';""")
    result = handle_db_queries("""SELECT * FROM applicants 
                               WHERE first_name='Jemima' AND last_name='Foreman';""")
    return result


def query_delete_applicants():
    handle_db_queries("""DELETE FROM applicants WHERE email LIKE '%@mauriseu.net';""")
    result = handle_db_queries("""SELECT * FROM applicants; """)
    return result