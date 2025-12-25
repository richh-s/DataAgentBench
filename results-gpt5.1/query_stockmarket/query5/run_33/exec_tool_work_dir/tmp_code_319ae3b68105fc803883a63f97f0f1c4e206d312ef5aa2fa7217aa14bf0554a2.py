code = """import json, pandas as pd
file = var_call_dVhE8qSckQds9jAQviWsPWCV
with open(file,'r') as f:
    data = json.load(f)

df = pd.DataFrame(data)
df['High'] = df['High'].astype(float)
df['Low'] = df['Low'].astype(float)
df['range_pct'] = (df['High'] - df['Low']) / df['Low']
res = df.groupby('Symbol')['range_pct'].apply(lambda x: (x>0.2).sum()).reset_index(name='days_over_20pct')
res = res.sort_values('days_over_20pct', ascending=False).head(5)
result = res.to_json(orient='records')
print("__RESULT__:")
print(result)"""

env_args = {'var_call_yAwZzrWyQVMkKPkWYf9G6yca': 'file_storage/call_yAwZzrWyQVMkKPkWYf9G6yca.json', 'var_call_wjDF1reXZ8tTsle6jzEeVTds': 'file_storage/call_wjDF1reXZ8tTsle6jzEeVTds.json', 'var_call_rlaiVj6cHnvIQ9KR84KFROXd': ['AGMH', 'ALACU', 'AMHC', 'ANDA', 'APEX', 'BCLI', 'BHAT', 'BIOC', 'BKYI', 'BLFS', 'BOSC', 'BOTJ', 'BWEN', 'CBAT', 'CCCL', 'CDMOP', 'CEMI', 'CFBK', 'CFFA', 'CLRB', 'CORV', 'CPAAU', 'CPAH', 'CUBA', 'CVV', 'DZSI', 'ELSE', 'EXPC', 'EYEG', 'FAMI', 'FNCB', 'FSBW', 'FTFT', 'GDYN', 'GLG', 'GRNVU', 'GTEC', 'HCCOU', 'HNNA', 'HQI', 'HRTX', 'IDEX', 'IGIC', 'IOTS', 'ISNS', 'ITI', 'LACQ', 'MBCN', 'MBNKP', 'MCEP', 'MLND', 'MMAC', 'MNCLU', 'MNPR', 'NVEE', 'NXTD', 'OPOF', 'OPTT', 'ORGO', 'ORSNU', 'OTEL', 'PBFS', 'PBTS', 'PCSB', 'PECK', 'PEIX', 'PFIE', 'PLIN', 'POPE', 'QRHC', 'SES', 'SHSP', 'SNSS', 'SSNT', 'STKS', 'TGLS', 'TMSR', 'VERB', 'VMD', 'VRRM', 'VTIQW', 'VVPR', 'WHLM', 'WHLR', 'XBIOW', 'XPEL'], 'var_call_dVhE8qSckQds9jAQviWsPWCV': 'file_storage/call_dVhE8qSckQds9jAQviWsPWCV.json'}

exec(code, env_args)
