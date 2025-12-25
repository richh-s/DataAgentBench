code = """import pandas as pd
import json

# Load the data from the stored file
# The key for the file path is 'var_function-call-9554777893084220839'
file_path = locals()['var_function-call-9554777893084220839']
with open(file_path, 'r') as f:
    data = json.load(f)

df = pd.DataFrame(data)
df['Date'] = pd.to_datetime(df['Date'])
df = df.sort_values(['Index', 'Date'])

# Define mapping
index_country_map = {
    "N225": "Japan",
    "HSI": "Hong Kong",
    "NYA": "United States",
    "IXIC": "United States",
    "000001.SS": "China",
    "399001.SZ": "China",
    "GSPTSE": "Canada",
    "NSEI": "India",
    "GDAXI": "Germany",
    "SSMI": "Switzerland",
    "TWII": "Taiwan",
    "J203.JO": "South Africa",
    "N100": "Europe"
}

results = []

for index_name, group in df.groupby('Index'):
    # Monthly investments
    # Create YearMonth column
    group = group.copy()
    group['YearMonth'] = group['Date'].dt.to_period('M')
    
    # Get first trading day of each month
    # We group by YearMonth and take the first entry (since it's sorted by Date)
    monthly_investments = group.groupby('YearMonth', as_index=False).first()
    
    # Ensure we use CloseUSD
    # If CloseUSD is missing or 0, we should handle it. 
    # Let's assume data is clean enough or drop NaNs.
    monthly_investments = monthly_investments[monthly_investments['CloseUSD'] > 0].copy()
    
    if monthly_investments.empty:
        continue
        
    # Invest 1 unit of currency (USD) each month
    monthly_investments['Units_Purchased'] = 1.0 / monthly_investments['CloseUSD']
    
    total_units = monthly_investments['Units_Purchased'].sum()
    total_invested = len(monthly_investments)
    
    # Current Value
    # Get the very last price available in the dataset for this index
    current_price = group.iloc[-1]['CloseUSD']
    
    final_value = total_units * current_price
    
    overall_return = (final_value - total_invested) / total_invested * 100
    
    country = index_country_map.get(index_name, "Unknown")
    
    results.append({
        "Index": index_name,
        "Country": country,
        "Return": overall_return,
        "Total_Invested": total_invested,
        "Final_Value": final_value
    })

# Sort by Return descending
results_df = pd.DataFrame(results).sort_values('Return', ascending=False)
top_5 = results_df.head(5)

print("__RESULT__:")
print(json.dumps(top_5.to_dict(orient='records')))"""

env_args = {'var_function-call-12267509282429008629': ['index_trade'], 'var_function-call-12267509282429009454': ['index_info'], 'var_function-call-12773024537366388109': [{'Index': 'J203.JO'}, {'Index': 'N225'}, {'Index': 'GSPTSE'}, {'Index': 'NSEI'}, {'Index': 'GDAXI'}, {'Index': 'IXIC'}, {'Index': 'HSI'}, {'Index': 'NYA'}, {'Index': '000001.SS'}, {'Index': 'SSMI'}, {'Index': 'TWII'}, {'Index': 'N100'}, {'Index': '399001.SZ'}], 'var_function-call-12773024537366385894': [{'Exchange': 'New York Stock Exchange', 'Currency': 'USD'}, {'Exchange': 'NASDAQ', 'Currency': 'USD'}, {'Exchange': 'Hong Kong Stock Exchange', 'Currency': 'HKD'}, {'Exchange': 'Shanghai Stock Exchange', 'Currency': 'CNY'}, {'Exchange': 'Tokyo Stock Exchange', 'Currency': 'JPY'}, {'Exchange': 'Euronext', 'Currency': 'EUR'}, {'Exchange': 'Shenzhen Stock Exchange', 'Currency': 'CNY'}, {'Exchange': 'Toronto Stock Exchange', 'Currency': 'CAD'}, {'Exchange': 'National Stock Exchange of India', 'Currency': 'INR'}, {'Exchange': 'Frankfurt Stock Exchange', 'Currency': 'EUR'}, {'Exchange': 'Korea Exchange', 'Currency': 'KRW'}, {'Exchange': 'SIX Swiss Exchange', 'Currency': 'CHF'}, {'Exchange': 'Taiwan Stock Exchange', 'Currency': 'TWD'}, {'Exchange': 'Johannesburg Stock Exchange', 'Currency': 'ZAR'}], 'var_function-call-9554777893084220839': 'file_storage/function-call-9554777893084220839.json'}

exec(code, env_args)
