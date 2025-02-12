# Payroll Management System

This project is a simple payroll management system that calculates the 
total payroll, bonuses, raises, and other financial aspects for employees.

## Project Structure

## Files

- **employee.py**: Contains the `Employee` class which represents an employee 
and includes methods to calculate various financial aspects of their compensation.
- **employee_details.py**: Contains the details of employees for the year 2024 
and a function to reset employee details.
- **payroll.py**: Contains the payroll data and calculates the total yearly, 
monthly, and weekly payroll.
- **raises_and_bonuses.py**: Calculates the total bonuses and raises for all 
employees and updates their payroll accordingly.
- **LICENSE.txt**: Contains the MIT License for the project.
- **requirements.txt**: Lists the dependencies required for the project 
  (currently empty).
- **README.md**: This file, which provides an overview of the project.

## Installation

1. Clone the repository:
    ```sh
    git clone https://github.com/theOrganizedMind/raises_and_bonuses.git
    cd raises_and_bonuses
    ```

2. Install the required packages:
    ```sh
    pip install -r requirements.txt
    ```

## Usage

1. **Calculate Payroll**:
   Run the `payroll.py` script to calculate and print the total yearly, monthly, 
   and weekly payroll.

   ```sh
   python payroll.py
   ```

## Contributing

1. Fork the repository.
2. Create a new branch (`git checkout -b feature-branch`).
3. Make your changes.
4. Commit your changes (`git commit -am 'Add new feature'`).
5. Push to the branch (`git push origin feature-branch`).
6. Create a new Pull Request.

## License

This project is licensed under the MIT License. 
See the LICENSE.txt file for details.
