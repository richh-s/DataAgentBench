code = """import json
import pandas as pd

# Read data directly from the file path we know from the query result
file_path = '/tmp/tmp_7c1x9j7.json'

# Load the data
with open(file_path, 'r') as f:
    data = json.load(f)

# Create DataFrame
df = pd.DataFrame(data)

# Parse dates and filter for 2000+
df['Date'] = pd.to_datetime(df['Date'])
df_2000 = df[df['Date'].dt.year >= 2000].copy()

# Create year-month for grouping
df_2000['YearMonth'] = df_2000['Date'].dt.to_period('M')

# Get first close price of each month for each index
monthly_data = df_2000.groupby(['Index', 'YearMonth']).first().reset_index()

# Calculate DCA returns
dca_results = []
monthly_investment = 100

for idx in monthly_data['Index'].unique():
    idx_monthly = monthly_data[monthly_data['Index'] == idx].sort_values('Date')
    
    if len(idx_monthly) < 12:  # Need at least 1 year of data
        continue
    
    # DCA calculation
    shares = monthly_investment / idx_monthly['CloseUSD']
    total_shares = shares.sum()
    total_invested = monthly_investment * len(idx_monthly)
    final_value = total_shares * idx_monthly['CloseUSD'].iloc[-1]
    return_pct = ((final_value - total_invested) / total_invested) * 100
    
    dca_results.append({
        'Index': idx,
        'Return_Pct': round(return_pct, 2),
        'Months': len(idx_monthly)
    })

# Sort by return
dca_results.sort(key=lambda x: x['Return_Pct'], reverse=True)

# Map to countries
country_map = {'N225': 'Japan', 'IXIC': 'USA', 'NYA': 'USA', 'HSI': 'Hong Kong', 
               'GDAXI': 'Germany', 'GSPTSE': 'Canada', 'SSMI': 'Switzerland', 
               'TWII': 'Taiwan', 'N100': 'Europe', '000001.SS': 'China', 
               '399001.SZ': 'China', 'NSEI': 'India', 'J203.JO': 'South Africa'}

# Top 5
top_5 = []
for item in dca_results[:5]:
    top_5.append({
        'Index': item['Index'],
        'Return_Pct': item['Return_Pct'],
        'Country': country_map.get(item['Index'], 'Unknown')
    })

print('__RESULT__:')
print(json.dumps(top_5, indent=2))"""

env_args = {'var_functions.list_db:0': ['index_info'], 'var_functions.query_db:2': [{'Exchange': 'New York Stock Exchange', 'Currency': 'USD'}, {'Exchange': 'NASDAQ', 'Currency': 'USD'}, {'Exchange': 'Hong Kong Stock Exchange', 'Currency': 'HKD'}, {'Exchange': 'Shanghai Stock Exchange', 'Currency': 'CNY'}, {'Exchange': 'Tokyo Stock Exchange', 'Currency': 'JPY'}, {'Exchange': 'Euronext', 'Currency': 'EUR'}, {'Exchange': 'Shenzhen Stock Exchange', 'Currency': 'CNY'}, {'Exchange': 'Toronto Stock Exchange', 'Currency': 'CAD'}, {'Exchange': 'National Stock Exchange of India', 'Currency': 'INR'}, {'Exchange': 'Frankfurt Stock Exchange', 'Currency': 'EUR'}, {'Exchange': 'Korea Exchange', 'Currency': 'KRW'}, {'Exchange': 'SIX Swiss Exchange', 'Currency': 'CHF'}, {'Exchange': 'Taiwan Stock Exchange', 'Currency': 'TWD'}, {'Exchange': 'Johannesburg Stock Exchange', 'Currency': 'ZAR'}], 'var_functions.list_db:5': ['index_trade'], 'var_functions.query_db:6': [{'Index': 'J203.JO'}, {'Index': 'N225'}, {'Index': 'GSPTSE'}, {'Index': 'NSEI'}, {'Index': 'GDAXI'}, {'Index': 'IXIC'}, {'Index': 'HSI'}, {'Index': 'NYA'}, {'Index': 'N100'}, {'Index': '399001.SZ'}, {'Index': '000001.SS'}, {'Index': 'SSMI'}, {'Index': 'TWII'}], 'var_functions.query_db:8': [{'Index': '000001.SS', 'min_date': '01 Apr 2003, 00:00', 'max_date': 'September 30, 2015 at 12:00 AM', 'record_count': '5791'}, {'Index': '399001.SZ', 'min_date': '01 Apr 2004, 00:00', 'max_date': 'September 30, 2015 at 12:00 AM', 'record_count': '5760'}, {'Index': 'GDAXI', 'min_date': '01 Apr 1992, 00:00', 'max_date': 'September 30, 2016 at 12:00 AM', 'record_count': '8438'}, {'Index': 'GSPTSE', 'min_date': '01 Apr 1981, 00:00', 'max_date': 'September 30, 2016 at 12:00 AM', 'record_count': '10526'}, {'Index': 'HSI', 'min_date': '01 Apr 1992, 00:00', 'max_date': 'September 30, 2019 at 12:00 AM', 'record_count': '8492'}, {'Index': 'IXIC', 'min_date': '01 Apr 1974, 00:00', 'max_date': 'September 30, 2015 at 12:00 AM', 'record_count': '12690'}, {'Index': 'J203.JO', 'min_date': '01 Apr 2016, 00:00', 'max_date': 'September 30, 2019 at 12:00 AM', 'record_count': '2346'}, {'Index': 'N100', 'min_date': '01 Apr 2003, 00:00', 'max_date': 'September 30, 2019 at 12:00 AM', 'record_count': '5474'}, {'Index': 'N225', 'min_date': '01 Apr 1971, 00:00', 'max_date': 'September 30, 2020 at 12:00 AM', 'record_count': '13874'}, {'Index': 'NSEI', 'min_date': '01 Apr 2014, 00:00', 'max_date': 'September 30, 2014 at 12:00 AM', 'record_count': '3346'}, {'Index': 'NYA', 'min_date': '01 Apr 1969, 00:00', 'max_date': 'September 30, 2020 at 12:00 AM', 'record_count': '13947'}, {'Index': 'SSMI', 'min_date': '01 Apr 1996, 00:00', 'max_date': 'September 30, 2020 at 12:00 AM', 'record_count': '7671'}, {'Index': 'TWII', 'min_date': '01 Apr 2004, 00:00', 'max_date': 'September 30, 2020 at 12:00 AM', 'record_count': '5869'}], 'var_functions.query_db:10': 'file_storage/functions.query_db:10.json', 'var_functions.query_db:20': [{'Index': '000001.SS', 'Date': '2000-01-04 00:00:00', 'CloseUSD': '225.01935552'}, {'Index': '000001.SS', 'Date': '2000-01-05 00:00:00', 'CloseUSD': '225.54912112'}, {'Index': '000001.SS', 'Date': '2000-01-10 00:00:00', 'CloseUSD': '247.21792976'}, {'Index': '000001.SS', 'Date': '2000-01-12 00:00:00', 'CloseUSD': '230.0832032'}, {'Index': '000001.SS', 'Date': '2000-01-14 00:00:00', 'CloseUSD': '225.41568352'}, {'Index': '000001.SS', 'Date': '2000-01-19 00:00:00', 'CloseUSD': '230.51583984'}, {'Index': '000001.SS', 'Date': '2000-01-20 00:00:00', 'CloseUSD': '234.69808592'}, {'Index': '000001.SS', 'Date': '2000-01-27 00:00:00', 'CloseUSD': '241.08271488'}, {'Index': '000001.SS', 'Date': '2000-01-28 00:00:00', 'CloseUSD': '245.59951168'}, {'Index': '000001.SS', 'Date': '2000-02-14 00:00:00', 'CloseUSD': '267.83087888'}], 'var_functions.query_db:22': 'file_storage/functions.query_db:22.json', 'var_functions.query_db:30': [{'Index': 'HSI', 'Date': '31 Dec 1986, 00:00', 'CloseUSD': '333.87900637'}], 'var_functions.query_db:36': 'file_storage/functions.query_db:36.json'}

exec(code, env_args)
