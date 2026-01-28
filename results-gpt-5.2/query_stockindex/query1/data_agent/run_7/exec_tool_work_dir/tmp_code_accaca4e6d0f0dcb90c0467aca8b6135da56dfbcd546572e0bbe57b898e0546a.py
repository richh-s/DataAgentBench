code = """import json, pandas as pd

# Determine highest avg intraday volatility since 2020 for Asia indices
# Asia indices present: N225 (Japan), HSI (Hong Kong), 000001.SS (China), 399001.SZ (China), TWII (Taiwan), NSEI (India)

asia = ['N225','HSI','000001.SS','399001.SZ','TWII','NSEI']

# Load all rows for these indices from DuckDB via separate SQL with minimal columns
# (We can't call query_db here; so we rely on doing computation in SQL with robust date parsing; instead we will just output SQL to run)

result = {
  'needs_query': True,
  'asia_indices': asia,
  'note': 'Need robust date parsing in DuckDB for mixed formats like "01 Apr 1971, 00:00" and "January 02, 1987 at 12:00 AM".'
}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_call_I0W574xJ8uTD6mNfmTberHd2': ['index_info'], 'var_call_YbXfakKvSyJCV1JDa9ykFFep': ['index_trade'], 'var_call_5llvHIRBxEk4pQBLhGuQPHcW': [{'Index': 'J203.JO', 'n_rows': '2346', 'min_date': '01 Apr 2016, 00:00', 'max_date': 'September 30, 2019 at 12:00 AM'}, {'Index': 'N225', 'n_rows': '13874', 'min_date': '01 Apr 1971, 00:00', 'max_date': 'September 30, 2020 at 12:00 AM'}, {'Index': 'GSPTSE', 'n_rows': '10526', 'min_date': '01 Apr 1981, 00:00', 'max_date': 'September 30, 2016 at 12:00 AM'}, {'Index': 'NSEI', 'n_rows': '3346', 'min_date': '01 Apr 2014, 00:00', 'max_date': 'September 30, 2014 at 12:00 AM'}, {'Index': 'GDAXI', 'n_rows': '8438', 'min_date': '01 Apr 1992, 00:00', 'max_date': 'September 30, 2016 at 12:00 AM'}, {'Index': 'IXIC', 'n_rows': '12690', 'min_date': '01 Apr 1974, 00:00', 'max_date': 'September 30, 2015 at 12:00 AM'}, {'Index': 'HSI', 'n_rows': '8492', 'min_date': '01 Apr 1992, 00:00', 'max_date': 'September 30, 2019 at 12:00 AM'}, {'Index': 'NYA', 'n_rows': '13947', 'min_date': '01 Apr 1969, 00:00', 'max_date': 'September 30, 2020 at 12:00 AM'}, {'Index': '000001.SS', 'n_rows': '5791', 'min_date': '01 Apr 2003, 00:00', 'max_date': 'September 30, 2015 at 12:00 AM'}, {'Index': 'SSMI', 'n_rows': '7671', 'min_date': '01 Apr 1996, 00:00', 'max_date': 'September 30, 2020 at 12:00 AM'}, {'Index': 'TWII', 'n_rows': '5869', 'min_date': '01 Apr 2004, 00:00', 'max_date': 'September 30, 2020 at 12:00 AM'}, {'Index': 'N100', 'n_rows': '5474', 'min_date': '01 Apr 2003, 00:00', 'max_date': 'September 30, 2019 at 12:00 AM'}, {'Index': '399001.SZ', 'n_rows': '5760', 'min_date': '01 Apr 2004, 00:00', 'max_date': 'September 30, 2015 at 12:00 AM'}]}

exec(code, env_args)
