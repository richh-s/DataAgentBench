code = """import pandas as pd
import json
import numpy as np

file_path = locals()['var_function-call-7351229990786155510']

with open(file_path, 'r') as f:
    data = json.load(f)

df = pd.DataFrame(data)

# Try to clean Date
# First, try to convert using to_datetime without arguments (it uses dateutil parser usually)
# If it fails, we handle it.
# We can use errors='coerce' to turn bad dates to NaT
df['Date'] = pd.to_datetime(df['Date'], errors='coerce')

# Drop rows with invalid dates
df = df.dropna(subset=['Date'])

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

indices = df['Index'].unique()
print(f"Indices found: {indices}")

for idx, group in df.groupby('Index'):
    group_reset = group.reset_index(drop=True)
    # Group by Year-Month
    group_reset['YM'] = group_reset['Date'].dt.to_period('M')
    invest_dates = group_reset.groupby('YM').first()
    
    # Filter >= 2000-01-01
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

env_args = {'var_function-call-15152579714944318513': ['index_info'], 'var_function-call-15152579714944316350': ['index_trade'], 'var_function-call-639504378125954384': [{'Exchange': 'New York Stock Exchange', 'Currency': 'USD'}, {'Exchange': 'NASDAQ', 'Currency': 'USD'}, {'Exchange': 'Hong Kong Stock Exchange', 'Currency': 'HKD'}, {'Exchange': 'Shanghai Stock Exchange', 'Currency': 'CNY'}, {'Exchange': 'Tokyo Stock Exchange', 'Currency': 'JPY'}], 'var_function-call-8645442487183065632': [{'Index': 'N225'}, {'Index': 'GSPTSE'}, {'Index': 'NSEI'}, {'Index': 'GDAXI'}, {'Index': 'IXIC'}, {'Index': 'HSI'}, {'Index': 'J203.JO'}, {'Index': 'NYA'}, {'Index': '000001.SS'}, {'Index': 'SSMI'}, {'Index': 'TWII'}, {'Index': 'N100'}, {'Index': '399001.SZ'}], 'var_function-call-7351229990786155510': 'file_storage/function-call-7351229990786155510.json', 'var_function-call-11488696693555089296': [{'Index': 'IXIC', 'Country': 'United States', 'Overall Return': 20.2129290069}, {'Index': 'NYA', 'Country': 'United States', 'Overall Return': 10.9859830713}, {'Index': 'N225', 'Country': 'Japan', 'Overall Return': 6.6072657707}, {'Index': 'HSI', 'Country': 'Hong Kong', 'Overall Return': 3.4665266996}, {'Index': 'GSPTSE', 'Country': 'Canada', 'Overall Return': 2.8950940057}], 'var_function-call-15039378581609006374': [{'Index': 'IXIC', 'Country': 'United States', 'Start Date': '2000-01-06 00:00:00', 'End Date': 'September 30, 2015 at 12:00 AM', 'Total Invested': 488000, 'Final Value': 10351909.355346203, 'Overall Return': 20.2129290069}, {'Index': 'NYA', 'Country': 'United States', 'Start Date': '2000-01-03 00:00:00', 'End Date': 'September 30, 2020 at 12:00 AM', 'Total Invested': 488000, 'Final Value': 5849159.7388037015, 'Overall Return': 10.9859830713}, {'Index': 'N225', 'Country': 'Japan', 'Start Date': '2000-01-04 00:00:00', 'End Date': 'September 30, 2020 at 12:00 AM', 'Total Invested': 485000, 'Final Value': 3689523.8988038315, 'Overall Return': 6.6072657707}, {'Index': 'HSI', 'Country': 'Hong Kong', 'Start Date': '2000-01-14 00:00:00', 'End Date': 'September 30, 2019 at 12:00 AM', 'Total Invested': 488000, 'Final Value': 2179665.0293991743, 'Overall Return': 3.4665266996}, {'Index': 'GSPTSE', 'Country': 'Canada', 'Start Date': '2000-01-05 00:00:00', 'End Date': 'September 30, 2016 at 12:00 AM', 'Total Invested': 486000, 'Final Value': 1893015.686757455, 'Overall Return': 2.8950940057}, {'Index': 'GDAXI', 'Country': 'Germany', 'Start Date': '2000-01-05 00:00:00', 'End Date': 'September 30, 2016 at 12:00 AM', 'Total Invested': 485000, 'Final Value': 1878005.7970944976, 'Overall Return': 2.8721769012}, {'Index': 'SSMI', 'Country': 'Switzerland', 'Start Date': '2000-01-05 00:00:00', 'End Date': 'September 30, 2020 at 12:00 AM', 'Total Invested': 487000, 'Final Value': 1318390.7939827074, 'Overall Return': 1.7071679548}, {'Index': '399001.SZ', 'Country': 'China', 'Start Date': '2000-01-05 00:00:00', 'End Date': 'September 30, 2015 at 12:00 AM', 'Total Invested': 489000, 'Final Value': 981130.8105138686, 'Overall Return': 1.0064024755}, {'Index': 'TWII', 'Country': 'Taiwan', 'Start Date': '2000-01-17 00:00:00', 'End Date': 'September 30, 2020 at 12:00 AM', 'Total Invested': 487000, 'Final Value': 856042.5938398953, 'Overall Return': 0.757787667}, {'Index': '000001.SS', 'Country': 'China', 'Start Date': '2000-01-04 00:00:00', 'End Date': 'September 30, 2015 at 12:00 AM', 'Total Invested': 488000, 'Final Value': 820455.7009406734, 'Overall Return': 0.6812616823}]}

exec(code, env_args)
