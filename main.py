from application.salary import calculate_salary
from application.db.people import get_employees
import datetime
import art

def date_printer():
    date = datetime.datetime.now()
    return date.strftime("%Y-%m-%d %H:%M:%S")

def art_printer(art_name):
    return art.tprint(art_name)

if __name__ == '__main__':
    print(calculate_salary())
    print(get_employees())
    print(art_printer(date_printer()))
