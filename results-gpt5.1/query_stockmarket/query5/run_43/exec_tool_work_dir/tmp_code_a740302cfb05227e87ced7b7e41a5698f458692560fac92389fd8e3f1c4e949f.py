code = """import json, pandas as pd

rows = json.load(open(var_call_v10XdqJXDy5oUhO2vaYkKwFn))
df = pd.DataFrame(rows)
for col in ['High','Low']:
    df[col] = pd.to_numeric(df[col])

mask = (df['High'] - df['Low']) > 0.2 * df['Low']
counts = df[mask].groupby('Symbol').size().sort_values(ascending=False)
Top5 = counts.head(5).to_dict()

symbols_info = json.load(open(var_call_WBOyChqARAlD8jzRvTJbm8eW))
info_df = pd.DataFrame(symbols_info)
name_map = dict(zip(info_df['Symbol'], info_df['Company Description']))

top5_list = []
for sym, cnt in Top5.items():
    top5_list.append({'Symbol': sym, 'Days': int(cnt), 'Company Description': name_map.get(sym, '')})

result = json.dumps(top5_list)
print("__RESULT__:")
print(result)"""

env_args = {'var_call_XKuyIBXOaMFNaGiYK67GWhRC': 'file_storage/call_XKuyIBXOaMFNaGiYK67GWhRC.json', 'var_call_WBOyChqARAlD8jzRvTJbm8eW': 'file_storage/call_WBOyChqARAlD8jzRvTJbm8eW.json', 'var_call_omucKGOAwqxfRWKJnYb7LgBA': ['AGMH', 'ALACU', 'AMHC', 'ANDA', 'APEX', 'BCLI', 'BHAT', 'BIOC', 'BKYI', 'BLFS', 'BOSC', 'BOTJ', 'BWEN', 'CBAT', 'CCCL', 'CDMOP', 'CEMI', 'CFBK', 'CFFA', 'CLRB', 'CORV', 'CPAAU', 'CPAH', 'CUBA', 'CVV', 'DZSI', 'ELSE', 'EXPC', 'EYEG', 'FAMI', 'FNCB', 'FSBW', 'FTFT', 'GDYN', 'GLG', 'GRNVU', 'GTEC', 'HCCOU', 'HNNA', 'HQI', 'HRTX', 'IDEX', 'IGIC', 'IOTS', 'ISNS', 'ITI', 'LACQ', 'MBCN', 'MBNKP', 'MCEP', 'MLND', 'MMAC', 'MNCLU', 'MNPR', 'NVEE', 'NXTD', 'OPOF', 'OPTT', 'ORGO', 'ORSNU', 'OTEL', 'PBFS', 'PBTS', 'PCSB', 'PECK', 'PEIX', 'PFIE', 'PLIN', 'POPE', 'QRHC', 'SES', 'SHSP', 'SNSS', 'SSNT', 'STKS', 'TGLS', 'TMSR', 'VERB', 'VMD', 'VRRM', 'VTIQW', 'VVPR', 'WHLM', 'WHLR', 'XBIOW', 'XPEL'], 'var_call_v10XdqJXDy5oUhO2vaYkKwFn': 'file_storage/call_v10XdqJXDy5oUhO2vaYkKwFn.json'}

exec(code, env_args)
