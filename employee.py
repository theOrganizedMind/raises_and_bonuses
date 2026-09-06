
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
                 bonus_percent_amount: float, monthly_health_insurance=0,
                 salary=None, weekly_health_insurance=0,
                 performance_rating=3):
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
        monthly_health_insurance : float or list of float
            The monthly health insurance cost components.
        salary : float, optional
            The employee's salary for the selected year.
        weekly_health_insurance : float, optional
            The weekly cost of health insurance.
        performance_rating : int, optional
            The employee's performance rating from 1 to 5.
        """
        self.name = name
        self.current_pay_amount = salary
        self.raise_dollar_amount = raise_dollar_amount
        self.bonus_percent_amount = bonus_percent_amount
        self.monthly_health_insurance = monthly_health_insurance
        self.weekly_health_insurance = weekly_health_insurance
        self.performance_rating = performance_rating
        self.total_bonus_amount = 0
        self.total_raise_amount = 0


    def calculate_yearly_health_insurance(self):
        """
        Calculate and print the yearly health insurance cost for the employee.
        """
        if isinstance(self.monthly_health_insurance, list):
            yearly_health_insurance = round(
                sum(self.monthly_health_insurance) * 12, 2)
        else:
            yearly_health_insurance = round(
                self.weekly_health_insurance * self.WEEKS, 2)
        if yearly_health_insurance > 0:
            print(f"Total yearly health insurance for {self.name}: "
                f"${yearly_health_insurance:,.2f}")
        else:
            print(f"{self.name} does not currently have health insurance through the company.")


    def calculate_bonus_amount(self):
        """
        Calculate and print the bonus amount from current pay and bonus rate.
        """
        self.bonus_amount = round(self.current_pay_amount * self.bonus_percent_amount, 2)
        self.total_bonus_amount += self.bonus_amount
        print(f"Total {self.bonus_percent_amount * 100}% bonus amount "
        f"for {self.name}: ${self.bonus_amount:,.2f}")


    def calculate_raise_amount(self):
        """
        Calculate and print the annual raise amount from the hourly increase.
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
        Calculate and print one week of vacation pay for the employee.
        """
        vacation_amount = round(self.current_pay_amount / self.WEEKS, 2)
        print(f"Total one week vacation amount for {self.name}: "
              f"${vacation_amount:,.2f}\n")

        
    def calculate_weekly_bcbs_deduction(self, 
                                        amounts=None,
                                        company_contribution=300, 
                                        weeks=4):
        """
        Calculate and print total health insurance cost and weekly deduction.

        Args:
            amounts (list of float, optional): List of health insurance cost
                components for the employee.
            company_contribution (float, optional): Amount contributed by the company. Defaults to 300.
            weeks (int, optional): Number of weeks to spread the deduction over. Defaults to 4.

        Prints:
            The total health insurance cost and the weekly deduction for the employee.
        """
        if amounts is None:
            amounts = self.monthly_health_insurance
        if not isinstance(amounts, list):
            amounts = [amounts]

        total = sum(amounts)
        if total > 0:
            weekly_deduction = (total - company_contribution) / weeks
            print(f"Total {self.name} Health Insurance = ${total:,.2f}")
            print(f"Total {self.name} Weekly Deduction = ${weekly_deduction:,.2f}\n")
        else:
            print(f"{self.name} does not currently have health insurance through the company.\n")
