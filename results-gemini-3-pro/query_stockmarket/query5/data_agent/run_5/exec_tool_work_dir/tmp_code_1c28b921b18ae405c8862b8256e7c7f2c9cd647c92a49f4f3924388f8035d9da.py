code = """import json

# Load the valid symbols
with open(locals()['var_function-call-1602718910402106253'], 'r') as f:
    symbols = json.load(f)

# Construct the query
subqueries = []
for sym in symbols:
    # Ensure table names are safe. DuckDB should handle standard names.
    # If the symbol has special chars (unlikely for these), we might need quotes.
    # Let's wrap in double quotes just in case.
    subqueries.append(f"SELECT '{sym}' as Symbol, COUNT(*) as Count FROM \"{sym}\" WHERE Date LIKE '2019%' AND (High - Low) > (0.2 * Low)")

full_query = " UNION ALL ".join(subqueries)
final_query = f"SELECT Symbol, Count FROM ({full_query}) ORDER BY Count DESC LIMIT 5"

print("__RESULT__:")
print(json.dumps(final_query))"""

env_args = {'var_function-call-16810362353464456006': 'file_storage/function-call-16810362353464456006.json', 'var_function-call-16803666523160065497': 'file_storage/function-call-16803666523160065497.json', 'var_function-call-1602718910402106253': ['AGMH', 'ALACU', 'AMHC', 'ANDA', 'APEX', 'BCLI', 'BHAT', 'BIOC', 'BKYI', 'BLFS', 'BOSC', 'BOTJ', 'BWEN', 'CBAT', 'CCCL', 'CDMOP', 'CEMI', 'CFBK', 'CFFA', 'CLRB', 'CORV', 'CPAAU', 'CPAH', 'CUBA', 'CVV', 'DZSI', 'ELSE', 'EXPC', 'EYEG', 'FAMI', 'FNCB', 'FSBW', 'FTFT', 'GDYN', 'GLG', 'GRNVU', 'GTEC', 'HCCOU', 'HNNA', 'HQI', 'HRTX', 'IDEX', 'IGIC', 'IOTS', 'ISNS', 'ITI', 'LACQ', 'MBCN', 'MBNKP', 'MCEP', 'MLND', 'MMAC', 'MNCLU', 'MNPR', 'NVEE', 'NXTD', 'OPOF', 'OPTT', 'ORGO', 'ORSNU', 'OTEL', 'PBFS', 'PBTS', 'PCSB', 'PECK', 'PEIX', 'PFIE', 'PLIN', 'POPE', 'QRHC', 'SES', 'SHSP', 'SNSS', 'SSNT', 'STKS', 'TGLS', 'TMSR', 'VERB', 'VMD', 'VRRM', 'VTIQW', 'VVPR', 'WHLM', 'WHLR', 'XBIOW', 'XPEL']}

exec(code, env_args)
