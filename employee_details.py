employee_details_2024 = [
    {
    "name": "John Doe", 
    "raise_dollar_amount": 0.00, 
    "bonus_percent_amount": 0.03, 
    "weekly_health_insurance": 72.00
    },
    {
    "name": "Jane Smith", 
    "raise_dollar_amount": 1.00,
    "bonus_percent_amount": 0.03, 
    "weekly_health_insurance": 66.50
    },
    {
    "name": "Alice Johnson", 
    "raise_dollar_amount": 5.00,
    "bonus_percent_amount": 0.025, 
    "weekly_health_insurance": 65.31
    },        
    {
    "name": "Bob Brown", 
    "raise_dollar_amount": 0.00, 
    "bonus_percent_amount": 0.01, 
    "weekly_health_insurance": 0.00
    },
    {
    "name": "Carol White", 
    "raise_dollar_amount": 1.00, 
    "bonus_percent_amount": 0.02, 
    "weekly_health_insurance": 72.00
    },        
    {
    "name": "David Black", 
    "raise_dollar_amount": 2.00, 
    "bonus_percent_amount": 0.01, 
    "weekly_health_insurance": 0.00
    },        
]


def reset_employee_details(details):
    """
    Resets the raise and bonus amounts for each employee in the provided list.

    Args:
        details (list): A list of dictionaries, where each dictionary contains
                        details of an employee including 'raise_dollar_amount' 
                        and 'bonus_percent_amount'.

    Returns:
        list: A new list of dictionaries with the same employee details, but 
              with 'raise_dollar_amount' and 'bonus_percent_amount' set to 0.00.
    """
    new_details = []
    for employee in details:
        new_employee = employee.copy()
        new_employee["raise_dollar_amount"] = 0.00
        new_employee["bonus_percent_amount"] = 0.00
        new_details.append(new_employee)
    return new_details


if __name__ == "__main__":
    updated_employee_details = reset_employee_details(employee_details_2024)
    for employee in updated_employee_details:
        print(f"{employee},")
