# events['vozrast'] = events.apply(lambda row: row['vozrast']%5, axis =1)
import re
import pandas as pd
import time


def to_month(string: str) -> str:
    # print(string)
    # time.sleep(0.5)
    string = str(string)
    years, months = 0, 0
    match_years  = re.search(r'\d+\s+(год(a)?|лет)', string.strip())
    years_str = match_years.group(0) if match_years is not None else None
    if years_str is not None:
        years = int(re.search(r'\d+',years_str).group(0))
    else:
        years = 0
    match_months  = re.search(r'\s*\d+\s+месяц(ев)?', string.strip())
    months_str = match_months.group(0) if match_months is not None else None
    if months_str is not None:
        months = int(re.search(r'\d+',months_str).group(0))
    else:
        months = 0
    if string is None or len(string) == 0 or string == 'nan':
        return ''
    else:
        return str(int(years*12 + months))


events = pd.read_csv("C:/Users/Тимофей/Desktop/Деловая среда - тестовое задание/события.csv")
events['stazh_na_poslednem_meste_raboty'] = events.apply(lambda row: to_month(row['stazh_na_poslednem_meste_raboty']), axis=1)
# events['stazh_na_poslednem_meste_raboty'] = pd.to_numeric(events['stazh_na_poslednem_meste_raboty'], downcast='integer')
events.to_csv("C:/Users/Тимофей/Desktop/Деловая среда - тестовое задание/events_1.csv",na_rep='', index=False,float_format="%.0f")