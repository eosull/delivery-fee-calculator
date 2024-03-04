# Wolt Software Engineer Intern (2024) Submission

**Preliminary Assignment for backend application. HTTP API delivery fee calculator**

**Submitted by Eoin O'Sullivan on 30.01.2024**

## Introduction

This application serves as a HTTP API, built in **Python**, which can be used to calculate delivery fees for a food delivery company based on the specifications provided in the [assigment brief](https://github.com/woltapp/engineering-internship-2024). The application can be run using JSON files to load requests and save responses or using a local server to send and receive HTTP requests. Instructions on how to do both is covered in the [Quickstart](##Quickstart) section.

## Table of Contents

- [Introduction](##Introduction)
- [Features](##features)
- [Installation Guide](##installation-guide)
- [Usage](##usage)
- [Testing](#testing)
- [Tools and Technologies](#tools-and-technologies)
- [Author](#author)

## Features

- Users can submit a JSON request containing information about a order including delivery distance, number of items and cart value.
- The program calculates a delivery fee (based on the rules provided in the [assignment brief](https://github.com/woltapp/engineering-internship-2024)) and returns a response JSON payload including calculated delivery fee.

## Installation Guide

There are **two ways** to run this program - by reading and responding to requests in local files or by using a client to send HTTP requests. The instructions for both can be found below.

In the project folder there is a virtual environment that contains the dependencies/installs needed that can be activated by navigating to the project directory and using the following command:

```
 source .venv/bin/activate
```

This can also be deactivated with:

```
deactivate
```

Before running the program you will also need check the **live** variable in the **wolt_delivery_fee_calculator.py** file. This is set to False as default but if you want to run using a client this will need to be set to True.

### Running with local JSON files

To run the program using local JSON files (in 'sample_orders' folder) you need to follow these steps:

- Navigate to project directory
- Ensure virtual environment is running & live variable is set to **False**
- Check that **order1.json** file contains desired delivery info
- Run the following command:

```
   python3 wolt_delivery_fee_calculator.py
```

- Now when you open **order1_incl_fees.json** you will see that delivery fees have been calculated and added to the JSON data along with order time in UTC.
- Editing the **order1.json** file before running again will allow you to test the program with different cart, item and distance values.

### Running with HTTP Client on VS Code

To run the program using a HTTP client you will need to follow some extra steps. I used Flask to host a local server and the VS Code extension [REST Client](https://marketplace.visualstudio.com/items?itemName=humao.rest-client) to handle HTTP requests. These instructions presume that you can run the program in a similar fashion.

- Open directory in VS Code.
- Ensure virtual environment is running & live variable is set to **True**.
- Enable [REST Client](https://marketplace.visualstudio.com/items?itemName=humao.rest-client) extension in VS Code.
- Start the flask app by running the following command:

```
flask --app wolt_delivery_fee_calculator run
```

- Once this is running, open the **request.http** file to check if JSON payload contains desired info.
- In the **request.http** file, above the local address, click 'Send Request'.
- This will send a JSON POST request to the Flask app and return the response in a side window in VS Code. This response should contain calculated delivery fee and order time.

## Usage

- This program runs from a central script, **wolt_delivery_fee_calculator.py**, which can use local JSON files or HTTP requests as initial information.
- This script utilises two classes stored in the _classes_ folder, **calculator.py** & **cart.py**, whose methods are used to create an order and calculate delivery fees.
- When the program is run, a new order object is created containing the information stored in the JSON payload. This order object is passed into a new calculator object which is used to calculate delivery fees.
- Finally, the response is either added to the locally stored JSON file or sent via HTTP client to the local server.

## Testing

The tests for this program were completed using the Python unit testing framework [unittest](https://docs.python.org/3/library/unittest.html). The test files can be viewed in the _test_ folder and contain the 'test\_' prefix.

Contained in these files are tests for each function used in the program, ensuring the results are what is expected. You can run these tests by using the following command:

```
python -m unittest
```

In the test files you will see tests for all of the sample values provided in the assignment brief.

## Tools and Technologies

- [Python](https://www.python.org/): Used to write core logic of program, complete calculations and complete tests
- [Flask](https://flask.palletsprojects.com/en/3.0.x/): Lightweight web framework used to create simple web applications. Provides a route to send and receive HTTP requests in this program.
- [JSON](https://docs.python.org/3/library/json.html): Built in Python package used to work with JSON data.
- [unittest](https://docs.python.org/3/library/unittest.html): Python unit testing framework. Used to test the functionality of individual functions in the program.

## Author

This program was built as part of an application for the Wolt 2024 Software Engineer Internship by Eoin O'Sullivan

- [GitHub](https://github.com/eosull)
- [LinkedIn](https://www.linkedin.com/in/eoin-o-sullivan-ab262b180/)
