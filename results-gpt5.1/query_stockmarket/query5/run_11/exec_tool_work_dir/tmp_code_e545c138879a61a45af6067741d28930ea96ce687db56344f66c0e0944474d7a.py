code = """import json
syms = var_call_HELrrhKdkKgivLd39qx9DlCH
qs = []
for s in syms:
  qs.append(f"SELECT '{s}' as Symbol, Date, High, Low FROM '{s}' WHERE Date LIKE '2019-%';")
query = ' UNION ALL '.join(qs)
print('__RESULT__:')
print(json.dumps(query))"""

env_args = {'var_call_H94lmzQaqTHEvqOzZgbJZ9EA': 'file_storage/call_H94lmzQaqTHEvqOzZgbJZ9EA.json', 'var_call_03Be6qECagmtBF6SITGZCPlD': 'file_storage/call_03Be6qECagmtBF6SITGZCPlD.json', 'var_call_HELrrhKdkKgivLd39qx9DlCH': ['AGMH', 'ALACU', 'AMHC', 'ANDA', 'APEX', 'BCLI', 'BHAT', 'BIOC', 'BKYI', 'BLFS', 'BOSC', 'BOTJ', 'BWEN', 'CBAT', 'CCCL', 'CDMOP', 'CEMI', 'CFBK', 'CFFA', 'CLRB', 'CORV', 'CPAAU', 'CPAH', 'CUBA', 'CVV', 'DZSI', 'ELSE', 'EXPC', 'EYEG', 'FAMI', 'FNCB', 'FSBW', 'FTFT', 'GDYN', 'GLG', 'GRNVU', 'GTEC', 'HCCOU', 'HNNA', 'HQI', 'HRTX', 'IDEX', 'IGIC', 'IOTS', 'ISNS', 'ITI', 'LACQ', 'MBCN', 'MBNKP', 'MCEP', 'MLND', 'MMAC', 'MNCLU', 'MNPR', 'NVEE', 'NXTD', 'OPOF', 'OPTT', 'ORGO', 'ORSNU', 'OTEL', 'PBFS', 'PBTS', 'PCSB', 'PECK', 'PEIX', 'PFIE', 'PLIN', 'POPE', 'QRHC', 'SES', 'SHSP', 'SNSS', 'SSNT', 'STKS', 'TGLS', 'TMSR', 'VERB', 'VMD', 'VRRM', 'VTIQW', 'VVPR', 'WHLM', 'WHLR', 'XBIOW', 'XPEL']}

exec(code, env_args)
