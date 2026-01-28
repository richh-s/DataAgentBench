code = """import json
with open(var_call_zS6ooOlqOTROyoR6BVuOpZjd, 'r') as f:
    stockinfo = json.load(f)
with open(var_call_VE63NDAtYBpaiHZ8oLi7Rhez, 'r') as f:
    tables = json.load(f)
companies = {rec['Symbol']: rec['Company Description'] for rec in stockinfo}
tables_set = set(tables)
intersection = [s for s in companies.keys() if s in tables_set]
parts = []
for sym in intersection:
    part = 'SELECT '\'' + sym + '\'' + " AS symbol, SUM(CASE WHEN \"Date\" >= '2019-01-01' AND \"Date\" <= '2019-12-31' AND (\"High\" - \"Low\") > 0.2 * \"Low\" THEN 1 ELSE 0 END) AS cnt FROM \"" + sym + '\"'
    parts.append(part)
union_sql = '\nUNION ALL\n'.join(parts)
final_sql = 'SELECT symbol, cnt FROM (\n' + union_sql + '\n) ORDER BY cnt DESC LIMIT 5;'
output = {'sql': final_sql, 'companies': {s: companies[s] for s in intersection}}
print('__RESULT__:')
print(json.dumps(output))"""

env_args = {'var_call_zS6ooOlqOTROyoR6BVuOpZjd': 'file_storage/call_zS6ooOlqOTROyoR6BVuOpZjd.json', 'var_call_VE63NDAtYBpaiHZ8oLi7Rhez': 'file_storage/call_VE63NDAtYBpaiHZ8oLi7Rhez.json'}

exec(code, env_args)
