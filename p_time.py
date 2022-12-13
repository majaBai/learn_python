from datetime import datetime, timedelta
import calendar
import time
from dateutil.relativedelta import relativedelta

def print_now_time():
    print(datetime.now())
    # print(datetime.now().time())

def trans_time_str(date_string):
    # 2020-02-25 16:20:00
    datetime_object = datetime.strptime(date_string, '%b %d %Y %I:%M%p')
    print(datetime_object)


def date_before_week(given_date):
    days_to_subtract = 7
    res_date = given_date - timedelta(days_to_subtract)
    print(res_date)

def date_to_str(give_date):
    # Tuesday 25 February 2020
    print(datetime.strftime(give_date, '%A %d %B %Y'))

def weekday_on(give_date):
    print(datetime.strftime(give_date, '%A'))
    # 整数
    indx = give_date.today().weekday()
    print(calendar.day_name[indx])

def add_7days_half(given_date):
    days_to_add = 7
    hours_to_add = 12
    res_date = given_date + timedelta(days = days_to_add, hours=hours_to_add)
    print(res_date)

def now_milliseconds():
    print(time.time())
    print(int(round(time.time() * 1000)))

def time_to_str(given_date):
    # "2020-02-25 00:00:00"
    print(datetime.strftime(given_date, '%Y-%m-%d %H:%M:%S'))
    print(datetime.strftime(given_date, '%Y-%m-%d'))
    print(datetime.strftime(given_date, '%Y'))

def future_4_month(given_date):
    months_to_add = 4
    res_date = given_date + relativedelta(months=+ months_to_add)
    print(res_date)

def days_bettwen(d1, d2):
    delta = abs(d1 - d2)
    print(delta.days)

def main():
    d = datetime(2020, 3, 22, 10, 0, 0)
    d2 = datetime(2020, 5, 22, 10, 0, 0)
    # print_now_time()
    # trans_time_str("Feb 25 2020 4:20PM")
    # date_before_week(datetime.now())
    # date_to_str(d)
    # weekday_on(d)
    # add_7days_half(d)
    # now_milliseconds()
    # time_to_str(d)
    # future_4_month(d.date())
    days_bettwen(d2, d)

main()
