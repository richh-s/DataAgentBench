code = """import json

data = locals()['var_function-call-13429679675044900580']
if isinstance(data, str):
    data = json.loads(data)

queries = []
current_batch = []
count = 0
for sym in data:
    # Construct query string using concatenation to be safe
    q = "SELECT '" + sym + "' as Symbol, COUNT(*) as HighVolDays FROM \"" + sym + "\" WHERE Date >= '2019-01-01' AND Date <= '2019-12-31' AND (High - Low) > (0.2 * Low)"
    current_batch.append(q)
    count += 1
    if count == 40:
        queries.append(" UNION ALL ".join(current_batch))
        current_batch = []
        count = 0

if len(current_batch) > 0:
    queries.append(" UNION ALL ".join(current_batch))

print("__RESULT__:")
print(json.dumps(queries))"""

env_args = {'var_function-call-17271658377004482034': 'file_storage/function-call-17271658377004482034.json', 'var_function-call-14055876743965767825': 'file_storage/function-call-14055876743965767825.json', 'var_function-call-13429679675044900580': ['AGMH', 'ALACU', 'AMHC', 'ANDA', 'APEX', 'BCLI', 'BHAT', 'BIOC', 'BKYI', 'BLFS', 'BOSC', 'BOTJ', 'BWEN', 'CBAT', 'CCCL', 'CDMOP', 'CEMI', 'CFBK', 'CFFA', 'CLRB', 'CORV', 'CPAAU', 'CPAH', 'CUBA', 'CVV', 'DZSI', 'ELSE', 'EXPC', 'EYEG', 'FAMI', 'FNCB', 'FSBW', 'FTFT', 'GDYN', 'GLG', 'GRNVU', 'GTEC', 'HCCOU', 'HNNA', 'HQI', 'HRTX', 'IDEX', 'IGIC', 'IOTS', 'ISNS', 'ITI', 'LACQ', 'MBCN', 'MBNKP', 'MCEP', 'MLND', 'MMAC', 'MNCLU', 'MNPR', 'NVEE', 'NXTD', 'OPOF', 'OPTT', 'ORGO', 'ORSNU', 'OTEL', 'PBFS', 'PBTS', 'PCSB', 'PECK', 'PEIX', 'PFIE', 'PLIN', 'POPE', 'QRHC', 'SES', 'SHSP', 'SNSS', 'SSNT', 'STKS', 'TGLS', 'TMSR', 'VERB', 'VMD', 'VRRM', 'VTIQW', 'VVPR', 'WHLM', 'WHLR', 'XBIOW', 'XPEL'], 'var_function-call-1735299512064745096': 'file_storage/function-call-1735299512064745096.json', 'var_function-call-12915711678069815314': 'file_storage/function-call-12915711678069815314.json'}

exec(code, env_args)
