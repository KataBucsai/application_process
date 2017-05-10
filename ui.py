from terminaltables import AsciiTable


# @table: list of lists - the table to print out
# @title_list: list of strings - the head of the table
def print_table(table, title_list):
    table_items = [title_list]
    for item in table:
        table_items.append(item)
    table = AsciiTable(table_items)
    table.inner_heading_row_border = True
    table.inner_row_border = True
    print(table.table)


# This function needs to print result of the special functions
# @result: string or list or dictionary - result of the special function
# @label: string - label of the result
def print_result(result, label):
    for row in range(len(result)):
        for column in range(len(result[0])):
            print(str(label[column]) + ": " + str(result[row][column]))


# @title: string - title of the menu
# @list_options: list of strings - the options in the menu
# @exit_message: string - the last option with (0) (example: "Back to main menu")
def print_menu(title, list_options, exit_message):
    print()
    print(title)
    print()
    menu_number = 1
    for options in list_options:
        print("(" + str(menu_number) + ")",  options)
        menu_number += 1
    print("(0)", exit_message)
    print()


# This function gets a list of inputs from the user by the terminal
#
# @list_labels: list of strings - the labels of the inputs
# @title: string - title of the "input section"
# @inputs: list of string - list of the received values from the user
def get_inputs(list_labels, title):
    inputs = []
    print(title)
    for item in list_labels:
        input_required = True
        while input_required:
            user_input = input(str(item))
            if user_input != '':
                inputs.append(user_input)
                input_required = False
            else:
                print("Please enter a valid input")
                continue
    return inputs


# This function needs to print an error message. (example: Error: @message)
#
# @message: string - the error message
def print_error_message(message):
    print("Error: %s" % message)
