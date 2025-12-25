code = """import json

p1 = locals()['var_function-call-3062241635553932877']
p2 = locals()['var_function-call-12393690622671255916']

with open(p1, 'r') as f:
    d1 = json.load(f)
with open(p2, 'r') as f:
    d2 = json.load(f)

syms = sorted(list(set(x['Symbol'] for x in d1).intersection(set(d2))))
batch = syms[:100]

dq = chr(34)
sq = chr(39)

qs = []
for s in batch:
    # SELECT 'SYM' as Sym FROM "SYM" WHERE "Date" LIKE '2015-%' AND "Adj Close" > 200 LIMIT 1
    q = "SELECT " + sq + s + sq + " as Sym FROM " + dq + s + dq + " WHERE " + dq + "Date" + dq + " LIKE " + sq + "2015-%" + sq + " AND " + dq + "Adj Close" + dq + " > 200 LIMIT 1"
    qs.append(q)

final_q = " UNION ALL ".join(qs)
print("__RESULT__:")
print(json.dumps(final_q))"""

env_args = {'var_function-call-3062241635553932877': 'file_storage/function-call-3062241635553932877.json', 'var_function-call-12393690622671255916': 'file_storage/function-call-12393690622671255916.json', 'var_function-call-3212137317014693496': 'file_storage/function-call-3212137317014693496.json', 'var_function-call-15925486148284491953': [{'Date': '2003-09-29'}], 'var_function-call-15136510880994038391': {'count': 1435, 'first_50': ['AAAU', 'AADR', 'ABEQ', 'ACSG', 'ACWF', 'AFK', 'AFLG', 'AFMC', 'AFSM', 'AFTY', 'AGG', 'AGGP', 'AGGY', 'AGQ', 'AGZ', 'AIEQ', 'AIIQ', 'AMLP', 'AMOM', 'AMZA', 'AOA', 'AOK', 'AOM', 'AOR', 'ARGT', 'ARKF', 'ARKK', 'ARKW', 'ARMR', 'ASEA', 'ASHR', 'ASHS', 'ASHX', 'AUSF', 'AVDE', 'AVDV', 'AVEM', 'AVUS', 'AVUV', 'AWAY', 'AWTM', 'AXJL', 'BAB', 'BATT', 'BBC', 'BBP', 'BCD', 'BCI', 'BDCY', 'BDRY']}, 'var_function-call-18155754807473582638': 'test', 'var_function-call-1125376442052737803': 'read p1 ok', 'var_function-call-5306680939791668335': 'AAAU'}

exec(code, env_args)
