# ------------------------------------------------------------------------------------------------- #
# Title: Assignment08-Main Module
# Description: A collection of tasks for managing the main body of the script
# ChangeLog:
# Nelly, 29.11.2023, Created Script
# --------------------------------------------------------------------------------

import json
import processing_classes as proc
import presentation_classes as pres
import data_classes as data


# Use FILE_NAME from data_classes module
file_name = data.FILE_NAME

# Create EmployeeRatings JSON file (list of Employee object rows)

employees = [
    {"FirstName": "Alice", "LastName": "Smith", "ReviewDate": "2021-01-01", "ReviewRating": 5},
    {"FirstName": "Bob", "LastName": "Johnson", "ReviewDate": "2021-02-15", "ReviewRating": 4}
]

with open('EmployeeRatings.json', 'w') as file:
    json.dump(employees, file, indent=4)


# Beginning of the main body of this script
employees = proc.FileProcessor.read_employee_data_from_file(file_name=file_name)

while True:

    pres.IO.output_menu(menu=data.MENU)

    menu_choice = pres.IO.input_menu_choice()

    if menu_choice == "1":  # Display current data
        try:
            pres.IO.output_employee_data(employee_data=employees)
        except Exception as e:
            pres.IO.output_error_messages(str(e))

    elif menu_choice == "2":  # Get new data (and display the change)
        try:
            employees = pres.IO.input_employee_data(employee_data=employees)
            pres.IO.output_employee_data(employee_data=employees)
        except Exception as e:
            pres.IO.output_error_messages(str(e))

    elif menu_choice == "3":  # Save data in a file
        try:
            proc.FileProcessor.write_employee_data_to_file(file_name=file_name, employee_data=employees)
            print(f"Data was saved to the {file_name} file.")
        except Exception as e:
            pres.IO.output_error_messages(str(e))

    elif menu_choice == "4":  # Exit the program
        print("Exiting the program. Goodbye!")
        break  # This exits the while loop, thus ending the program

    else:  # Handle invalid choices
        print("That's not a valid option. Please choose a valid menu number.")
