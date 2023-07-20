
import time


def days_between_dates(dt1, dt2):
    date_format = "%d/%m/%Y"
    a = time.mktime(time.strptime(dt1, date_format))
    b = time.mktime(time.strptime(dt2, date_format))
    delta = b - a
    day_num=delta/86400
    year_num=day_num//365
    count_months=(day_num-(year_num*365))//30.417
    days=(day_num-((year_num*365)+year_num//4)-(count_months*30.417))
    print(f"You are {int(year_num)} years, {int(count_months)} months and {int(days)} days old")
    print(f"Or {int(day_num//30.417)} months and {int(days)} days old")
    print(f"Or {int(day_num)} days old")



print("Format should be dd/mm/yyyy, Ex - 26/07/2023")
date1=input("Enter Birth date : ")
date2=input("Enter calculation date : ")
days_between_dates(date1,date2)