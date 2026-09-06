# Employee Benefits Calculator

This project calculates employee payroll, raises, bonuses, vacation pay,
health insurance costs, and BCBS weekly deductions. It includes a Tkinter GUI
for selecting calculations, filtering employees, viewing history, and charting
salary totals by year.

## Project Structure

- **employee_benefits.py**: Loads employee configuration and runs the Tkinter
  application and calculation reports.
- **employee.py**: Defines the `Employee` class and its compensation and
  insurance calculations.
- **json_files/employee_details.json**: Private employee configuration used
  when it exists.
- **employee_details.json**: Public fallback employee configuration.
- **payroll.py**: Standalone payroll totals example using its employee map.
- **requirements.txt**: Dependency list. The application currently uses only
  Python standard-library modules.
- **LICENSE.txt**: MIT license.

## Installation

1. Clone the repository:
    ```sh
    git clone https://github.com/theOrganizedMind/employee-benefits.git
    cd employee-benefits
    ```

2. Install the listed packages:
    ```sh
    pip install -r requirements.txt
    ```

## Usage

### Employee Benefits GUI

Run the application from the project directory:

```sh
python employee_benefits.py
```

Use the **Calculation** dropdown to choose one of these options:

- **BCBS weekly deductions**: Shows current-year health insurance totals and
  weekly employee deductions.
- **Raises and bonuses**: Calculates health insurance, bonuses, raises,
  vacation pay, and updated payroll totals.
- **Employee history**: Displays each selected employee's salary, raise, bonus,
  and performance rating for every configured year.
- **Salary by year line chart**: Displays total salary by year for the selected
  employee or all employees.

The **Employee filter** supports selecting all employees or typing part of an
employee's name to narrow the choices. Click **Calculate** to display the
selected report.

### Payroll Totals Script

To run the standalone payroll totals example:

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
