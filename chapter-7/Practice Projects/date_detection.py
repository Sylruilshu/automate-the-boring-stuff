import re, sys


def detect_leap_year(year: str) -> bool:
    if int(year) % 4 == 0:
        if int(year) % 100 == 0 and int(year) % 400 == 0:
            return True
        elif int(year) % 100 == 0:
            return False
        else:
            return True
    return False


# 1. TODO: Detect dates in DD/MM/YYYY format using Regex.
date_detector = re.compile(
    r"""
    (\d{1,2})       # Day (DD)    
    /               # Forward Slash       
    (\d{1,2})       # Month (MM)
    /               # Forward Slash
    (\d{4})         # Year (YYYY)
    """,
    re.VERBOSE,
)


# 2. TODO: Store varirables into strings named day, month && year.
match_object = date_detector.search("Todays date is: 34/03/2005")

day = match_object.group(1)
month = match_object.group(2)
year = match_object.group(3)

if day in ["1", "2", "3", "4", "5", "6", "7", "8", "9"]:
    day = "0" + day

if month in ["1", "2", "3", "4", "5", "6", "7", "8", "9"]:
    month = "0" + month


# 3. TODO: Detect if the date is valid.
max_days_to_month = {
    28: ["02"],
    29: ["02"],
    30: ["04", "06", "09", "11"],
    31: ["01", "03", "05", "07", "08", "10", "12"],
}

if month in max_days_to_month[30]:
    if day > "30" or day < "1":
        print("Invalid date: That month has 30 days not " + day)
        sys.exit(1)


if month in max_days_to_month[31]:
    if day > "31" or day < "1":
        print("Invalid date: That month has 31 days not " + day)
        sys.exit(1)


# 4. TODO: detect leap years
if detect_leap_year(year):
    if day > "29" and month in max_days_to_month[29]:
        print("Invalid date: there is only 29 days in Feb if its a leap year.")
        sys.exit(1)

if not detect_leap_year(year):
    if day > "28" and month in max_days_to_month[28]:
        print("Invalid date: there is only 28 days in Feb if its not a leap year.")
        sys.exit(1)
