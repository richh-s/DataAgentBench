code = """import json, pandas as pd, os
paths = ['var_call_5DOLgQIfejUbBgbxteQ6iK1g','var_call_6R6LzUalje2Q3UDeZhP2UUiu','var_call_MN72x2dLzIFf2ZVJAzbsaXFy','var_call_6kEfror1SdmCcPLX83KUT6LY','var_call_u2tcOvMf4V4rfS0f3l1nwX68']
frames = []
for p in paths:
    v = globals().get(p)
    if isinstance(v, str) and v.endswith('.json'):
        with open(v,'r') as f: data = json.load(f)
    else:
        data = v
    if not data: 
        continue
    frames.append(pd.DataFrame(data))
if frames:
    df = pd.concat(frames, ignore_index=True)
    df['High'] = df['High'].astype(float)
    df['Low'] = df['Low'].astype(float)
    df['range_pct'] = (df['High']-df['Low'])/df['Low']
    res = df.groupby('Symbol')['range_pct'].apply(lambda s: (s>0.2).sum()).reset_index(name='days_over_20pct')
    res = res.sort_values('days_over_20pct', ascending=False).head(5)
    result = res.to_dict(orient='records')
else:
    result = []
print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_call_3fBkMDb2Wy6SLJy6JARMpgQZ': 'file_storage/call_3fBkMDb2Wy6SLJy6JARMpgQZ.json', 'var_call_4KIck4CiBiWAcU82mdPQamwm': 'file_storage/call_4KIck4CiBiWAcU82mdPQamwm.json', 'var_call_wFxt1ZBoCaK0iClaR6l7aHNe': ['AGMH', 'ALACU', 'AMHC', 'ANDA', 'APEX', 'BCLI', 'BHAT', 'BIOC', 'BKYI', 'BLFS', 'BOSC', 'BOTJ', 'BWEN', 'CBAT', 'CCCL', 'CDMOP', 'CEMI', 'CFBK', 'CFFA', 'CLRB', 'CORV', 'CPAAU', 'CPAH', 'CUBA', 'CVV', 'DZSI', 'ELSE', 'EXPC', 'EYEG', 'FAMI', 'FNCB', 'FSBW', 'FTFT', 'GDYN', 'GLG', 'GRNVU', 'GTEC', 'HCCOU', 'HNNA', 'HQI', 'HRTX', 'IDEX', 'IGIC', 'IOTS', 'ISNS', 'ITI', 'LACQ', 'MBCN', 'MBNKP', 'MCEP', 'MLND', 'MMAC', 'MNCLU', 'MNPR', 'NVEE', 'NXTD', 'OPOF', 'OPTT', 'ORGO', 'ORSNU', 'OTEL', 'PBFS', 'PBTS', 'PCSB', 'PECK', 'PEIX', 'PFIE', 'PLIN', 'POPE', 'QRHC', 'SES', 'SHSP', 'SNSS', 'SSNT', 'STKS', 'TGLS', 'TMSR', 'VERB', 'VMD', 'VRRM', 'VTIQW', 'VVPR', 'WHLM', 'WHLR', 'XBIOW', 'XPEL'], 'var_call_cYxyVts2jbBPJkfO7STEuI1D': ['AGMH', 'ALACU', 'AMHC', 'ANDA', 'APEX', 'BCLI', 'BHAT', 'BIOC', 'BKYI', 'BLFS', 'BOSC', 'BOTJ', 'BWEN', 'CBAT', 'CCCL', 'CDMOP', 'CEMI', 'CFBK', 'CFFA', 'CLRB', 'CORV', 'CPAAU', 'CPAH', 'CUBA', 'CVV', 'DZSI', 'ELSE', 'EXPC', 'EYEG', 'FAMI', 'FNCB', 'FSBW', 'FTFT', 'GDYN', 'GLG', 'GRNVU', 'GTEC', 'HCCOU', 'HNNA', 'HQI', 'HRTX', 'IDEX', 'IGIC', 'IOTS', 'ISNS', 'ITI', 'LACQ', 'MBCN', 'MBNKP', 'MCEP', 'MLND', 'MMAC', 'MNCLU', 'MNPR', 'NVEE', 'NXTD', 'OPOF', 'OPTT', 'ORGO', 'ORSNU', 'OTEL', 'PBFS', 'PBTS', 'PCSB', 'PECK', 'PEIX', 'PFIE', 'PLIN', 'POPE', 'QRHC', 'SES', 'SHSP', 'SNSS', 'SSNT', 'STKS', 'TGLS', 'TMSR', 'VERB', 'VMD', 'VRRM', 'VTIQW', 'VVPR', 'WHLM', 'WHLR', 'XBIOW', 'XPEL'], 'var_call_5DOLgQIfejUbBgbxteQ6iK1g': 'file_storage/call_5DOLgQIfejUbBgbxteQ6iK1g.json', 'var_call_6R6LzUalje2Q3UDeZhP2UUiu': 'file_storage/call_6R6LzUalje2Q3UDeZhP2UUiu.json', 'var_call_MN72x2dLzIFf2ZVJAzbsaXFy': [], 'var_call_6kEfror1SdmCcPLX83KUT6LY': 'file_storage/call_6kEfror1SdmCcPLX83KUT6LY.json', 'var_call_u2tcOvMf4V4rfS0f3l1nwX68': 'file_storage/call_u2tcOvMf4V4rfS0f3l1nwX68.json'}

exec(code, env_args)
