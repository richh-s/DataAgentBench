code = """import json

# Load trade tables
src2 = var_call_R5Fm9qJw8IdgrwecTb if False else var_call_R5Fm9qBHEnIjJw8IdgrwecTb
if isinstance(src2, str):
    with open(src2,'r') as f:
        trade_tables = set(json.load(f))
else:
    trade_tables = set(src2)

# Load stockinfo records
src = var_call_9KkYakqJdaS1o0ssxYdG90nb
if isinstance(src, str):
    with open(src,'r') as f:
        recs = json.load(f)
else:
    recs = src

# only symbols that are valid table names (present in trade_tables)
valid = []
name_map = {}
for r in recs:
    sym = str(r['Symbol'])
    if sym in trade_tables:
        valid.append(sym)
        name_map[sym] = r.get('company_name')

# chunk union all queries
chunk_size = 200
chunks = [valid[i:i+chunk_size] for i in range(0, len(valid), chunk_size)]
chunk_queries = []
for ch in chunks:
    parts = []
    for sym in ch:
        t = '"' + sym.replace('"','""') + '"'
        parts.append(
            "SELECT '{}' AS Symbol, ".format(sym) +
            "SUM(CASE WHEN Close > Open THEN 1 ELSE 0 END) AS up_days, " +
            "SUM(CASE WHEN Close < Open THEN 1 ELSE 0 END) AS down_days " +
            "FROM {} WHERE Date >= '2017-01-01' AND Date <= '2017-12-31'".format(t)
        )
    chunk_queries.append(" UNION ALL ".join(parts))

print('__RESULT__:')
print(json.dumps({'chunk_queries': chunk_queries, 'name_map': name_map, 'valid_count': len(valid)}))"""

env_args = {'var_call_R5Fm9qBHEnIjJw8IdgrwecTb': 'file_storage/call_R5Fm9qBHEnIjJw8IdgrwecTb.json', 'var_call_9KkYakqJdaS1o0ssxYdG90nb': 'file_storage/call_9KkYakqJdaS1o0ssxYdG90nb.json', 'var_call_pSlDq3Iya59P4L94vtKPK8Li': 'file_storage/call_pSlDq3Iya59P4L94vtKPK8Li.json', 'var_call_33fgjpjrXsOxarmSqxpiXVXf': 'file_storage/call_33fgjpjrXsOxarmSqxpiXVXf.json', 'var_call_0XfaOrnx4aN78Mfl2GOtwk4K': 'file_storage/call_0XfaOrnx4aN78Mfl2GOtwk4K.json'}

exec(code, env_args)
