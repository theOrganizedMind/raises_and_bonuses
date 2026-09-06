import os
import json
import io
import tkinter as tk
from contextlib import redirect_stdout
from datetime import datetime
from tkinter import messagebox, ttk

from employee import Employee

# ========================================================================== #
# ================================== INFO ================================== #
# ========================================================================== #

# ========================================================================== #
# ================================== TODO ================================== #
# ========================================================================== #
# TODO:  
# ========================================================================== #

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
PRIVATE_CONFIG_PATH = os.path.join(BASE_DIR, "json_files", "employee_details.json")
PUBLIC_CONFIG_PATH = os.path.join(BASE_DIR, "employee_details.json")

CURRENT_YEAR = str(datetime.now().year)


def load_employee_details():
    """Load employee details from the private config, falling back to public."""
    config_path = (PRIVATE_CONFIG_PATH if os.path.isfile(PRIVATE_CONFIG_PATH)
                   else PUBLIC_CONFIG_PATH)
    with open(config_path, encoding="utf-8") as config_file:
        return json.load(config_file)


employee_details = load_employee_details()
employee_details_current_year = []
for details in employee_details:
    current_year_details = details[CURRENT_YEAR]
    employee_details_current_year.append({
        "name": details["name"],
        "monthly_health_insurance": details.get("monthly_health_insurance", 0),
        **current_year_details,
    })


def get_employee_names():
    """Return the names of all employees in the active configuration."""
    return [details["name"] for details in employee_details]


def get_selected_employee_details(selected_employee="All employees"):
    """Return all employee records or the record matching the selected name."""
    if selected_employee == "All employees":
        return employee_details
    return [
        details for details in employee_details
        if details["name"] == selected_employee
    ]


def get_selected_current_year_details(selected_employee="All employees"):
    """Return current-year records for the selected employee or all employees."""
    selected_names = {
        details["name"] for details in
        get_selected_employee_details(selected_employee)
    }
    return [
        details for details in employee_details_current_year
        if details["name"] in selected_names
    ]


def get_years():
    """Return all configured employee-data years in ascending order."""
    years = {
        year
        for details in employee_details
        for year in details
        if year.isdigit()
    }
    return sorted(years, key=int)


def employee_history_report(selected_employee="All employees"):
    """Print salary, compensation, and performance history for selected employees."""
    employees = get_selected_employee_details(selected_employee)

    for details in employees:
        print(f"\n{details['name']}")
        for year in get_years():
            year_details = details.get(year)
            if year_details is None:
                continue
            print(f"{year}: Salary ${year_details['salary']:,.2f}, "
                  f"Raise ${year_details.get('raise_dollar_amount', 0):,.2f}, "
                  f"Bonus {year_details.get('bonus_percent_amount', 0) * 100:.1f}%, "
                  f"Performance: {'⭐' * int(year_details.get('performance_rating', 3))}")


def salary_totals_by_year(selected_employee="All employees"):
    """Return total salaries by year for the selected employee or all employees."""
    totals = {}
    employees = get_selected_employee_details(selected_employee)
    for year in get_years():
        totals[year] = round(sum(
            details[year]["salary"] for details in employees
            if year in details
        ), 2)
    return totals


def calculate_raises_and_bonuses(selected_employee="All employees"):
    """Print raises, bonuses, benefits, and payroll totals for selected employees."""
    employees = [Employee(**data) for data in
                 get_selected_current_year_details(selected_employee)]
    updated_employee_payroll = {}

    total_bonus_amount = 0
    total_raise_amount = 0
    total_current_payroll = round(
        sum(employee.current_pay_amount for employee in employees), 2)

    for employee in employees:
        print(f"\nCalculating for {employee.name}:")                        
        employee.calculate_yearly_health_insurance()
        employee.calculate_bonus_amount()
        employee.calculate_raise_amount()
        employee.calculate_vacation_amount()

        total_bonus_amount += employee.total_bonus_amount
        total_raise_amount += employee.total_raise_amount

        new_pay_amount = employee.current_pay_amount + employee.total_raise_amount
        updated_employee_payroll[employee.name] = new_pay_amount

    new_current_payroll = round(total_current_payroll + total_raise_amount, 2)
    percent_increase = round((new_current_payroll - total_current_payroll)\
                            / total_current_payroll * 100, 2)


    print(" Total Amounts ".center(50, "-"))
    print(f"Total bonus amount for all employees = ${total_bonus_amount:,.2f}")
    print(f"Total raise amount for all employees = ${total_raise_amount:,.2f}")
    print(f"Total payroll for previous year = ${total_current_payroll:,.2f}")
    print(f"Total payroll after raises = ${new_current_payroll:,.2f}")
    print(f"Total percent increase in payroll = {percent_increase}%")

    print("\n")
    print("Updated Employee Payroll Amounts:")
    print(updated_employee_payroll)


def calculate_bcbs_deductions(selected_employee="All employees"):
    """Print weekly BCBS deductions for the selected employee or all employees."""
    for details in get_selected_current_year_details(selected_employee):
        employee = Employee(**details)
        employee.calculate_weekly_bcbs_deduction()


def create_gui():
    """Create and run the Tkinter employee benefits calculator window."""
    window = tk.Tk()
    window.title("Employee Benefits Calculator")
    window.geometry("720x900")
    window.minsize(560, 400)

    calculation_options = {
        "BCBS weekly deductions": calculate_bcbs_deductions,
        "Raises and bonuses": calculate_raises_and_bonuses,
        "Employee history": employee_history_report,
        "Salary by year line chart": salary_totals_by_year,
    }
    selected_calculation = tk.StringVar(value="Raises and bonuses")
    selected_employee = tk.StringVar(value="All employees")
    employee_names = get_employee_names()

    main_frame = ttk.Frame(window, padding=16)
    main_frame.pack(fill=tk.BOTH, expand=True)

    ttk.Label(main_frame, text="Calculation").pack(anchor=tk.W)
    calculation_menu = ttk.Combobox(
        main_frame,
        textvariable=selected_calculation,
        values=list(calculation_options),
        state="readonly",
    )
    calculation_menu.pack(fill=tk.X, pady=(4, 12))

    ttk.Label(main_frame, text="Employee filter").pack(anchor=tk.W)
    employee_menu = ttk.Combobox(
        main_frame,
        textvariable=selected_employee,
        values=["All employees"] + employee_names,
        state="normal",
    )
    employee_menu.pack(fill=tk.X, pady=(4, 12))

    def filter_employee_menu(_event=None):
        """Filter employee combobox choices using the text currently entered."""
        typed_name = selected_employee.get().strip().lower()
        matching_names = [
            name for name in employee_names
            if typed_name in name.lower()
        ]
        employee_menu["values"] = ["All employees"] + matching_names
        if typed_name and matching_names:
            employee_menu.event_generate("<Down>")

    employee_menu.bind("<KeyRelease>", filter_employee_menu)

    chart = tk.Canvas(main_frame, height=220, background="white",
                      highlightthickness=1, highlightbackground="#cccccc")
    chart.pack(fill=tk.X, pady=(0, 12))

    output = tk.Text(main_frame, height=20, font=("Times New Roman", 14), 
                     wrap=tk.WORD, state=tk.DISABLED)
    output.pack(fill=tk.BOTH, expand=True)

    def calculate_selected():
        """Run the selected calculation and display its captured output."""
        output.configure(state=tk.NORMAL)
        output.delete("1.0", tk.END)
        chart.delete("all")
        try:
            report = io.StringIO()
            with redirect_stdout(report):
                if selected_calculation.get() == "Salary by year line chart":
                    salary_totals = salary_totals_by_year(selected_employee.get())
                else:
                    calculation_options[selected_calculation.get()](
                        selected_employee.get()
                    )
            if selected_calculation.get() == "Salary by year line chart":
                draw_salary_chart(chart, salary_totals)
                output.insert(tk.END, "Total salary by year:\n")
                for year, total in salary_totals.items():
                    output.insert(tk.END, f"{year}: ${total:,.2f}\n")
            else:
                output.insert(tk.END, report.getvalue())
        except (KeyError, OSError, TypeError, ValueError) as error:
            messagebox.showerror("Calculation error", str(error), parent=window)
        finally:
            output.configure(state=tk.DISABLED)

    ttk.Button(main_frame, text="Calculate", command=calculate_selected).pack(
        anchor=tk.E, pady=(12, 0)
    )
    window.mainloop()


def draw_salary_chart(chart, salary_totals):
    """Draw total salary values by year on the supplied Tkinter canvas."""
    chart.update_idletasks()
    chart_width = max(chart.winfo_width(), 560)
    chart_height = max(chart.winfo_height(), 220)
    left, right, top, bottom = 60, 20, 20, 35
    values = list(salary_totals.values())
    maximum = max(values) if values else 1
    minimum = min(values) if values else 0
    value_range = maximum - minimum or 1
    points = []

    chart.create_text(left, 8, anchor=tk.W, text="Total salary")
    for index, (year, total) in enumerate(salary_totals.items()):
        x = left + index * (chart_width - left - right) / max(len(values) - 1, 1)
        y = top + (maximum - total) / value_range * (chart_height - top - bottom)
        points.append((x, y))
        chart.create_text(x, chart_height - bottom + 15, text=year)
        chart.create_text(x, y - 10, text=f"${total:,.0f}")

    if len(points) > 1:
        chart.create_line(points, fill="#1f6aa5", width=3, smooth=True)
    for x, y in points:
        chart.create_oval(x - 4, y - 4, x + 4, y + 4, fill="#d95f02",
                          outline="#d95f02")


if __name__ == "__main__":
    create_gui()
