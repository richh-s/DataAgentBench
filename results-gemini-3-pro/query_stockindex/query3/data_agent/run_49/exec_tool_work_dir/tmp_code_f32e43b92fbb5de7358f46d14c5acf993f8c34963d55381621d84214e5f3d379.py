code = """import pandas as pd
import json
import dateutil.parser

# Load data
with open(locals()['var_function-call-13237732875607271320'], 'r') as f:
    data = json.load(f)

df = pd.DataFrame(data)

# Convert Close to numeric
df['Close'] = pd.to_numeric(df['Close'], errors='coerce')
df = df.dropna(subset=['Close'])

# Helper for date parsing
def robust_parse(s):
    try:
        return dateutil.parser.parse(s)
    except:
        return None

# Date parsing
# Clean the string first to help pd.to_datetime
# The format "January 02, 1987 at 12:00 AM" can be handled by dateutil, but let's try to make it standard
# replacing ' at ' with ' ' might help pd.to_datetime in some versions, or not.
# Given the previous error was only about Close, let's assume date parsing logic was mostly fine or didn't run yet.
# But "at" inside date string is definitely non-standard for pd.to_datetime default.

# Let's just use dateutil on unique dates to save time, then map back
unique_dates = df['Date'].unique()
parsed_dates = {}
for d in unique_dates:
    parsed_dates[d] = robust_parse(d)

df['Date'] = df['Date'].map(parsed_dates)
df = df.dropna(subset=['Date'])

# Filter >= 2000
df = df[df['Date'] >= '2000-01-01']

# Sort
df = df.sort_values(['Index', 'Date'])

# Define country mapping
country_map = {
    'HSI': 'Hong Kong',
    'NYA': 'United States',
    'IXIC': 'United States',
    '000001.SS': 'China',
    'N225': 'Japan',
    'N100': 'Europe', 
    '399001.SZ': 'China',
    'GSPTSE': 'Canada',
    'NSEI': 'India',
    'GDAXI': 'Germany',
    'SSMI': 'Switzerland',
    'TWII': 'Taiwan',
    'J203.JO': 'South Africa'
}

# Calculate returns
results = []
indices = df['Index'].unique()

for idx in indices:
    sub_df = df[df['Index'] == idx].copy()
    if sub_df.empty:
        continue
        
    sub_df['YearMonth'] = sub_df['Date'].dt.to_period('M')
    
    # Get first trading day of each month
    monthly_investments = sub_df.groupby('YearMonth').first().reset_index()
    
    # Investment strategy
    # Invest 1 unit each month
    # Avoid division by zero
    monthly_investments = monthly_investments[monthly_investments['Close'] > 0]
    
    monthly_investments['Units'] = 1 / monthly_investments['Close']
    
    total_invested = len(monthly_investments)
    total_units = monthly_investments['Units'].sum()
    
    # Final value
    final_price = sub_df.iloc[-1]['Close']
    final_value = total_units * final_price
    
    # Return
    if total_invested > 0:
        total_return_pct = ((final_value - total_invested) / total_invested) * 100
    else:
        total_return_pct = 0
    
    results.append({
        'Index': idx,
        'Country': country_map.get(idx, 'Unknown'),
        'Return_Pct': total_return_pct
    })

results_df = pd.DataFrame(results)
top_5 = results_df.sort_values('Return_Pct', ascending=False).head(5)

print("__RESULT__:")
print(top_5.to_json(orient='records'))"""

env_args = {'var_function-call-12101079041343883570': ['index_info'], 'var_function-call-12101079041343881597': ['index_trade'], 'var_function-call-4749332889615379040': [{'Exchange': 'New York Stock Exchange', 'Currency': 'USD'}, {'Exchange': 'NASDAQ', 'Currency': 'USD'}, {'Exchange': 'Hong Kong Stock Exchange', 'Currency': 'HKD'}, {'Exchange': 'Shanghai Stock Exchange', 'Currency': 'CNY'}, {'Exchange': 'Tokyo Stock Exchange', 'Currency': 'JPY'}], 'var_function-call-4749332889615378389': [{'Index': 'HSI', 'Date': '31 Dec 1986, 00:00', 'Open': '2568.300049', 'High': '2568.300049', 'Low': '2568.300049', 'Close': '2568.300049', 'Adj Close': '2568.300049', 'CloseUSD': '333.87900637'}, {'Index': 'HSI', 'Date': 'January 02, 1987 at 12:00 AM', 'Open': '2540.100098', 'High': '2540.100098', 'Low': '2540.100098', 'Close': '2540.100098', 'Adj Close': '2540.100098', 'CloseUSD': '330.21301274'}, {'Index': 'HSI', 'Date': '1987-01-05 00:00:00', 'Open': '2552.399902', 'High': '2552.399902', 'Low': '2552.399902', 'Close': '2552.399902', 'Adj Close': '2552.399902', 'CloseUSD': '331.81198726'}, {'Index': 'HSI', 'Date': '06 Jan 1987, 00:00', 'Open': '2583.899902', 'High': '2583.899902', 'Low': '2583.899902', 'Close': '2583.899902', 'Adj Close': '2583.899902', 'CloseUSD': '335.90698726000005'}, {'Index': 'HSI', 'Date': '07 Jan 1987, 00:00', 'Open': '2607.100098', 'High': '2607.100098', 'Low': '2607.100098', 'Close': '2607.100098', 'Adj Close': '2607.100098', 'CloseUSD': '338.92301274'}], 'var_function-call-12489958211256487686': [{'Index': 'J203.JO'}, {'Index': 'IXIC'}, {'Index': 'HSI'}, {'Index': 'NYA'}, {'Index': 'N225'}, {'Index': 'GSPTSE'}, {'Index': 'NSEI'}, {'Index': 'GDAXI'}, {'Index': '000001.SS'}, {'Index': 'SSMI'}, {'Index': 'TWII'}, {'Index': 'N100'}, {'Index': '399001.SZ'}], 'var_function-call-4746713472755702773': [{'Exchange': 'New York Stock Exchange', 'Currency': 'USD'}, {'Exchange': 'NASDAQ', 'Currency': 'USD'}, {'Exchange': 'Hong Kong Stock Exchange', 'Currency': 'HKD'}, {'Exchange': 'Shanghai Stock Exchange', 'Currency': 'CNY'}, {'Exchange': 'Tokyo Stock Exchange', 'Currency': 'JPY'}, {'Exchange': 'Euronext', 'Currency': 'EUR'}, {'Exchange': 'Shenzhen Stock Exchange', 'Currency': 'CNY'}, {'Exchange': 'Toronto Stock Exchange', 'Currency': 'CAD'}, {'Exchange': 'National Stock Exchange of India', 'Currency': 'INR'}, {'Exchange': 'Frankfurt Stock Exchange', 'Currency': 'EUR'}, {'Exchange': 'Korea Exchange', 'Currency': 'KRW'}, {'Exchange': 'SIX Swiss Exchange', 'Currency': 'CHF'}, {'Exchange': 'Taiwan Stock Exchange', 'Currency': 'TWD'}, {'Exchange': 'Johannesburg Stock Exchange', 'Currency': 'ZAR'}], 'var_function-call-13237732875607271320': 'file_storage/function-call-13237732875607271320.json'}

exec(code, env_args)
