code = """import pandas as pd
import json

# Load data
with open(locals()['var_function-call-15418031616304384514'], 'r') as f:
    data = json.load(f)

df = pd.DataFrame(data)

# Fix Date parsing
# Use mixed format inference
df['Date'] = pd.to_datetime(df['Date'], format='mixed', dayfirst=False, errors='coerce')

# Filter for dates >= 2000-01-01
df = df[df['Date'] >= '2000-01-01']

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
    group = group.set_index('Date')
    monthly_data = group.resample('MS').first().dropna()
    
    # Start monthly investments
    monthly_investment = 1000.0
    total_units = 0.0
    total_invested = 0.0
    
    for date, row in monthly_data.iterrows():
        price = row['CloseUSD']
        if price > 0:
            units = monthly_investment / price
            total_units += units
            total_invested += monthly_investment
        
    # Final value
    # Use the very last available price in the dataset for this index
    if not group.empty:
        last_price = group.iloc[-1]['CloseUSD']
        final_value = total_units * last_price
        
        if total_invested > 0:
            overall_return = (final_value - total_invested) / total_invested
        else:
            overall_return = 0
            
        results.append({
            "Index": index_name,
            "Country": country_map.get(index_name, "Unknown"),
            "Return": overall_return,
            "Final_Value": final_value,
            "Total_Invested": total_invested
        })

# Convert to DataFrame to sort
results_df = pd.DataFrame(results)
results_df = results_df.sort_values('Return', ascending=False)

top_5 = results_df.head(5)[['Index', 'Country', 'Return']]

print("__RESULT__:")
print(top_5.to_json(orient='records'))"""

env_args = {'var_function-call-12320111116943804548': ['index_info'], 'var_function-call-12320111116943804071': ['index_trade'], 'var_function-call-7371888173575617540': [{'Exchange': 'New York Stock Exchange', 'Currency': 'USD'}, {'Exchange': 'NASDAQ', 'Currency': 'USD'}, {'Exchange': 'Hong Kong Stock Exchange', 'Currency': 'HKD'}, {'Exchange': 'Shanghai Stock Exchange', 'Currency': 'CNY'}, {'Exchange': 'Tokyo Stock Exchange', 'Currency': 'JPY'}], 'var_function-call-3489654952358117405': [{'Index': 'J203.JO'}, {'Index': 'N225'}, {'Index': 'GSPTSE'}, {'Index': 'NSEI'}, {'Index': 'GDAXI'}, {'Index': 'IXIC'}, {'Index': 'HSI'}, {'Index': 'NYA'}, {'Index': '000001.SS'}, {'Index': 'SSMI'}, {'Index': 'TWII'}, {'Index': 'N100'}, {'Index': '399001.SZ'}], 'var_function-call-10331012001117657373': 'file_storage/function-call-10331012001117657373.json', 'var_function-call-8974196404492106585': [{'Index': 'IXIC', 'Country': 'USA', 'Return': 39.2222487639}, {'Index': 'NYA', 'Country': 'USA', 'Return': 11.2680318352}, {'Index': 'N225', 'Country': 'Japan', 'Return': 3.6241681327}, {'Index': 'GDAXI', 'Country': 'Germany', 'Return': 3.2899857508}, {'Index': 'GSPTSE', 'Country': 'Canada', 'Return': 2.9656619215}], 'var_function-call-1916111007274748501': {'Min': 55.48, 'Max': 14138.78027, 'Count': 7351, 'First': 3727.129883, 'Last': 4620.160156}, 'var_function-call-4715541387608823558': {'Min_Date': 'October 01, 1974 at 12:00 AM', 'Min_Val': 55.48, 'Max_Date': 'April 26, 2021 at 12:00 AM', 'Max_Val': 14138.78027, 'Last_Date': 'September 30, 2015 at 12:00 AM', 'Last_Val': 4620.160156}, 'var_function-call-15418031616304384514': 'file_storage/function-call-15418031616304384514.json'}

exec(code, env_args)
