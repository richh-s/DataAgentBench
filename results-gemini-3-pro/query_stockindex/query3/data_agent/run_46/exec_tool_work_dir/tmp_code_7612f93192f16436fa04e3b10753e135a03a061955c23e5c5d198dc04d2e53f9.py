code = """import json
import pandas as pd

file_path = locals()['var_function-call-5900596531419111934']
with open(file_path, 'r') as f:
    data = json.load(f)

df = pd.DataFrame(data)
df['Date'] = pd.to_datetime(df['Date'], format='mixed', errors='coerce')
df = df.dropna(subset=['Date'])

print(f"Overall Date Range: {df['Date'].min()} to {df['Date'].max()}")
print(f"Rows with Date < 2000: {len(df[df['Date'] < '2000-01-01'])}")

ixic = df[df['Index'] == 'IXIC']
print(f"IXIC Date Range: {ixic['Date'].min()} to {ixic['Date'].max()}")
print(f"IXIC Rows: {len(ixic)}")
ixic_monthly = ixic['Date'].dt.to_period('M').unique()
print(f"IXIC Unique Months: {len(ixic_monthly)}")"""

env_args = {'var_function-call-13501008299029343830': ['index_info'], 'var_function-call-13501008299029341129': ['index_trade'], 'var_function-call-17345393264304504446': [{'Exchange': 'New York Stock Exchange', 'Currency': 'USD'}, {'Exchange': 'NASDAQ', 'Currency': 'USD'}, {'Exchange': 'Hong Kong Stock Exchange', 'Currency': 'HKD'}, {'Exchange': 'Shanghai Stock Exchange', 'Currency': 'CNY'}, {'Exchange': 'Tokyo Stock Exchange', 'Currency': 'JPY'}, {'Exchange': 'Euronext', 'Currency': 'EUR'}, {'Exchange': 'Shenzhen Stock Exchange', 'Currency': 'CNY'}, {'Exchange': 'Toronto Stock Exchange', 'Currency': 'CAD'}, {'Exchange': 'National Stock Exchange of India', 'Currency': 'INR'}, {'Exchange': 'Frankfurt Stock Exchange', 'Currency': 'EUR'}, {'Exchange': 'Korea Exchange', 'Currency': 'KRW'}, {'Exchange': 'SIX Swiss Exchange', 'Currency': 'CHF'}, {'Exchange': 'Taiwan Stock Exchange', 'Currency': 'TWD'}, {'Exchange': 'Johannesburg Stock Exchange', 'Currency': 'ZAR'}], 'var_function-call-17345393264304504609': [{'Index': 'J203.JO'}, {'Index': 'IXIC'}, {'Index': 'HSI'}, {'Index': 'N225'}, {'Index': 'GSPTSE'}, {'Index': 'NSEI'}, {'Index': 'GDAXI'}, {'Index': 'NYA'}, {'Index': '000001.SS'}, {'Index': 'SSMI'}, {'Index': 'TWII'}, {'Index': 'N100'}, {'Index': '399001.SZ'}], 'var_function-call-5900596531419111934': 'file_storage/function-call-5900596531419111934.json', 'var_function-call-12143783687575214824': [{'Index': 'IXIC', 'ROI': 39.2222487639, 'ROI_Percent': 3922.2248763898, 'Total_Invested': 604, 'Final_Value': 24294.2382533945}, {'Index': 'NYA', 'ROI': 11.2680318352, 'ROI_Percent': 1126.8031835225, 'Total_Invested': 666, 'Final_Value': 8170.5092022597}, {'Index': 'N225', 'ROI': 3.6241681327, 'ROI_Percent': 362.4168132743, 'Total_Invested': 678, 'Final_Value': 3135.1859939999}, {'Index': 'GDAXI', 'ROI': 3.2899857508, 'ROI_Percent': 328.9985750795, 'Total_Invested': 402, 'Final_Value': 1724.5742718196}, {'Index': 'GSPTSE', 'ROI': 2.9713386608, 'ROI_Percent': 297.1338660808, 'Total_Invested': 504, 'Final_Value': 2001.5546850471}]}

exec(code, env_args)
