def main():
    """
    Main function that caluclate all Pythagore dates between two years (here between 2000 and 2100)

    Params: /
    """
    for y in range(10,3000):
        for m in range(1,13):
            dTotal = month_length(m,y)
            for d in range(1,dTotal+1):
                if is_pythagore(d,m,y):
                    print(str(d)+"/"+str(m)+"/"+str(y)+" est une date pythagore")

def is_pythagore(day,month,year):
    """
    Return True if a date is Pyhtagore, False otherwise

    Params:

        day (int) - the day of the date
        month (int) - the month of the date
        year (int) - the year of the date

    Examples:

    >>> is_pythagore(16,12,2020)
    True
    >>> is_pythagore(17,12,2020)
    False
    >>> is_pythagore(24,7,2025)
    True
    """
    year=str(year)[-2:] # Recover the 2 last number of the year
    if ((day**2 + month**2) == int(year)**2) :
        return True
    return False

def month_length(month,year):
    """
    Return the number of day in a month

    Params:

        month (int) - the month number
        year (int) - the year in YYYY format

    Examples:

    >>> month_length(12,2020)
    31
    >>> month_length(3,2009)
    30
    >>> month_length(2,2020)
    29
    >>> month_length(2,2021)
    28
    
    """
    if month in (1,3,5,7,8,10,12):
        return 31
    elif month == 2 :
        if is_bissextile(year):
            return 29
        else:
            return 28
    else:
        return 30

def is_bissextile(year):
    """
    Return True if a year is bissextile, False otherwise

    Params:

        year (int) - the year in YYYY format

    Examples:

    >>> is_bissextile(2017)
    False
    >>> is_bissextile(2020)
    True
    >>> is_bissextile(2022)
    False
    >>> is_bissextile(2024)
    True
    
    """
    if(year%4==0 and year%100!=0 or year%400==0):
        return True
    else:
        return False

if __name__ == "__main__":
    # execute only if run as a script
    main()
