code = """import json, pandas as pd
import os

path = var_call_yQr0YjJ0perbiXI9sqEMRXDW
with open(path, 'r') as f:
    data = json.load(f)

df = pd.DataFrame(data)
for col in ['Open','Close']:
    df[col] = pd.to_numeric(df[col], errors='coerce')

up_down = df.groupby('Index').apply(lambda g: pd.Series({
    'up_days': (g['Close'] > g['Open']).sum(),
    'down_days': (g['Close'] < g['Open']).sum()
})).reset_index()

# North American indices in this dataset: NYA (New York Stock Exchange Composite), IXIC (NASDAQ Composite), GSPTSE (S&P/TSX Composite)
na_indices = ['NYA','IXIC','GSPTSE']
res = up_down[up_down['Index'].isin(na_indices)]
res['more_up_than_down'] = res['up_days'] > res['down_days']

result = res.to_dict(orient='records')

out = json.dumps(result)
print("__RESULT__:")
print(out)"""

env_args = {'var_call_FUgRIdogtvcYSsTPldnsMYOB': ['index_info'], 'var_call_njdN7le7Kb2Rre9R1I37CHGx': ['index_trade'], 'var_call_Lsa16sXxR83eDIubPlRXMGzi': [{'Exchange': 'New York Stock Exchange'}, {'Exchange': 'NASDAQ'}, {'Exchange': 'Hong Kong Stock Exchange'}, {'Exchange': 'Shanghai Stock Exchange'}, {'Exchange': 'Tokyo Stock Exchange'}, {'Exchange': 'Euronext'}, {'Exchange': 'Shenzhen Stock Exchange'}, {'Exchange': 'Toronto Stock Exchange'}, {'Exchange': 'National Stock Exchange of India'}, {'Exchange': 'Frankfurt Stock Exchange'}, {'Exchange': 'Korea Exchange'}, {'Exchange': 'SIX Swiss Exchange'}, {'Exchange': 'Taiwan Stock Exchange'}, {'Exchange': 'Johannesburg Stock Exchange'}], 'var_call_8ghTQcKEPaGaYZQ8Sg4jLNBX': [{'Index': 'J203.JO'}, {'Index': 'N225'}, {'Index': 'GSPTSE'}, {'Index': 'NSEI'}, {'Index': 'GDAXI'}, {'Index': 'IXIC'}, {'Index': '000001.SS'}, {'Index': 'SSMI'}, {'Index': 'TWII'}, {'Index': 'HSI'}, {'Index': 'NYA'}, {'Index': 'N100'}, {'Index': '399001.SZ'}], 'var_call_yQr0YjJ0perbiXI9sqEMRXDW': 'file_storage/call_yQr0YjJ0perbiXI9sqEMRXDW.json'}

exec(code, env_args)
