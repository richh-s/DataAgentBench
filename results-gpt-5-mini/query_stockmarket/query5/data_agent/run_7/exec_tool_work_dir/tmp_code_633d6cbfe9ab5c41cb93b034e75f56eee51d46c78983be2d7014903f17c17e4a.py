code = """import json
p = var_call_4sbjtOXtdORPt2oBnxRCNCTC
with open(p, 'r') as f:
    data = json.load(f)
symbols = data['symbols']
parts = []
for s in symbols:
    # ensure double quotes around table name for DuckDB
    parts.append(f"(SELECT '{s}' AS Symbol, COUNT(*) AS cnt FROM \"{s}\" WHERE Date >= '2019-01-01' AND Date <= '2019-12-31' AND High > 1.2 * Low)")
if parts:
    union_sql = ' UNION ALL '.join(parts)
    sql = f'SELECT Symbol, cnt FROM ({union_sql}) AS t ORDER BY cnt DESC LIMIT 5;'
else:
    sql = ''
print('__RESULT__:')
print(json.dumps(sql))"""

env_args = {'var_call_g29DMfGZ1F5iPmMFwe0rGJmZ': 'file_storage/call_g29DMfGZ1F5iPmMFwe0rGJmZ.json', 'var_call_NxAzjzgAprbtYGql6TUtUGiP': 'file_storage/call_NxAzjzgAprbtYGql6TUtUGiP.json', 'var_call_4sbjtOXtdORPt2oBnxRCNCTC': 'file_storage/call_4sbjtOXtdORPt2oBnxRCNCTC.json', 'var_call_aEHqy1wGYvVbtndyo9NiupWw': 86}

exec(code, env_args)
