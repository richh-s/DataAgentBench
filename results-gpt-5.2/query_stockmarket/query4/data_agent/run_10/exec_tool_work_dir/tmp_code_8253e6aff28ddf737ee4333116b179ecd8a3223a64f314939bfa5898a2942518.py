code = """import json, pandas as pd

nyse = var_call_ESxQfLXNtYi7iF1mTPzNi1Nm
if isinstance(nyse, str):
    with open(nyse, 'r') as f:
        nyse = json.load(f)
nyse_df = pd.DataFrame(nyse)
nyse_syms = set(nyse_df['Symbol'].astype(str))

tbls = var_call_GddjJRLCfA5HbkYvrQ9vNhxZ
if isinstance(tbls, str):
    with open(tbls, 'r') as f:
        tbls = json.load(f)
trade_syms = set(tbls)

syms = sorted(nyse_syms.intersection(trade_syms))
chunks = [syms[i:i+200] for i in range(0, len(syms), 200)]
queries = []
for ch in chunks:
    parts = []
    for s in ch:
        parts.append(
            "SELECT '{s}' AS Symbol, "
            "SUM(CASE WHEN Close>Open THEN 1 ELSE 0 END) AS up_days, "
            "SUM(CASE WHEN Close<Open THEN 1 ELSE 0 END) AS down_days "
            "FROM \"{s}\" "
            "WHERE Date>='2017-01-01' AND Date<='2017-12-31'".format(s=s)
        )
    queries.append(' UNION ALL '.join(parts))

print('__RESULT__:')
print(json.dumps({'symbol_count': len(syms), 'chunk_count': len(queries), 'first_query_len': len(queries[0]) if queries else 0}))"""

env_args = {'var_call_bipitrdzzeAsIqrjfiNtDaA9': ['stockinfo'], 'var_call_ESxQfLXNtYi7iF1mTPzNi1Nm': 'file_storage/call_ESxQfLXNtYi7iF1mTPzNi1Nm.json', 'var_call_GddjJRLCfA5HbkYvrQ9vNhxZ': 'file_storage/call_GddjJRLCfA5HbkYvrQ9vNhxZ.json'}

exec(code, env_args)
