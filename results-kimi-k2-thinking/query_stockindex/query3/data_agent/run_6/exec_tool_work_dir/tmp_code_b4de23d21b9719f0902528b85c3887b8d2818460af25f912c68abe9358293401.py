code = """import json
import pandas as pd

# Get data from previous query
summary_data = var_functions.query_db:44

# Create DataFrame
df = pd.DataFrame(summary_data)

# Map indices to countries and select only those with data from 2000
country_map = {
    'N225': 'Japan',
    'IXIC': 'USA', 
    'NYA': 'USA',
    'HSI': 'Hong Kong',
    'GDAXI': 'Germany',
    'GSPTSE': 'Canada',
    'SSMI': 'Switzerland',
    'TWII': 'Taiwan',
    'N100': 'Europe (Euronext)',
    '000001.SS': 'China (Shanghai)',
    '399001.SZ': 'China (Shenzhen)',
    'NSEI': 'India',
    'J203.JO': 'South Africa'
}

df['Country'] = df['Index'].map(country_map)

# Filter indices with data starting from 2000
indices_from_2000 = ['N225', 'IXIC', 'NYA', 'HSI', 'GDAXI', 'GSPTSE', 'SSMI', 'TWII', 'N100', '000001.SS', '399001.SZ']
df_filtered = df[df['Index'].isin(indices_from_2000)].copy()

# Parse dates
df_filtered['start_date'] = pd.to_datetime(df_filtered['start_date'])
df_filtered['end_date'] = pd.to_datetime(df_filtered['end_date'], errors='coerce')

print('Filtered indices:', len(df_filtered))
print(df_filtered[['Index', 'Country', 'start_date', 'end_date']].to_string(index=False))"""

env_args = {'var_functions.list_db:0': ['index_info'], 'var_functions.query_db:2': [{'Exchange': 'New York Stock Exchange', 'Currency': 'USD'}, {'Exchange': 'NASDAQ', 'Currency': 'USD'}, {'Exchange': 'Hong Kong Stock Exchange', 'Currency': 'HKD'}, {'Exchange': 'Shanghai Stock Exchange', 'Currency': 'CNY'}, {'Exchange': 'Tokyo Stock Exchange', 'Currency': 'JPY'}, {'Exchange': 'Euronext', 'Currency': 'EUR'}, {'Exchange': 'Shenzhen Stock Exchange', 'Currency': 'CNY'}, {'Exchange': 'Toronto Stock Exchange', 'Currency': 'CAD'}, {'Exchange': 'National Stock Exchange of India', 'Currency': 'INR'}, {'Exchange': 'Frankfurt Stock Exchange', 'Currency': 'EUR'}, {'Exchange': 'Korea Exchange', 'Currency': 'KRW'}, {'Exchange': 'SIX Swiss Exchange', 'Currency': 'CHF'}, {'Exchange': 'Taiwan Stock Exchange', 'Currency': 'TWD'}, {'Exchange': 'Johannesburg Stock Exchange', 'Currency': 'ZAR'}], 'var_functions.list_db:5': ['index_trade'], 'var_functions.query_db:6': [{'Index': 'J203.JO'}, {'Index': 'N225'}, {'Index': 'GSPTSE'}, {'Index': 'NSEI'}, {'Index': 'GDAXI'}, {'Index': 'IXIC'}, {'Index': 'HSI'}, {'Index': 'NYA'}, {'Index': 'N100'}, {'Index': '399001.SZ'}, {'Index': '000001.SS'}, {'Index': 'SSMI'}, {'Index': 'TWII'}], 'var_functions.query_db:8': [{'Index': '000001.SS', 'min_date': '01 Apr 2003, 00:00', 'max_date': 'September 30, 2015 at 12:00 AM', 'record_count': '5791'}, {'Index': '399001.SZ', 'min_date': '01 Apr 2004, 00:00', 'max_date': 'September 30, 2015 at 12:00 AM', 'record_count': '5760'}, {'Index': 'GDAXI', 'min_date': '01 Apr 1992, 00:00', 'max_date': 'September 30, 2016 at 12:00 AM', 'record_count': '8438'}, {'Index': 'GSPTSE', 'min_date': '01 Apr 1981, 00:00', 'max_date': 'September 30, 2016 at 12:00 AM', 'record_count': '10526'}, {'Index': 'HSI', 'min_date': '01 Apr 1992, 00:00', 'max_date': 'September 30, 2019 at 12:00 AM', 'record_count': '8492'}, {'Index': 'IXIC', 'min_date': '01 Apr 1974, 00:00', 'max_date': 'September 30, 2015 at 12:00 AM', 'record_count': '12690'}, {'Index': 'J203.JO', 'min_date': '01 Apr 2016, 00:00', 'max_date': 'September 30, 2019 at 12:00 AM', 'record_count': '2346'}, {'Index': 'N100', 'min_date': '01 Apr 2003, 00:00', 'max_date': 'September 30, 2019 at 12:00 AM', 'record_count': '5474'}, {'Index': 'N225', 'min_date': '01 Apr 1971, 00:00', 'max_date': 'September 30, 2020 at 12:00 AM', 'record_count': '13874'}, {'Index': 'NSEI', 'min_date': '01 Apr 2014, 00:00', 'max_date': 'September 30, 2014 at 12:00 AM', 'record_count': '3346'}, {'Index': 'NYA', 'min_date': '01 Apr 1969, 00:00', 'max_date': 'September 30, 2020 at 12:00 AM', 'record_count': '13947'}, {'Index': 'SSMI', 'min_date': '01 Apr 1996, 00:00', 'max_date': 'September 30, 2020 at 12:00 AM', 'record_count': '7671'}, {'Index': 'TWII', 'min_date': '01 Apr 2004, 00:00', 'max_date': 'September 30, 2020 at 12:00 AM', 'record_count': '5869'}], 'var_functions.query_db:10': 'file_storage/functions.query_db:10.json', 'var_functions.query_db:20': [{'Index': '000001.SS', 'Date': '2000-01-04 00:00:00', 'CloseUSD': '225.01935552'}, {'Index': '000001.SS', 'Date': '2000-01-05 00:00:00', 'CloseUSD': '225.54912112'}, {'Index': '000001.SS', 'Date': '2000-01-10 00:00:00', 'CloseUSD': '247.21792976'}, {'Index': '000001.SS', 'Date': '2000-01-12 00:00:00', 'CloseUSD': '230.0832032'}, {'Index': '000001.SS', 'Date': '2000-01-14 00:00:00', 'CloseUSD': '225.41568352'}, {'Index': '000001.SS', 'Date': '2000-01-19 00:00:00', 'CloseUSD': '230.51583984'}, {'Index': '000001.SS', 'Date': '2000-01-20 00:00:00', 'CloseUSD': '234.69808592'}, {'Index': '000001.SS', 'Date': '2000-01-27 00:00:00', 'CloseUSD': '241.08271488'}, {'Index': '000001.SS', 'Date': '2000-01-28 00:00:00', 'CloseUSD': '245.59951168'}, {'Index': '000001.SS', 'Date': '2000-02-14 00:00:00', 'CloseUSD': '267.83087888'}], 'var_functions.query_db:22': 'file_storage/functions.query_db:22.json', 'var_functions.query_db:30': [{'Index': 'HSI', 'Date': '31 Dec 1986, 00:00', 'CloseUSD': '333.87900637'}], 'var_functions.query_db:36': 'file_storage/functions.query_db:36.json', 'var_functions.query_db:44': [{'Index': '000001.SS', 'start_date': '2000-01-04 00:00:00', 'end_date': 'September 30, 2015 at 12:00 AM', 'avg_price': '389.6999728009173'}, {'Index': '399001.SZ', 'start_date': '2000-01-05 00:00:00', 'end_date': 'September 30, 2015 at 12:00 AM', 'avg_price': '1305.142708748053'}, {'Index': 'GDAXI', 'start_date': '2000-01-05 00:00:00', 'end_date': 'September 30, 2016 at 12:00 AM', 'avg_price': '7936.756931484456'}, {'Index': 'GSPTSE', 'start_date': '2000-01-05 00:00:00', 'end_date': 'September 30, 2016 at 12:00 AM', 'avg_price': '7688.001953578097'}, {'Index': 'HSI', 'start_date': '2000-01-14 00:00:00', 'end_date': 'September 30, 2019 at 12:00 AM', 'avg_price': '2171.752110109059'}, {'Index': 'IXIC', 'start_date': '2000-01-06 00:00:00', 'end_date': 'September 30, 2015 at 12:00 AM', 'avg_price': '2496.204517953201'}, {'Index': 'J203.JO', 'start_date': '2012-02-08 00:00:00', 'end_date': 'September 30, 2019 at 12:00 AM', 'avg_price': '3559.500105210677'}, {'Index': 'N100', 'start_date': '2000-01-10 00:00:00', 'end_date': 'September 30, 2019 at 12:00 AM', 'avg_price': '1004.1303717488653'}, {'Index': 'N225', 'start_date': '2000-01-04 00:00:00', 'end_date': 'September 30, 2020 at 12:00 AM', 'avg_price': '133.52814088639033'}, {'Index': 'NSEI', 'start_date': '2007-09-25 00:00:00', 'end_date': 'September 30, 2014 at 12:00 AM', 'avg_price': '76.40927922187028'}, {'Index': 'NYA', 'start_date': '2000-01-03 00:00:00', 'end_date': 'September 30, 2020 at 12:00 AM', 'avg_price': '5489.189061573103'}, {'Index': 'SSMI', 'start_date': '2000-01-05 00:00:00', 'end_date': 'September 30, 2020 at 12:00 AM', 'avg_price': '7572.72269026704'}, {'Index': 'TWII', 'start_date': '2000-01-17 00:00:00', 'end_date': 'September 30, 2020 at 12:00 AM', 'avg_price': '322.36542159113344'}]}

exec(code, env_args)
