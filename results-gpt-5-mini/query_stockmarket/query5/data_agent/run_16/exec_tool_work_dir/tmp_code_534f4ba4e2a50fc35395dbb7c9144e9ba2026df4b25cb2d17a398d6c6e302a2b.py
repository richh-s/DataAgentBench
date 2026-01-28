code = """import json
p1 = var_call_M0U5buiAvISz429MtqwKvqqA
p2 = var_call_4e328mmHfSVOI68hPDqpaEt8
with open(p1, 'r') as f:
    data1 = json.load(f)
with open(p2, 'r') as f:
    data2 = json.load(f)
# data1 is list of dicts with Symbol and Company Description
symbol_to_company = {rec['Symbol']: rec.get('Company Description','') for rec in data1}
tables = set(data2)
common = [s for s in symbol_to_company.keys() if s in tables]
# Build SQL query
selects = []
for s in common:
    comp = symbol_to_company[s].replace("'", "''")
    sel = f"SELECT '{s}' AS symbol, '{comp}' AS company, SUM(CASE WHEN (\"High\" - \"Low\") > 0.2 * \"Low\" AND \"Date\" >= '2019-01-01' AND \"Date\" <= '2019-12-31' THEN 1 ELSE 0 END) AS cnt FROM \"{s}\""
    selects.append(sel)
sql = ' UNION ALL '.join(selects) + ';'
output = {'sql': sql, 'symbols_count': len(common)}
print('__RESULT__:')
print(json.dumps(output))"""

env_args = {'var_call_M0U5buiAvISz429MtqwKvqqA': 'file_storage/call_M0U5buiAvISz429MtqwKvqqA.json', 'var_call_4e328mmHfSVOI68hPDqpaEt8': 'file_storage/call_4e328mmHfSVOI68hPDqpaEt8.json'}

exec(code, env_args)
