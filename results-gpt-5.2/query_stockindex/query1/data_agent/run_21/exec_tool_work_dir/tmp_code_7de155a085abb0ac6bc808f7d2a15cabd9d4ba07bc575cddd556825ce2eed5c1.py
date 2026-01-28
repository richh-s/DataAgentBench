code = """import pandas as pd, json, re
from datetime import datetime

def parse_date(s):
    if s is None:
        return None
    fmts = [
        '%d %b %Y, %H:%M',
        '%B %d, %Y at %I:%M %p',
        '%b %d, %Y at %I:%M %p',
        '%Y-%m-%d'
    ]
    for f in fmts:
        try:
            return datetime.strptime(s, f)
        except Exception:
            pass
    return None

# pull all rows for indices that have any data from 2020 onward after parsing
# We'll load full table via duckdb query with minimal columns
print('__RESULT__:')
print(json.dumps({'status':'need_query'}))"""

env_args = {'var_call_hvqcYoyLM8UqyjCb2USQjDNU': ['index_info'], 'var_call_gzFCtXNROBaNJit1QRl76hah': ['index_trade'], 'var_call_e4EjPLdsv064OsmkGsIgLQvn': [{'Index': 'NYA', 'n_rows': '13947', 'min_date': '01 Apr 1969, 00:00', 'max_date': 'September 30, 2020 at 12:00 AM'}, {'Index': 'N225', 'n_rows': '13874', 'min_date': '01 Apr 1971, 00:00', 'max_date': 'September 30, 2020 at 12:00 AM'}, {'Index': 'IXIC', 'n_rows': '12690', 'min_date': '01 Apr 1974, 00:00', 'max_date': 'September 30, 2015 at 12:00 AM'}, {'Index': 'GSPTSE', 'n_rows': '10526', 'min_date': '01 Apr 1981, 00:00', 'max_date': 'September 30, 2016 at 12:00 AM'}, {'Index': 'HSI', 'n_rows': '8492', 'min_date': '01 Apr 1992, 00:00', 'max_date': 'September 30, 2019 at 12:00 AM'}, {'Index': 'GDAXI', 'n_rows': '8438', 'min_date': '01 Apr 1992, 00:00', 'max_date': 'September 30, 2016 at 12:00 AM'}, {'Index': 'SSMI', 'n_rows': '7671', 'min_date': '01 Apr 1996, 00:00', 'max_date': 'September 30, 2020 at 12:00 AM'}, {'Index': 'TWII', 'n_rows': '5869', 'min_date': '01 Apr 2004, 00:00', 'max_date': 'September 30, 2020 at 12:00 AM'}, {'Index': '000001.SS', 'n_rows': '5791', 'min_date': '01 Apr 2003, 00:00', 'max_date': 'September 30, 2015 at 12:00 AM'}, {'Index': '399001.SZ', 'n_rows': '5760', 'min_date': '01 Apr 2004, 00:00', 'max_date': 'September 30, 2015 at 12:00 AM'}, {'Index': 'N100', 'n_rows': '5474', 'min_date': '01 Apr 2003, 00:00', 'max_date': 'September 30, 2019 at 12:00 AM'}, {'Index': 'NSEI', 'n_rows': '3346', 'min_date': '01 Apr 2014, 00:00', 'max_date': 'September 30, 2014 at 12:00 AM'}, {'Index': 'J203.JO', 'n_rows': '2346', 'min_date': '01 Apr 2016, 00:00', 'max_date': 'September 30, 2019 at 12:00 AM'}], 'var_call_Z0yCWTHmhTAgUp3ARY6FXTLd': [{'Index': '000001.SS', 'Date': 'September 30, 2015 at 12:00 AM', 'Open': '3052.841064', 'High': '3073.300049', 'Low': '3039.741943', 'Close': '3052.781006'}, {'Index': '000001.SS', 'Date': 'September 30, 2014 at 12:00 AM', 'Open': '2361.318115', 'High': '2365.490967', 'Low': '2354.268066', 'Close': '2363.870117'}, {'Index': '000001.SS', 'Date': 'September 30, 2011 at 12:00 AM', 'Open': '2368.397949', 'High': '2377.541992', 'Low': '2348.217041', 'Close': '2359.218994'}, {'Index': '000001.SS', 'Date': 'September 30, 2009 at 12:00 AM', 'Open': '2772.569092', 'High': '2803.85791', 'Low': '2763.711914', 'Close': '2779.426025'}, {'Index': '000001.SS', 'Date': 'September 30, 1997 at 12:00 AM', 'Open': '1083.41394', 'High': '1100.385986', 'Low': '1083.232056', 'Close': '1097.383057'}], 'var_call_MT82qW69Us75ykFIjoklIhbo': [{'Index': 'HSI', 'Date': '31 Dec 1986, 00:00', 'Open': '2568.300049', 'High': '2568.300049', 'Low': '2568.300049', 'Close': '2568.300049'}, {'Index': 'HSI', 'Date': 'January 02, 1987 at 12:00 AM', 'Open': '2540.100098', 'High': '2540.100098', 'Low': '2540.100098', 'Close': '2540.100098'}, {'Index': 'HSI', 'Date': 'January 15, 1987 at 12:00 AM', 'Open': '2559.100098', 'High': '2559.100098', 'Low': '2559.100098', 'Close': '2559.100098'}, {'Index': 'HSI', 'Date': 'January 16, 1987 at 12:00 AM', 'Open': '2542.600098', 'High': '2542.600098', 'Low': '2542.600098', 'Close': '2542.600098'}, {'Index': 'HSI', 'Date': 'January 19, 1987 at 12:00 AM', 'Open': '2460.5', 'High': '2460.5', 'Low': '2460.5', 'Close': '2460.5'}]}

exec(code, env_args)
