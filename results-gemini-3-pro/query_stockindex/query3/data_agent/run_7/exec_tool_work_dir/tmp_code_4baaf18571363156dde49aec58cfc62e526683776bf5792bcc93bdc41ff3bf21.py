code = """import json
import pandas as pd

with open(locals()['var_function-call-5773205835372737063'], 'r') as f:
    data = json.load(f)

df = pd.DataFrame(data)
df['Date'] = pd.to_datetime(df['Date'], format='mixed', errors='coerce')

# Filter again just in case the query didn't work as expected (it should have)
df = df[df['Date'] >= '2000-01-01']

stats = []
for name, group in df.groupby('Index'):
    min_date = group['Date'].min()
    max_date = group['Date'].max()
    unique_months = group['Date'].dt.to_period('M').nunique()
    stats.append({
        'Index': name,
        'Min_Date': str(min_date),
        'Max_Date': str(max_date),
        'Months': unique_months,
        'Rows': len(group)
    })

print("__RESULT__:")
print(json.dumps(stats))"""

env_args = {'var_function-call-10021783300953503103': ['index_info'], 'var_function-call-11595194589530822852': [{'Exchange': 'New York Stock Exchange', 'Currency': 'USD'}, {'Exchange': 'NASDAQ', 'Currency': 'USD'}, {'Exchange': 'Hong Kong Stock Exchange', 'Currency': 'HKD'}, {'Exchange': 'Shanghai Stock Exchange', 'Currency': 'CNY'}, {'Exchange': 'Tokyo Stock Exchange', 'Currency': 'JPY'}], 'var_function-call-6069480066467942252': ['index_trade'], 'var_function-call-3250475692665861912': [{'Index': 'J203.JO'}, {'Index': 'IXIC'}, {'Index': 'HSI'}, {'Index': 'N225'}, {'Index': 'GSPTSE'}, {'Index': 'NSEI'}, {'Index': 'GDAXI'}, {'Index': '000001.SS'}, {'Index': 'SSMI'}, {'Index': 'TWII'}, {'Index': 'N100'}, {'Index': '399001.SZ'}, {'Index': 'NYA'}], 'var_function-call-14715549604581522807': [{'Exchange': 'New York Stock Exchange', 'Currency': 'USD'}, {'Exchange': 'NASDAQ', 'Currency': 'USD'}, {'Exchange': 'Hong Kong Stock Exchange', 'Currency': 'HKD'}, {'Exchange': 'Shanghai Stock Exchange', 'Currency': 'CNY'}, {'Exchange': 'Tokyo Stock Exchange', 'Currency': 'JPY'}, {'Exchange': 'Euronext', 'Currency': 'EUR'}, {'Exchange': 'Shenzhen Stock Exchange', 'Currency': 'CNY'}, {'Exchange': 'Toronto Stock Exchange', 'Currency': 'CAD'}, {'Exchange': 'National Stock Exchange of India', 'Currency': 'INR'}, {'Exchange': 'Frankfurt Stock Exchange', 'Currency': 'EUR'}, {'Exchange': 'Korea Exchange', 'Currency': 'KRW'}, {'Exchange': 'SIX Swiss Exchange', 'Currency': 'CHF'}, {'Exchange': 'Taiwan Stock Exchange', 'Currency': 'TWD'}, {'Exchange': 'Johannesburg Stock Exchange', 'Currency': 'ZAR'}], 'var_function-call-5773205835372737063': 'file_storage/function-call-5773205835372737063.json', 'var_function-call-7036163351833230080': [{'Index': 'IXIC', 'Country': 'United States', 'Total_Invested': 60400.0, 'Final_Value': 2429423.8253394477, 'Return_Pct': 3922.2248763898}, {'Index': 'NYA', 'Country': 'United States', 'Total_Invested': 66600.0, 'Final_Value': 817050.9202259702, 'Return_Pct': 1126.8031835225}, {'Index': 'N225', 'Country': 'Japan', 'Total_Invested': 67800.0, 'Final_Value': 313518.5993999899, 'Return_Pct': 362.4168132743}, {'Index': 'GDAXI', 'Country': 'Germany', 'Total_Invested': 40200.0, 'Final_Value': 172457.4271819551, 'Return_Pct': 328.9985750795}, {'Index': 'GSPTSE', 'Country': 'Canada', 'Total_Invested': 50400.0, 'Final_Value': 200155.4685047093, 'Return_Pct': 297.1338660808}]}

exec(code, env_args)
