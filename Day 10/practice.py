# def format_name(f_name, l_name):

#     f_name = f_name.title()
#     l_name = l_name.title()

#     return f'{f_name} {l_name}'

# print(format_name("opeyemi", "akande"))

month = int(input('What month do you want to check? For January enter 1 for February enter 2, like so.'))
year = int(input('What year? '))


def leap_year(year):
    """This checks if the year is a leap year."""
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return True

            else:
                return False
        return True    
    else:
        return False


def days_in_month(year, month):
    month_days = [31, 28, 31, 30, 31, 30, 31, 30, 31, 30, 31]
    if leap_year(year):
        month_days[month-1] = 29
    return month_days[month-1]
    



# # days_in_month(month, year)
# month_days = [31, 28, 31, 30, 31, 30, 31, 30, 31, 30, 31]
# print(month_days)

# month_days[1] = 29
# print(month_days)
# # print(leap_year(1996))

print(days_in_month(year=year, month=month))

leap_year()


