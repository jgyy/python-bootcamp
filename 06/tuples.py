"""
46: Tuple unpacking with python functions
"""

def employee_check(work_hours):
    """
    function to check working hours
    """
    current_max = 0
    employee_of_month = ""
    for employee, hours in work_hours:
        if hours > current_max:
            current_max = hours
            employee_of_month = employee
        else:
            pass
    return (employee_of_month, current_max)


stock_prices = [("APPL", 200), ("GOOG", 400), ("MSFT", 100)]
for item in stock_prices:
    print(item)
for ticker, price in stock_prices:
    print(round(price * 1.1, 2))
work_hour = [("Abby", 100), ("Billy", 400), ("Cassie", 800)]
name, hour = employee_check(work_hour)
print(name, hour)
