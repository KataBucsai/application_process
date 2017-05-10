import sys
import os
import ui
import db_manager


def choose():
    inputs = ui.get_inputs(["Please enter a number: "], "")
    option = inputs[0]
    if option == "1":
        db_manager.mentors_name()
    elif option == "2":
        db_manager.nicknames_from_miskolc()
    elif option == "3":
        db_manager.carols_data()
    elif option == "4":
        db_manager.aduni_students_data()
    elif option == "5":
        db_manager.new_applicant()
    elif option == "6":
        db_manager.update_phonenumber()
    elif option == "7":
        db_manager.delete_applicants()
    elif option == "0":
        sys.exit(0)
    else:
        raise KeyError("There is no such option.")


def handle_menu():
    options = ["Names of the mentors",
               "Nicknames of mentors from Miskolc",
               "Full name and phone number of Carol ",
               "Full name and phone number of student from Adipiscingenimmi University",
               "Add new applicant",
               "Update Jemima's phone number",
               "Delete applicants with @mauriseu.net email address"]

    ui.print_menu("Application process menu", options, "Exit program")


def main():
    while True:
        handle_menu()
        try:
            choose()
        except KeyError as err:
            print(err)


if __name__ == '__main__':
    main()