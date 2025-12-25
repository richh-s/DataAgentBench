code = """import pandas as pd
import json
import numpy as np

# Load index_trade data
with open(locals()['var_function-call-4995019058411676957'], 'r') as f:
    trade_data = json.load(f)

df = pd.DataFrame(trade_data)

# Parse Date
# The dates are mixed format. pd.to_datetime with format='mixed' helps.
# Note: 'format="mixed"' is available in pandas >= 2.0. If older, might need to be careful.
# But usually the environment is recent. 
# The preview shows: "31 Dec 1986, 00:00", "January 02, 1987 at 12:00 AM", "1987-01-05 00:00:00"
# These should be parseable.

# Clean up 'at 12:00 AM' which might confuse parser if not mixed
df['Date_clean'] = df['Date'].astype(str).str.replace(' at 12:00 AM', '', regex=False)
df['Date_clean'] = df['Date_clean'].str.replace(', 00:00', '', regex=False)

df['Date'] = pd.to_datetime(df['Date_clean'], errors='coerce')

# Filter >= 2000-01-01
df = df[df['Date'] >= '2000-01-01']

# Convert CloseUSD to float
df['CloseUSD'] = pd.to_numeric(df['CloseUSD'], errors='coerce')

# Drop rows with invalid Date or CloseUSD
df = df.dropna(subset=['Date', 'CloseUSD'])
df = df[df['CloseUSD'] > 0]

# Mapping based on hints and manual inference
# Index -> Exchange -> Country
# J203.JO -> Johannesburg -> South Africa
# N225 -> Tokyo -> Japan
# GSPTSE -> Toronto -> Canada
# NSEI -> National Stock Exchange of India -> India
# GDAXI -> Frankfurt -> Germany
# IXIC -> NASDAQ -> USA
# NYA -> NYSE -> USA
# HSI -> Hong Kong -> Hong Kong
# 000001.SS -> Shanghai -> China
# SSMI -> SIX Swiss -> Switzerland
# TWII -> Taiwan -> Taiwan
# N100 -> Euronext -> Europe
# 399001.SZ -> Shenzhen -> China

index_country_map = {
    'J203.JO': 'South Africa',
    'N225': 'Japan',
    'GSPTSE': 'Canada',
    'NSEI': 'India',
    'GDAXI': 'Germany',
    'IXIC': 'United States',
    'NYA': 'United States',
    'HSI': 'Hong Kong',
    '000001.SS': 'China',
    'SSMI': 'Switzerland',
    'TWII': 'Taiwan',
    'N100': 'Europe',
    '399001.SZ': 'China'
}

# Calculate returns
results = []
indices = df['Index'].unique()

for idx in indices:
    sub = df[df['Index'] == idx].sort_values('Date')
    
    if sub.empty:
        continue
        
    # Group by Year-Month and take first entry
    sub['YearMonth'] = sub['Date'].dt.to_period('M')
    monthly_investments = sub.groupby('YearMonth').first().reset_index()
    
    # Investment strategy
    monthly_amount = 100.0
    units = []
    total_invested = 0.0
    
    for _, row in monthly_investments.iterrows():
        price = row['CloseUSD']
        purchased_units = monthly_amount / price
        units.append(purchased_units)
        total_invested += monthly_amount
        
    total_units = sum(units)
    
    # Final value is based on the LAST available price in the dataset for that index
    last_price = sub.iloc[-1]['CloseUSD']
    final_value = total_units * last_price
    
    overall_return = (final_value - total_invested) / total_invested
    
    results.append({
        'Index': idx,
        'Country': index_country_map.get(idx, 'Unknown'),
        'Total_Invested': total_invested,
        'Final_Value': final_value,
        'Return': overall_return
    })

# Sort by Return descending
results_df = pd.DataFrame(results).sort_values('Return', ascending=False)
top_5 = results_df.head(5)

print("__RESULT__:")
print(top_5.to_json(orient='records'))"""

env_args = {'var_function-call-6351218874878718676': ['index_info'], 'var_function-call-6351218874878721305': ['index_trade'], 'var_function-call-655075090629505893': [{'Exchange': 'New York Stock Exchange', 'Currency': 'USD'}, {'Exchange': 'NASDAQ', 'Currency': 'USD'}, {'Exchange': 'Hong Kong Stock Exchange', 'Currency': 'HKD'}, {'Exchange': 'Shanghai Stock Exchange', 'Currency': 'CNY'}, {'Exchange': 'Tokyo Stock Exchange', 'Currency': 'JPY'}], 'var_function-call-655075090629506308': [{'Index': 'HSI', 'Date': '31 Dec 1986, 00:00', 'Open': '2568.300049', 'High': '2568.300049', 'Low': '2568.300049', 'Close': '2568.300049', 'Adj Close': '2568.300049', 'CloseUSD': '333.87900637'}, {'Index': 'HSI', 'Date': 'January 02, 1987 at 12:00 AM', 'Open': '2540.100098', 'High': '2540.100098', 'Low': '2540.100098', 'Close': '2540.100098', 'Adj Close': '2540.100098', 'CloseUSD': '330.21301274'}, {'Index': 'HSI', 'Date': '1987-01-05 00:00:00', 'Open': '2552.399902', 'High': '2552.399902', 'Low': '2552.399902', 'Close': '2552.399902', 'Adj Close': '2552.399902', 'CloseUSD': '331.81198726'}, {'Index': 'HSI', 'Date': '06 Jan 1987, 00:00', 'Open': '2583.899902', 'High': '2583.899902', 'Low': '2583.899902', 'Close': '2583.899902', 'Adj Close': '2583.899902', 'CloseUSD': '335.90698726000005'}, {'Index': 'HSI', 'Date': '07 Jan 1987, 00:00', 'Open': '2607.100098', 'High': '2607.100098', 'Low': '2607.100098', 'Close': '2607.100098', 'Adj Close': '2607.100098', 'CloseUSD': '338.92301274'}], 'var_function-call-2782381439195642394': [{'cid': '0', 'name': 'Exchange', 'type': 'TEXT', 'notnull': '0', 'dflt_value': 'None', 'pk': '0'}, {'cid': '1', 'name': 'Currency', 'type': 'TEXT', 'notnull': '0', 'dflt_value': 'None', 'pk': '0'}], 'var_function-call-14868652550335193109': [{'Index': 'J203.JO'}, {'Index': 'N225'}, {'Index': 'GSPTSE'}, {'Index': 'NSEI'}, {'Index': 'GDAXI'}, {'Index': 'IXIC'}, {'Index': 'NYA'}, {'Index': 'HSI'}, {'Index': '000001.SS'}, {'Index': 'SSMI'}, {'Index': 'TWII'}, {'Index': 'N100'}, {'Index': '399001.SZ'}], 'var_function-call-14868652550335196314': [{'Exchange': 'New York Stock Exchange', 'Currency': 'USD'}, {'Exchange': 'NASDAQ', 'Currency': 'USD'}, {'Exchange': 'Hong Kong Stock Exchange', 'Currency': 'HKD'}, {'Exchange': 'Shanghai Stock Exchange', 'Currency': 'CNY'}, {'Exchange': 'Tokyo Stock Exchange', 'Currency': 'JPY'}, {'Exchange': 'Euronext', 'Currency': 'EUR'}, {'Exchange': 'Shenzhen Stock Exchange', 'Currency': 'CNY'}, {'Exchange': 'Toronto Stock Exchange', 'Currency': 'CAD'}, {'Exchange': 'National Stock Exchange of India', 'Currency': 'INR'}, {'Exchange': 'Frankfurt Stock Exchange', 'Currency': 'EUR'}, {'Exchange': 'Korea Exchange', 'Currency': 'KRW'}, {'Exchange': 'SIX Swiss Exchange', 'Currency': 'CHF'}, {'Exchange': 'Taiwan Stock Exchange', 'Currency': 'TWD'}, {'Exchange': 'Johannesburg Stock Exchange', 'Currency': 'ZAR'}], 'var_function-call-16537858144805175888': [{'count_star()': '104224'}], 'var_function-call-4995019058411676957': 'file_storage/function-call-4995019058411676957.json'}

exec(code, env_args)
