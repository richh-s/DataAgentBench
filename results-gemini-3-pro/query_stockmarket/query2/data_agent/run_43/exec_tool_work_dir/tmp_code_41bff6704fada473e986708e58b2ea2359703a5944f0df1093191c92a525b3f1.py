code = """import json

# Read lists
with open(locals()['var_function-call-3062241635553932877'], 'r') as f:
    etf_list = json.load(f)
with open(locals()['var_function-call-12393690622671255916'], 'r') as f:
    tables_list = json.load(f)

etf_symbols = set(item['Symbol'] for item in etf_list)
common_symbols = sorted(list(etf_symbols.intersection(set(tables_list))))

batch_symbols = common_symbols[0:100]

# Construct query
parts = []
for sym in batch_symbols:
    # Use "Date" LIKE '2015-%' to be safe and specific
    # Using double quotes for identifiers is safer in DuckDB if symbols have reserved words, but usually safe.
    # Note: DuckDB table names are case sensitive if created that way? 
    # The list_db returned keys. I should use them exactly.
    # The list_db result showed uppercase.
    part = f"SELECT '{sym}' as Sym FROM \"{sym}\" WHERE \"Date\" LIKE '2015-%' AND \"Adj Close\" > 200 LIMIT 1"
    parts.append(part)

query = " UNION ALL ".join(parts)
print("__RESULT__:")
print(json.dumps(query))"""

env_args = {'var_function-call-3062241635553932877': 'file_storage/function-call-3062241635553932877.json', 'var_function-call-12393690622671255916': 'file_storage/function-call-12393690622671255916.json', 'var_function-call-3212137317014693496': 'file_storage/function-call-3212137317014693496.json', 'var_function-call-15925486148284491953': [{'Date': '2003-09-29'}], 'var_function-call-15136510880994038391': {'count': 1435, 'first_50': ['AAAU', 'AADR', 'ABEQ', 'ACSG', 'ACWF', 'AFK', 'AFLG', 'AFMC', 'AFSM', 'AFTY', 'AGG', 'AGGP', 'AGGY', 'AGQ', 'AGZ', 'AIEQ', 'AIIQ', 'AMLP', 'AMOM', 'AMZA', 'AOA', 'AOK', 'AOM', 'AOR', 'ARGT', 'ARKF', 'ARKK', 'ARKW', 'ARMR', 'ASEA', 'ASHR', 'ASHS', 'ASHX', 'AUSF', 'AVDE', 'AVDV', 'AVEM', 'AVUS', 'AVUV', 'AWAY', 'AWTM', 'AXJL', 'BAB', 'BATT', 'BBC', 'BBP', 'BCD', 'BCI', 'BDCY', 'BDRY']}}

exec(code, env_args)
