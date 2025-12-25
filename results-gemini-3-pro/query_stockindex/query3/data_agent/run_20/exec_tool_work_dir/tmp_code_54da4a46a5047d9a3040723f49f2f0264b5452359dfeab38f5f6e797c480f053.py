code = """import pandas as pd
import json

# Load data
with open(locals()['var_function-call-10331012001117657373'], 'r') as f:
    data = json.load(f)

df = pd.DataFrame(data)
df['Date'] = pd.to_datetime(df['Date'])
df['CloseUSD'] = pd.to_numeric(df['CloseUSD'])

# Sort by Index and Date
df = df.sort_values(['Index', 'Date'])

# Country mapping
country_map = {
    "J203.JO": "South Africa",
    "N225": "Japan",
    "GSPTSE": "Canada",
    "NSEI": "India",
    "GDAXI": "Germany",
    "IXIC": "USA",
    "HSI": "Hong Kong",
    "NYA": "USA",
    "000001.SS": "China",
    "SSMI": "Switzerland",
    "TWII": "Taiwan",
    "N100": "Europe",
    "399001.SZ": "China"
}

results = []

for index_name, group in df.groupby('Index'):
    # Resample to get the first trading day of each month
    # We can do this by setting Date as index and resampling
    group = group.set_index('Date')
    # Resample to month start, taking the first available 'CloseUSD'
    monthly_data = group.resample('MS').first().dropna()
    
    # Check if data starts near 2000
    # The query asks "since 2000". If an index starts much later, it might not be fair,
    # but the user asks "if an investor had made... since 2000".
    # If data is missing for early 2000s, we can only invest when data is available.
    # But usually this implies we start in 2000.
    # Let's assume we start investing from the first available month in the dataset (which is filtered >= 2000-01-01)
    
    monthly_investment = 1000.0
    total_units = 0.0
    total_invested = 0.0
    
    for date, row in monthly_data.iterrows():
        price = row['CloseUSD']
        units = monthly_investment / price
        total_units += units
        total_invested += monthly_investment
        
    # Final value
    # We need the latest price available in the dataset, not necessarily the month start of the last month
    # But for consistency, let's use the last available price in the original group
    last_price = group.iloc[-1]['CloseUSD']
    final_value = total_units * last_price
    
    overall_return = (final_value - total_invested) / total_invested
    
    results.append({
        "Index": index_name,
        "Country": country_map.get(index_name, "Unknown"),
        "Total_Invested": total_invested,
        "Final_Value": final_value,
        "Return": overall_return,
        "Start_Date": monthly_data.index[0].strftime('%Y-%m-%d'),
        "End_Date": group.index[-1].strftime('%Y-%m-%d')
    })

# Convert to DataFrame to sort
results_df = pd.DataFrame(results)
results_df = results_df.sort_values('Return', ascending=False)

top_5 = results_df.head(5)[['Index', 'Country', 'Return']]

print("__RESULT__:")
print(top_5.to_json(orient='records'))"""

env_args = {'var_function-call-12320111116943804548': ['index_info'], 'var_function-call-12320111116943804071': ['index_trade'], 'var_function-call-7371888173575617540': [{'Exchange': 'New York Stock Exchange', 'Currency': 'USD'}, {'Exchange': 'NASDAQ', 'Currency': 'USD'}, {'Exchange': 'Hong Kong Stock Exchange', 'Currency': 'HKD'}, {'Exchange': 'Shanghai Stock Exchange', 'Currency': 'CNY'}, {'Exchange': 'Tokyo Stock Exchange', 'Currency': 'JPY'}], 'var_function-call-3489654952358117405': [{'Index': 'J203.JO'}, {'Index': 'N225'}, {'Index': 'GSPTSE'}, {'Index': 'NSEI'}, {'Index': 'GDAXI'}, {'Index': 'IXIC'}, {'Index': 'HSI'}, {'Index': 'NYA'}, {'Index': '000001.SS'}, {'Index': 'SSMI'}, {'Index': 'TWII'}, {'Index': 'N100'}, {'Index': '399001.SZ'}], 'var_function-call-10331012001117657373': 'file_storage/function-call-10331012001117657373.json'}

exec(code, env_args)
