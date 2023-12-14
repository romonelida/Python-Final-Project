# ------------------------------------------------------------------------------------------------- #
# Title: Assignment08-Tests for Presentation Classes Module
# Description: A collection of tasks for testing the Presentation Classes Module
# ChangeLog:
# Nelly, 29.11.2023, Created Script
# ---------------------------------------------------------------------------------------------------#
import unittest
from unittest.mock import patch
from presentation_classes import IO


class TestIO(unittest.TestCase):

    def test_input_menu_choice(self):
        with patch('builtins.input', return_value='2'):
            choice = IO.input_menu_choice()
            self.assertEqual('2', choice)

    def test_input_employee_data(self):
        with patch('builtins.input', side_effect=['John', 'Doe', '2021-01-01', '3']):
            employee_data = []
            IO.input_employee_data(employee_data)
            self.assertEqual(1, len(employee_data))
            self.assertEqual("John", employee_data[0].first_name)
            self.assertEqual("Doe", employee_data[0].last_name)
            self.assertEqual(employee_data[0].review_date.strftime("%Y-%m-%d"), "2021-01-01")
            self.assertEqual(3, employee_data[0].review_rating)


if __name__ == '__main__':
    unittest.main()
