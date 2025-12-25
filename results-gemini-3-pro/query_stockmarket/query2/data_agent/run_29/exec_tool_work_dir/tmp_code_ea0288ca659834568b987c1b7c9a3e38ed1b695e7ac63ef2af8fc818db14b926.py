code = """import json

key = 'var_function-call-7704237748048051693'
with open(locals()[key], 'r') as f:
    syms = json.load(f)

qs = []
for i in range(0, len(syms), 300):
    chunk = syms[i:i+300]
    parts = []
    for s in chunk:
        # construct string carefully
        # We want: SELECT 'S' as Symbol FROM "S" WHERE "Date" LIKE '2015-%' AND "Adj Close" > 200 LIMIT 1
        # Using single quotes for python strings where possible
        part = 'SELECT \'' + s + '\' as Symbol FROM "' + s + '" WHERE "Date" LIKE \'2015-%\' AND "Adj Close" > 200 LIMIT 1'
        parts.append(part)
    qs.append(" UNION ALL ".join(parts))

print("__RESULT__:")
print(json.dumps(qs))"""

env_args = {'var_function-call-3424898909852780043': [{'ETF': 'Y', 'Listing Exchange': 'P'}, {'ETF': 'N', 'Listing Exchange': 'Q'}, {'ETF': 'Y', 'Listing Exchange': 'Q'}, {'ETF': 'Y', 'Listing Exchange': 'Z'}, {'ETF': 'N', 'Listing Exchange': 'A'}, {'ETF': 'N', 'Listing Exchange': 'N'}, {'ETF': 'N', 'Listing Exchange': 'Z'}, {'ETF': 'N', 'Listing Exchange': 'P'}, {'ETF': 'Y', 'Listing Exchange': 'A'}], 'var_function-call-2015005240419911970': 'file_storage/function-call-2015005240419911970.json', 'var_function-call-3113271170216609049': 'file_storage/function-call-3113271170216609049.json', 'var_function-call-7704237748048051693': 'file_storage/function-call-7704237748048051693.json', 'var_function-call-735419123404957743': 1435}

exec(code, env_args)
