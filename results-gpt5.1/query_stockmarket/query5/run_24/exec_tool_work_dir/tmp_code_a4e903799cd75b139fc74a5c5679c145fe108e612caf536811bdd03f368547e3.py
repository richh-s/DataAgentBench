code = """import json, pandas as pd, os
paths = ['var_call_tqj5Qjrvbd156WrLtkVZIcJw','var_call_nL08OScxZJgxW1CC0X6Fqp3H','var_call_rLCSnY78waFOpfF1e5xYTjeN','var_call_Cmkjbyeu7iG1PfPgtsU8IzQa','var_call_RfOPwjwghySo5bpnKEv8IovY']
frames = []
for p in paths:
    v = globals().get(p)
    if isinstance(v,str) and v.endswith('.json'):
        with open(v,'r') as f: data = json.load(f)
    else:
        data = v
    if not data:
        continue
    frames.append(pd.DataFrame(data))

all_frames = []
if frames:
    frames[0]['High']=frames[0]['High'].astype(float)
    frames[0]['Low']=frames[0]['Low'].astype(float)
    frames[0]['range_pct']=(frames[0]['High']-frames[0]['Low'])/frames[0]['Low']
    res_new = frames[0].groupby('Symbol')['range_pct'].apply(lambda s:(s>0.2).sum()).reset_index(name='days_over_20pct')
    all_frames.append(res_new)

# existing results
prev = var_call_Fm4ZifNOKvrEIxD5fFXB3rr2
prev_df = pd.DataFrame(prev)
all_frames.append(prev_df)

final = pd.concat(all_frames, ignore_index=True).groupby('Symbol')['days_over_20pct'].sum().reset_index()
final = final.sort_values('days_over_20pct', ascending=False).head(5)
result = final.to_dict(orient='records')
print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_call_3fBkMDb2Wy6SLJy6JARMpgQZ': 'file_storage/call_3fBkMDb2Wy6SLJy6JARMpgQZ.json', 'var_call_4KIck4CiBiWAcU82mdPQamwm': 'file_storage/call_4KIck4CiBiWAcU82mdPQamwm.json', 'var_call_wFxt1ZBoCaK0iClaR6l7aHNe': ['AGMH', 'ALACU', 'AMHC', 'ANDA', 'APEX', 'BCLI', 'BHAT', 'BIOC', 'BKYI', 'BLFS', 'BOSC', 'BOTJ', 'BWEN', 'CBAT', 'CCCL', 'CDMOP', 'CEMI', 'CFBK', 'CFFA', 'CLRB', 'CORV', 'CPAAU', 'CPAH', 'CUBA', 'CVV', 'DZSI', 'ELSE', 'EXPC', 'EYEG', 'FAMI', 'FNCB', 'FSBW', 'FTFT', 'GDYN', 'GLG', 'GRNVU', 'GTEC', 'HCCOU', 'HNNA', 'HQI', 'HRTX', 'IDEX', 'IGIC', 'IOTS', 'ISNS', 'ITI', 'LACQ', 'MBCN', 'MBNKP', 'MCEP', 'MLND', 'MMAC', 'MNCLU', 'MNPR', 'NVEE', 'NXTD', 'OPOF', 'OPTT', 'ORGO', 'ORSNU', 'OTEL', 'PBFS', 'PBTS', 'PCSB', 'PECK', 'PEIX', 'PFIE', 'PLIN', 'POPE', 'QRHC', 'SES', 'SHSP', 'SNSS', 'SSNT', 'STKS', 'TGLS', 'TMSR', 'VERB', 'VMD', 'VRRM', 'VTIQW', 'VVPR', 'WHLM', 'WHLR', 'XBIOW', 'XPEL'], 'var_call_cYxyVts2jbBPJkfO7STEuI1D': ['AGMH', 'ALACU', 'AMHC', 'ANDA', 'APEX', 'BCLI', 'BHAT', 'BIOC', 'BKYI', 'BLFS', 'BOSC', 'BOTJ', 'BWEN', 'CBAT', 'CCCL', 'CDMOP', 'CEMI', 'CFBK', 'CFFA', 'CLRB', 'CORV', 'CPAAU', 'CPAH', 'CUBA', 'CVV', 'DZSI', 'ELSE', 'EXPC', 'EYEG', 'FAMI', 'FNCB', 'FSBW', 'FTFT', 'GDYN', 'GLG', 'GRNVU', 'GTEC', 'HCCOU', 'HNNA', 'HQI', 'HRTX', 'IDEX', 'IGIC', 'IOTS', 'ISNS', 'ITI', 'LACQ', 'MBCN', 'MBNKP', 'MCEP', 'MLND', 'MMAC', 'MNCLU', 'MNPR', 'NVEE', 'NXTD', 'OPOF', 'OPTT', 'ORGO', 'ORSNU', 'OTEL', 'PBFS', 'PBTS', 'PCSB', 'PECK', 'PEIX', 'PFIE', 'PLIN', 'POPE', 'QRHC', 'SES', 'SHSP', 'SNSS', 'SSNT', 'STKS', 'TGLS', 'TMSR', 'VERB', 'VMD', 'VRRM', 'VTIQW', 'VVPR', 'WHLM', 'WHLR', 'XBIOW', 'XPEL'], 'var_call_5DOLgQIfejUbBgbxteQ6iK1g': 'file_storage/call_5DOLgQIfejUbBgbxteQ6iK1g.json', 'var_call_6R6LzUalje2Q3UDeZhP2UUiu': 'file_storage/call_6R6LzUalje2Q3UDeZhP2UUiu.json', 'var_call_MN72x2dLzIFf2ZVJAzbsaXFy': [], 'var_call_6kEfror1SdmCcPLX83KUT6LY': 'file_storage/call_6kEfror1SdmCcPLX83KUT6LY.json', 'var_call_u2tcOvMf4V4rfS0f3l1nwX68': 'file_storage/call_u2tcOvMf4V4rfS0f3l1nwX68.json', 'var_call_Fm4ZifNOKvrEIxD5fFXB3rr2': [{'Symbol': 'APEX', 'days_over_20pct': 15}, {'Symbol': 'AGMH', 'days_over_20pct': 13}, {'Symbol': 'ALACU', 'days_over_20pct': 0}, {'Symbol': 'ANDA', 'days_over_20pct': 0}], 'var_call_KptEXRBht4tVm2jukU9kFZTE': ['BCLI', 'BHAT', 'BIOC', 'BKYI', 'BLFS', 'BOSC', 'BOTJ', 'BWEN', 'CBAT', 'CCCL', 'CDMOP', 'CEMI', 'CFBK', 'CFFA', 'CLRB', 'CORV', 'CPAAU', 'CPAH', 'CUBA', 'CVV', 'DZSI', 'ELSE', 'EXPC', 'EYEG', 'FAMI', 'FNCB', 'FSBW', 'FTFT', 'GDYN', 'GLG', 'GRNVU', 'GTEC', 'HCCOU', 'HNNA', 'HQI', 'HRTX', 'IDEX', 'IGIC', 'IOTS', 'ISNS', 'ITI', 'LACQ', 'MBCN', 'MBNKP', 'MCEP', 'MLND', 'MMAC', 'MNCLU', 'MNPR', 'NVEE', 'NXTD', 'OPOF', 'OPTT', 'ORGO', 'ORSNU', 'OTEL', 'PBFS', 'PBTS', 'PCSB', 'PECK', 'PEIX', 'PFIE', 'PLIN', 'POPE', 'QRHC', 'SES', 'SHSP', 'SNSS', 'SSNT', 'STKS', 'TGLS', 'TMSR', 'VERB', 'VMD', 'VRRM', 'VTIQW', 'VVPR', 'WHLM', 'WHLR', 'XBIOW', 'XPEL'], 'var_call_hrLYcls5TC19Rly49bN2yyCO': [['AGMH', 'ALACU', 'AMHC', 'ANDA', 'APEX', 'BCLI', 'BHAT', 'BIOC', 'BKYI', 'BLFS', 'BOSC', 'BOTJ', 'BWEN', 'CBAT', 'CCCL', 'CDMOP', 'CEMI', 'CFBK', 'CFFA', 'CLRB', 'CORV', 'CPAAU', 'CPAH', 'CUBA', 'CVV', 'DZSI', 'ELSE', 'EXPC', 'EYEG', 'FAMI', 'FNCB', 'FSBW', 'FTFT', 'GDYN', 'GLG', 'GRNVU', 'GTEC', 'HCCOU', 'HNNA', 'HQI'], ['HRTX', 'IDEX', 'IGIC', 'IOTS', 'ISNS', 'ITI', 'LACQ', 'MBCN', 'MBNKP', 'MCEP', 'MLND', 'MMAC', 'MNCLU', 'MNPR', 'NVEE', 'NXTD', 'OPOF', 'OPTT', 'ORGO', 'ORSNU', 'OTEL', 'PBFS', 'PBTS', 'PCSB', 'PECK', 'PEIX', 'PFIE', 'PLIN', 'POPE', 'QRHC', 'SES', 'SHSP', 'SNSS', 'SSNT', 'STKS', 'TGLS', 'TMSR', 'VERB', 'VMD', 'VRRM'], ['VTIQW', 'VVPR', 'WHLM', 'WHLR', 'XBIOW', 'XPEL']], 'var_call_tqj5Qjrvbd156WrLtkVZIcJw': 'file_storage/call_tqj5Qjrvbd156WrLtkVZIcJw.json', 'var_call_nL08OScxZJgxW1CC0X6Fqp3H': 'file_storage/call_nL08OScxZJgxW1CC0X6Fqp3H.json', 'var_call_rLCSnY78waFOpfF1e5xYTjeN': 'file_storage/call_rLCSnY78waFOpfF1e5xYTjeN.json', 'var_call_Cmkjbyeu7iG1PfPgtsU8IzQa': 'file_storage/call_Cmkjbyeu7iG1PfPgtsU8IzQa.json', 'var_call_RfOPwjwghySo5bpnKEv8IovY': 'file_storage/call_RfOPwjwghySo5bpnKEv8IovY.json'}

exec(code, env_args)
