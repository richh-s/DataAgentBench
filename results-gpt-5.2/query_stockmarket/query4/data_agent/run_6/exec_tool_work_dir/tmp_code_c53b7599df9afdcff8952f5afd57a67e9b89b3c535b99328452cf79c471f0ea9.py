code = """import json
path = var_call_aVBZfUMD37JtWx1yok1UClxY
with open(path,'r') as f:
    q=json.load(f)['query']
q=q.replace('FROM +tbl+','FROM "AEFC"')
print('__RESULT__:')
print(json.dumps(q[:2000]))"""

env_args = {'var_call_FQnZeeqY6jpP92SSHDkMcZsR': 'file_storage/call_FQnZeeqY6jpP92SSHDkMcZsR.json', 'var_call_o12akxaYuEB1Fv7HiBkYhkab': 'file_storage/call_o12akxaYuEB1Fv7HiBkYhkab.json', 'var_call_opCijmaeUXZdRBS5lKhefJMz': 'file_storage/call_opCijmaeUXZdRBS5lKhefJMz.json', 'var_call_Uyj2b73FTABzHMBKhLz9PIMy': 'file_storage/call_Uyj2b73FTABzHMBKhLz9PIMy.json', 'var_call_ZvHnxSV6ZpRAd5PRHjjrXX0n': {'syms': ['AEFC', 'AIN', 'AIV', 'AIZP', 'AJRD'], 'n': 234}, 'var_call_qDmxYxPMxZY6rB1Nd6cQB444': {'len': 48135, 'head': "SELECT symbol, up_days, down_days, (up_days - down_days) AS diff FROM (SELECT 'AEFC' AS symbol, SUM(CASE WHEN Close>Open THEN 1 ELSE 0 END) AS up_days, SUM(CASE WHEN Close<Open THEN 1 ELSE 0 END) AS down_days FROM +tbl+ WHERE Date>='2017-01-01' AND Date<'2018-01-01' UNION ALL SELECT 'AIN' AS symbol, SUM(CASE WHEN Close>Open THEN 1 ELSE 0 END) AS up_days, SUM(CASE WHEN Close<Open THEN 1 ELSE 0 END) AS down_days FROM +tbl+ WHERE Date>='2017-01-01' AND Date<'2018-01-01' UNION ALL SELECT 'AIV' AS sy"}, 'var_call_aVBZfUMD37JtWx1yok1UClxY': 'file_storage/call_aVBZfUMD37JtWx1yok1UClxY.json'}

exec(code, env_args)
