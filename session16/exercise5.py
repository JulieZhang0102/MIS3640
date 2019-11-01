from datetime import date
import datetime

today = date.today()

weekDays = ("Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday")
week_day_number = today.weekday()
weekday = weekDays[week_day_number]

print("Today's date: {}, {}".format(today,weekday))

def birthday_calculate(birthday):
    '''
    Enter your birthday in YYYY-MM-DD format
    Function will return your age and days, hours, minutes and seconds until your next birthday
    '''
    year, month, day = map(int, birthday.split('-'))
    birthday_date = datetime.date(year, month, day)
    today = date.today()
    age = today.year - birthday_date.year
    if today.month > birthday_date.month:
        today = datetime.datetime.now()
        next_birthday = datetime.datetime(today.year+1, month, day, 00, 00, 00)
        diff = next_birthday - today
    elif today.month == birthday_date.month and today.day > birthday_date.day:
        today = datetime.datetime.now()
        next_birthday = datetime.datetime(today.year+1, month, day, 00, 00, 00)
        diff = next_birthday - today
    elif today.month == birthday_date.month and today.day == birthday_date.day:
        diff = "no days left. It is today!"
    elif today.month == birthday_date.month and today.day < birthday_date.day:
        today = datetime.datetime.now()
        next_birthday = datetime.datetime(today.year, month, day, 00, 00, 00)
        diff = next_birthday - today
        age -= 1
    else:
        today = datetime.datetime.now()
        next_birthday = datetime.datetime(today.year, month, day, 00, 00, 00)
        diff = next_birthday - today
        age -= 1
    print('Your age is :', age)
    print('Until your next birthday, there are {}.'.format(diff))


birthday_calculate('1999-01-02')

def find_double_day(bday1, bday2):
    """
    bday1 is the older person.
    Enter birthday in YYYY-MM-DD format
    """
    year1, month1, day1 = map(int, bday1.split('-'))
    bday1_date = datetime.date(year1, month1, day1)
    year2, month2, day2 = map(int, bday2.split('-'))
    bday2_date = datetime.date(year2, month2, day2)

    diff = bday2_date - bday1_date

    p1 = int(diff.days)
    p2 = 0

    while p2 * 2 != p1:
        p1 += 1
        p2 += 1
    
    double_day = bday2_date + datetime.timedelta(days=p2)
    print('The double day is {}.'.format(double_day))


find_double_day('1999-01-02', '2001-01-13')

def find_n_times_day(bday1, bday2, n):
    """
    bday1 is the older person.
    Enter birthday in YYYY-MM-DD format
    """
    year1, month1, day1 = map(int, bday1.split('-'))
    bday1_date = datetime.date(year1, month1, day1)
    year2, month2, day2 = map(int, bday2.split('-'))
    bday2_date = datetime.date(year2, month2, day2)

    diff = bday2_date - bday1_date

    p1 = int(diff.days)
    p2 = 0

    while p2 * n != p1:
        if p2 * n > p1:
            print('This will never occurr')
            return None
        p1 += 1
        p2 += 1
    
    n_times_day = bday2_date + datetime.timedelta(days=p2)
    print('The {} times day is {}.'.format(n, n_times_day))

find_n_times_day('1999-01-02', '2001-01-13', 3)
