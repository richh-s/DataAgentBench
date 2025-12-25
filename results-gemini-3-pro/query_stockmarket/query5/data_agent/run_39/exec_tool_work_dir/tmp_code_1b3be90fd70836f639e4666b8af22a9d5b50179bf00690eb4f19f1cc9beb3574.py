code = """import json

# Get common symbols from previous result
common_symbols = locals()['var_function-call-12421252814377455322']

# Construct the query
subqueries = []
for sym in common_symbols:
    # Ensure symbol is safe for SQL injection (though here it comes from a list of valid tables)
    # Using double quotes for table identifiers if needed, but typically DuckDB handles standard names.
    # Note: If table names have special characters they need quotes. The list looks alphanumeric.
    sq = f"SELECT '{sym}' as Symbol, COUNT(*) as cnt FROM \"{sym}\" WHERE Date LIKE '2019-%' AND (High - Low) > 0.2 * Low"
    subqueries.append(sq)

full_query = " UNION ALL ".join(subqueries)
full_query += " ORDER BY cnt DESC LIMIT 5"

print("__RESULT__:")
print(json.dumps(full_query))"""

env_args = {'var_function-call-4097608082559162712': 'file_storage/function-call-4097608082559162712.json', 'var_function-call-14328794898966256946': 'file_storage/function-call-14328794898966256946.json', 'var_function-call-12421252814377455322': ['AGMH', 'ALACU', 'AMHC', 'ANDA', 'APEX', 'BCLI', 'BHAT', 'BIOC', 'BKYI', 'BLFS', 'BOSC', 'BOTJ', 'BWEN', 'CBAT', 'CCCL', 'CDMOP', 'CEMI', 'CFBK', 'CFFA', 'CLRB', 'CORV', 'CPAAU', 'CPAH', 'CUBA', 'CVV', 'DZSI', 'ELSE', 'EXPC', 'EYEG', 'FAMI', 'FNCB', 'FSBW', 'FTFT', 'GDYN', 'GLG', 'GRNVU', 'GTEC', 'HCCOU', 'HNNA', 'HQI', 'HRTX', 'IDEX', 'IGIC', 'IOTS', 'ISNS', 'ITI', 'LACQ', 'MBCN', 'MBNKP', 'MCEP', 'MLND', 'MMAC', 'MNCLU', 'MNPR', 'NVEE', 'NXTD', 'OPOF', 'OPTT', 'ORGO', 'ORSNU', 'OTEL', 'PBFS', 'PBTS', 'PCSB', 'PECK', 'PEIX', 'PFIE', 'PLIN', 'POPE', 'QRHC', 'SES', 'SHSP', 'SNSS', 'SSNT', 'STKS', 'TGLS', 'TMSR', 'VERB', 'VMD', 'VRRM', 'VTIQW', 'VVPR', 'WHLM', 'WHLR', 'XBIOW', 'XPEL']}

exec(code, env_args)
