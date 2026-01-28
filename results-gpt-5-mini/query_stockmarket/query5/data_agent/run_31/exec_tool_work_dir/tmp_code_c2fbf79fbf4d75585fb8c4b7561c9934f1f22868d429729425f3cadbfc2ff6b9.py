code = """import json
p = var_call_BaZERWkVvuAfM9byRYoBpmVZ
with open(p) as f:
    data = json.load(f)
symbols = data['symbols']
# Build and run per-symbol queries via query_db? But must use tools. Instead, prepare the SQL union here and return it
parts = []
for s in symbols:
    parts.append("SELECT '{}' AS symbol, COUNT(*) AS cnt FROM \"{}\" WHERE Date >= '2019-01-01' AND Date <= '2019-12-31' AND (High - Low)/Low > 0.2".format(s,s))
union_sql = "\nUNION ALL\n".join(parts)
sql = 'SELECT symbol, cnt FROM (\n' + union_sql + '\n) ORDER BY cnt DESC LIMIT 5;'
print("__RESULT__:")
print(json.dumps({'sql': sql}))"""

env_args = {'var_call_5ITtwdMNsU1VtppAgfjRubYb': 'file_storage/call_5ITtwdMNsU1VtppAgfjRubYb.json', 'var_call_Ukj7TVJicBB40tkmvqenGyBx': 'file_storage/call_Ukj7TVJicBB40tkmvqenGyBx.json', 'var_call_JjKrgSqh4gfIUOF4WM1EfHvX': {'n_symbols': 86, 'symbols_head': ['AGMH', 'ALACU', 'AMHC', 'ANDA', 'APEX', 'BCLI', 'BHAT', 'BIOC', 'BKYI', 'BLFS', 'BOSC', 'BOTJ', 'BWEN', 'CBAT', 'CCCL', 'CDMOP', 'CEMI', 'CFBK', 'CFFA', 'CLRB']}, 'var_call_BaZERWkVvuAfM9byRYoBpmVZ': 'file_storage/call_BaZERWkVvuAfM9byRYoBpmVZ.json'}

exec(code, env_args)
