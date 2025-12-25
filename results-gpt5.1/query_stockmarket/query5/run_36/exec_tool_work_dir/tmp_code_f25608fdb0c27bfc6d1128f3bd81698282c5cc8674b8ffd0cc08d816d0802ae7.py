code = """import json, pandas as pd

results = [var_call_lbXuaNVRJvUb0wPdcCO7iAut, var_call_9OtbxWpi7uc0KO036vlhN2KB, var_call_mvZxIoImzYsMHD4r1GgrDSVV, var_call_fwX4HABsBR8QzhHfY9JCBhhQ, var_call_UNkh3cIBd5k4ASQDhnqTRGZ4]
syms = ['AGMH','ALACU','AMHC','ANDA','APEX']
rows = []
for sym, res in zip(syms, results):
    cnt = int(res[0]['cnt'])
    rows.append({'Symbol': sym, 'cnt2019': cnt})

df = pd.DataFrame(rows).sort_values('cnt2019', ascending=False)
result = df.to_json(orient='records')
print('__RESULT__:')
print(result)"""

env_args = {'var_call_VVzGVAQojORj5Kibor2gdtMq': 'file_storage/call_VVzGVAQojORj5Kibor2gdtMq.json', 'var_call_8DQPbtO3dKYO6n32ZAdgBBVJ': 'file_storage/call_8DQPbtO3dKYO6n32ZAdgBBVJ.json', 'var_call_ZlC9TSlvUfmkMS88B3KIgmDY': {'symbols_subset': ['AGMH', 'ALACU', 'AMHC', 'ANDA', 'APEX', 'BCLI', 'BHAT', 'BIOC', 'BKYI', 'BLFS', 'BOSC', 'BOTJ', 'BWEN', 'CBAT', 'CCCL', 'CDMOP', 'CEMI', 'CFBK', 'CFFA', 'CLRB', 'CORV', 'CPAAU', 'CPAH', 'CUBA', 'CVV', 'DZSI', 'ELSE', 'EXPC', 'EYEG', 'FAMI', 'FNCB', 'FSBW', 'FTFT', 'GDYN', 'GLG', 'GRNVU', 'GTEC', 'HCCOU', 'HNNA', 'HQI', 'HRTX', 'IDEX', 'IGIC', 'IOTS', 'ISNS', 'ITI', 'LACQ', 'MBCN', 'MBNKP', 'MCEP', 'MLND', 'MMAC', 'MNCLU', 'MNPR', 'NVEE', 'NXTD', 'OPOF', 'OPTT', 'ORGO', 'ORSNU', 'OTEL', 'PBFS', 'PBTS', 'PCSB', 'PECK', 'PEIX', 'PFIE', 'PLIN', 'POPE', 'QRHC', 'SES', 'SHSP', 'SNSS', 'SSNT', 'STKS', 'TGLS', 'TMSR', 'VERB', 'VMD', 'VRRM', 'VTIQW', 'VVPR', 'WHLM', 'WHLR', 'XBIOW', 'XPEL'], 'valid_in_trade_db': ['AGMH', 'ALACU', 'AMHC', 'ANDA', 'APEX', 'BCLI', 'BHAT', 'BIOC', 'BKYI', 'BLFS', 'BOSC', 'BOTJ', 'BWEN', 'CBAT', 'CCCL', 'CDMOP', 'CEMI', 'CFBK', 'CFFA', 'CLRB', 'CORV', 'CPAAU', 'CPAH', 'CUBA', 'CVV', 'DZSI', 'ELSE', 'EXPC', 'EYEG', 'FAMI', 'FNCB', 'FSBW', 'FTFT', 'GDYN', 'GLG', 'GRNVU', 'GTEC', 'HCCOU', 'HNNA', 'HQI', 'HRTX', 'IDEX', 'IGIC', 'IOTS', 'ISNS', 'ITI', 'LACQ', 'MBCN', 'MBNKP', 'MCEP', 'MLND', 'MMAC', 'MNCLU', 'MNPR', 'NVEE', 'NXTD', 'OPOF', 'OPTT', 'ORGO', 'ORSNU', 'OTEL', 'PBFS', 'PBTS', 'PCSB', 'PECK', 'PEIX', 'PFIE', 'PLIN', 'POPE', 'QRHC', 'SES', 'SHSP', 'SNSS', 'SSNT', 'STKS', 'TGLS', 'TMSR', 'VERB', 'VMD', 'VRRM', 'VTIQW', 'VVPR', 'WHLM', 'WHLR', 'XBIOW', 'XPEL']}, 'var_call_lbXuaNVRJvUb0wPdcCO7iAut': [{'cnt': '13'}], 'var_call_9OtbxWpi7uc0KO036vlhN2KB': [{'cnt': '0'}], 'var_call_mvZxIoImzYsMHD4r1GgrDSVV': [{'cnt': '0'}], 'var_call_fwX4HABsBR8QzhHfY9JCBhhQ': [{'cnt': '0'}], 'var_call_UNkh3cIBd5k4ASQDhnqTRGZ4': [{'cnt': '15'}]}

exec(code, env_args)
