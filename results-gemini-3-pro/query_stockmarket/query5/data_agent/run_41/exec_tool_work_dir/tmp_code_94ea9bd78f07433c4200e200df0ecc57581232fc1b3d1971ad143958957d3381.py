code = """import json

path1 = locals()['var_function-call-4138560473481984299']
path2 = locals()['var_function-call-1719822641682209723']

with open(path1, 'r') as f:
    stock_info = json.load(f)

with open(path2, 'r') as f:
    all_tables = json.load(f)

# unique symbols from stockinfo
target_symbols = set()
for item in stock_info:
    target_symbols.add(item['Symbol'])

# check against tables
valid_symbols = []
for sym in target_symbols:
    if sym in all_tables:
        valid_symbols.append(sym)

# Construct query
queries = []
for sym in valid_symbols:
    # Use format to avoid quote escaping hell if possible
    # SQL: SELECT 'SYM' as Symbol, COUNT(*) as DayCount FROM "SYM" WHERE Date >= '2019-01-01' AND Date <= '2019-12-31' AND (High - Low) > (0.2 * Low)
    q = "SELECT '{0}' as Symbol, COUNT(*) as DayCount FROM \"{0}\" WHERE Date >= '2019-01-01' AND Date <= '2019-12-31' AND (High - Low) > (0.2 * Low)".format(sym)
    queries.append(q)

if not queries:
    final_query = "SELECT 'None' as Symbol, 0 as DayCount"
else:
    final_query = " UNION ALL ".join(queries)
    final_query += " ORDER BY DayCount DESC LIMIT 5"

print("__RESULT__:")
print(json.dumps(final_query))"""

env_args = {'var_function-call-4138560473481984299': 'file_storage/function-call-4138560473481984299.json', 'var_function-call-14789780059638436224': ['AGMH', 'ALACU', 'AMHC', 'ANDA', 'APEX', 'BCLI', 'BHAT', 'BIOC', 'BKYI', 'BLFS', 'BOSC', 'BOTJ', 'BWEN', 'CBAT', 'CCCL', 'CDMOP', 'CEMI', 'CFBK', 'CFFA', 'CLRB', 'CORV', 'CPAAU', 'CPAH', 'CUBA', 'CVV', 'DZSI', 'ELSE', 'EXPC', 'EYEG', 'FAMI', 'FNCB', 'FSBW', 'FTFT', 'GDYN', 'GLG', 'GRNVU', 'GTEC', 'HCCOU', 'HNNA', 'HQI', 'HRTX', 'IDEX', 'IGIC', 'IOTS', 'ISNS', 'ITI', 'LACQ', 'MBCN', 'MBNKP', 'MCEP', 'MLND', 'MMAC', 'MNCLU', 'MNPR', 'NVEE', 'NXTD', 'OPOF', 'OPTT', 'ORGO', 'ORSNU', 'OTEL', 'PBFS', 'PBTS', 'PCSB', 'PECK', 'PEIX', 'PFIE', 'PLIN', 'POPE', 'QRHC', 'SES', 'SHSP', 'SNSS', 'SSNT', 'STKS', 'TGLS', 'TMSR', 'VERB', 'VMD', 'VRRM', 'VTIQW', 'VVPR', 'WHLM', 'WHLR', 'XBIOW', 'XPEL'], 'var_function-call-1719822641682209723': 'file_storage/function-call-1719822641682209723.json'}

exec(code, env_args)
