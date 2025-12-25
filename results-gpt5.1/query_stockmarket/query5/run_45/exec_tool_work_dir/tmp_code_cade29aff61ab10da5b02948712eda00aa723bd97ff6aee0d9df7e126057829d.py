code = """import json
symbols = var_call_MfUHnN5Zi01CZowe8NijTq4m

queries = []
for sym in symbols:
    q = f"SELECT '{sym}' AS Symbol, Date, High, Low FROM '{sym}' WHERE Date LIKE '2019-%';"
    queries.append(q)

union_query = " UNION ALL ".join(queries)

print("__RESULT__:")
print(json.dumps(union_query))"""

env_args = {'var_call_B2M7G0jKhwkzf7Yh3TG2wneV': 'file_storage/call_B2M7G0jKhwkzf7Yh3TG2wneV.json', 'var_call_AcKDswczsOcXnXZEVKxFjaXp': 'file_storage/call_AcKDswczsOcXnXZEVKxFjaXp.json', 'var_call_MfUHnN5Zi01CZowe8NijTq4m': ['AGMH', 'ALACU', 'AMHC', 'ANDA', 'APEX', 'BCLI', 'BHAT', 'BIOC', 'BKYI', 'BLFS', 'BOSC', 'BOTJ', 'BWEN', 'CBAT', 'CCCL', 'CDMOP', 'CEMI', 'CFBK', 'CFFA', 'CLRB', 'CORV', 'CPAAU', 'CPAH', 'CUBA', 'CVV', 'DZSI', 'ELSE', 'EXPC', 'EYEG', 'FAMI', 'FNCB', 'FSBW', 'FTFT', 'GDYN', 'GLG', 'GRNVU', 'GTEC', 'HCCOU', 'HNNA', 'HQI', 'HRTX', 'IDEX', 'IGIC', 'IOTS', 'ISNS', 'ITI', 'LACQ', 'MBCN', 'MBNKP', 'MCEP', 'MLND', 'MMAC', 'MNCLU', 'MNPR', 'NVEE', 'NXTD', 'OPOF', 'OPTT', 'ORGO', 'ORSNU', 'OTEL', 'PBFS', 'PBTS', 'PCSB', 'PECK', 'PEIX', 'PFIE', 'PLIN', 'POPE', 'QRHC', 'SES', 'SHSP', 'SNSS', 'SSNT', 'STKS', 'TGLS', 'TMSR', 'VERB', 'VMD', 'VRRM', 'VTIQW', 'VVPR', 'WHLM', 'WHLR', 'XBIOW', 'XPEL']}

exec(code, env_args)
