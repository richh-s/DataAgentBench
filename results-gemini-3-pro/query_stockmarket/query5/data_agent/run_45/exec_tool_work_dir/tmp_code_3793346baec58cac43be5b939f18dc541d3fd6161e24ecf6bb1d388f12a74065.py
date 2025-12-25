code = """import json

symbols = locals()['var_function-call-5644259161849807501']
dq = chr(34) # double quote
sq = chr(39) # single quote

# Template: SELECT 'SYM' as Symbol, COUNT(*) as DayCount FROM "SYM" WHERE Date LIKE '2019-%' AND (High - Low) > 0.2 * Low
parts = []
for s in symbols:
    q = "SELECT " + sq + s + sq + " as Symbol, COUNT(*) as DayCount FROM " + dq + s + dq + " WHERE Date LIKE " + sq + "2019-%" + sq + " AND (High - Low) > 0.2 * Low"
    parts.append(q)

query = " UNION ALL ".join(parts)
query += " ORDER BY DayCount DESC LIMIT 5"

print("__RESULT__:")
print(json.dumps(query))"""

env_args = {'var_function-call-752038609392442353': 'file_storage/function-call-752038609392442353.json', 'var_function-call-16254905597670293192': 'file_storage/function-call-16254905597670293192.json', 'var_function-call-5644259161849807501': ['AGMH', 'ALACU', 'AMHC', 'ANDA', 'APEX', 'BCLI', 'BHAT', 'BIOC', 'BKYI', 'BLFS', 'BOSC', 'BOTJ', 'BWEN', 'CBAT', 'CCCL', 'CDMOP', 'CEMI', 'CFBK', 'CFFA', 'CLRB', 'CORV', 'CPAAU', 'CPAH', 'CUBA', 'CVV', 'DZSI', 'ELSE', 'EXPC', 'EYEG', 'FAMI', 'FNCB', 'FSBW', 'FTFT', 'GDYN', 'GLG', 'GRNVU', 'GTEC', 'HCCOU', 'HNNA', 'HQI', 'HRTX', 'IDEX', 'IGIC', 'IOTS', 'ISNS', 'ITI', 'LACQ', 'MBCN', 'MBNKP', 'MCEP', 'MLND', 'MMAC', 'MNCLU', 'MNPR', 'NVEE', 'NXTD', 'OPOF', 'OPTT', 'ORGO', 'ORSNU', 'OTEL', 'PBFS', 'PBTS', 'PCSB', 'PECK', 'PEIX', 'PFIE', 'PLIN', 'POPE', 'QRHC', 'SES', 'SHSP', 'SNSS', 'SSNT', 'STKS', 'TGLS', 'TMSR', 'VERB', 'VMD', 'VRRM', 'VTIQW', 'VVPR', 'WHLM', 'WHLR', 'XBIOW', 'XPEL'], 'var_function-call-14571389207841715059': 'file_storage/function-call-14571389207841715059.json', 'var_function-call-6245818421001581415': "<class 'list'> : ['AGMH', 'ALACU', 'AMHC', 'ANDA', 'APEX', 'BCLI', 'BHAT', 'BIOC', 'BKYI', 'BLFS', 'BOSC', 'BOTJ', 'B"}

exec(code, env_args)
