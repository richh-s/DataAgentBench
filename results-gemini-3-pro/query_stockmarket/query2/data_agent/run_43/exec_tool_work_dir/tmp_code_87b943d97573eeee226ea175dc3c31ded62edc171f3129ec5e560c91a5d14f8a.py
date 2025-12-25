code = """import json

# Read lists
path1 = locals()['var_function-call-3062241635553932877']
path2 = locals()['var_function-call-12393690622671255916']

with open(path1, 'r') as f:
    etf_list = json.load(f)
with open(path2, 'r') as f:
    tables_list = json.load(f)

etf_symbols = set(item['Symbol'] for item in etf_list)
common_symbols = sorted(list(etf_symbols.intersection(set(tables_list))))

batch_symbols = common_symbols[0:100]

parts = []
for sym in batch_symbols:
    # "Date" usually YYYY-MM-DD
    q = "SELECT '{0}' as Sym FROM \"{0}\" WHERE \"Date\" LIKE '2015-%' AND \"Adj Close\" > 200 LIMIT 1".format(sym)
    parts.append(q)

query = " UNION ALL ".join(parts)
print("__RESULT__:")
print(json.dumps(query))"""

env_args = {'var_function-call-3062241635553932877': 'file_storage/function-call-3062241635553932877.json', 'var_function-call-12393690622671255916': 'file_storage/function-call-12393690622671255916.json', 'var_function-call-3212137317014693496': 'file_storage/function-call-3212137317014693496.json', 'var_function-call-15925486148284491953': [{'Date': '2003-09-29'}], 'var_function-call-15136510880994038391': {'count': 1435, 'first_50': ['AAAU', 'AADR', 'ABEQ', 'ACSG', 'ACWF', 'AFK', 'AFLG', 'AFMC', 'AFSM', 'AFTY', 'AGG', 'AGGP', 'AGGY', 'AGQ', 'AGZ', 'AIEQ', 'AIIQ', 'AMLP', 'AMOM', 'AMZA', 'AOA', 'AOK', 'AOM', 'AOR', 'ARGT', 'ARKF', 'ARKK', 'ARKW', 'ARMR', 'ASEA', 'ASHR', 'ASHS', 'ASHX', 'AUSF', 'AVDE', 'AVDV', 'AVEM', 'AVUS', 'AVUV', 'AWAY', 'AWTM', 'AXJL', 'BAB', 'BATT', 'BBC', 'BBP', 'BCD', 'BCI', 'BDCY', 'BDRY']}}

exec(code, env_args)
