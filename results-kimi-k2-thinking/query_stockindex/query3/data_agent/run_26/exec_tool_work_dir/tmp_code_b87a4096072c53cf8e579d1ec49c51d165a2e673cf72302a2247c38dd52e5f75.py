code = """import json
import pandas as pd
from datetime import datetime
import numpy as np
import re

# Load the index info data
index_info = locals()['var_functions.query_db:8']

# Create a mapping of index symbols to countries/regions based on the data we have
# This mapping is based on the index symbols and common knowledge
index_to_country = {
    '000001.SS': 'China',
    '399001.SZ': 'China',
    'GDAXI': 'Germany',
    'GSPTSE': 'Canada',
    'HSI': 'Hong Kong',
    'IXIC': 'USA',
    'J203.JO': 'South Africa',
    'N100': 'Netherlands',
    'N225': 'Japan',
    'NSEI': 'India',
    'NYA': 'USA',
    'SSMI': 'Switzerland',
    'TWII': 'Taiwan'
}

print('__RESULT__:')
print(json.dumps(index_to_country))"""

env_args = {'var_functions.list_db:0': ['index_info'], 'var_functions.query_db:2': [{'Exchange': 'New York Stock Exchange', 'Currency': 'USD'}, {'Exchange': 'NASDAQ', 'Currency': 'USD'}, {'Exchange': 'Hong Kong Stock Exchange', 'Currency': 'HKD'}, {'Exchange': 'Shanghai Stock Exchange', 'Currency': 'CNY'}, {'Exchange': 'Tokyo Stock Exchange', 'Currency': 'JPY'}, {'Exchange': 'Euronext', 'Currency': 'EUR'}, {'Exchange': 'Shenzhen Stock Exchange', 'Currency': 'CNY'}, {'Exchange': 'Toronto Stock Exchange', 'Currency': 'CAD'}, {'Exchange': 'National Stock Exchange of India', 'Currency': 'INR'}, {'Exchange': 'Frankfurt Stock Exchange', 'Currency': 'EUR'}], 'var_functions.query_db:3': [{'Index': 'HSI', 'Date': '31 Dec 1986, 00:00', 'Open': '2568.300049', 'High': '2568.300049', 'Low': '2568.300049', 'Close': '2568.300049', 'Adj Close': '2568.300049', 'CloseUSD': '333.87900637'}, {'Index': 'HSI', 'Date': 'January 02, 1987 at 12:00 AM', 'Open': '2540.100098', 'High': '2540.100098', 'Low': '2540.100098', 'Close': '2540.100098', 'Adj Close': '2540.100098', 'CloseUSD': '330.21301274'}, {'Index': 'HSI', 'Date': '1987-01-05 00:00:00', 'Open': '2552.399902', 'High': '2552.399902', 'Low': '2552.399902', 'Close': '2552.399902', 'Adj Close': '2552.399902', 'CloseUSD': '331.81198726'}, {'Index': 'HSI', 'Date': '06 Jan 1987, 00:00', 'Open': '2583.899902', 'High': '2583.899902', 'Low': '2583.899902', 'Close': '2583.899902', 'Adj Close': '2583.899902', 'CloseUSD': '335.90698726000005'}, {'Index': 'HSI', 'Date': '07 Jan 1987, 00:00', 'Open': '2607.100098', 'High': '2607.100098', 'Low': '2607.100098', 'Close': '2607.100098', 'Adj Close': '2607.100098', 'CloseUSD': '338.92301274'}, {'Index': 'HSI', 'Date': '1987-01-08 00:00:00', 'Open': '2603.300049', 'High': '2603.300049', 'Low': '2603.300049', 'Close': '2603.300049', 'Adj Close': '2603.300049', 'CloseUSD': '338.42900637'}, {'Index': 'HSI', 'Date': '1987-01-09 00:00:00', 'Open': '2561.699951', 'High': '2561.699951', 'Low': '2561.699951', 'Close': '2561.699951', 'Adj Close': '2561.699951', 'CloseUSD': '333.02099363'}, {'Index': 'HSI', 'Date': '1987-01-12 00:00:00', 'Open': '2614.899902', 'High': '2614.899902', 'Low': '2614.899902', 'Close': '2614.899902', 'Adj Close': '2614.899902', 'CloseUSD': '339.93698726'}, {'Index': 'HSI', 'Date': '1987-01-13 00:00:00', 'Open': '2590.800049', 'High': '2590.800049', 'Low': '2590.800049', 'Close': '2590.800049', 'Adj Close': '2590.800049', 'CloseUSD': '336.80400637'}, {'Index': 'HSI', 'Date': '1987-01-14 00:00:00', 'Open': '2578.199951', 'High': '2578.199951', 'Low': '2578.199951', 'Close': '2578.199951', 'Adj Close': '2578.199951', 'CloseUSD': '335.16599363'}], 'var_functions.query_db:4': [{'Index': '000001.SS'}, {'Index': '399001.SZ'}, {'Index': 'GDAXI'}, {'Index': 'GSPTSE'}, {'Index': 'HSI'}, {'Index': 'IXIC'}, {'Index': 'J203.JO'}, {'Index': 'N100'}, {'Index': 'N225'}, {'Index': 'NSEI'}, {'Index': 'NYA'}, {'Index': 'SSMI'}, {'Index': 'TWII'}], 'var_functions.query_db:8': [{'Exchange': 'New York Stock Exchange', 'Currency': 'USD'}, {'Exchange': 'NASDAQ', 'Currency': 'USD'}, {'Exchange': 'Hong Kong Stock Exchange', 'Currency': 'HKD'}, {'Exchange': 'Shanghai Stock Exchange', 'Currency': 'CNY'}, {'Exchange': 'Tokyo Stock Exchange', 'Currency': 'JPY'}, {'Exchange': 'Euronext', 'Currency': 'EUR'}, {'Exchange': 'Shenzhen Stock Exchange', 'Currency': 'CNY'}, {'Exchange': 'Toronto Stock Exchange', 'Currency': 'CAD'}, {'Exchange': 'National Stock Exchange of India', 'Currency': 'INR'}, {'Exchange': 'Frankfurt Stock Exchange', 'Currency': 'EUR'}, {'Exchange': 'Korea Exchange', 'Currency': 'KRW'}, {'Exchange': 'SIX Swiss Exchange', 'Currency': 'CHF'}, {'Exchange': 'Taiwan Stock Exchange', 'Currency': 'TWD'}, {'Exchange': 'Johannesburg Stock Exchange', 'Currency': 'ZAR'}], 'var_functions.query_db:9': [{'min(Date)': '01 Apr 1969, 00:00', 'max(Date)': 'September 30, 2020 at 12:00 AM'}], 'var_functions.query_db:12': [{'Index': '000001.SS', 'earliest_date': '01 Apr 2003, 00:00', 'latest_date': 'September 30, 2015 at 12:00 AM', 'total_records': '5791'}, {'Index': '399001.SZ', 'earliest_date': '01 Apr 2004, 00:00', 'latest_date': 'September 30, 2015 at 12:00 AM', 'total_records': '5760'}, {'Index': 'GDAXI', 'earliest_date': '01 Apr 1992, 00:00', 'latest_date': 'September 30, 2016 at 12:00 AM', 'total_records': '8438'}, {'Index': 'GSPTSE', 'earliest_date': '01 Apr 1981, 00:00', 'latest_date': 'September 30, 2016 at 12:00 AM', 'total_records': '10526'}, {'Index': 'HSI', 'earliest_date': '01 Apr 1992, 00:00', 'latest_date': 'September 30, 2019 at 12:00 AM', 'total_records': '8492'}, {'Index': 'IXIC', 'earliest_date': '01 Apr 1974, 00:00', 'latest_date': 'September 30, 2015 at 12:00 AM', 'total_records': '12690'}, {'Index': 'J203.JO', 'earliest_date': '01 Apr 2016, 00:00', 'latest_date': 'September 30, 2019 at 12:00 AM', 'total_records': '2346'}, {'Index': 'N100', 'earliest_date': '01 Apr 2003, 00:00', 'latest_date': 'September 30, 2019 at 12:00 AM', 'total_records': '5474'}, {'Index': 'N225', 'earliest_date': '01 Apr 1971, 00:00', 'latest_date': 'September 30, 2020 at 12:00 AM', 'total_records': '13874'}, {'Index': 'NSEI', 'earliest_date': '01 Apr 2014, 00:00', 'latest_date': 'September 30, 2014 at 12:00 AM', 'total_records': '3346'}, {'Index': 'NYA', 'earliest_date': '01 Apr 1969, 00:00', 'latest_date': 'September 30, 2020 at 12:00 AM', 'total_records': '13947'}, {'Index': 'SSMI', 'earliest_date': '01 Apr 1996, 00:00', 'latest_date': 'September 30, 2020 at 12:00 AM', 'total_records': '7671'}, {'Index': 'TWII', 'earliest_date': '01 Apr 2004, 00:00', 'latest_date': 'September 30, 2020 at 12:00 AM', 'total_records': '5869'}]}

exec(code, env_args)
