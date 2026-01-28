code = """import json
import pandas as pd
import numpy as np

# Load the file path from storage
file_path = locals()['var_functions.query_db:20']

# Load the data
with open(file_path, 'r') as f:
    data = json.load(f)

# Create DataFrame and clean data
df = pd.DataFrame(data)
df['CloseUSD'] = pd.to_numeric(df['CloseUSD'], errors='coerce')
df['Date'] = pd.to_datetime(df['Date'], errors='coerce')
df = df.dropna(subset=['Date', 'CloseUSD'])

# Filter for data from 2000 onwards
df_filtered = df[df['Date'] >= '2000-01-01'].copy()

# Country mapping
index_to_country = {
    'GDAXI': 'Germany', 'GSPTSE': 'Canada', 'HSI': 'Hong Kong',
    'IXIC': 'USA', 'N225': 'Japan', 'NYA': 'USA',
    'SSMI': 'Switzerland', '000001.SS': 'China', '399001.SZ': 'China',
    'TWII': 'Taiwan', 'N100': 'Europe', 'NSEI': 'India',
    'J203.JO': 'South Africa'
}

results = []
monthly_investment = 100

for index in df_filtered['Index'].unique():
    index_data = df_filtered[df_filtered['Index'] == index].copy()
    index_data = index_data.sort_values('Date')
    
    if len(index_data) < 100:
        continue
    
    start_date = index_data['Date'].min()
    end_date = index_data['Date'].max()
    
    # Create monthly dates
    monthly_dates = pd.date_range(start=start_date, end=end_date, freq='MS')
    
    total_shares = 0
    total_invested = 0
    
    for invest_date in monthly_dates:
        future_dates = index_data['Date'][index_data['Date'] >= invest_date]
        if len(future_dates) == 0:
            continue
        trade_date = future_dates.iloc[0]
        price = index_data.loc[index_data['Date'] == trade_date, 'CloseUSD'].iloc[0]
        
        if pd.isna(price) or price <= 0:
            continue
            
        shares_bought = monthly_investment / price
        total_shares += shares_bought
        total_invested += monthly_investment
    
    if total_shares <= 0:
        continue
    
    final_price = index_data['CloseUSD'].iloc[-1]
    final_value = total_shares * final_price
    
    total_return = final_value - total_invested
    total_return_pct = (total_return / total_invested) * 100
    
    years = (end_date - start_date).days / 365.25
    if years > 0:
        annualized_return = ((final_value / total_invested) ** (1/years) - 1) * 100
    else:
        annualized_return = 0
    
    results.append({
        'index': index,
        'country': index_to_country.get(index, 'Unknown'),
        'start_date': start_date.isoformat(),
        'end_date': end_date.isoformat(),
        'years': round(years, 2),
        'num_investments': len(monthly_dates),
        'total_invested': round(total_invested, 2),
        'final_value': round(final_value, 2),
        'total_return': round(total_return, 2),
        'total_return_pct': round(total_return_pct, 2),
        'annualized_return_pct': round(annualized_return, 2)
    })

results_df = pd.DataFrame(results)
if not results_df.empty:
    results_df = results_df.sort_values('total_return_pct', ascending=False)

print('__RESULT__:')
print(results_df.head(10).to_json(orient='records'))"""

env_args = {'var_functions.list_db:0': ['index_info'], 'var_functions.query_db:2': [{'Exchange': 'New York Stock Exchange', 'Currency': 'USD'}, {'Exchange': 'NASDAQ', 'Currency': 'USD'}, {'Exchange': 'Hong Kong Stock Exchange', 'Currency': 'HKD'}, {'Exchange': 'Shanghai Stock Exchange', 'Currency': 'CNY'}, {'Exchange': 'Tokyo Stock Exchange', 'Currency': 'JPY'}, {'Exchange': 'Euronext', 'Currency': 'EUR'}, {'Exchange': 'Shenzhen Stock Exchange', 'Currency': 'CNY'}, {'Exchange': 'Toronto Stock Exchange', 'Currency': 'CAD'}, {'Exchange': 'National Stock Exchange of India', 'Currency': 'INR'}, {'Exchange': 'Frankfurt Stock Exchange', 'Currency': 'EUR'}, {'Exchange': 'Korea Exchange', 'Currency': 'KRW'}, {'Exchange': 'SIX Swiss Exchange', 'Currency': 'CHF'}, {'Exchange': 'Taiwan Stock Exchange', 'Currency': 'TWD'}, {'Exchange': 'Johannesburg Stock Exchange', 'Currency': 'ZAR'}], 'var_functions.list_db:5': ['index_trade'], 'var_functions.query_db:6': [{'Index': 'J203.JO'}, {'Index': 'IXIC'}, {'Index': 'N225'}, {'Index': 'GSPTSE'}, {'Index': 'NSEI'}, {'Index': 'GDAXI'}, {'Index': 'NYA'}, {'Index': '000001.SS'}, {'Index': 'SSMI'}, {'Index': 'TWII'}, {'Index': 'N100'}, {'Index': '399001.SZ'}, {'Index': 'HSI'}], 'var_functions.execute_python:8': {'status': 'mapping loaded', 'count': 13}, 'var_functions.query_db:10': [{'Index': '000001.SS', 'min_date': '01 Apr 2003, 00:00', 'max_date': 'September 30, 2015 at 12:00 AM', 'total_records': '5791'}, {'Index': '399001.SZ', 'min_date': '01 Apr 2004, 00:00', 'max_date': 'September 30, 2015 at 12:00 AM', 'total_records': '5760'}, {'Index': 'GDAXI', 'min_date': '01 Apr 1992, 00:00', 'max_date': 'September 30, 2016 at 12:00 AM', 'total_records': '8438'}, {'Index': 'GSPTSE', 'min_date': '01 Apr 1981, 00:00', 'max_date': 'September 30, 2016 at 12:00 AM', 'total_records': '10526'}, {'Index': 'HSI', 'min_date': '01 Apr 1992, 00:00', 'max_date': 'September 30, 2019 at 12:00 AM', 'total_records': '8492'}, {'Index': 'IXIC', 'min_date': '01 Apr 1974, 00:00', 'max_date': 'September 30, 2015 at 12:00 AM', 'total_records': '12690'}, {'Index': 'J203.JO', 'min_date': '01 Apr 2016, 00:00', 'max_date': 'September 30, 2019 at 12:00 AM', 'total_records': '2346'}, {'Index': 'N100', 'min_date': '01 Apr 2003, 00:00', 'max_date': 'September 30, 2019 at 12:00 AM', 'total_records': '5474'}, {'Index': 'N225', 'min_date': '01 Apr 1971, 00:00', 'max_date': 'September 30, 2020 at 12:00 AM', 'total_records': '13874'}, {'Index': 'NSEI', 'min_date': '01 Apr 2014, 00:00', 'max_date': 'September 30, 2014 at 12:00 AM', 'total_records': '3346'}, {'Index': 'NYA', 'min_date': '01 Apr 1969, 00:00', 'max_date': 'September 30, 2020 at 12:00 AM', 'total_records': '13947'}, {'Index': 'SSMI', 'min_date': '01 Apr 1996, 00:00', 'max_date': 'September 30, 2020 at 12:00 AM', 'total_records': '7671'}, {'Index': 'TWII', 'min_date': '01 Apr 2004, 00:00', 'max_date': 'September 30, 2020 at 12:00 AM', 'total_records': '5869'}], 'var_functions.query_db:12': 'file_storage/functions.query_db:12.json', 'var_functions.query_db:18': 'file_storage/functions.query_db:18.json', 'var_functions.query_db:20': 'file_storage/functions.query_db:20.json', 'var_functions.execute_python:22': {'status': 'data_loaded', 'eligible_count': 11}, 'var_functions.execute_python:24': {'status': 'analysis_ready', 'indices_count': 13}}

exec(code, env_args)
