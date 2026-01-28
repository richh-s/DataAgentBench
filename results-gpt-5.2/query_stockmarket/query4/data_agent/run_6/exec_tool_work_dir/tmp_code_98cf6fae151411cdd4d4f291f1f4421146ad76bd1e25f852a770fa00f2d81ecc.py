code = """import json
path = var_call_Uyj2b73FTABzHMBKhLz9PIMy
with open(path,'r') as f:
    obj=json.load(f)
syms=obj['avail_symbols']

# create union query with counts for 2017
parts=[]
for s in syms:
    tbl=s.replace('"','')
    q=f"SELECT '{tbl}' AS symbol, SUM(CASE WHEN Close>Open THEN 1 ELSE 0 END) AS up_days, SUM(CASE WHEN Close<Open THEN 1 ELSE 0 END) AS down_days FROM \"{tbl}\" WHERE Date>='2017-01-01' AND Date<'2018-01-01'"
    parts.append(q)
union=' UNION ALL '.join(parts)
final=f"SELECT symbol, up_days, down_days, (up_days - down_days) AS diff FROM ({union}) t WHERE up_days>down_days ORDER BY diff DESC, up_days DESC LIMIT 5;"
print('__RESULT__:')
print(json.dumps({'query': final[:1000], 'len': len(final)}))"""

env_args = {'var_call_FQnZeeqY6jpP92SSHDkMcZsR': 'file_storage/call_FQnZeeqY6jpP92SSHDkMcZsR.json', 'var_call_o12akxaYuEB1Fv7HiBkYhkab': 'file_storage/call_o12akxaYuEB1Fv7HiBkYhkab.json', 'var_call_opCijmaeUXZdRBS5lKhefJMz': 'file_storage/call_opCijmaeUXZdRBS5lKhefJMz.json', 'var_call_Uyj2b73FTABzHMBKhLz9PIMy': 'file_storage/call_Uyj2b73FTABzHMBKhLz9PIMy.json', 'var_call_ZvHnxSV6ZpRAd5PRHjjrXX0n': {'syms': ['AEFC', 'AIN', 'AIV', 'AIZP', 'AJRD'], 'n': 234}}

exec(code, env_args)
