code = """import json

valid_symbols = locals()['var_function-call-13429679675044900580']
if isinstance(valid_symbols, str):
    valid_symbols_list = json.loads(valid_symbols)
else:
    valid_symbols_list = valid_symbols

batch_size = 20
batches = [valid_symbols_list[i:i + batch_size] for i in range(0, len(valid_symbols_list), batch_size)]

queries = []
for batch in batches:
    sub_queries = []
    for sym in batch:
        q = "SELECT '" + sym + "' as Symbol, COUNT(*) as HighVolDays FROM \"" + sym + "\" WHERE Date >= '2019-01-01' AND Date <= '2019-12-31' AND (High - Low) > (0.2 * Low)"
        sub_queries.append(q)
    
    full_query = " UNION ALL ".join(sub_queries)
    queries.append(full_query)

print("__RESULT__:")
print(json.dumps(queries))"""

env_args = {'var_function-call-17271658377004482034': 'file_storage/function-call-17271658377004482034.json', 'var_function-call-14055876743965767825': 'file_storage/function-call-14055876743965767825.json', 'var_function-call-13429679675044900580': ['AGMH', 'ALACU', 'AMHC', 'ANDA', 'APEX', 'BCLI', 'BHAT', 'BIOC', 'BKYI', 'BLFS', 'BOSC', 'BOTJ', 'BWEN', 'CBAT', 'CCCL', 'CDMOP', 'CEMI', 'CFBK', 'CFFA', 'CLRB', 'CORV', 'CPAAU', 'CPAH', 'CUBA', 'CVV', 'DZSI', 'ELSE', 'EXPC', 'EYEG', 'FAMI', 'FNCB', 'FSBW', 'FTFT', 'GDYN', 'GLG', 'GRNVU', 'GTEC', 'HCCOU', 'HNNA', 'HQI', 'HRTX', 'IDEX', 'IGIC', 'IOTS', 'ISNS', 'ITI', 'LACQ', 'MBCN', 'MBNKP', 'MCEP', 'MLND', 'MMAC', 'MNCLU', 'MNPR', 'NVEE', 'NXTD', 'OPOF', 'OPTT', 'ORGO', 'ORSNU', 'OTEL', 'PBFS', 'PBTS', 'PCSB', 'PECK', 'PEIX', 'PFIE', 'PLIN', 'POPE', 'QRHC', 'SES', 'SHSP', 'SNSS', 'SSNT', 'STKS', 'TGLS', 'TMSR', 'VERB', 'VMD', 'VRRM', 'VTIQW', 'VVPR', 'WHLM', 'WHLR', 'XBIOW', 'XPEL'], 'var_function-call-1735299512064745096': 'file_storage/function-call-1735299512064745096.json'}

exec(code, env_args)
