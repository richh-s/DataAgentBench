code = """import json
v = var_call_4sbjtOXtdORPt2oBnxRCNCTC
symbols = v['symbols']
# build SQL safely
parts = []
for s in symbols:
    # table name
    t = s
    part = '(SELECT \'' + s + '\' AS Symbol, COUNT(*) AS cnt FROM "' + t + '" WHERE Date >= \'2019-01-01\' AND Date <= \'2019-12-31\' AND High > 1.2 * Low)'
    parts.append(part)
if parts:
    sql = ' UNION ALL '.join(parts)
    sql = 'SELECT Symbol, cnt FROM (' + sql + ') AS t ORDER BY cnt DESC LIMIT 5;'
else:
    sql = ''
print('__RESULT__:')
print(json.dumps(sql))"""

env_args = {'var_call_g29DMfGZ1F5iPmMFwe0rGJmZ': 'file_storage/call_g29DMfGZ1F5iPmMFwe0rGJmZ.json', 'var_call_NxAzjzgAprbtYGql6TUtUGiP': 'file_storage/call_NxAzjzgAprbtYGql6TUtUGiP.json', 'var_call_4sbjtOXtdORPt2oBnxRCNCTC': 'file_storage/call_4sbjtOXtdORPt2oBnxRCNCTC.json'}

exec(code, env_args)
