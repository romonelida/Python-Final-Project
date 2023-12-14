# ------------------------------------------------------------------------------------------------- #
# Title: Assignment08-Tests for Processing Classes Module
# Description: A collection of tasks for testing the Processing Classes Module
# ChangeLog:
# Nelly, 29.11.2023, Created Script
# ---------------------------------------------------------------------------------------------------#

from processing_classes import FileProcessor
import json
import unittest
import tempfile
from data_classes import Employee
import datetime


class TestFileProcessor(unittest.TestCase):
    def setUp(self):
        self.temp_file = tempfile.NamedTemporaryFile(delete=False)
        self.temp_file_name = self.temp_file.name

    def tearDown(self):
        self.temp_file.close()

    def test_read_employee_data_from_file(self):
        sample_data = [
            {"FirstName": "Alice", "LastName": "Smith", "ReviewDate": "2021-01-01", "ReviewRating": 3}
        ]
        with open(self.temp_file_name, "w") as file:
            json.dump(sample_data, file)

        employee = FileProcessor.read_employee_data_from_file(file_name=self.temp_file_name)

        self.assertEqual(len(sample_data), len(employee))

        for i in range(len(sample_data)):
            self.assertEqual(sample_data[i]['FirstName'], employee[i].first_name)
            self.assertEqual(sample_data[i]['LastName'], employee[i].last_name)
            self.assertEqual(datetime.date.fromisoformat(sample_data[i]['ReviewDate']), employee[i].review_date)
            self.assertEqual(sample_data[i]['ReviewRating'], employee[i].review_rating)

    def test_read_employee_data_from_file_invalid_json(self):
        with open(self.temp_file_name, "w") as file:
            file.write("hello world")

        with self.assertRaises(json.JSONDecodeError):
            FileProcessor.read_employee_data_from_file(file_name=self.temp_file_name)

    def test_write_employee_data_to_file(self):
        sample_data = [
            Employee(first_name="Alice", last_name="Smith", review_date="2021-01-01", review_rating=3),
            Employee(first_name="Bob", last_name="Johnson", review_date="2022-02-02", review_rating=4)
        ]
        FileProcessor.write_employee_data_to_file(file_name=self.temp_file_name, employee_data=sample_data)
        with open(self.temp_file_name, "r") as file:
            file_data = json.load(file)

        self.assertEqual(len(sample_data), len(file_data))

        for i in range(len(sample_data)):
            self.assertEqual(sample_data[i].first_name, file_data[i]['first_name'])
            self.assertEqual(sample_data[i].last_name, file_data[i]['last_name'])
            self.assertEqual(sample_data[i].review_date, file_data[i]["review_date"])
            self.assertEqual(sample_data[i].review_rating, file_data[i]["review_rating"])


if __name__ == '__main__':
    unittest.main()
