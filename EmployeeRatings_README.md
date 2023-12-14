## Application Name
Employee Ratings

## Brief Description
The application prompts the user to enter the employee's first name and last name, followed by the review date and rating and presents the collected data. Data collected is added to a two-dimensional list table (list of Employee objects). Data is written to a JSON file.

The application allows users to enter multiple employee reviews, display multiple employee reviews and to save multiple employee reviews to a file.

The application also provides structured error handling for all functions.

This application was created with the purpose of learning about how to create multimodule applications. 

## Installation Instructions

### Prerequisites
For the main.py there dependencies with the following libraries and modules in my application: json, processing_classes as proc, presentation_classes as pres and data_classes as data.

For the presentation_classes module there is a dependency with data_classes module. 

Also, for processing_classes module there are dependencies with the following libraries and modules in my application: json, datetime, data_classes, and presentation_classes.

Lastly, for data_classes module there is only a dependency with datetime Python standard library.

In terms of organizing the modules for the application to run properly, having all the files at the same level would be recommended.


### Application Structure 
- `main.py`: The main script that runs the application.
- `data_classes.py`: Handles the data structures used in the application.
- `processing_classes.py`: Contains logic for processing data.
- `presentation_classes.py`: Manages the presentation layer of the application.
- `test_*.py`: Test files for the respective classes.

### Running the Application
The application runs correctly in both PyCharm and from the console or term. 
To execute the application run the main.py file.

### Additional Information
When the application starts, the contents of the "EmployeeRatings.json" are automatically read into a two-dimensional list table (a list of Employee object rows). 

## Application Modules

### Presentation Classes Module

### Presentation Classes Module Documentation

#### Class IO

#### Overview
The `IO` class in the `presentation_classes` module is a critical component of the Employee Ratings application. It handles all presentation-layer functions related to managing user input and output, providing a seamless interface for interaction with the application.

#### Methods

##### output_error_messages
- **Description**: Displays custom error messages to the user.
- **Parameters**:
  - `message`: A string containing the message to display.
  - `error`: An optional `Exception` object containing technical message details.
- **Usage**: Used to inform the user of errors in a readable format, providing both a general message and, if available, technical details of the exception.

##### output_menu
- **Description**: Presents a menu of choices to the user.
- **Parameters**:
  - `menu`: A string representing the menu to be displayed.
- **Usage**: Used to display various menu options to the user.

##### input_menu_choice
- **Description**: Captures and validates the user's menu selection.
- **Returns**: A string representing the user's choice.
- **Usage**: Ensures that the user inputs a valid menu option, prompting re-entry if the input is invalid.

##### output_employee_data
- **Description**: Displays a list of employee data to the user.
- **Parameters**:
  - `employee_data`: A list of employee objects to be displayed.
- **Usage**: Formats and presents employee information, including names and review ratings, to the user.

##### input_employee_data
- **Description**: Collects and stores employee information input by the user.
- **Parameters**:
  - `employee_data`: A list of `Employee` objects to be filled with input data.
- **Returns**: The updated list with the new employee data.
- **Usage**: Interactively collects data such as the employee's first name, last name, review date, and rating, and appends this data to the provided list.

#### ChangeLog
- The `IO` class was created by Nelly on 23.11.2023 and has been instrumental in facilitating user interaction within the Employee Ratings application.

### Data Classes Module

### Data Classes Module Documentation

#### Overview
The `data_classes` module is an essential part of the Employee Ratings application, providing structured data models for handling person and employee information. It defines the classes for storing and managing data attributes relevant to persons and employees.

#### Classes

##### Person Class

###### Description
The `Person` class serves as a base class representing general person data.

###### Properties
- `first_name` (str): The person's first name. Should contain only alphabetic characters.
- `last_name` (str): The person's last name. Should contain only alphabetic characters.

###### Methods
- `__init__`: Constructor to initialize a `Person` object with `first_name` and `last_name`.
- Getters and Setters for `first_name` and `last_name`.

###### ChangeLog
- Created by Nelly on 29.11.2023.

##### Employee Class

###### Description
The `Employee` class, inheriting from `Person`, represents detailed employee data.

###### Properties
- Inherits `first_name` and `last_name` from `Person`.
- `review_date` (date): The date of the employee review. Expected format: YYYY-MM-DD.
- `review_rating` (int): The review rating of the employee's performance, ranging from 1 (lowest) to 5 (highest).

###### Methods
- `__init__`: Constructor to initialize an `Employee` object with `first_name`, `last_name`, `review_date`, and `review_rating`.
- Getters and Setters for `review_date` and `review_rating`.

###### Usage
- The `Employee` class is used to create and manage employee objects, containing both personal and review-related information.

###### ChangeLog
- Created by Nelly on 29.11.2023.

#### General Usage
Both `Person` and `Employee` classes are pivotal for managing data throughout the Employee Ratings application. They ensure data integrity and provide a structured way to handle employee information.


### Processing Classes Module

### Processing Classes Module Documentation

#### Overview
The `processing_classes` module in the Employee Ratings application includes classes that handle processing tasks, specifically dealing with JSON file operations. This module ensures efficient data handling and serialization for the application.

#### Classes

##### CustomJSONEncoder Class

###### Description
`CustomJSONEncoder` extends `json.JSONEncoder` to customize JSON encoding, particularly for date objects.

###### Methods
- `default`: Overridden method to handle date objects, converting them into an ISO format string for JSON serialization.

###### ChangeLog
- Created by Nelly on 30.11.2023, to facilitate JSON serialization of date objects.

##### FileProcessor Class

###### Description
The `FileProcessor` class contains static methods for reading from and writing to JSON files, handling employee data serialization and deserialization.

###### Methods

###### read_employee_data_from_file
- **Description**: Reads data from a JSON file and converts it into a list of `Employee` objects.
- **Parameters**:
  - `file_name` (str): The name of the file to read from.
- **Returns**: A list of `Employee` objects.
- **Exceptions Handled**: `FileNotFoundError`, `json.JSONDecodeError`, and other general exceptions.

###### write_employee_data_to_file
- **Description**: Writes a list of `Employee` objects to a JSON file, converting them into a JSON format.
- **Parameters**:
  - `file_name` (str): The name of the file to write to.
  - `employee_data` (list): A list of `Employee` objects to be serialized.
- **Exceptions Handled**: General exceptions during file writing.

###### Usage
- `read_employee_data_from_file` and `write_employee_data_to_file` are used for persisting employee data in a JSON file, ensuring data is correctly read and stored in the application.

###### ChangeLog
- Created by Nelly on 30.11.2023, to manage file operations related to employee data.

#### General Usage
The `processing_classes` module plays a crucial role in the Employee Ratings application, dealing with the complexities of file operations and ensuring that the data is correctly managed and persisted.

## Usage
When the application starts, there is a main menu that prompts the user to select an option from 1 to 4. 
Select Option 1 to show what is currently saved in the JSON file.
Select Option 2 to enter new employee rating data, Figure 4 below.
Select Option 3 to save the data of the new employee rating data added previously.
Select Option 4 to finish the program.

## Features
For my application, there are key features that I would like to point out and are the most important or attractive aspects of my application that make it useful, unique, or appealing to its users.

In terms of data handling, this application has a robust data import capabilities and an effective data management and organization.
For customization and flexibility, the modular architecture allows for expansion or modification.
In relation to the user interface and experience, I consider the application, an intuitive and user-friendly interface.

## Credits and Acknowledgements

I would like to extend my special thanks to my Python class professors, Anubhaw Ayra and Julian Peterson, for their invaluable guidance and support during this course. Their expertise and insights have been crucial in shaping both the technical and conceptual aspects to complete this project. Their dedication to teaching and commitment to fostering a deep understanding of Python and software development principles have significantly contributed to my skills and this application's success. 

Additionally, the following sources of information and support were used in this assignment:

1. Slides and videos from class, laboratories and Demo/Videos of this course in Modules 1 to 8.

2. Starting script included in the Module 08 from class materials. I used this script to start this Final Project, Assignment 08.

3. Open AI ChatGPT, Oct. 2023, chat.openai.com/chat: A few aspects of this assignment were informed by queries submitted to the ChatGPT. 

## Support and Contact Information

My contact information is included below in case needed.
romonelida@gmail.com
