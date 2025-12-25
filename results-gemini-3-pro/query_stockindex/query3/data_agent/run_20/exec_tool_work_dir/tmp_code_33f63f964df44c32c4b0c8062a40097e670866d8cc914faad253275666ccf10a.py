code = """import pandas as pd
import json

# Load data
with open(locals()['var_function-call-15418031616304384514'], 'r') as f:
    data = json.load(f)

df = pd.DataFrame(data)
df['Date'] = pd.to_datetime(df['Date'], format='mixed', dayfirst=False, errors='coerce')
df = df[df['Date'] >= '2000-01-01']
df['CloseUSD'] = pd.to_numeric(df['CloseUSD'])

indices = ["IXIC", "NSEI", "399001.SZ", "GDAXI", "TWII"]
res = []
for idx in indices:
    sub = df[df['Index'] == idx].sort_values('Date')
    if not sub.empty:
        res.append({
            "Index": idx,
            "Start": str(sub.iloc[0]['Date']),
            "End": str(sub.iloc[-1]['Date']),
            "StartPrice": sub.iloc[0]['CloseUSD'],
            "EndPrice": sub.iloc[-1]['CloseUSD']
        })
print("__RESULT__:")
print(json.dumps(res))"""

env_args = {'var_function-call-12320111116943804548': ['index_info'], 'var_function-call-12320111116943804071': ['index_trade'], 'var_function-call-7371888173575617540': [{'Exchange': 'New York Stock Exchange', 'Currency': 'USD'}, {'Exchange': 'NASDAQ', 'Currency': 'USD'}, {'Exchange': 'Hong Kong Stock Exchange', 'Currency': 'HKD'}, {'Exchange': 'Shanghai Stock Exchange', 'Currency': 'CNY'}, {'Exchange': 'Tokyo Stock Exchange', 'Currency': 'JPY'}], 'var_function-call-3489654952358117405': [{'Index': 'J203.JO'}, {'Index': 'N225'}, {'Index': 'GSPTSE'}, {'Index': 'NSEI'}, {'Index': 'GDAXI'}, {'Index': 'IXIC'}, {'Index': 'HSI'}, {'Index': 'NYA'}, {'Index': '000001.SS'}, {'Index': 'SSMI'}, {'Index': 'TWII'}, {'Index': 'N100'}, {'Index': '399001.SZ'}], 'var_function-call-10331012001117657373': 'file_storage/function-call-10331012001117657373.json', 'var_function-call-8974196404492106585': [{'Index': 'IXIC', 'Country': 'USA', 'Return': 39.2222487639}, {'Index': 'NYA', 'Country': 'USA', 'Return': 11.2680318352}, {'Index': 'N225', 'Country': 'Japan', 'Return': 3.6241681327}, {'Index': 'GDAXI', 'Country': 'Germany', 'Return': 3.2899857508}, {'Index': 'GSPTSE', 'Country': 'Canada', 'Return': 2.9656619215}], 'var_function-call-1916111007274748501': {'Min': 55.48, 'Max': 14138.78027, 'Count': 7351, 'First': 3727.129883, 'Last': 4620.160156}, 'var_function-call-4715541387608823558': {'Min_Date': 'October 01, 1974 at 12:00 AM', 'Min_Val': 55.48, 'Max_Date': 'April 26, 2021 at 12:00 AM', 'Max_Val': 14138.78027, 'Last_Date': 'September 30, 2015 at 12:00 AM', 'Last_Val': 4620.160156}, 'var_function-call-15418031616304384514': 'file_storage/function-call-15418031616304384514.json', 'var_function-call-7812723058100869502': [{'Index': 'IXIC', 'Country': 'USA', 'Return': 3.8269431542}, {'Index': 'NSEI', 'Country': 'India', 'Return': 1.3584273446}, {'Index': '399001.SZ', 'Country': 'China', 'Return': 1.3474636719}, {'Index': 'GDAXI', 'Country': 'Germany', 'Return': 1.3470287159}, {'Index': 'TWII', 'Country': 'Taiwan', 'Return': 1.2982003158}]}

exec(code, env_args)
