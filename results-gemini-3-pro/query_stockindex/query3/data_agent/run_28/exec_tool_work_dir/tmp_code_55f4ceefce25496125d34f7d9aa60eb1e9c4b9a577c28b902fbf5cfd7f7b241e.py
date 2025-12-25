code = """import json
import pandas as pd
from dateutil import parser

# Load data
with open(locals()['var_function-call-14740721055669295453'], 'r') as f:
    data = json.load(f)

df = pd.DataFrame(data)

# Parse dates
# The dates are messy. use dateutil.parser.parse which is robust.
# However, it can be slow on large lists.
# Let's try to normalize format first if possible, or just apply parser.
# Given 3 patterns seen:
# 1. "03 Jan 2000, 00:00"
# 2. "January 04, 2000 at 12:00 AM"
# 3. "2000-01-14 00:00:00"

def parse_date(d_str):
    try:
        return parser.parse(d_str)
    except:
        return None

# Apply parsing (might take a moment, but for filtered dataset should be fine)
# Note: The loaded data is already filtered for strings containing '200', '201', '202'.
# But checking length first.
# print(f"Rows: {len(df)}") 

df['Date_Parsed'] = df['Date'].apply(parse_date)

# Filter valid dates and Date >= 2000-01-01
df = df.dropna(subset=['Date_Parsed'])
df = df[df['Date_Parsed'] >= pd.Timestamp('2000-01-01')]

# Ensure CloseUSD is float
df['CloseUSD'] = pd.to_numeric(df['CloseUSD'], errors='coerce')
df = df.dropna(subset=['CloseUSD'])

# Sort by Index and Date
df = df.sort_values(by=['Index', 'Date_Parsed'])

# Monthly Investment Simulation
results = []
indices = df['Index'].unique()

for idx in indices:
    sub = df[df['Index'] == idx].copy()
    
    if sub.empty:
        continue
        
    # Create a 'YearMonth' column
    sub['YearMonth'] = sub['Date_Parsed'].dt.to_period('M')
    
    # Group by YearMonth and take the first entry (Monthly Investment)
    # We invest on the first trading day of the month.
    monthly_invest = sub.groupby('YearMonth').first().reset_index()
    
    # Investment details
    monthly_amount = 1.0
    total_invested = len(monthly_invest) * monthly_amount
    
    # Calculate units bought
    # Units = Investment / Price
    units_bought = (monthly_amount / monthly_invest['CloseUSD']).sum()
    
    # Final Value
    # Current Value of Portfolio = Total Units * Last Available Price
    last_price = sub.iloc[-1]['CloseUSD']
    final_value = units_bought * last_price
    
    # Overall Return
    # Return = (Final Value - Total Invested) / Total Invested
    if total_invested > 0:
        overall_return = (final_value - total_invested) / total_invested
    else:
        overall_return = 0
        
    results.append({
        'Index': idx,
        'Return': overall_return,
        'Total_Invested': total_invested,
        'Final_Value': final_value,
        'Start_Date': sub.iloc[0]['Date_Parsed'],
        'End_Date': sub.iloc[-1]['Date_Parsed']
    })

results_df = pd.DataFrame(results)
results_df = results_df.sort_values(by='Return', ascending=False)

# Mapping to Countries (based on Index/Exchange info)
country_map = {
    "HSI": "Hong Kong",
    "N225": "Japan",
    "GSPTSE": "Canada",
    "NSEI": "India",
    "GDAXI": "Germany",
    "IXIC": "United States", # NASDAQ
    "NYA": "United States", # NYSE
    "N100": "Europe",
    "399001.SZ": "China",
    "000001.SS": "China",
    "SSMI": "Switzerland",
    "TWII": "Taiwan",
    "J203.JO": "South Africa"
}

results_df['Country'] = results_df['Index'].map(country_map)

# Print top 5
top_5 = results_df.head(5)[['Index', 'Country', 'Return']]
print("__RESULT__:")
print(top_5.to_json(orient='records'))"""

env_args = {'var_function-call-1465575915268182391': ['index_info'], 'var_function-call-1465575915268183182': ['index_trade'], 'var_function-call-9877151531753513932': [{'Exchange': 'New York Stock Exchange', 'Currency': 'USD'}, {'Exchange': 'NASDAQ', 'Currency': 'USD'}, {'Exchange': 'Hong Kong Stock Exchange', 'Currency': 'HKD'}, {'Exchange': 'Shanghai Stock Exchange', 'Currency': 'CNY'}, {'Exchange': 'Tokyo Stock Exchange', 'Currency': 'JPY'}], 'var_function-call-9877151531753516503': [{'Index': 'HSI', 'Date': '31 Dec 1986, 00:00', 'Open': '2568.300049', 'High': '2568.300049', 'Low': '2568.300049', 'Close': '2568.300049', 'Adj Close': '2568.300049', 'CloseUSD': '333.87900637'}, {'Index': 'HSI', 'Date': 'January 02, 1987 at 12:00 AM', 'Open': '2540.100098', 'High': '2540.100098', 'Low': '2540.100098', 'Close': '2540.100098', 'Adj Close': '2540.100098', 'CloseUSD': '330.21301274'}, {'Index': 'HSI', 'Date': '1987-01-05 00:00:00', 'Open': '2552.399902', 'High': '2552.399902', 'Low': '2552.399902', 'Close': '2552.399902', 'Adj Close': '2552.399902', 'CloseUSD': '331.81198726'}, {'Index': 'HSI', 'Date': '06 Jan 1987, 00:00', 'Open': '2583.899902', 'High': '2583.899902', 'Low': '2583.899902', 'Close': '2583.899902', 'Adj Close': '2583.899902', 'CloseUSD': '335.90698726000005'}, {'Index': 'HSI', 'Date': '07 Jan 1987, 00:00', 'Open': '2607.100098', 'High': '2607.100098', 'Low': '2607.100098', 'Close': '2607.100098', 'Adj Close': '2607.100098', 'CloseUSD': '338.92301274'}], 'var_function-call-14537918089797713165': [{'Exchange': 'New York Stock Exchange', 'Currency': 'USD'}, {'Exchange': 'NASDAQ', 'Currency': 'USD'}, {'Exchange': 'Hong Kong Stock Exchange', 'Currency': 'HKD'}, {'Exchange': 'Shanghai Stock Exchange', 'Currency': 'CNY'}, {'Exchange': 'Tokyo Stock Exchange', 'Currency': 'JPY'}, {'Exchange': 'Euronext', 'Currency': 'EUR'}, {'Exchange': 'Shenzhen Stock Exchange', 'Currency': 'CNY'}, {'Exchange': 'Toronto Stock Exchange', 'Currency': 'CAD'}, {'Exchange': 'National Stock Exchange of India', 'Currency': 'INR'}, {'Exchange': 'Frankfurt Stock Exchange', 'Currency': 'EUR'}, {'Exchange': 'Korea Exchange', 'Currency': 'KRW'}, {'Exchange': 'SIX Swiss Exchange', 'Currency': 'CHF'}, {'Exchange': 'Taiwan Stock Exchange', 'Currency': 'TWD'}, {'Exchange': 'Johannesburg Stock Exchange', 'Currency': 'ZAR'}], 'var_function-call-14537918089797710198': [{'Index': 'J203.JO'}, {'Index': 'N225'}, {'Index': 'GSPTSE'}, {'Index': 'NSEI'}, {'Index': 'GDAXI'}, {'Index': 'IXIC'}, {'Index': 'HSI'}, {'Index': 'NYA'}, {'Index': 'N100'}, {'Index': '399001.SZ'}, {'Index': '000001.SS'}, {'Index': 'SSMI'}, {'Index': 'TWII'}], 'var_function-call-14740721055669295453': 'file_storage/function-call-14740721055669295453.json'}

exec(code, env_args)
