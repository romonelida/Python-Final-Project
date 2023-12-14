# -------------------------------------------------------------------------------- #
# Title: Assignment08-Processing Classes Module
# Description: A collection of processing classes for managing the application
# ChangeLog:
# Nelly, 29.11.2023, Created Script
# --------------------------------------------------------------------------------#


import json
import data_classes as data
import presentation_classes as pres
from datetime import date


class CustomJSONEncoder(json.JSONEncoder):
    """
        Extends json.JSONEncoder and override the default method to handle date objects.

        ChangeLog:
        Nelly, 30.11.2023, Created Class
    """

    def default(self, o):
        if isinstance(o, date):
            return o.isoformat()  # Convert date to ISO format string
        return json.JSONEncoder.default(self, o)


class FileProcessor:
    """
    A collection of processing layer functions that work with Json files

    ChangeLog:
    Nelly, 30.11.2023, Created Class
    """

    @staticmethod
    def read_employee_data_from_file(file_name: str) -> list:
        """ Reads data from a json file and loads it into a list of employee objects.

        ChangeLog:
        Nelly, 30.11.2023, Created function

        :param file_name: string data with name of file to read from
        :return: list of employee objects
        """
        employee_data = []
        try:
            with open(file_name, "r") as file:
                list_of_dictionary_data = json.load(file)  # the load function returns a list of dictionary rows.
                for employee in list_of_dictionary_data:
                    employee_object = data.Employee()
                    employee_object.first_name = employee["FirstName"]
                    employee_object.last_name = employee["LastName"]
                    employee_object.review_date = employee["ReviewDate"]
                    employee_object.review_rating = employee["ReviewRating"]
                    employee_data.append(employee_object)
        except FileNotFoundError as e:
            pres.IO.output_error_messages("The file was not found. Please check the file path.", e)
        except json.JSONDecodeError as e:
            pres.IO.output_error_messages("The file does not contain valid JSON.", e)
        except Exception as e:
            pres.IO.output_error_messages("An unexpected error occurred.", e)
        return employee_data

    @staticmethod
    def write_employee_data_to_file(file_name: str, employee_data: list):
        """ Writes data to a json file with data from a list of employee objects

        ChangeLog:
        Nelly, 30.11.2023, Created function

        :param file_name: string data with name of file to write to
        :param employee_data: list of employee data to be writen to the file

        :return: None
        """
        try:
            list_of_dictionary_data: list = []
            for employee in employee_data:  # Convert List of employee objects to list of dictionary rows.
                employee_json: dict = {"FirstName": employee.first_name,
                                       "LastName": employee.last_name,
                                       "ReviewDate": employee.review_date,
                                       "ReviewRating": employee.review_rating
                                       }
                list_of_dictionary_data.append(employee_json)

            with open(file_name, "w") as file:
                json.dump(list_of_dictionary_data, file, cls=CustomJSONEncoder)
        except Exception as e:
            pres.IO.output_error_messages("An error occurred while writing to the file.", e)
