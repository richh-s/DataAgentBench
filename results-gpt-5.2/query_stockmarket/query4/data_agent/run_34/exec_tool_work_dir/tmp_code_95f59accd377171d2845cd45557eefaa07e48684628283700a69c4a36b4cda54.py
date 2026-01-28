code = """import json
import pandas as pd

nyse_path = var_call_W9DknPtITkO5E8fVFyGGCP1i
with open(nyse_path, 'r') as f:
    nyse = json.load(f)
nyse_df = pd.DataFrame(nyse)

trade_path = var_call_IkdZGIDgN5BwsY28UnCmseZJ
with open(trade_path, 'r') as f:
    trade_tables = set(json.load(f))

symbols = sorted(set(nyse_df['Symbol']).intersection(trade_tables))

chunks = [symbols[i:i+300] for i in range(0, len(symbols), 300)]
queries = []
for chunk in chunks:
    parts = []
    for sym in chunk:
        q = (
            "SELECT '{0}' AS Symbol, "
            "SUM(CASE WHEN Close>Open THEN 1 ELSE 0 END) AS up_days, "
            "SUM(CASE WHEN Close<Open THEN 1 ELSE 0 END) AS down_days "
            "FROM \"{0}\" "
            "WHERE Date >= '2017-01-01' AND Date < '2018-01-01'"
        ).format(sym)
        parts.append(q)
    queries.append(" UNION ALL ".join(parts))

out = {
    'symbol_chunks': chunks,
    'duckdb_queries': queries,
    'nyse_map': nyse_df.set_index('Symbol')['company_name'].to_dict(),
    'n_symbols': len(symbols)
}

print('__RESULT__:')
print(json.dumps(out))"""

env_args = {'var_call_W9DknPtITkO5E8fVFyGGCP1i': 'file_storage/call_W9DknPtITkO5E8fVFyGGCP1i.json', 'var_call_IkdZGIDgN5BwsY28UnCmseZJ': 'file_storage/call_IkdZGIDgN5BwsY28UnCmseZJ.json'}

exec(code, env_args)
