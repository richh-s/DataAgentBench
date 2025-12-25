code = """import pandas as pd
import json

# Load data
with open(locals()['var_function-call-10331012001117657373'], 'r') as f:
    data = json.load(f)

df = pd.DataFrame(data)
df = df[df['Index'] == 'IXIC']
df['CloseUSD'] = pd.to_numeric(df['CloseUSD'])
min_row = df.loc[df['CloseUSD'].idxmin()]
max_row = df.loc[df['CloseUSD'].idxmax()]
last_row = df.iloc[-1]

res = {
    "Min_Date": str(min_row['Date']),
    "Min_Val": min_row['CloseUSD'],
    "Max_Date": str(max_row['Date']),
    "Max_Val": max_row['CloseUSD'],
    "Last_Date": str(last_row['Date']),
    "Last_Val": last_row['CloseUSD']
}
print("__RESULT__:")
print(json.dumps(res))"""

env_args = {'var_function-call-12320111116943804548': ['index_info'], 'var_function-call-12320111116943804071': ['index_trade'], 'var_function-call-7371888173575617540': [{'Exchange': 'New York Stock Exchange', 'Currency': 'USD'}, {'Exchange': 'NASDAQ', 'Currency': 'USD'}, {'Exchange': 'Hong Kong Stock Exchange', 'Currency': 'HKD'}, {'Exchange': 'Shanghai Stock Exchange', 'Currency': 'CNY'}, {'Exchange': 'Tokyo Stock Exchange', 'Currency': 'JPY'}], 'var_function-call-3489654952358117405': [{'Index': 'J203.JO'}, {'Index': 'N225'}, {'Index': 'GSPTSE'}, {'Index': 'NSEI'}, {'Index': 'GDAXI'}, {'Index': 'IXIC'}, {'Index': 'HSI'}, {'Index': 'NYA'}, {'Index': '000001.SS'}, {'Index': 'SSMI'}, {'Index': 'TWII'}, {'Index': 'N100'}, {'Index': '399001.SZ'}], 'var_function-call-10331012001117657373': 'file_storage/function-call-10331012001117657373.json', 'var_function-call-8974196404492106585': [{'Index': 'IXIC', 'Country': 'USA', 'Return': 39.2222487639}, {'Index': 'NYA', 'Country': 'USA', 'Return': 11.2680318352}, {'Index': 'N225', 'Country': 'Japan', 'Return': 3.6241681327}, {'Index': 'GDAXI', 'Country': 'Germany', 'Return': 3.2899857508}, {'Index': 'GSPTSE', 'Country': 'Canada', 'Return': 2.9656619215}], 'var_function-call-1916111007274748501': {'Min': 55.48, 'Max': 14138.78027, 'Count': 7351, 'First': 3727.129883, 'Last': 4620.160156}}

exec(code, env_args)
