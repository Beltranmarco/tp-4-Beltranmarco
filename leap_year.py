def leap_year():
        year = int(imput(""))

    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        print(f"El año {year} es biciesto")
    else:
        print(f"el año {year} no es biciesto")
