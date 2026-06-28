from datetime import date

year = int(input("Enter Year of Birth: "))
month = int(input("Enter Month of Birth: "))
day = int(input("Enter Day: "))

today = date.today()

age_year = today.year - year
age_month = today.month - month
age_day = today.day - day

if age_month <0:
    age_month += 12
    age_year -= 1

if age_day <0:
    age_day += 30
    age_month -= 1

print("You are",age_year,"years,",age_month,"months and",age_day,"days old.")
