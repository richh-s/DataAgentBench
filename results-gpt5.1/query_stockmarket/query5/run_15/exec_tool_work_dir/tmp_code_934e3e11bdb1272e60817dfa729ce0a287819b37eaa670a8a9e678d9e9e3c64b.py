code = """import json, pandas as pd

path = var_call_2SsMy2qxpTfgt1xStRLQtIng
with open(path, 'r') as f:
    data = json.load(f)

df = pd.DataFrame(data)
for col in ['High','Low']:
    df[col] = pd.to_numeric(df[col])

mask = (df['High'] - df['Low']) > 0.2 * df['Low']
counts = df[mask].groupby('Symbol').size().sort_values(ascending=False)

top5 = counts.head(5).reset_index()
top5.columns = ['Symbol','Days']

# map to company names
path_info = var_call_27OZ5X7c07iVF4YQv2tkxwVi
with open(path_info, 'r') as f:
    info = json.load(f)

df_info = pd.DataFrame(info)

merged = top5.merge(df_info, left_on='Symbol', right_on='Symbol', how='left')
result = merged[['Symbol','Company Description','Days']].to_dict(orient='records')

out = json.dumps(result)
print("__RESULT__:")
print(out)"""

env_args = {'var_call_MrkNbn6l6PQHlzA0ui9E6OYt': 'file_storage/call_MrkNbn6l6PQHlzA0ui9E6OYt.json', 'var_call_27OZ5X7c07iVF4YQv2tkxwVi': 'file_storage/call_27OZ5X7c07iVF4YQv2tkxwVi.json', 'var_call_qQzwxmVKb9c7sa3FpVEGOvpM': {'symbols': ['AGMH', 'ALACU', 'AMHC', 'ANDA', 'APEX', 'BCLI', 'BHAT', 'BIOC', 'BKYI', 'BLFS', 'BOSC', 'BOTJ', 'BWEN', 'CBAT', 'CCCL', 'CDMOP', 'CEMI', 'CFBK', 'CFFA', 'CLRB', 'CORV', 'CPAAU', 'CPAH', 'CUBA', 'CVV', 'DZSI', 'ELSE', 'EXPC', 'EYEG', 'FAMI', 'FNCB', 'FSBW', 'FTFT', 'GDYN', 'GLG', 'GRNVU', 'GTEC', 'HCCOU', 'HNNA', 'HQI', 'HRTX', 'IDEX', 'IGIC', 'IOTS', 'ISNS', 'ITI', 'LACQ', 'MBCN', 'MBNKP', 'MCEP'], 'total_symbols_capital_market': 86, 'total_symbols_with_trades': 86}, 'var_call_2SsMy2qxpTfgt1xStRLQtIng': 'file_storage/call_2SsMy2qxpTfgt1xStRLQtIng.json'}

exec(code, env_args)
