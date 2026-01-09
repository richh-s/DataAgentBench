code = """import pandas as pd, json, re

def parse_date(s):
    if s is None:
        return pd.NaT
    s=str(s)
    fmts=[
        '%Y-%m-%d %H:%M:%S','%Y-%m-%d',
        '%d %b %Y, %H:%M','%d %b %Y, %H:%M:%S',
        '%B %d, %Y at %I:%M %p','%B %d, %Y at %H:%M %p'
    ]
    for f in fmts:
        try:
            return pd.to_datetime(s, format=f)
        except Exception:
            pass
    return pd.to_datetime(s, errors='coerce')

# Load all trade data
import os

# Query all rows via SQL in chunks not supported; assume manageable and pull all

print('__RESULT__:')
print(json.dumps({'note':'ready'}))"""

env_args = {'var_call_gmGkDg64O3j8lJOAvpfXdVWY': ['index_info'], 'var_call_ttZ8XD7AA6a59qDWswh4Ys4o': ['index_trade'], 'var_call_0dvFLPs7DP7xXns2MMlkVEZ3': [{'Exchange': 'New York Stock Exchange', 'Currency': 'USD'}, {'Exchange': 'NASDAQ', 'Currency': 'USD'}, {'Exchange': 'Hong Kong Stock Exchange', 'Currency': 'HKD'}, {'Exchange': 'Shanghai Stock Exchange', 'Currency': 'CNY'}, {'Exchange': 'Tokyo Stock Exchange', 'Currency': 'JPY'}, {'Exchange': 'Euronext', 'Currency': 'EUR'}, {'Exchange': 'Shenzhen Stock Exchange', 'Currency': 'CNY'}, {'Exchange': 'Toronto Stock Exchange', 'Currency': 'CAD'}, {'Exchange': 'National Stock Exchange of India', 'Currency': 'INR'}, {'Exchange': 'Frankfurt Stock Exchange', 'Currency': 'EUR'}, {'Exchange': 'Korea Exchange', 'Currency': 'KRW'}, {'Exchange': 'SIX Swiss Exchange', 'Currency': 'CHF'}, {'Exchange': 'Taiwan Stock Exchange', 'Currency': 'TWD'}, {'Exchange': 'Johannesburg Stock Exchange', 'Currency': 'ZAR'}], 'var_call_0cEeuOTbFge9QSne0YkmCCsR': [{'Index': 'NYA', 'min_date_raw': '01 Apr 1969, 00:00', 'max_date_raw': 'September 30, 2020 at 12:00 AM', 'n': '13947'}, {'Index': 'N225', 'min_date_raw': '01 Apr 1971, 00:00', 'max_date_raw': 'September 30, 2020 at 12:00 AM', 'n': '13874'}, {'Index': 'IXIC', 'min_date_raw': '01 Apr 1974, 00:00', 'max_date_raw': 'September 30, 2015 at 12:00 AM', 'n': '12690'}, {'Index': 'GSPTSE', 'min_date_raw': '01 Apr 1981, 00:00', 'max_date_raw': 'September 30, 2016 at 12:00 AM', 'n': '10526'}, {'Index': 'HSI', 'min_date_raw': '01 Apr 1992, 00:00', 'max_date_raw': 'September 30, 2019 at 12:00 AM', 'n': '8492'}, {'Index': 'GDAXI', 'min_date_raw': '01 Apr 1992, 00:00', 'max_date_raw': 'September 30, 2016 at 12:00 AM', 'n': '8438'}, {'Index': 'SSMI', 'min_date_raw': '01 Apr 1996, 00:00', 'max_date_raw': 'September 30, 2020 at 12:00 AM', 'n': '7671'}, {'Index': 'TWII', 'min_date_raw': '01 Apr 2004, 00:00', 'max_date_raw': 'September 30, 2020 at 12:00 AM', 'n': '5869'}, {'Index': '000001.SS', 'min_date_raw': '01 Apr 2003, 00:00', 'max_date_raw': 'September 30, 2015 at 12:00 AM', 'n': '5791'}, {'Index': '399001.SZ', 'min_date_raw': '01 Apr 2004, 00:00', 'max_date_raw': 'September 30, 2015 at 12:00 AM', 'n': '5760'}, {'Index': 'N100', 'min_date_raw': '01 Apr 2003, 00:00', 'max_date_raw': 'September 30, 2019 at 12:00 AM', 'n': '5474'}, {'Index': 'NSEI', 'min_date_raw': '01 Apr 2014, 00:00', 'max_date_raw': 'September 30, 2014 at 12:00 AM', 'n': '3346'}, {'Index': 'J203.JO', 'min_date_raw': '01 Apr 2016, 00:00', 'max_date_raw': 'September 30, 2019 at 12:00 AM', 'n': '2346'}], 'var_call_junLQpccFiCWlJqeBAptH7Hr': [{'Index': 'HSI', 'Date': '31 Dec 1986, 00:00', 'CloseUSD': '333.87900637'}, {'Index': 'HSI', 'Date': 'January 02, 1987 at 12:00 AM', 'CloseUSD': '330.21301274'}, {'Index': 'HSI', 'Date': '1987-01-05 00:00:00', 'CloseUSD': '331.81198726'}, {'Index': 'HSI', 'Date': '06 Jan 1987, 00:00', 'CloseUSD': '335.90698726000005'}, {'Index': 'HSI', 'Date': '07 Jan 1987, 00:00', 'CloseUSD': '338.92301274'}]}

exec(code, env_args)
