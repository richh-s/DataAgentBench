code = """import pandas as pd
import json

file_path = locals()['var_function-call-9554777893084220839']
with open(file_path, 'r') as f:
    data = json.load(f)
df = pd.DataFrame(data)
df['Date'] = pd.to_datetime(df['Date'], errors='coerce')
df = df.dropna(subset=['Date'])

stats = df.groupby('Index')['Date'].agg(['min', 'max'])
print("__RESULT__:")
print(stats.to_json(date_format='iso'))"""

env_args = {'var_function-call-12267509282429008629': ['index_trade'], 'var_function-call-12267509282429009454': ['index_info'], 'var_function-call-12773024537366388109': [{'Index': 'J203.JO'}, {'Index': 'N225'}, {'Index': 'GSPTSE'}, {'Index': 'NSEI'}, {'Index': 'GDAXI'}, {'Index': 'IXIC'}, {'Index': 'HSI'}, {'Index': 'NYA'}, {'Index': '000001.SS'}, {'Index': 'SSMI'}, {'Index': 'TWII'}, {'Index': 'N100'}, {'Index': '399001.SZ'}], 'var_function-call-12773024537366385894': [{'Exchange': 'New York Stock Exchange', 'Currency': 'USD'}, {'Exchange': 'NASDAQ', 'Currency': 'USD'}, {'Exchange': 'Hong Kong Stock Exchange', 'Currency': 'HKD'}, {'Exchange': 'Shanghai Stock Exchange', 'Currency': 'CNY'}, {'Exchange': 'Tokyo Stock Exchange', 'Currency': 'JPY'}, {'Exchange': 'Euronext', 'Currency': 'EUR'}, {'Exchange': 'Shenzhen Stock Exchange', 'Currency': 'CNY'}, {'Exchange': 'Toronto Stock Exchange', 'Currency': 'CAD'}, {'Exchange': 'National Stock Exchange of India', 'Currency': 'INR'}, {'Exchange': 'Frankfurt Stock Exchange', 'Currency': 'EUR'}, {'Exchange': 'Korea Exchange', 'Currency': 'KRW'}, {'Exchange': 'SIX Swiss Exchange', 'Currency': 'CHF'}, {'Exchange': 'Taiwan Stock Exchange', 'Currency': 'TWD'}, {'Exchange': 'Johannesburg Stock Exchange', 'Currency': 'ZAR'}], 'var_function-call-9554777893084220839': 'file_storage/function-call-9554777893084220839.json', 'var_function-call-9548907123683491810': [{'Index': 'IXIC', 'Country': 'United States', 'Return': 382.20467671180944, 'Total_Invested': 257, 'Final_Value': 1239.2660191493503}, {'Index': 'NSEI', 'Country': 'India', 'Return': 136.08849755128486, 'Total_Invested': 165, 'Final_Value': 389.54602095962}, {'Index': 'GDAXI', 'Country': 'Germany', 'Return': 134.7462383645538, 'Total_Invested': 257, 'Final_Value': 603.2978325969033}, {'Index': '399001.SZ', 'Country': 'China', 'Return': 134.4545336356674, 'Total_Invested': 258, 'Final_Value': 604.8926967800219}, {'Index': 'TWII', 'Country': 'Taiwan', 'Return': 123.74061754244634, 'Total_Invested': 257, 'Final_Value': 575.0133870840871}]}

exec(code, env_args)
