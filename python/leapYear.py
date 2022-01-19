def is_leap_year(n):
    '''
    Returns a boolean depending if year n is a leap year.
    '''
    if n % 400 == 0:
        return True
    elif n % 100 == 0:
        return False
    elif n % 4 == 0:
        return True
    else:
        return False

if __name__=="__main__":
    print(is_leap_year(1))
    print(is_leap_year(4))
    print(is_leap_year(100))
    print(is_leap_year(400))
