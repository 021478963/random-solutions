def day(d, m, y):
    k = y % 100
    if m == 1 or m == 2:
        m += 12
        k -= 1
    j = y // 100

    day = (d +(13 * (m + 1)) // 5 + k + k // 4 + j // 4 + 5 * j + 6) % 7
    days = ["sunday", "monday", "tuesday", "wednesday", "thursday", "friday", "saturday"]
    return days[day]


if __name__=="__main__":
    print(day(1, 1, 2216821))