import re


def detect_leap_year(year: str) -> bool:
    if int(year) % 4 == 0:
        if int(year) % 100 == 0 and int(year) % 400 == 0:
            return "leap"
        elif int(year) % 100 == 0:
            return "regular"
        else:
            return "leap"
    return "regular"


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
match_object = date_detector.search("Todays date is: 29/02/2001")

day = match_object.group(1)
month = match_object.group(2)
year = match_object.group(3)

if day in ["1", "2", "3", "4", "5", "6", "7", "8", "9"]:
    day = "0" + day

if month in ["1", "2", "3", "4", "5", "6", "7", "8", "9"]:
    month = "0" + month


# 3. TODO: Detect if the date is valid.
month_to_max_days = {
    1: {"leap": 31, "regular": 31},
    2: {"leap": 29, "regular": 28},
    3: {"leap": 31, "regular": 31},
    4: {"leap": 30, "regular": 30},
    5: {"leap": 31, "regular": 31},
    6: {"leap": 30, "regular": 30},
    7: {"leap": 31, "regular": 31},
    8: {"leap": 31, "regular": 31},
    9: {"leap": 30, "regular": 30},
    10: {"leap": 31, "regular": 31},
    11: {"leap": 30, "regular": 30},
    12: {"leap": 31, "regular": 31},
}

is_leap_year = detect_leap_year(year)
if int(day) > month_to_max_days[int(month)][is_leap_year]:
    print("More days than there are valid days in that month.")
