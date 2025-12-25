code = """import pandas as pd
import json
import numpy as np

# Load data
file_path = locals()['var_function-call-14266471608875344840']
with open(file_path, 'r') as f:
    data = json.load(f)

df = pd.DataFrame(data)

# Convert CloseUSD to float
# Some values might be invalid or None, handle them
df['CloseUSD'] = pd.to_numeric(df['CloseUSD'], errors='coerce')

# Parse Date
# The dates are mixed format. pd.to_datetime usually handles this well.
df['Date'] = pd.to_datetime(df['Date'], errors='coerce')

# Drop rows with invalid date or CloseUSD
df = df.dropna(subset=['Date', 'CloseUSD'])

# Filter data since 2000-01-01
df = df[df['Date'] >= '2000-01-01']

# Sort by Index and Date
df = df.sort_values(['Index', 'Date'])

# Define function to calculate ROI for an index
def calculate_roi(group):
    # Resample to monthly frequency, taking the first available day
    # Create a YearMonth column
    group['YearMonth'] = group['Date'].dt.to_period('M')
    
    # Drop duplicates to keep first entry per month
    monthly_data = group.drop_duplicates(subset=['YearMonth'], keep='first')
    
    if len(monthly_data) == 0:
        return -1.0 # No data
    
    # Investment Amount per month (e.g., $100)
    investment_amount = 100.0
    
    # Calculate units bought
    monthly_data['Units'] = investment_amount / monthly_data['CloseUSD']
    
    total_units = monthly_data['Units'].sum()
    total_invested = len(monthly_data) * investment_amount
    
    # Final price (last available price in the full dataset for this index)
    # Note: We should use the last price of the index, not just the last monthly price.
    last_price = group.iloc[-1]['CloseUSD']
    
    final_value = total_units * last_price
    
    roi = (final_value - total_invested) / total_invested
    
    return roi

# Calculate ROI for each index
rois = []
indices = df['Index'].unique()

for idx in indices:
    group = df[df['Index'] == idx].copy()
    roi = calculate_roi(group)
    rois.append({'Index': idx, 'ROI': roi})

roi_df = pd.DataFrame(rois)
roi_df = roi_df.sort_values('ROI', ascending=False)

top_5 = roi_df.head(5)

# Mapping to Country
mapping = {
    'J203.JO': 'South Africa',
    'N225': 'Japan',
    'GSPTSE': 'Canada',
    'NSEI': 'India',
    'GDAXI': 'Germany',
    'IXIC': 'United States',
    'HSI': 'Hong Kong',
    'NYA': 'United States',
    '000001.SS': 'China',
    'SSMI': 'Switzerland',
    'TWII': 'Taiwan',
    'N100': 'Europe',
    '399001.SZ': 'China'
}

top_5['Country'] = top_5['Index'].map(mapping)

result_list = top_5[['Index', 'ROI', 'Country']].to_dict(orient='records')

print("__RESULT__:")
print(json.dumps(result_list))"""

env_args = {'var_function-call-15856443943548344881': ['index_info'], 'var_function-call-15856443943548345030': ['index_trade'], 'var_function-call-14547687805056477972': [{'Exchange': 'New York Stock Exchange', 'Currency': 'USD'}, {'Exchange': 'NASDAQ', 'Currency': 'USD'}, {'Exchange': 'Hong Kong Stock Exchange', 'Currency': 'HKD'}, {'Exchange': 'Shanghai Stock Exchange', 'Currency': 'CNY'}, {'Exchange': 'Tokyo Stock Exchange', 'Currency': 'JPY'}], 'var_function-call-14547687805056475955': [{'Index': 'HSI', 'Date': '31 Dec 1986, 00:00', 'Open': '2568.300049', 'High': '2568.300049', 'Low': '2568.300049', 'Close': '2568.300049', 'Adj Close': '2568.300049', 'CloseUSD': '333.87900637'}, {'Index': 'HSI', 'Date': 'January 02, 1987 at 12:00 AM', 'Open': '2540.100098', 'High': '2540.100098', 'Low': '2540.100098', 'Close': '2540.100098', 'Adj Close': '2540.100098', 'CloseUSD': '330.21301274'}, {'Index': 'HSI', 'Date': '1987-01-05 00:00:00', 'Open': '2552.399902', 'High': '2552.399902', 'Low': '2552.399902', 'Close': '2552.399902', 'Adj Close': '2552.399902', 'CloseUSD': '331.81198726'}, {'Index': 'HSI', 'Date': '06 Jan 1987, 00:00', 'Open': '2583.899902', 'High': '2583.899902', 'Low': '2583.899902', 'Close': '2583.899902', 'Adj Close': '2583.899902', 'CloseUSD': '335.90698726000005'}, {'Index': 'HSI', 'Date': '07 Jan 1987, 00:00', 'Open': '2607.100098', 'High': '2607.100098', 'Low': '2607.100098', 'Close': '2607.100098', 'Adj Close': '2607.100098', 'CloseUSD': '338.92301274'}], 'var_function-call-1204772786044151916': [{'Exchange': 'New York Stock Exchange', 'Currency': 'USD'}, {'Exchange': 'NASDAQ', 'Currency': 'USD'}, {'Exchange': 'Hong Kong Stock Exchange', 'Currency': 'HKD'}, {'Exchange': 'Shanghai Stock Exchange', 'Currency': 'CNY'}, {'Exchange': 'Tokyo Stock Exchange', 'Currency': 'JPY'}, {'Exchange': 'Euronext', 'Currency': 'EUR'}, {'Exchange': 'Shenzhen Stock Exchange', 'Currency': 'CNY'}, {'Exchange': 'Toronto Stock Exchange', 'Currency': 'CAD'}, {'Exchange': 'National Stock Exchange of India', 'Currency': 'INR'}, {'Exchange': 'Frankfurt Stock Exchange', 'Currency': 'EUR'}, {'Exchange': 'Korea Exchange', 'Currency': 'KRW'}, {'Exchange': 'SIX Swiss Exchange', 'Currency': 'CHF'}, {'Exchange': 'Taiwan Stock Exchange', 'Currency': 'TWD'}, {'Exchange': 'Johannesburg Stock Exchange', 'Currency': 'ZAR'}], 'var_function-call-1204772786044153029': [{'Index': 'J203.JO'}, {'Index': 'N225'}, {'Index': 'GSPTSE'}, {'Index': 'NSEI'}, {'Index': 'GDAXI'}, {'Index': 'IXIC'}, {'Index': 'HSI'}, {'Index': 'NYA'}, {'Index': '000001.SS'}, {'Index': 'SSMI'}, {'Index': 'TWII'}, {'Index': 'N100'}, {'Index': '399001.SZ'}], 'var_function-call-1644841522759135565': [{'count_star()': '104224'}], 'var_function-call-14266471608875344840': 'file_storage/function-call-14266471608875344840.json'}

exec(code, env_args)
