code = """import json
symbols = var_call_SPTjz6NxUPJwCqBAqotOVftP

parts = []
for s in symbols:
    part = f"SELECT '{s}' AS Symbol, COUNT(*) AS cnt FROM \"{s}\" WHERE \"Date\" >= '2019-01-01' AND \"Date\" <= '2019-12-31' AND ((\"High\" - \"Low\") / NULLIF(\"Low\",0)) > 0.2"
    parts.append(part)

sql = 'SELECT Symbol, cnt FROM (' + ' UNION ALL '.join(parts) + ') ORDER BY cnt DESC LIMIT 5;'
res = {'sql': sql}
print('__RESULT__:')
print(json.dumps(res))"""

env_args = {'var_call_glwAqwUanNo8ExlokGyMH5xr': 'file_storage/call_glwAqwUanNo8ExlokGyMH5xr.json', 'var_call_b8L0GzZtBYwGmNoVw96WDvnt': 'file_storage/call_b8L0GzZtBYwGmNoVw96WDvnt.json', 'var_call_3rCgDdperyl00Y2GTbxKWHEa': 'file_storage/call_3rCgDdperyl00Y2GTbxKWHEa.json', 'var_call_Phj0Ocjc3o8Ydg7irHG2GHq1': {'symbols_considered_count': 86, 'first_20': ['AGMH', 'ALACU', 'AMHC', 'ANDA', 'APEX', 'BCLI', 'BHAT', 'BIOC', 'BKYI', 'BLFS', 'BOSC', 'BOTJ', 'BWEN', 'CBAT', 'CCCL', 'CDMOP', 'CEMI', 'CFBK', 'CFFA', 'CLRB']}, 'var_call_SPTjz6NxUPJwCqBAqotOVftP': ['AGMH', 'ALACU', 'AMHC', 'ANDA', 'APEX', 'BCLI', 'BHAT', 'BIOC', 'BKYI', 'BLFS', 'BOSC', 'BOTJ', 'BWEN', 'CBAT', 'CCCL', 'CDMOP', 'CEMI', 'CFBK', 'CFFA', 'CLRB', 'CORV', 'CPAAU', 'CPAH', 'CUBA', 'CVV', 'DZSI', 'ELSE', 'EXPC', 'EYEG', 'FAMI', 'FNCB', 'FSBW', 'FTFT', 'GDYN', 'GLG', 'GRNVU', 'GTEC', 'HCCOU', 'HNNA', 'HQI', 'HRTX', 'IDEX', 'IGIC', 'IOTS', 'ISNS', 'ITI', 'LACQ', 'MBCN', 'MBNKP', 'MCEP', 'MLND', 'MMAC', 'MNCLU', 'MNPR', 'NVEE', 'NXTD', 'OPOF', 'OPTT', 'ORGO', 'ORSNU', 'OTEL', 'PBFS', 'PBTS', 'PCSB', 'PECK', 'PEIX', 'PFIE', 'PLIN', 'POPE', 'QRHC', 'SES', 'SHSP', 'SNSS', 'SSNT', 'STKS', 'TGLS', 'TMSR', 'VERB', 'VMD', 'VRRM', 'VTIQW', 'VVPR', 'WHLM', 'WHLR', 'XBIOW', 'XPEL']}

exec(code, env_args)
