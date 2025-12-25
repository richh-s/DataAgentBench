code = """import pandas as pd
import json
import os
from dateutil import parser

# Load data
file_path = locals()['var_function-call-9022757848387367442']
with open(file_path, 'r') as f:
    data = json.load(f)

df = pd.DataFrame(data)

# Convert CloseUSD to numeric
# Errors='coerce' will turn non-parseable strings to NaN
df['CloseUSD'] = pd.to_numeric(df['CloseUSD'], errors='coerce')
df.dropna(subset=['CloseUSD'], inplace=True)

# Parse Date
try:
    df['Date'] = pd.to_datetime(df['Date'], format='mixed')
except:
    df['Date'] = df['Date'].apply(parser.parse)

# Filter for >= 2000-01-01
df = df[df['Date'] >= '2000-01-01'].copy()

# Sort
df.sort_values(by=['Index', 'Date'], inplace=True)

# Add Year-Month column
df['YearMonth'] = df['Date'].dt.to_period('M')

# Select the first trading day of each month
monthly_investments = df.groupby(['Index', 'YearMonth']).first().reset_index()

# Calculate returns
results = []
indices = df['Index'].unique()

for idx in indices:
    idx_data = monthly_investments[monthly_investments['Index'] == idx]
    
    if idx_data.empty:
        continue
        
    # Investment strategy: Invest $1 each month
    units_bought = 1.0 / idx_data['CloseUSD']
    total_units = units_bought.sum()
    total_invested = len(idx_data) # $1 * number of months
    
    # Final value using the very last available price
    last_price = df[df['Index'] == idx].iloc[-1]['CloseUSD']
    
    final_value = total_units * last_price
    
    if total_invested > 0:
        roi = (final_value - total_invested) / total_invested
    else:
        roi = 0
    
    results.append({
        'Index': idx,
        'ROI': roi,
        'Total_Invested': total_invested,
        'Final_Value': final_value
    })

results_df = pd.DataFrame(results)
results_df.sort_values(by='ROI', ascending=False, inplace=True)
top_5 = results_df.head(5)

# Country Mapping
country_map = {
    "N225": "Japan",
    "HSI": "Hong Kong",
    "NYA": "United States",
    "IXIC": "United States",
    "GDAXI": "Germany",
    "000001.SS": "China",
    "399001.SZ": "China",
    "GSPTSE": "Canada",
    "NSEI": "India",
    "SSMI": "Switzerland",
    "TWII": "Taiwan",
    "J203.JO": "South Africa",
    "N100": "Europe" 
}

final_output = []
for _, row in top_5.iterrows():
    idx = row['Index']
    country = country_map.get(idx, "Unknown")
    final_output.append({
        "Index": idx,
        "Country": country,
        "ROI_Percent": round(row['ROI'] * 100, 2)
    })

print("__RESULT__:")
print(json.dumps(final_output))"""

env_args = {'var_function-call-17525473965656348366': ['index_info'], 'var_function-call-3452483382046624346': ['index_trade'], 'var_function-call-12593582505441031887': [{'Exchange': 'New York Stock Exchange', 'Currency': 'USD'}, {'Exchange': 'NASDAQ', 'Currency': 'USD'}, {'Exchange': 'Hong Kong Stock Exchange', 'Currency': 'HKD'}, {'Exchange': 'Shanghai Stock Exchange', 'Currency': 'CNY'}, {'Exchange': 'Tokyo Stock Exchange', 'Currency': 'JPY'}], 'var_function-call-6368262193383318313': [{'Index': 'J203.JO'}, {'Index': 'N225'}, {'Index': 'GSPTSE'}, {'Index': 'NSEI'}, {'Index': 'GDAXI'}, {'Index': 'IXIC'}, {'Index': 'HSI'}, {'Index': 'NYA'}, {'Index': '000001.SS'}, {'Index': 'SSMI'}, {'Index': 'TWII'}, {'Index': 'N100'}, {'Index': '399001.SZ'}], 'var_function-call-17437071214585225644': [{'Date': '31 Dec 1986, 00:00'}, {'Date': 'January 02, 1987 at 12:00 AM'}, {'Date': '1987-01-05 00:00:00'}, {'Date': '06 Jan 1987, 00:00'}, {'Date': '07 Jan 1987, 00:00'}], 'var_function-call-2332105594782792239': [{'count_star()': '104224'}], 'var_function-call-9321045524774388209': [{'count_star()': '0'}], 'var_function-call-4622754187584196602': [{'Exchange': 'New York Stock Exchange', 'Currency': 'USD'}, {'Exchange': 'NASDAQ', 'Currency': 'USD'}, {'Exchange': 'Hong Kong Stock Exchange', 'Currency': 'HKD'}, {'Exchange': 'Shanghai Stock Exchange', 'Currency': 'CNY'}, {'Exchange': 'Tokyo Stock Exchange', 'Currency': 'JPY'}, {'Exchange': 'Euronext', 'Currency': 'EUR'}, {'Exchange': 'Shenzhen Stock Exchange', 'Currency': 'CNY'}, {'Exchange': 'Toronto Stock Exchange', 'Currency': 'CAD'}, {'Exchange': 'National Stock Exchange of India', 'Currency': 'INR'}, {'Exchange': 'Frankfurt Stock Exchange', 'Currency': 'EUR'}, {'Exchange': 'Korea Exchange', 'Currency': 'KRW'}, {'Exchange': 'SIX Swiss Exchange', 'Currency': 'CHF'}, {'Exchange': 'Taiwan Stock Exchange', 'Currency': 'TWD'}, {'Exchange': 'Johannesburg Stock Exchange', 'Currency': 'ZAR'}], 'var_function-call-9022757848387367442': 'file_storage/function-call-9022757848387367442.json'}

exec(code, env_args)
