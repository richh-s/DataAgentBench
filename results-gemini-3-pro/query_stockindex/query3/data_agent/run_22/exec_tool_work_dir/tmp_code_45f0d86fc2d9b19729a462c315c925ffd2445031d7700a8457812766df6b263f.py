code = """import pandas as pd
import json
import warnings

warnings.filterwarnings("ignore")

file_path = locals()['var_function-call-7351229990786155510']

with open(file_path, 'r') as f:
    data = json.load(f)

df = pd.DataFrame(data)
# Try flexible parsing
df['Date'] = pd.to_datetime(df['Date'])
df['Adj Close'] = pd.to_numeric(df['Adj Close'], errors='coerce')
df = df.dropna(subset=['Adj Close'])
df = df.sort_values(['Index', 'Date'])

results = []

country_map = {
    "N225": "Japan",
    "GSPTSE": "Canada",
    "NSEI": "India",
    "GDAXI": "Germany",
    "IXIC": "United States",
    "HSI": "Hong Kong",
    "J203.JO": "South Africa",
    "NYA": "United States",
    "000001.SS": "China",
    "SSMI": "Switzerland",
    "TWII": "Taiwan",
    "N100": "Europe",
    "399001.SZ": "China"
}

for idx, group in df.groupby('Index'):
    group_reset = group.reset_index(drop=True)
    group_reset['YM'] = group_reset['Date'].dt.to_period('M')
    invest_dates = group_reset.groupby('YM').first()
    
    invest_dates = invest_dates[invest_dates['Date'] >= '2000-01-01']
    
    if invest_dates.empty:
        continue
    
    monthly_amount = 1000 
    total_invested = 0
    total_units = 0
    
    for _, row in invest_dates.iterrows():
        price = row['Adj Close']
        units = monthly_amount / price
        total_units += units
        total_invested += monthly_amount
        
    last_price = group_reset.iloc[-1]['Adj Close']
    final_value = total_units * last_price
    
    if total_invested > 0:
        overall_return = (final_value - total_invested) / total_invested
    else:
        overall_return = 0
    
    results.append({
        "Index": idx,
        "Country": country_map.get(idx, "Unknown"),
        "Overall Return": overall_return
    })

results_df = pd.DataFrame(results)
results_df = results_df.sort_values('Overall Return', ascending=False)

print("__RESULT__:")
print(results_df.head(5).to_json(orient='records'))"""

env_args = {'var_function-call-15152579714944318513': ['index_info'], 'var_function-call-15152579714944316350': ['index_trade'], 'var_function-call-639504378125954384': [{'Exchange': 'New York Stock Exchange', 'Currency': 'USD'}, {'Exchange': 'NASDAQ', 'Currency': 'USD'}, {'Exchange': 'Hong Kong Stock Exchange', 'Currency': 'HKD'}, {'Exchange': 'Shanghai Stock Exchange', 'Currency': 'CNY'}, {'Exchange': 'Tokyo Stock Exchange', 'Currency': 'JPY'}], 'var_function-call-8645442487183065632': [{'Index': 'N225'}, {'Index': 'GSPTSE'}, {'Index': 'NSEI'}, {'Index': 'GDAXI'}, {'Index': 'IXIC'}, {'Index': 'HSI'}, {'Index': 'J203.JO'}, {'Index': 'NYA'}, {'Index': '000001.SS'}, {'Index': 'SSMI'}, {'Index': 'TWII'}, {'Index': 'N100'}, {'Index': '399001.SZ'}], 'var_function-call-7351229990786155510': 'file_storage/function-call-7351229990786155510.json'}

exec(code, env_args)
