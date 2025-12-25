code = """import json

# Get valid_symbols from previous step
valid_symbols = locals()['var_function-call-5644259161849807501']

# Construct query
subqueries = []
for sym in valid_symbols:
    # Use double quotes for table names just in case, though they are likely standard.
    # Check date using string slicing or LIKE for '2019-%'
    # Condition: (High - Low) > 0.2 * Low
    sq = f"SELECT '{sym}' as Symbol, COUNT(*) as DayCount FROM \"{sym}\" WHERE Date LIKE '2019-%' AND (High - Low) > 0.2 * Low"
    subqueries.append(sq)

full_query = " UNION ALL ".join(subqueries) + " ORDER BY DayCount DESC LIMIT 5"

print("__RESULT__:")
print(json.dumps(full_query))"""

env_args = {'var_function-call-752038609392442353': 'file_storage/function-call-752038609392442353.json', 'var_function-call-16254905597670293192': 'file_storage/function-call-16254905597670293192.json', 'var_function-call-5644259161849807501': ['AGMH', 'ALACU', 'AMHC', 'ANDA', 'APEX', 'BCLI', 'BHAT', 'BIOC', 'BKYI', 'BLFS', 'BOSC', 'BOTJ', 'BWEN', 'CBAT', 'CCCL', 'CDMOP', 'CEMI', 'CFBK', 'CFFA', 'CLRB', 'CORV', 'CPAAU', 'CPAH', 'CUBA', 'CVV', 'DZSI', 'ELSE', 'EXPC', 'EYEG', 'FAMI', 'FNCB', 'FSBW', 'FTFT', 'GDYN', 'GLG', 'GRNVU', 'GTEC', 'HCCOU', 'HNNA', 'HQI', 'HRTX', 'IDEX', 'IGIC', 'IOTS', 'ISNS', 'ITI', 'LACQ', 'MBCN', 'MBNKP', 'MCEP', 'MLND', 'MMAC', 'MNCLU', 'MNPR', 'NVEE', 'NXTD', 'OPOF', 'OPTT', 'ORGO', 'ORSNU', 'OTEL', 'PBFS', 'PBTS', 'PCSB', 'PECK', 'PEIX', 'PFIE', 'PLIN', 'POPE', 'QRHC', 'SES', 'SHSP', 'SNSS', 'SSNT', 'STKS', 'TGLS', 'TMSR', 'VERB', 'VMD', 'VRRM', 'VTIQW', 'VVPR', 'WHLM', 'WHLR', 'XBIOW', 'XPEL']}

exec(code, env_args)
