code = """import json
symbols = var_call_BNs6rjym3Bdskv5OiHCnDKTI
queries = []
for s in symbols:
    q = f"SELECT '{s}' AS Symbol, Date, High, Low FROM '{s}' WHERE Date >= '2019-01-01' AND Date <= '2019-12-31';"
    queries.append(q)
print('__RESULT__:')
print(json.dumps(queries))"""

env_args = {'var_call_oWJH2e2TESGyf4ocBKpENPsu': 'file_storage/call_oWJH2e2TESGyf4ocBKpENPsu.json', 'var_call_6IJ97gnR2UJFBusSADOta3S1': 'file_storage/call_6IJ97gnR2UJFBusSADOta3S1.json', 'var_call_ClBzZxwRmbNznzLwBaUNHlGs': 'file_storage/call_ClBzZxwRmbNznzLwBaUNHlGs.json', 'var_call_BNs6rjym3Bdskv5OiHCnDKTI': ['AGMH', 'ALACU', 'AMHC', 'ANDA', 'APEX', 'BCLI', 'BHAT', 'BIOC', 'BKYI', 'BLFS', 'BOSC', 'BOTJ', 'BWEN', 'CBAT', 'CCCL', 'CDMOP', 'CEMI', 'CFBK', 'CFFA', 'CLRB', 'CORV', 'CPAAU', 'CPAH', 'CUBA', 'CVV', 'DZSI', 'ELSE', 'EXPC', 'EYEG', 'FAMI', 'FNCB', 'FSBW', 'FTFT', 'GDYN', 'GLG', 'GRNVU', 'GTEC', 'HCCOU', 'HNNA', 'HQI', 'HRTX', 'IDEX', 'IGIC', 'IOTS', 'ISNS', 'ITI', 'LACQ', 'MBCN', 'MBNKP', 'MCEP', 'MLND', 'MMAC', 'MNCLU', 'MNPR', 'NVEE', 'NXTD', 'OPOF', 'OPTT', 'ORGO', 'ORSNU', 'OTEL', 'PBFS', 'PBTS', 'PCSB', 'PECK', 'PEIX', 'PFIE', 'PLIN', 'POPE', 'QRHC', 'SES', 'SHSP', 'SNSS', 'SSNT', 'STKS', 'TGLS', 'TMSR', 'VERB', 'VMD', 'VRRM', 'VTIQW', 'VVPR', 'WHLM', 'WHLR', 'XBIOW', 'XPEL']}

exec(code, env_args)
