import payroll


class Employee:
    """
    A class to represent an employee and calculate various financial aspects
    of their compensation.

    Attributes
    ----------
    WEEKS : int
        Number of weeks in a year (default is 52).
    REG_HOURS : int 
        Regular working hours per week (default is 40).
    OT_HOURS : int
        Overtime hours per week (default is 10).
    OVERTIME_MULTIPLIER : float
        Multiplier for overtime pay (default is 1.5).

    Methods
    -------
    __init__(self, name: str, raise_dollar_amount: float, 
    bonus_percent_amount: float, weekly_health_insurance: float):
        Initializes the employee with the given attributes.

    calculate_yearly_health_insurance(self):
        Calculates and prints the yearly health insurance cost for the employee.

    calculate_bonus_amount(self):
        Calculates and prints the bonus amount for the employee based on their 
        current pay and bonus percentage.

    calculate_raise_amount(self):
        Calculates and prints the raise amount for the employee based on their
        raise dollar amount and working hours.

    calculate_vacation_amount(self):
        Calculates and prints the one-week vacation pay for the employee.
    """

    WEEKS = 52
    REG_HOURS = 40
    OT_HOURS = 10
    OVERTIME_MULTIPLIER = 1.5


    def __init__(self, name: str, raise_dollar_amount: float, 
                 bonus_percent_amount: float, 
                 weekly_health_insurance: float):
        """
        Initializes the employee with the given attributes.

        Parameters
        ----------
        name : str
            The name of the employee.
        raise_dollar_amount : float
            The dollar amount of the raise per hour.
        bonus_percent_amount : float
            The percentage amount of the bonus.
        weekly_health_insurance : float
            The weekly cost of health insurance.
        """
        self.name = name
        self.current_pay_amount = payroll.employees.get(name, 0)
        self.raise_dollar_amount = raise_dollar_amount
        self.bonus_percent_amount = bonus_percent_amount
        self.weekly_health_insurance = weekly_health_insurance
        self.total_bonus_amount = 0
        self.total_raise_amount = 0


    def calculate_yearly_health_insurance(self):
        """
        Calculates and prints the yearly health insurance cost for the employee.
        """
        yearly_health_insurance = round(self.weekly_health_insurance \
                                    * self.WEEKS, 2)
        if self.weekly_health_insurance > 0:
            print(f"Total yearly health insurance for {self.name}: "
                f"${yearly_health_insurance:,.2f}")
        else:
            print(f"{self.name} does not currently have health insurance through the company.")


    def calculate_bonus_amount(self):
        """
        Calculates and prints the bonus amount for the employee based on their 
        current pay and bonus percentage.
        """
        self.bonus_amount = round(self.current_pay_amount * self.bonus_percent_amount, 2)
        self.total_bonus_amount += self.bonus_amount
        print(f"Total {self.bonus_percent_amount * 100}% bonus amount "
        f"for {self.name}: ${self.bonus_amount:,.2f}")


    def calculate_raise_amount(self):
        """
        Calculates and prints the raise amount for the employee based on their
        raise dollar amount and working hours.
        """
        raise_amount = round(((self.raise_dollar_amount * self.REG_HOURS) + \
                              (self.raise_dollar_amount * self.OVERTIME_MULTIPLIER \
                                * self.OT_HOURS)) \
                                * self.WEEKS, 2)
        self.total_raise_amount += raise_amount
        self.new_pay_amount = self.current_pay_amount + raise_amount
        print(f"Total ${self.raise_dollar_amount} raise amount for "
              f"{self.name}: ${raise_amount:,.2f}")
        

    def calculate_vacation_amount(self):
        """
        Calculates and prints the one-week vacation pay for the employee.
        """
        vacation_amount = round(self.current_pay_amount / self.WEEKS, 2)
        print(f"Total one week vacation amount for {self.name}: "
              f"${vacation_amount:,.2f}\n")
