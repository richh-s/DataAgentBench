code = """# Create mapping between index symbols and their exchanges/countries
index_mapping = {
    '000001.SS': {'exchange': 'Shanghai Stock Exchange', 'country': 'China', 'name': 'Shanghai Composite'},
    '399001.SZ': {'exchange': 'Shenzhen Stock Exchange', 'country': 'China', 'name': 'Shenzhen Component'},
    'GDAXI': {'exchange': 'Frankfurt Stock Exchange', 'country': 'Germany', 'name': 'DAX'},
    'GSPTSE': {'exchange': 'Toronto Stock Exchange', 'country': 'Canada', 'name': 'S&P/TSX Composite'},
    'HSI': {'exchange': 'Hong Kong Stock Exchange', 'country': 'Hong Kong', 'name': 'Hang Seng Index'},
    'IXIC': {'exchange': 'NASDAQ', 'country': 'USA', 'name': 'NASDAQ Composite'},
    'J203.JO': {'exchange': 'Johannesburg Stock Exchange', 'country': 'South Africa', 'name': 'FTSE/JSE All Share'},
    'N100': {'exchange': 'Euronext', 'country': 'Europe', 'name': 'Euronext 100'},
    'N225': {'exchange': 'Tokyo Stock Exchange', 'country': 'Japan', 'name': 'Nikkei 225'},
    'NSEI': {'exchange': 'National Stock Exchange of India', 'country': 'India', 'name': 'NIFTY 50'},
    'NYA': {'exchange': 'New York Stock Exchange', 'country': 'USA', 'name': 'NYSE Composite'},
    'SSMI': {'exchange': 'SIX Swiss Exchange', 'country': 'Switzerland', 'name': 'Swiss Market Index'},
    'TWII': {'exchange': 'Taiwan Stock Exchange', 'country': 'Taiwan', 'name': 'TAIEX'}
}

print('__RESULT__:')
print('{"status": "mapping_created"}')"""

env_args = {'var_functions.list_db:0': ['index_info'], 'var_functions.query_db:2': [{'Exchange': 'New York Stock Exchange', 'Currency': 'USD'}, {'Exchange': 'NASDAQ', 'Currency': 'USD'}, {'Exchange': 'Hong Kong Stock Exchange', 'Currency': 'HKD'}, {'Exchange': 'Shanghai Stock Exchange', 'Currency': 'CNY'}, {'Exchange': 'Tokyo Stock Exchange', 'Currency': 'JPY'}, {'Exchange': 'Euronext', 'Currency': 'EUR'}, {'Exchange': 'Shenzhen Stock Exchange', 'Currency': 'CNY'}, {'Exchange': 'Toronto Stock Exchange', 'Currency': 'CAD'}, {'Exchange': 'National Stock Exchange of India', 'Currency': 'INR'}, {'Exchange': 'Frankfurt Stock Exchange', 'Currency': 'EUR'}, {'Exchange': 'Korea Exchange', 'Currency': 'KRW'}, {'Exchange': 'SIX Swiss Exchange', 'Currency': 'CHF'}, {'Exchange': 'Taiwan Stock Exchange', 'Currency': 'TWD'}, {'Exchange': 'Johannesburg Stock Exchange', 'Currency': 'ZAR'}], 'var_functions.list_db:5': ['index_trade'], 'var_functions.query_db:6': [{'Index': '000001.SS'}, {'Index': '399001.SZ'}, {'Index': 'GDAXI'}, {'Index': 'GSPTSE'}, {'Index': 'HSI'}, {'Index': 'IXIC'}, {'Index': 'J203.JO'}, {'Index': 'N100'}, {'Index': 'N225'}, {'Index': 'NSEI'}, {'Index': 'NYA'}, {'Index': 'SSMI'}, {'Index': 'TWII'}], 'var_functions.query_db:8': [{'Index': '000001.SS', 'first_date': '01 Apr 2003, 00:00', 'last_date': 'September 30, 2015 at 12:00 AM', 'total_records': '5791'}, {'Index': '399001.SZ', 'first_date': '01 Apr 2004, 00:00', 'last_date': 'September 30, 2015 at 12:00 AM', 'total_records': '5760'}, {'Index': 'GDAXI', 'first_date': '01 Apr 1992, 00:00', 'last_date': 'September 30, 2016 at 12:00 AM', 'total_records': '8438'}, {'Index': 'GSPTSE', 'first_date': '01 Apr 1981, 00:00', 'last_date': 'September 30, 2016 at 12:00 AM', 'total_records': '10526'}, {'Index': 'HSI', 'first_date': '01 Apr 1992, 00:00', 'last_date': 'September 30, 2019 at 12:00 AM', 'total_records': '8492'}, {'Index': 'IXIC', 'first_date': '01 Apr 1974, 00:00', 'last_date': 'September 30, 2015 at 12:00 AM', 'total_records': '12690'}, {'Index': 'J203.JO', 'first_date': '01 Apr 2016, 00:00', 'last_date': 'September 30, 2019 at 12:00 AM', 'total_records': '2346'}, {'Index': 'N100', 'first_date': '01 Apr 2003, 00:00', 'last_date': 'September 30, 2019 at 12:00 AM', 'total_records': '5474'}, {'Index': 'N225', 'first_date': '01 Apr 1971, 00:00', 'last_date': 'September 30, 2020 at 12:00 AM', 'total_records': '13874'}, {'Index': 'NSEI', 'first_date': '01 Apr 2014, 00:00', 'last_date': 'September 30, 2014 at 12:00 AM', 'total_records': '3346'}, {'Index': 'NYA', 'first_date': '01 Apr 1969, 00:00', 'last_date': 'September 30, 2020 at 12:00 AM', 'total_records': '13947'}, {'Index': 'SSMI', 'first_date': '01 Apr 1996, 00:00', 'last_date': 'September 30, 2020 at 12:00 AM', 'total_records': '7671'}, {'Index': 'TWII', 'first_date': '01 Apr 2004, 00:00', 'last_date': 'September 30, 2020 at 12:00 AM', 'total_records': '5869'}]}

exec(code, env_args)
