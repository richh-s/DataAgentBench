code = """import json, pandas as pd, os

path = var_call_f0tZYwaaJXmBTZbZRBoXwb1q
with open(path, 'r') as f:
    tables = json.load(f)
valid = sorted({row['table_name'] for row in tables})

queries = []
for sym in valid:
    q = f"SELECT '{sym}' AS Symbol, Date, `Adj Close` FROM `{sym}` WHERE Date >= '2015-01-01' AND Date <= '2015-12-31' AND `Adj Close` > 200.0"
    queries.append(q)

if queries:
    union_query = " UNION ALL ".join(queries)
else:
    union_query = "SELECT NULL AS Symbol, NULL AS Date, NULL AS `Adj Close` WHERE 1=0"

print("__RESULT__:")
print(json.dumps(union_query))"""

env_args = {'var_call_wqklihAasrBKRuoWyy8oUS7J': 'file_storage/call_wqklihAasrBKRuoWyy8oUS7J.json', 'var_call_OsjvFxMov1crpVghIc8litG0': 'file_storage/call_OsjvFxMov1crpVghIc8litG0.json', 'var_call_j9IsO58A2IOQawvk4SsZtfHH': 'file_storage/call_j9IsO58A2IOQawvk4SsZtfHH.json', 'var_call_2aeL0LJVfvfpaVKAGBUrgufy': 'file_storage/call_2aeL0LJVfvfpaVKAGBUrgufy.json', 'var_call_f0tZYwaaJXmBTZbZRBoXwb1q': 'file_storage/call_f0tZYwaaJXmBTZbZRBoXwb1q.json'}

exec(code, env_args)
