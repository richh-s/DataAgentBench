code = """import json, pandas as pd

src = var_call_kAC0K9TV4dAzsdbJNSCCsokM
if isinstance(src, str) and src.endswith('.json'):
    with open(src, 'r') as f:
        recs = json.load(f)
else:
    recs = src

df = pd.DataFrame(recs)
symbols = sorted(df['Symbol'].dropna().unique().tolist())

sym_list_sql = '(' + ','.join(["'" + s.replace("'","''") + "'" for s in symbols]) + ')'
sql = (
    "SELECT table_name AS Symbol "
    "FROM information_schema.tables "
    "WHERE table_schema = 'main' "
    "AND table_type = 'BASE TABLE' "
    f"AND table_name IN {sym_list_sql};"
)

print('__RESULT__:')
print(json.dumps({'symbols_total': len(symbols), 'symbols_sql': sql}))"""

env_args = {'var_call_kAC0K9TV4dAzsdbJNSCCsokM': 'file_storage/call_kAC0K9TV4dAzsdbJNSCCsokM.json'}

exec(code, env_args)
