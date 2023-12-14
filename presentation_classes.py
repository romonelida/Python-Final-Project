# ------------------------------------------------------------------------------ #
# Title: Assignment08-Presentation Classes Module
# Description: A collection of presentation classes for managing the application
# ChangeLog:
# Nelly, 29.11.2023, Created Script
# --------------------------------------------------------------------------------#

import data_classes as data


class IO:
    """
    A collection of presentation layer functions that manage user input and output

    ChangeLog:
    Nelly,23.11.2023,Created Class
    """
    pass

    @staticmethod
    def output_error_messages(message: str, error: Exception = None):
        """ Displays a custom error messages to the user

        ChangeLog:
        Nelly, 29.11.2023, Created function

        :param message: string with message data to display
        :param error: Exception object with technical message to display

        :return: None
        """

        print(message, end="\n\n")
        if error is not None:
            print("-- Technical Error Message -- ")
            print(error, error.__doc__, type(error), sep='\n')

    @staticmethod
    def output_menu(menu: str):
        """ Displays the menu of choices to the user

        ChangeLog:
        Nelly,29.11.2023,Created function

        :return: None
        """
        print()
        print(menu)
        print()

    @staticmethod
    def input_menu_choice():
        """ Gets a menu choice from the user

        ChangeLog:
        Nelly, 29.11.2023, Created function

        :return: string with the users choice
        """
        while True:
            choice = input("Enter your menu choice number: ")
            if choice in ("1", "2", "3", "4"):
                return choice
            else:
                IO.output_error_messages("Please, choose only 1, 2, 3, or 4")

    @staticmethod
    def output_employee_data(employee_data: list):
        """ Displays employee data to the user

        ChangeLog:
        Nelly, 29.11.2023, Created function

        :param employee_data: list of employee object data to be displayed

        :return: None
        """
        # message:str = ''
        print("\n" + "-" * 50)
        for employee in employee_data:
            if employee.review_rating == 5:
                message = " {} {} is rated as 5 (Leading)"
            elif employee.review_rating == 4:
                message = " {} {} is rated as 4 (Strong)"
            elif employee.review_rating == 3:
                message = " {} {} is rated as 3 (Solid)"
            elif employee.review_rating == 2:
                message = " {} {} is rated as 2 (Building)"
            elif employee.review_rating == 1:
                message = " {} {} is rated as 1 (Not Meeting Expectations"
            else:
                message = "Rating not defined for {} {}"

            print(message.format(employee.first_name, employee.last_name))
        print("-" * 50 + "\n")

    @staticmethod
    def input_employee_data(employee_data: list):
        """ Gets the first name, last name, and review date and rating from the user

        ChangeLog:
        Nelly, 29.11.2023,Created function

        :param employee_data: list of Employee objects to be filled with input data

        :return: list
        """

        try:
            # Input the data
            employee_object = data.Employee()
            employee_object.first_name = input("What is the employee's first name? ")
            employee_object.last_name = input("What is the employee's last name? ")
            employee_object.review_date = input("What is their review date? ")
            employee_object.review_rating = int(input("What is their review rating? "))
            employee_data.append(employee_object)

        except ValueError as e:
            IO.output_error_messages("That value is not the correct type of data!", e)
        except Exception as e:
            IO.output_error_messages("There was a non-specific error!", e)

        return employee_data
