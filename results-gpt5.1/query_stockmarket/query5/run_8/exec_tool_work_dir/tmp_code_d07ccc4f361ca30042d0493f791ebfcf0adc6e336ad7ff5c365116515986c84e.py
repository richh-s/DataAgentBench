code = """import json, pandas as pd
syms = pd.read_json(var_call_eDEUoFdO3AlK3ZqN1lwcKxnN)
cap = syms[['Symbol','CompanyDescription']]
common = json.loads(var_call_rga9pWVLAtM82MarheUU7X6b)
cap = cap[cap['Symbol'].isin(common)]
symbols = cap['Symbol'].tolist()
chunks = [symbols[i:i+20] for i in range(0,len(symbols),20)]
result = json.dumps(chunks)
print('__RESULT__:')
print(result)"""

env_args = {'var_call_8svJJRcv22dlEMDmzMyXjkiI': 'file_storage/call_8svJJRcv22dlEMDmzMyXjkiI.json', 'var_call_eDEUoFdO3AlK3ZqN1lwcKxnN': 'file_storage/call_eDEUoFdO3AlK3ZqN1lwcKxnN.json', 'var_call_rga9pWVLAtM82MarheUU7X6b': ['AGMH', 'ALACU', 'AMHC', 'ANDA', 'APEX', 'BCLI', 'BHAT', 'BIOC', 'BKYI', 'BLFS', 'BOSC', 'BOTJ', 'BWEN', 'CBAT', 'CCCL', 'CDMOP', 'CEMI', 'CFBK', 'CFFA', 'CLRB', 'CORV', 'CPAAU', 'CPAH', 'CUBA', 'CVV', 'DZSI', 'ELSE', 'EXPC', 'EYEG', 'FAMI', 'FNCB', 'FSBW', 'FTFT', 'GDYN', 'GLG', 'GRNVU', 'GTEC', 'HCCOU', 'HNNA', 'HQI', 'HRTX', 'IDEX', 'IGIC', 'IOTS', 'ISNS', 'ITI', 'LACQ', 'MBCN', 'MBNKP', 'MCEP', 'MLND', 'MMAC', 'MNCLU', 'MNPR', 'NVEE', 'NXTD', 'OPOF', 'OPTT', 'ORGO', 'ORSNU', 'OTEL', 'PBFS', 'PBTS', 'PCSB', 'PECK', 'PEIX', 'PFIE', 'PLIN', 'POPE', 'QRHC', 'SES', 'SHSP', 'SNSS', 'SSNT', 'STKS', 'TGLS', 'TMSR', 'VERB', 'VMD', 'VRRM', 'VTIQW', 'VVPR', 'WHLM', 'WHLR', 'XBIOW', 'XPEL'], 'var_call_BjrJBwTAil9s4PNTq3in0rN4': [{'Symbol': 'ELSE', 'Date': '2019-01-02', 'High': '3.559999942779541', 'Low': '3.559999942779541'}]}

exec(code, env_args)
