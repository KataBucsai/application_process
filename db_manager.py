import psycopg2
import ui


def handle_db_queries(command):
    connect_str = "dbname='kata' user='kata' host='localhost' password='berendel'"
    conn = psycopg2.connect(connect_str)
    conn.autocommit = True
    cursor = conn.cursor()
    cursor.execute(command)
    if "SELECT" in command:
        rows = cursor.fetchall()
        return rows


def mentors_name():
    result = handle_db_queries("""SELECT first_name, last_name FROM mentors; """)
    ui.print_table(result, ("First name", "Last name"))


def nicknames_from_miskolc():
    result = handle_db_queries("""SELECT nick_name FROM mentors WHERE city='Miskolc'; """)
    ui.print_table(result, ["Nickname"])


def carols_data():
    result = handle_db_queries("""SELECT first_name, last_name, phone_number 
                               FROM applicants WHERE first_name='Carol'; """)
    final_result = [((result[0][0] + " " + result[0][1]), result[0][2])]
    ui.print_table(final_result, ["Full name", "Phone number"])


def aduni_students_data():
    result = handle_db_queries("""SELECT first_name, last_name, phone_number 
                               FROM applicants WHERE email 
                               LIKE '%@adipiscingenimmi.edu'; """)
    final_result = [((result[0][0] + " " + result[0][1]), result[0][2])]
    ui.print_table(final_result, ["Full name", "Phone number"])


def new_applicant():
    handle_db_queries("""INSERT INTO applicants VALUES (11, 'Markus', 'Schaffarzyk',
                      '003620/725-2666', 'djnovus@groovecoverage.com', 54823);""")
    result = handle_db_queries("""SELECT * FROM applicants 
                               WHERE application_code=54823; """)
    ui.print_table(result, ["ID", "First name", "Last name", "Phone number", "Email",
                            "Application code"])


def update_phonenumber():
    handle_db_queries("""UPDATE applicants SET phone_number='003670/223-7459' 
                      WHERE first_name='Jemima' AND last_name='Foreman';""")
    result = handle_db_queries("""SELECT * FROM applicants 
                               WHERE first_name='Jemima' AND last_name='Foreman';""")
    ui.print_table(result, ("ID", "First name", "Last name", "Phone number", "Email",
                            "Application code"))


def delete_applicants():
    handle_db_queries("""DELETE FROM applicants WHERE email LIKE '%@mauriseu.net';""")
    result = handle_db_queries("""SELECT * FROM applicants; """)
    ui.print_table(result, ("ID", "First name", "Last name", "Phone number", "Email",
                            "Application code"))