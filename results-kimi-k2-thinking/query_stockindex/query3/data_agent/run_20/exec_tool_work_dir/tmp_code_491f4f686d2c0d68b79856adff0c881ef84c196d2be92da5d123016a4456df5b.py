code = """import json, pandas as pd
storage = locals()
file_key = 'var_functions.query_db:18'
data_file = storage[file_key]

if isinstance(data_file, str) and data_file.endswith('.json'):
    with open(data_file, 'r') as f:
        data = json.load(f)
else:
    data = data_file

df = pd.DataFrame(data)
df['Date'] = pd.to_datetime(df['Date'], errors='coerce')
df['CloseUSD'] = pd.to_numeric(df['CloseUSD'], errors='coerce')
df = df[df['Date'] >= '2000-01-01'].dropna()

index_country = {'000001.SS': 'China', '399001.SZ': 'China', 'GDAXI': 'Germany', 'GSPTSE': 'Canada', 'HSI': 'Hong Kong', 'IXIC': 'USA', 'J203.JO': 'South Africa', 'N100': 'Europe', 'N225': 'Japan', 'NSEI': 'India', 'NYA': 'USA', 'SSMI': 'Switzerland', 'TWII': 'Taiwan'}
index_name = {'000001.SS': 'Shanghai Composite', '399001.SZ': 'Shenzhen Component', 'GDAXI': 'DAX', 'GSPTSE': 'S&P/TSX Composite', 'HSI': 'Hang Seng Index', 'IXIC': 'NASDAQ Composite', 'J203.JO': 'FTSE/JSE All Share', 'N100': 'Euronext 100', 'N225': 'Nikkei 225', 'NSEI': 'NIFTY 50', 'NYA': 'NYSE Composite', 'SSMI': 'Swiss Market Index', 'TWII': 'TAIEX'}

def calc_dca(group, monthly=100):
    if group.empty:
        return 0, 0, 0
    group = group.sort_values('Date')
    start = group['Date'].min()
    end = group['Date'].max()
    
    invest_dates = []
    cur = start
    while cur <= end:
        month_end = cur + pd.offsets.MonthEnd(1)
        month_data = group[(group['Date'] >= cur) & (group['Date'] <= month_end)]
        if not month_data.empty:
            invest_dates.append(month_data.iloc[0]['Date'])
        cur = cur + pd.offsets.MonthBegin(1)
    
    if not invest_dates:
        return 0, 0, 0
    
    invested = 0
    units = 0
    for d in invest_dates:
        price_data = group[group['Date'] == d]
        if price_data.empty:
            continue
        price = price_data.iloc[0]['CloseUSD']
        invested += monthly
        units += monthly / price
    
    final_value = units * group.iloc[-1]['CloseUSD']
    return_pct = ((final_value - invested) / invested * 100) if invested > 0 else 0
    return invested, return_pct, final_value

results = []
for idx in df['Index'].unique():
    data_idx = df[df['Index'] == idx].copy()
    if data_idx['Date'].max() - data_idx['Date'].min() < pd.Timedelta(days=365):
        continue
    invested, return_pct, final_val = calc_dca(data_idx)
    if invested > 0:
        results.append({'symbol': idx, 'name': index_name.get(idx, idx), 'country': index_country.get(idx, 'Unknown'), 'return_pct': round(return_pct, 2)})

top5 = sorted(results, key=lambda x: x['return_pct'], reverse=True)[:5]
print('__RESULT__:')
print(json.dumps(top5))"""

env_args = {'var_functions.list_db:0': ['index_info'], 'var_functions.query_db:2': [{'Exchange': 'New York Stock Exchange', 'Currency': 'USD'}, {'Exchange': 'NASDAQ', 'Currency': 'USD'}, {'Exchange': 'Hong Kong Stock Exchange', 'Currency': 'HKD'}, {'Exchange': 'Shanghai Stock Exchange', 'Currency': 'CNY'}, {'Exchange': 'Tokyo Stock Exchange', 'Currency': 'JPY'}, {'Exchange': 'Euronext', 'Currency': 'EUR'}, {'Exchange': 'Shenzhen Stock Exchange', 'Currency': 'CNY'}, {'Exchange': 'Toronto Stock Exchange', 'Currency': 'CAD'}, {'Exchange': 'National Stock Exchange of India', 'Currency': 'INR'}, {'Exchange': 'Frankfurt Stock Exchange', 'Currency': 'EUR'}, {'Exchange': 'Korea Exchange', 'Currency': 'KRW'}, {'Exchange': 'SIX Swiss Exchange', 'Currency': 'CHF'}, {'Exchange': 'Taiwan Stock Exchange', 'Currency': 'TWD'}, {'Exchange': 'Johannesburg Stock Exchange', 'Currency': 'ZAR'}], 'var_functions.list_db:5': ['index_trade'], 'var_functions.query_db:6': [{'Index': '000001.SS'}, {'Index': '399001.SZ'}, {'Index': 'GDAXI'}, {'Index': 'GSPTSE'}, {'Index': 'HSI'}, {'Index': 'IXIC'}, {'Index': 'J203.JO'}, {'Index': 'N100'}, {'Index': 'N225'}, {'Index': 'NSEI'}, {'Index': 'NYA'}, {'Index': 'SSMI'}, {'Index': 'TWII'}], 'var_functions.query_db:8': [{'Index': '000001.SS', 'first_date': '01 Apr 2003, 00:00', 'last_date': 'September 30, 2015 at 12:00 AM', 'total_records': '5791'}, {'Index': '399001.SZ', 'first_date': '01 Apr 2004, 00:00', 'last_date': 'September 30, 2015 at 12:00 AM', 'total_records': '5760'}, {'Index': 'GDAXI', 'first_date': '01 Apr 1992, 00:00', 'last_date': 'September 30, 2016 at 12:00 AM', 'total_records': '8438'}, {'Index': 'GSPTSE', 'first_date': '01 Apr 1981, 00:00', 'last_date': 'September 30, 2016 at 12:00 AM', 'total_records': '10526'}, {'Index': 'HSI', 'first_date': '01 Apr 1992, 00:00', 'last_date': 'September 30, 2019 at 12:00 AM', 'total_records': '8492'}, {'Index': 'IXIC', 'first_date': '01 Apr 1974, 00:00', 'last_date': 'September 30, 2015 at 12:00 AM', 'total_records': '12690'}, {'Index': 'J203.JO', 'first_date': '01 Apr 2016, 00:00', 'last_date': 'September 30, 2019 at 12:00 AM', 'total_records': '2346'}, {'Index': 'N100', 'first_date': '01 Apr 2003, 00:00', 'last_date': 'September 30, 2019 at 12:00 AM', 'total_records': '5474'}, {'Index': 'N225', 'first_date': '01 Apr 1971, 00:00', 'last_date': 'September 30, 2020 at 12:00 AM', 'total_records': '13874'}, {'Index': 'NSEI', 'first_date': '01 Apr 2014, 00:00', 'last_date': 'September 30, 2014 at 12:00 AM', 'total_records': '3346'}, {'Index': 'NYA', 'first_date': '01 Apr 1969, 00:00', 'last_date': 'September 30, 2020 at 12:00 AM', 'total_records': '13947'}, {'Index': 'SSMI', 'first_date': '01 Apr 1996, 00:00', 'last_date': 'September 30, 2020 at 12:00 AM', 'total_records': '7671'}, {'Index': 'TWII', 'first_date': '01 Apr 2004, 00:00', 'last_date': 'September 30, 2020 at 12:00 AM', 'total_records': '5869'}], 'var_functions.execute_python:12': {'status': 'mapping_created'}, 'var_functions.query_db:14': [{'Index': 'GDAXI', 'Date': '01 Apr 1992, 00:00', 'CloseUSD': '2082.1617280200003'}, {'Index': 'GDAXI', 'Date': '01 Apr 1993, 00:00', 'CloseUSD': '2037.44884758'}, {'Index': 'GDAXI', 'Date': '01 Apr 1997, 00:00', 'CloseUSD': '4003.38115242'}, {'Index': 'GDAXI', 'Date': '01 Apr 2005, 00:00', 'CloseUSD': '5335.7063377'}, {'Index': 'GDAXI', 'Date': '01 Apr 2008, 00:00', 'CloseUSD': '8198.80269516'}, {'Index': 'GDAXI', 'Date': '01 Apr 2011, 00:00', 'CloseUSD': '8759.36827198'}, {'Index': 'GDAXI', 'Date': '01 Apr 2015, 00:00', 'CloseUSD': '14641.6834536'}, {'Index': 'GDAXI', 'Date': '01 Apr 2019, 00:00', 'CloseUSD': '14252.0280806'}, {'Index': 'GDAXI', 'Date': '01 Apr 2020, 00:00', 'CloseUSD': '11644.595'}, {'Index': 'GDAXI', 'Date': '01 Aug 1988, 00:00', 'CloseUSD': '1452.61745368'}, {'Index': 'GDAXI', 'Date': '01 Aug 1995, 00:00', 'CloseUSD': '2697.7372122'}, {'Index': 'GDAXI', 'Date': '01 Aug 2001, 00:00', 'CloseUSD': '7118.9805756'}, {'Index': 'GDAXI', 'Date': '01 Aug 2006, 00:00', 'CloseUSD': '6828.023085479999'}, {'Index': 'GDAXI', 'Date': '01 Aug 2008, 00:00', 'CloseUSD': '7803.681152419999'}, {'Index': 'GDAXI', 'Date': '01 Aug 2013, 00:00', 'CloseUSD': '10261.09117218'}, {'Index': 'GDAXI', 'Date': '01 Aug 2016, 00:00', 'CloseUSD': '12603.2338266'}, {'Index': 'GDAXI', 'Date': '01 Dec 1992, 00:00', 'CloseUSD': '1887.12033412'}, {'Index': 'GDAXI', 'Date': '01 Dec 1997, 00:00', 'CloseUSD': '5033.62230484'}, {'Index': 'GDAXI', 'Date': '01 Dec 2003, 00:00', 'CloseUSD': '4661.86394022'}, {'Index': 'GDAXI', 'Date': '01 Dec 2004, 00:00', 'CloseUSD': '5106.9563377'}], 'var_functions.query_db:16': [{'Index': '000001.SS', 'first_date': '2000-01-04 00:00:00', 'last_date': 'September 30, 2015 at 12:00 AM'}, {'Index': '399001.SZ', 'first_date': '2000-01-05 00:00:00', 'last_date': 'September 30, 2015 at 12:00 AM'}, {'Index': 'GDAXI', 'first_date': '2000-01-05 00:00:00', 'last_date': 'September 30, 2016 at 12:00 AM'}, {'Index': 'GSPTSE', 'first_date': '2000-01-05 00:00:00', 'last_date': 'September 30, 2016 at 12:00 AM'}, {'Index': 'HSI', 'first_date': '2000-01-14 00:00:00', 'last_date': 'September 30, 2019 at 12:00 AM'}, {'Index': 'IXIC', 'first_date': '2000-01-06 00:00:00', 'last_date': 'September 30, 2015 at 12:00 AM'}, {'Index': 'J203.JO', 'first_date': '2012-02-08 00:00:00', 'last_date': 'September 30, 2019 at 12:00 AM'}, {'Index': 'N100', 'first_date': '2000-01-10 00:00:00', 'last_date': 'September 30, 2019 at 12:00 AM'}, {'Index': 'N225', 'first_date': '2000-01-04 00:00:00', 'last_date': 'September 30, 2020 at 12:00 AM'}, {'Index': 'NSEI', 'first_date': '2007-09-25 00:00:00', 'last_date': 'September 30, 2014 at 12:00 AM'}, {'Index': 'NYA', 'first_date': '2000-01-03 00:00:00', 'last_date': 'September 30, 2020 at 12:00 AM'}, {'Index': 'SSMI', 'first_date': '2000-01-05 00:00:00', 'last_date': 'September 30, 2020 at 12:00 AM'}, {'Index': 'TWII', 'first_date': '2000-01-17 00:00:00', 'last_date': 'September 30, 2020 at 12:00 AM'}], 'var_functions.query_db:18': 'file_storage/functions.query_db:18.json', 'var_functions.execute_python:22': {'records_loaded': 21342, 'indices': 13}}

exec(code, env_args)
