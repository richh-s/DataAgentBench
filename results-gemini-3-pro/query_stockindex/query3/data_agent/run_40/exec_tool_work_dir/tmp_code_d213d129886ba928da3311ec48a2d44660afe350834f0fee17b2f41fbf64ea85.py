code = """import pandas as pd
import json
import dateutil.parser

# Load index_trade data
file_path = locals()['var_function-call-405685236303482527']
with open(file_path, 'r') as f:
    trade_data = json.load(f)

df = pd.DataFrame(trade_data)

# Parse dates
def parse_date(date_str):
    try:
        return dateutil.parser.parse(date_str)
    except:
        return None

df['Date'] = df['Date'].apply(parse_date)

# Convert CloseUSD to float
df['CloseUSD'] = pd.to_numeric(df['CloseUSD'], errors='coerce')

# Filter valid dates and CloseUSD
df = df.dropna(subset=['Date', 'CloseUSD'])
df = df[df['Date'] >= pd.Timestamp('2000-01-01')]

# Sort by Index and Date
df = df.sort_values(by=['Index', 'Date'])

# Resample to monthly (first trading day)
df['YM'] = df['Date'].dt.to_period('M')
monthly_df = df.groupby(['Index', 'YM']).first().reset_index()

# Calculate returns
results = []
for index_name, group in monthly_df.groupby('Index'):
    group = group.sort_values('Date')
    
    # Simulate monthly investment
    investment_per_month = 1.0
    units_bought = investment_per_month / group['CloseUSD']
    total_units = units_bought.sum()
    total_invested = len(group) * investment_per_month
    
    # Final value
    last_price = group['CloseUSD'].iloc[-1]
    final_value = total_units * last_price
    
    overall_return = (final_value - total_invested) / total_invested
    
    results.append({
        'Index': index_name,
        'Return': overall_return,
        'FinalValue': final_value,
        'TotalInvested': total_invested
    })

results_df = pd.DataFrame(results)
top_5 = results_df.sort_values('Return', ascending=False).head(5)

# Mapping dictionary
index_mapping = {
    "NYA": "USA", 
    "IXIC": "USA", 
    "HSI": "Hong Kong", 
    "000001.SS": "China", 
    "N225": "Japan", 
    "399001.SZ": "China", 
    "GSPTSE": "Canada", 
    "NSEI": "India", 
    "GDAXI": "Germany", 
    "SSMI": "Switzerland", 
    "TWII": "Taiwan", 
    "J203.JO": "South Africa", 
    "N100": "Europe" 
}

top_5['Country'] = top_5['Index'].map(index_mapping)

print("__RESULT__:")
print(top_5[['Index', 'Country', 'Return']].to_json(orient='records'))"""

env_args = {'var_function-call-7463530722576996683': ['index_info'], 'var_function-call-7463530722576994424': ['index_trade'], 'var_function-call-5165717859289830406': [{'Exchange': 'New York Stock Exchange', 'Currency': 'USD'}, {'Exchange': 'NASDAQ', 'Currency': 'USD'}, {'Exchange': 'Hong Kong Stock Exchange', 'Currency': 'HKD'}, {'Exchange': 'Shanghai Stock Exchange', 'Currency': 'CNY'}, {'Exchange': 'Tokyo Stock Exchange', 'Currency': 'JPY'}], 'var_function-call-5165717859289831787': [{'Index': 'J203.JO'}, {'Index': 'N225'}, {'Index': 'GSPTSE'}, {'Index': 'NSEI'}, {'Index': 'GDAXI'}, {'Index': 'IXIC'}, {'Index': 'HSI'}, {'Index': 'NYA'}, {'Index': '000001.SS'}, {'Index': 'SSMI'}, {'Index': 'TWII'}, {'Index': 'N100'}, {'Index': '399001.SZ'}], 'var_function-call-16432162134560375367': [{'Exchange': 'New York Stock Exchange', 'Currency': 'USD'}, {'Exchange': 'NASDAQ', 'Currency': 'USD'}, {'Exchange': 'Hong Kong Stock Exchange', 'Currency': 'HKD'}, {'Exchange': 'Shanghai Stock Exchange', 'Currency': 'CNY'}, {'Exchange': 'Tokyo Stock Exchange', 'Currency': 'JPY'}, {'Exchange': 'Euronext', 'Currency': 'EUR'}, {'Exchange': 'Shenzhen Stock Exchange', 'Currency': 'CNY'}, {'Exchange': 'Toronto Stock Exchange', 'Currency': 'CAD'}, {'Exchange': 'National Stock Exchange of India', 'Currency': 'INR'}, {'Exchange': 'Frankfurt Stock Exchange', 'Currency': 'EUR'}, {'Exchange': 'Korea Exchange', 'Currency': 'KRW'}, {'Exchange': 'SIX Swiss Exchange', 'Currency': 'CHF'}, {'Exchange': 'Taiwan Stock Exchange', 'Currency': 'TWD'}, {'Exchange': 'Johannesburg Stock Exchange', 'Currency': 'ZAR'}], 'var_function-call-8074681657804701164': [{'Date': '31 Dec 1986, 00:00'}, {'Date': 'January 02, 1987 at 12:00 AM'}, {'Date': '1987-01-05 00:00:00'}, {'Date': '06 Jan 1987, 00:00'}, {'Date': '07 Jan 1987, 00:00'}, {'Date': '1987-01-08 00:00:00'}, {'Date': '1987-01-09 00:00:00'}, {'Date': '1987-01-12 00:00:00'}, {'Date': '1987-01-13 00:00:00'}, {'Date': '1987-01-14 00:00:00'}, {'Date': 'January 15, 1987 at 12:00 AM'}, {'Date': 'January 16, 1987 at 12:00 AM'}, {'Date': 'January 19, 1987 at 12:00 AM'}, {'Date': '20 Jan 1987, 00:00'}, {'Date': 'January 21, 1987 at 12:00 AM'}, {'Date': '22 Jan 1987, 00:00'}, {'Date': 'January 23, 1987 at 12:00 AM'}, {'Date': 'January 26, 1987 at 12:00 AM'}, {'Date': '27 Jan 1987, 00:00'}, {'Date': 'January 28, 1987 at 12:00 AM'}], 'var_function-call-10280706891561696089': [{'count_star()': '104224'}], 'var_function-call-405685236303482527': 'file_storage/function-call-405685236303482527.json'}

exec(code, env_args)
