code = """import json
import pandas as pd
import datetime

# Load the data
file_path = locals()['var_function-call-18290400044494617747']
with open(file_path, 'r') as f:
    data = json.load(f)

df = pd.DataFrame(data)

# robust datetime conversion
df['Date'] = pd.to_datetime(df['Date'], errors='coerce')
df = df.dropna(subset=['Date'])
df['CloseUSD'] = pd.to_numeric(df['CloseUSD'], errors='coerce')
df = df.dropna(subset=['CloseUSD'])

results = []

for index_name, group in df.groupby('Index'):
    group = group.sort_values('Date')
    
    # Check start date
    min_date = group['Date'].min()
    if min_date > datetime.datetime(2000, 1, 31):
        continue
    
    # Monthly investments
    group['YYYYMM'] = group['Date'].dt.to_period('M')
    monthly_investments = group.groupby('YYYYMM').first()
    
    # Invest 1 unit of currency (USD)
    monthly_investments['Units'] = 1.0 / monthly_investments['CloseUSD']
    
    total_invested = len(monthly_investments)
    total_units = monthly_investments['Units'].sum()
    
    last_price = group.iloc[-1]['CloseUSD']
    final_value = total_units * last_price
    
    if total_invested == 0:
        continue

    overall_return = (final_value - total_invested) / total_invested
    
    results.append({
        'Index': index_name,
        'Return': overall_return,
        'Total_Invested': total_invested,
        'Final_Value': final_value,
        'Start_Date': min_date.strftime('%Y-%m-%d')
    })

results_df = pd.DataFrame(results)
if not results_df.empty:
    results_df = results_df.sort_values('Return', ascending=False)
    top_5 = results_df.head(5).to_dict(orient='records')
else:
    top_5 = []

print("__RESULT__:")
print(json.dumps(top_5))"""

env_args = {'var_function-call-14237980817686352787': ['index_info'], 'var_function-call-14237980817686355800': ['index_trade'], 'var_function-call-6521325472598358813': [{'cid': '0', 'name': 'Exchange', 'type': 'TEXT', 'notnull': '0', 'dflt_value': 'None', 'pk': '0'}, {'cid': '1', 'name': 'Currency', 'type': 'TEXT', 'notnull': '0', 'dflt_value': 'None', 'pk': '0'}], 'var_function-call-6521325472598356170': [{'column_name': 'Index', 'column_type': 'VARCHAR', 'null': 'YES', 'key': 'None', 'default': 'None', 'extra': 'None'}, {'column_name': 'Date', 'column_type': 'VARCHAR', 'null': 'YES', 'key': 'None', 'default': 'None', 'extra': 'None'}, {'column_name': 'Open', 'column_type': 'DOUBLE', 'null': 'YES', 'key': 'None', 'default': 'None', 'extra': 'None'}, {'column_name': 'High', 'column_type': 'DOUBLE', 'null': 'YES', 'key': 'None', 'default': 'None', 'extra': 'None'}, {'column_name': 'Low', 'column_type': 'DOUBLE', 'null': 'YES', 'key': 'None', 'default': 'None', 'extra': 'None'}, {'column_name': 'Close', 'column_type': 'DOUBLE', 'null': 'YES', 'key': 'None', 'default': 'None', 'extra': 'None'}, {'column_name': 'Adj Close', 'column_type': 'DOUBLE', 'null': 'YES', 'key': 'None', 'default': 'None', 'extra': 'None'}, {'column_name': 'CloseUSD', 'column_type': 'DOUBLE', 'null': 'YES', 'key': 'None', 'default': 'None', 'extra': 'None'}], 'var_function-call-8928407560405953400': [{'count_star()': '67948'}], 'var_function-call-18290400044494617747': 'file_storage/function-call-18290400044494617747.json', 'var_function-call-18290400044494615910': [{'Exchange': 'New York Stock Exchange', 'Currency': 'USD'}, {'Exchange': 'NASDAQ', 'Currency': 'USD'}, {'Exchange': 'Hong Kong Stock Exchange', 'Currency': 'HKD'}, {'Exchange': 'Shanghai Stock Exchange', 'Currency': 'CNY'}, {'Exchange': 'Tokyo Stock Exchange', 'Currency': 'JPY'}, {'Exchange': 'Euronext', 'Currency': 'EUR'}, {'Exchange': 'Shenzhen Stock Exchange', 'Currency': 'CNY'}, {'Exchange': 'Toronto Stock Exchange', 'Currency': 'CAD'}, {'Exchange': 'National Stock Exchange of India', 'Currency': 'INR'}, {'Exchange': 'Frankfurt Stock Exchange', 'Currency': 'EUR'}, {'Exchange': 'Korea Exchange', 'Currency': 'KRW'}, {'Exchange': 'SIX Swiss Exchange', 'Currency': 'CHF'}, {'Exchange': 'Taiwan Stock Exchange', 'Currency': 'TWD'}, {'Exchange': 'Johannesburg Stock Exchange', 'Currency': 'ZAR'}]}

exec(code, env_args)
