code = """import json, pandas as pd
from datetime import datetime

# load full sample file (but we'll query full year per index directly to reduce)

# Query all rows for 2018 for NA indices via DuckDB is hard due to date parsing; we'll pull all rows for each index and parse in python.

import duckdb

# Instead, fetch needed columns for three indices only (all history) from tool storage file is only NYA sample.

# We'll directly query DB for these indices without date filter, then filter in python."""

env_args = {'var_call_aRdqmsXiMaoxxSyoua3YCSzS': ['index_info'], 'var_call_PXRgAraG2sbzukr4Gn1TkBvX': ['index_trade'], 'var_call_FifB7Eicgmi4hQh1gfqRTO0K': [{'Exchange': 'New York Stock Exchange'}, {'Exchange': 'NASDAQ'}, {'Exchange': 'Hong Kong Stock Exchange'}, {'Exchange': 'Shanghai Stock Exchange'}, {'Exchange': 'Tokyo Stock Exchange'}, {'Exchange': 'Euronext'}, {'Exchange': 'Shenzhen Stock Exchange'}, {'Exchange': 'Toronto Stock Exchange'}, {'Exchange': 'National Stock Exchange of India'}, {'Exchange': 'Frankfurt Stock Exchange'}, {'Exchange': 'Korea Exchange'}, {'Exchange': 'SIX Swiss Exchange'}, {'Exchange': 'Taiwan Stock Exchange'}, {'Exchange': 'Johannesburg Stock Exchange'}], 'var_call_MOmm8MZZ8YGVXPyiCU0oXtsx': [{'Index': 'J203.JO'}, {'Index': 'N225'}, {'Index': 'GSPTSE'}, {'Index': 'NSEI'}, {'Index': 'GDAXI'}, {'Index': 'IXIC'}, {'Index': 'HSI'}, {'Index': '000001.SS'}, {'Index': 'SSMI'}, {'Index': 'TWII'}, {'Index': 'N100'}, {'Index': '399001.SZ'}, {'Index': 'NYA'}], 'var_call_2W0xmcDC3rSrdRrW7O1qP0P6': [{'Date': '31 Dec 1986, 00:00'}, {'Date': 'January 02, 1987 at 12:00 AM'}, {'Date': '1987-01-05 00:00:00'}, {'Date': '06 Jan 1987, 00:00'}, {'Date': '07 Jan 1987, 00:00'}], 'var_call_CCv7Ud5ajr5uuBfGJ7DLPAUj': 'file_storage/call_CCv7Ud5ajr5uuBfGJ7DLPAUj.json'}

exec(code, env_args)
