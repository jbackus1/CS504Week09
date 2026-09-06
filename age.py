import datetime

def calculate_age(year, month, day):
    today = datetime.date.today()
    age = today.year - year
    # subtract a year if the birthday hasn't happened yet this year
    if (today.month, today.day) < (month, day):
        age -= 1
    return age

birth_year = 1990
birth_month = 6
birth_day = 8

age = calculate_age(birth_year, birth_month, birth_day)
print(f"Your age is: {age}")