code = """import json

# Load symbols from previous result
with open(locals()['var_function-call-4138560473481984299'], 'r') as f:
    stock_info = json.load(f)
target_symbols = set([item['Symbol'] for item in stock_info])

# Load tables from list_db result
with open(locals()['var_function-call-1719822641682209723'], 'r') as f:
    all_tables = json.load(f)

# Find intersection
# Note: table names in DuckDB might be case sensitive or not, usually they match the ticker.
# The previous output showed symbols like "AGMH" and tables like "AGMH".
valid_symbols = [s for s in target_symbols if s in all_tables]

print(f"Found {len(valid_symbols)} valid symbols out of {len(target_symbols)} targets.")

# Construct the SQL query
# We want: 5 companies with highest number of days in 2019 where (High - Low) > 0.2 * Low
# Query structure:
# SELECT 'SYM' as Symbol, COUNT(*) as DayCount FROM SYM WHERE Date BETWEEN '2019-01-01' AND '2019-12-31' AND (High - Low) > (0.2 * Low)
# UNION ALL ...
# ORDER BY DayCount DESC LIMIT 5

queries = []
for sym in valid_symbols:
    # Double quote table names just in case
    q = f"SELECT '{sym}' as Symbol, COUNT(*) as DayCount FROM \"{sym}\" WHERE Date >= '2019-01-01' AND Date <= '2019-12-31' AND (High - Low) > (0.2 * Low)"
    queries.append(q)

final_query = " UNION ALL ".join(queries) + " ORDER BY DayCount DESC LIMIT 5"

print("__RESULT__:")
print(json.dumps(final_query))"""

env_args = {'var_function-call-4138560473481984299': 'file_storage/function-call-4138560473481984299.json', 'var_function-call-14789780059638436224': ['AGMH', 'ALACU', 'AMHC', 'ANDA', 'APEX', 'BCLI', 'BHAT', 'BIOC', 'BKYI', 'BLFS', 'BOSC', 'BOTJ', 'BWEN', 'CBAT', 'CCCL', 'CDMOP', 'CEMI', 'CFBK', 'CFFA', 'CLRB', 'CORV', 'CPAAU', 'CPAH', 'CUBA', 'CVV', 'DZSI', 'ELSE', 'EXPC', 'EYEG', 'FAMI', 'FNCB', 'FSBW', 'FTFT', 'GDYN', 'GLG', 'GRNVU', 'GTEC', 'HCCOU', 'HNNA', 'HQI', 'HRTX', 'IDEX', 'IGIC', 'IOTS', 'ISNS', 'ITI', 'LACQ', 'MBCN', 'MBNKP', 'MCEP', 'MLND', 'MMAC', 'MNCLU', 'MNPR', 'NVEE', 'NXTD', 'OPOF', 'OPTT', 'ORGO', 'ORSNU', 'OTEL', 'PBFS', 'PBTS', 'PCSB', 'PECK', 'PEIX', 'PFIE', 'PLIN', 'POPE', 'QRHC', 'SES', 'SHSP', 'SNSS', 'SSNT', 'STKS', 'TGLS', 'TMSR', 'VERB', 'VMD', 'VRRM', 'VTIQW', 'VVPR', 'WHLM', 'WHLR', 'XBIOW', 'XPEL'], 'var_function-call-1719822641682209723': 'file_storage/function-call-1719822641682209723.json'}

exec(code, env_args)
