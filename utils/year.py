
from datetime import date, timedelta

import numpy as np


def get_year_array(year):
    week_arr = np.zeros((53, 7), dtype='datetime64[D]')
    week_arr[True] = None

    first_day_of_year = date(year, 1, 1)

    d = first_day_of_year

    days_to_first_sunday = (6-d.weekday()) % 7
    # get first week
    for _ in range(days_to_first_sunday):
        week_arr[0][d.weekday() + 1 if d.weekday() != 6 else 0] = d
        d += timedelta(days=1)

    
    week = 1
    # get other
    while d.year == year:
        for _ in range(7):
            week_arr[week][d.weekday() + 1 if d.weekday() != 6 else 0] = d
            d += timedelta(days=1)
        week = week + 1

    return week_arr

print(get_year_array(2019))