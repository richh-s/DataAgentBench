code = """import json
import pandas as pd

file_path = locals()['var_function-call-6375617379289947384']
with open(file_path, 'r') as f:
    data = json.load(f)

df = pd.DataFrame(data)
df['Date'] = pd.to_datetime(df['Date'], errors='coerce')
df = df.dropna(subset=['Date'])
df['CloseUSD'] = pd.to_numeric(df['CloseUSD'], errors='coerce')

indices = ['N225']
stats = []
for idx in indices:
    sub = df[df['Index'] == idx].sort_values('Date')
    if not sub.empty:
        stats.append({
            'Index': idx,
            'Start': sub.iloc[0]['Date'],
            'End': sub.iloc[-1]['Date']
        })
print("__RESULT__:")
print(json.dumps(stats, default=str))"""

env_args = {'var_function-call-110759798618603580': ['index_info'], 'var_function-call-110759798618606141': ['index_trade'], 'var_function-call-1888189874408097317': [{'Exchange': 'New York Stock Exchange', 'Currency': 'USD'}, {'Exchange': 'NASDAQ', 'Currency': 'USD'}, {'Exchange': 'Hong Kong Stock Exchange', 'Currency': 'HKD'}, {'Exchange': 'Shanghai Stock Exchange', 'Currency': 'CNY'}, {'Exchange': 'Tokyo Stock Exchange', 'Currency': 'JPY'}], 'var_function-call-3993405376474384505': [{'Index': 'J203.JO'}, {'Index': 'IXIC'}, {'Index': 'N225'}, {'Index': 'GSPTSE'}, {'Index': 'NSEI'}, {'Index': 'GDAXI'}, {'Index': 'HSI'}, {'Index': 'NYA'}, {'Index': '000001.SS'}, {'Index': 'SSMI'}, {'Index': 'TWII'}, {'Index': 'N100'}, {'Index': '399001.SZ'}], 'var_function-call-8702784125424971527': [{'Exchange': 'New York Stock Exchange', 'Currency': 'USD'}, {'Exchange': 'NASDAQ', 'Currency': 'USD'}, {'Exchange': 'Hong Kong Stock Exchange', 'Currency': 'HKD'}, {'Exchange': 'Shanghai Stock Exchange', 'Currency': 'CNY'}, {'Exchange': 'Tokyo Stock Exchange', 'Currency': 'JPY'}, {'Exchange': 'Euronext', 'Currency': 'EUR'}, {'Exchange': 'Shenzhen Stock Exchange', 'Currency': 'CNY'}, {'Exchange': 'Toronto Stock Exchange', 'Currency': 'CAD'}, {'Exchange': 'National Stock Exchange of India', 'Currency': 'INR'}, {'Exchange': 'Frankfurt Stock Exchange', 'Currency': 'EUR'}, {'Exchange': 'Korea Exchange', 'Currency': 'KRW'}, {'Exchange': 'SIX Swiss Exchange', 'Currency': 'CHF'}, {'Exchange': 'Taiwan Stock Exchange', 'Currency': 'TWD'}, {'Exchange': 'Johannesburg Stock Exchange', 'Currency': 'ZAR'}], 'var_function-call-4714428077862934541': [{'count_star()': '67948'}], 'var_function-call-6375617379289947384': 'file_storage/function-call-6375617379289947384.json', 'var_function-call-10425347508208401933': [{'Index': 'IXIC', 'Return': 3.8220467671}, {'Index': 'NSEI', 'Return': 1.3608849755}, {'Index': 'GDAXI', 'Return': 1.3474623836}, {'Index': '399001.SZ', 'Return': 1.3445453364}, {'Index': 'TWII', 'Return': 1.2374061754}, {'Index': 'N225', 'Return': 1.1545960543}, {'Index': 'NYA', 'Return': 1.0065591545}, {'Index': 'GSPTSE', 'Return': 0.6754596567}, {'Index': '000001.SS', 'Return': 0.6416057718}, {'Index': 'N100', 'Return': 0.5986654389}], 'var_function-call-14059307093851038887': [{'Index': 'IXIC', 'Start': '2000-01-06 00:00:00', 'End': '2021-05-27 00:00:00', 'Count': 1853, 'FirstPrice': 3727.129883, 'LastPrice': 13736.28027}, {'Index': 'NSEI', 'Start': '2007-09-25 00:00:00', 'End': '2021-05-31 00:00:00', 'Count': 1083, 'FirstPrice': 49.38850098, 'LastPrice': 155.8279981}, {'Index': 'GDAXI', 'Start': '2000-01-05 00:00:00', 'End': '2021-05-31 00:00:00', 'Count': 1833, 'FirstPrice': 7932.52518528, 'LastPrice': 18813.7784536}, {'Index': '399001.SZ', 'Start': '2000-01-05 00:00:00', 'End': '2021-06-02 00:00:00', 'Count': 1758, 'FirstPrice': 557.80640624, 'LastPrice': 2377.2656256}, {'Index': 'TWII', 'Start': '2000-01-17 00:00:00', 'End': '2021-05-26 00:00:00', 'Count': 1754, 'FirstPrice': 372.61718752, 'LastPrice': 665.7475780000001}]}

exec(code, env_args)
