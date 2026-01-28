code = """import json
import pandas as pd
from datetime import datetime

# Load price data
price_data_path = var_functions.query_db:48
with open(price_data_path, 'r') as f:
    price_data = json.load(f)

# Convert to DataFrame
df = pd.DataFrame(price_data)

# Process data
df['Date'] = pd.to_datetime(df['Date'])
df['CloseUSD'] = pd.to_numeric(df['CloseUSD'])
df = df.sort_values(['Index', 'Date'])

# Map indices to exchanges and countries
index_country_map = {
    '000001.SS': 'China - Shanghai',      # Shanghai Stock Exchange
    '399001.SZ': 'China - Shenzhen',      # Shenzhen Stock Exchange  
    'GDAXI': 'Germany',                   # Frankfurt Stock Exchange
    'GSPTSE': 'Canada',                   # Toronto Stock Exchange
    'HSI': 'Hong Kong',                   # Hong Kong Stock Exchange
    'IXIC': 'United States - NASDAQ',     # NASDAQ
    'N100': 'Europe - Euronext',          # Euronext
    'N225': 'Japan',                      # Tokyo Stock Exchange
    'NYA': 'United States - NYSE',        # New York Stock Exchange
    'SSMI': 'Switzerland',                 # SIX Swiss Exchange
    'TWII': 'Taiwan'                      # Taiwan Stock Exchange
}

# Monthly DCA simulation
monthly_investment = 100
results = []

for index in df['Index'].unique():
    idx_data = df[df['Index'] == index].copy()
    
    # Check minimum data requirement
    if len(idx_data) < 100:  # Need decent data coverage
        continue
    
    # Get monthly data (first trading day of each month)
    idx_data['YearMonth'] = idx_data['Date'].dt.to_period('M')
    monthly_data = idx_data.groupby('YearMonth').first().reset_index()
    
    # DCA simulation
    total_invested = 0
    total_shares = 0
    
    for _, row in monthly_data.iterrows():
        price = float(row['CloseUSD'])
        if price > 0:
            shares_bought = monthly_investment / price
            total_shares += shares_bought
            total_invested += monthly_investment
    
    # Calculate final metrics
    current_price = float(idx_data['CloseUSD'].iloc[-1])
    current_value = total_shares * current_price
    
    if total_invested > 0:
        total_return_pct = ((current_value - total_invested) / total_invested) * 100
        
        # Annualized return
        years = (idx_data['Date'].iloc[-1] - idx_data['Date'].iloc[0]).days / 365.25
        if years > 0:
            annualized = (((current_value / total_invested) ** (1/years)) - 1) * 100
        else:
            annualized = 0
    else:
        total_return_pct = 0
        annualized = 0
    
    country = index_country_map.get(index, 'Unknown')
    
    results.append({
        'Rank': 0,
        'Index': index,
        'Country': country,
        'Total_Return_Pct': total_return_pct,
        'Annualized_Return_Pct': annualized,
        'Total_Invested': total_invested,
        'Current_Value': current_value,
        'Data_Points': len(idx_data),
        'Years': years if 'years' in locals() else 0
    })

# Convert to DataFrame and sort
results_df = pd.DataFrame(results)
results_df = results_df.sort_values('Total_Return_Pct', ascending=False).reset_index(drop=True)

# Add ranking
results_df['Rank'] = results_df.index + 1

# Get top 5
top_5 = results_df.head(5)

# Format results
output = []
for _, row in top_5.iterrows():
    output.append({
        'Rank': int(row['Rank']),
        'Index': row['Index'],
        'Country': row['Country'],
        'Total_Return_Pct': round(row['Total_Return_Pct'], 1),
        'Annualized_Return_Pct': round(row['Annualized_Return_Pct'], 1),
        'Total_Invested': round(row['Total_Invested'], 0),
        'Current_Value': round(row['Current_Value'], 0)
    })

result_json = json.dumps(output, indent=2)
print('__RESULT__:')
print(result_json)"""

env_args = {'var_functions.list_db:0': ['index_info'], 'var_functions.list_db:2': ['index_trade'], 'var_functions.query_db:5': [{'Exchange': 'New York Stock Exchange', 'Currency': 'USD'}, {'Exchange': 'NASDAQ', 'Currency': 'USD'}, {'Exchange': 'Hong Kong Stock Exchange', 'Currency': 'HKD'}, {'Exchange': 'Shanghai Stock Exchange', 'Currency': 'CNY'}, {'Exchange': 'Tokyo Stock Exchange', 'Currency': 'JPY'}, {'Exchange': 'Euronext', 'Currency': 'EUR'}, {'Exchange': 'Shenzhen Stock Exchange', 'Currency': 'CNY'}, {'Exchange': 'Toronto Stock Exchange', 'Currency': 'CAD'}, {'Exchange': 'National Stock Exchange of India', 'Currency': 'INR'}, {'Exchange': 'Frankfurt Stock Exchange', 'Currency': 'EUR'}, {'Exchange': 'Korea Exchange', 'Currency': 'KRW'}, {'Exchange': 'SIX Swiss Exchange', 'Currency': 'CHF'}, {'Exchange': 'Taiwan Stock Exchange', 'Currency': 'TWD'}, {'Exchange': 'Johannesburg Stock Exchange', 'Currency': 'ZAR'}], 'var_functions.query_db:9': [{'Index': '000001.SS'}, {'Index': '399001.SZ'}, {'Index': 'GDAXI'}, {'Index': 'GSPTSE'}, {'Index': 'HSI'}, {'Index': 'IXIC'}, {'Index': 'J203.JO'}, {'Index': 'N100'}, {'Index': 'N225'}, {'Index': 'NSEI'}, {'Index': 'NYA'}, {'Index': 'SSMI'}, {'Index': 'TWII'}], 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json', 'var_functions.list_db:20': ['index_info'], 'var_functions.query_db:22': 'file_storage/functions.query_db:22.json', 'var_functions.query_db:28': [{'Index': 'J203.JO', 'days': '1854', 'first_date': '2012-02-08 00:00:00', 'last_date': 'September 30, 2019 at 12:00 AM', 'min_price': '2302.1214454000005', 'max_price': '4805.917265800001'}, {'Index': 'IXIC', 'days': '7351', 'first_date': '2000-01-06 00:00:00', 'last_date': 'September 30, 2015 at 12:00 AM', 'min_price': '55.48', 'max_price': '14138.78027'}, {'Index': 'HSI', 'days': '5604', 'first_date': '2000-01-14 00:00:00', 'last_date': 'September 30, 2019 at 12:00 AM', 'min_price': '265.27799688', 'max_price': '4310.0357417000005'}, {'Index': 'NYA', 'days': '7960', 'first_date': '2000-01-03 00:00:00', 'last_date': 'September 30, 2020 at 12:00 AM', 'min_price': '347.769989', 'max_price': '16590.42969'}, {'Index': '000001.SS', 'days': '4354', 'first_date': '2000-01-04 00:00:00', 'last_date': 'September 30, 2015 at 12:00 AM', 'min_price': '161.9355176', 'max_price': '965.80492192'}, {'Index': 'SSMI', 'days': '5188', 'first_date': '2000-01-05 00:00:00', 'last_date': 'September 30, 2020 at 12:00 AM', 'min_price': '1466.19902664', 'max_price': '12683.026932900002'}, {'Index': 'TWII', 'days': '4385', 'first_date': '2000-01-17 00:00:00', 'last_date': 'September 30, 2020 at 12:00 AM', 'min_price': '137.8504004', 'max_price': '703.8360156'}, {'Index': 'N225', 'days': '7979', 'first_date': '2000-01-04 00:00:00', 'last_date': 'September 30, 2020 at 12:00 AM', 'min_price': '10.2677002', 'max_price': '388.7694141'}, {'Index': 'GSPTSE', 'days': '6506', 'first_date': '2000-01-05 00:00:00', 'last_date': 'September 30, 2016 at 12:00 AM', 'min_price': '1122.40904067', 'max_price': '16477.325352599997'}, {'Index': 'NSEI', 'days': '2577', 'first_date': '2007-09-25 00:00:00', 'last_date': 'September 30, 2014 at 12:00 AM', 'min_price': '25.24199951', 'max_price': '155.8279981'}, {'Index': 'GDAXI', 'days': '5590', 'first_date': '2000-01-05 00:00:00', 'last_date': 'September 30, 2016 at 12:00 AM', 'min_price': '1158.0727878', 'max_price': '18934.3761734'}, {'Index': 'N100', 'days': '4245', 'first_date': '2000-01-10 00:00:00', 'last_date': 'September 30, 2019 at 12:00 AM', 'min_price': '531.27340122', 'max_price': '1541.6163939'}, {'Index': '399001.SZ', 'days': '4355', 'first_date': '2000-01-05 00:00:00', 'last_date': 'September 30, 2015 at 12:00 AM', 'min_price': '411.37601568', 'max_price': '3124.9840624'}], 'var_functions.query_db:31': 'file_storage/functions.query_db:31.json', 'var_functions.query_db:32': [{'Exchange': 'New York Stock Exchange'}, {'Exchange': 'NASDAQ'}, {'Exchange': 'Hong Kong Stock Exchange'}, {'Exchange': 'Shanghai Stock Exchange'}, {'Exchange': 'Tokyo Stock Exchange'}, {'Exchange': 'Euronext'}, {'Exchange': 'Shenzhen Stock Exchange'}, {'Exchange': 'Toronto Stock Exchange'}, {'Exchange': 'National Stock Exchange of India'}, {'Exchange': 'Frankfurt Stock Exchange'}, {'Exchange': 'Korea Exchange'}, {'Exchange': 'SIX Swiss Exchange'}, {'Exchange': 'Taiwan Stock Exchange'}, {'Exchange': 'Johannesburg Stock Exchange'}], 'var_functions.query_db:34': 'file_storage/functions.query_db:34.json', 'var_functions.query_db:38': 'file_storage/functions.query_db:38.json', 'var_functions.query_db:42': 'file_storage/functions.query_db:42.json', 'var_functions.query_db:44': [{'Index': '000001.SS', 'first_date': '2000-01-04 00:00:00', 'last_date': '2020-12-30 00:00:00', 'records': '1676'}, {'Index': '399001.SZ', 'first_date': '2000-01-05 00:00:00', 'last_date': '2020-12-30 00:00:00', 'records': '1718'}, {'Index': 'GDAXI', 'first_date': '2000-01-05 00:00:00', 'last_date': '2020-12-29 00:00:00', 'records': '1798'}, {'Index': 'GSPTSE', 'first_date': '2000-01-05 00:00:00', 'last_date': '2020-12-31 00:00:00', 'records': '1769'}, {'Index': 'HSI', 'first_date': '2000-01-14 00:00:00', 'last_date': '2020-12-31 00:00:00', 'records': '1677'}, {'Index': 'IXIC', 'first_date': '2000-01-06 00:00:00', 'last_date': '2020-12-29 00:00:00', 'records': '1812'}, {'Index': 'J203.JO', 'first_date': '2012-02-08 00:00:00', 'last_date': '2020-12-18 00:00:00', 'records': '731'}, {'Index': 'N100', 'first_date': '2000-01-10 00:00:00', 'last_date': '2020-12-31 00:00:00', 'records': '1744'}, {'Index': 'N225', 'first_date': '2000-01-04 00:00:00', 'last_date': '2020-12-30 00:00:00', 'records': '1703'}, {'Index': 'NSEI', 'first_date': '2007-09-25 00:00:00', 'last_date': '2020-12-31 00:00:00', 'records': '1048'}, {'Index': 'NYA', 'first_date': '2000-01-03 00:00:00', 'last_date': '2020-12-28 00:00:00', 'records': '1779'}, {'Index': 'SSMI', 'first_date': '2000-01-05 00:00:00', 'last_date': '2020-12-30 00:00:00', 'records': '1714'}, {'Index': 'TWII', 'first_date': '2000-01-17 00:00:00', 'last_date': '2020-12-25 00:00:00', 'records': '1721'}], 'var_functions.query_db:48': 'file_storage/functions.query_db:48.json'}

exec(code, env_args)
