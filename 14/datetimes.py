"""
106: Python Datetime Module
"""
from datetime import time, date, datetime

if __name__ == "__main__":
    mytime = time(1, 2, 3, 4)
    print(mytime)
    today = date.today()
    print(today)
    print(today.ctime())
    mydatetime = datetime(2021, 1, 2, 3, 4, 5, 6)
    mydatetime = mydatetime.replace(year=2022)
    print(mydatetime)
    date1 = date(2021, 2, 3)
    date2 = date(2022, 3, 4)
    result = date2 - date1
    print(result)
