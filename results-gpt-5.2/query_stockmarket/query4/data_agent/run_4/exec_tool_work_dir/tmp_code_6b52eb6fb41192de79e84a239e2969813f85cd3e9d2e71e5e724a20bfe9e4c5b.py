code = """import json, pandas as pd

sym_src = var_call_EJnjIyamO9JbQqPIIhhNpeTp
if isinstance(sym_src, str):
    with open(sym_src, 'r') as f:
        sym_src = json.load(f)
nyse_df = pd.DataFrame(sym_src)
nyse_syms = set(nyse_df['Symbol'].astype(str))

# trade tables
tbl_src = var_call_cGSbCvlnqeKUTDEQTSOWVQyw
if isinstance(tbl_src, str):
    with open(tbl_src, 'r') as f:
        tbl_src = json.load(f)
trade_tables = set(map(str, tbl_src))

syms = sorted(nyse_syms.intersection(trade_tables))

batch_size = 150
batches = [syms[i:i+batch_size] for i in range(0, len(syms), batch_size)]

union_queries = []
for batch in batches:
    parts = []
    for s in batch:
        t = s.replace('"','""')
        parts.append(
            "SELECT '"+s+"' AS Symbol, "
            "SUM(CASE WHEN Close > Open THEN 1 ELSE 0 END) AS up_days, "
            "SUM(CASE WHEN Close < Open THEN 1 ELSE 0 END) AS down_days "
            "FROM \""+t+"\" WHERE Date >= '2017-01-01' AND Date < '2018-01-01'"
        )
    union_queries.append(" UNION ALL ".join(parts))

print('__RESULT__:')
print(json.dumps({'symbols_count': len(syms), 'batches': len(batches), 'union_queries': union_queries}))"""

env_args = {'var_call_EJnjIyamO9JbQqPIIhhNpeTp': 'file_storage/call_EJnjIyamO9JbQqPIIhhNpeTp.json', 'var_call_cGSbCvlnqeKUTDEQTSOWVQyw': 'file_storage/call_cGSbCvlnqeKUTDEQTSOWVQyw.json'}

exec(code, env_args)
