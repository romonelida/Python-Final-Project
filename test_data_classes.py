# ------------------------------------------------------------------------------------------------- #
# Title: Assignment08-Tests for Data Classes Module
# Description: A collection of tasks for testing the Data Classes Module
# ChangeLog:
# Nelly, 29.11.2023, Created Script
# --------------------------------------------------------------------------------

import unittest
import datetime
from data_classes import Person, Employee


class TestPerson(unittest.TestCase):

    def test_person_init(self):  # Tests the constructor
        person = Person("John", "Doe")
        self.assertEqual(person.first_name, "John")
        self.assertEqual(person.last_name, "Doe")

    def test_person_invalid_name(self):   # Test the first and last name validations
        with self.assertRaises(ValueError):
            Person("123", "Doe")  # Test for invalid first name
        with self.assertRaises(ValueError):
            Person("John", "123")  # Test for invalid last name

    def test_person_str(self):  # Tests the __str__() magic method
        person = Person("John", "Doe")
        self.assertEqual(str(person), "John,Doe")

    def test_person_title_case(self):
        person = Person("joHn", "doE")
        self.assertEqual(person.first_name, "John")
        self.assertEqual(person.last_name, "Doe")

    def test_person_empty_name(self):
        person = Person("", "")
        self.assertEqual(person.first_name, "")
        self.assertEqual(person.last_name, "")


class TestEmployee(unittest.TestCase):

    def test_employee_init(self):  # Tests the constructor
        employee = Employee("Alice", "Smith",  "2021-01-01", 3)
        self.assertEqual(employee.first_name, "Alice")
        self.assertEqual(employee.last_name, "Smith")
        self.assertEqual(employee.review_date, datetime.date(2021, 1, 1))
        self.assertEqual(employee.review_rating, 3)

    def test_employee_review_rating_type(self):  # Test the review rating validation
        with self.assertRaises(ValueError):
            Employee("Bob", "Johnson", "2021-01-01", 6)  # Provide an invalid review rating (e.g., a number outside 1-5)

    def test_employee_invalid_review_date(self):
        with self.assertRaises(ValueError):
            Employee("Eve", "Brown", "2021-31-01", 4)

    def test_employee_str(self):
        employee = Employee("Eve", "Brown", "2021-01-01",   4)  # Tests the __str__() magic method
        self.assertEqual(str(employee), "Eve Brown, Review Date: 2021-01-01, Rating: 4")


if __name__ == '__main__':
    unittest.main()
