code = """import json, pandas as pd

# load stockinfo results
p = var_call_4aGwTzh70bt8xarEObPHR1xp
with open(p, 'r') as f:
    info = json.load(f)
info_df = pd.DataFrame(info)

# load available trade tables
p2 = var_call_ptTAFVhG5hNvbNHxEpsBJBbz
with open(p2, 'r') as f:
    tables = json.load(f)
tables_set = set(tables)

# only tickers that have a corresponding price table
symbols = [s for s in info_df['Symbol'].tolist() if s in tables_set]

# build a UNION ALL query across tickers to count qualifying days in 2019
# condition: (High-Low) > 0.2*Low  <=> High > 1.2*Low ; ensure Low>0
parts = []
for sym in symbols:
    # duckdb needs double quotes for table/column names with spaces; here columns have spaces? 'Adj Close' only, we don't use.
    parts.append(f"SELECT '{sym}' AS Symbol, COUNT(*) AS days FROM \"{sym}\" WHERE Date >= '2019-01-01' AND Date <= '2019-12-31' AND Low > 0 AND High > 1.2*Low")

union_query = "\nUNION ALL\n".join(parts)
# wrap to get top 5
final_query = f"SELECT Symbol, days FROM ({union_query}) t ORDER BY days DESC, Symbol ASC LIMIT 5;"

print('__RESULT__:')
print(json.dumps({'symbols': symbols, 'query': final_query}))"""

env_args = {'var_call_4aGwTzh70bt8xarEObPHR1xp': 'file_storage/call_4aGwTzh70bt8xarEObPHR1xp.json', 'var_call_ptTAFVhG5hNvbNHxEpsBJBbz': 'file_storage/call_ptTAFVhG5hNvbNHxEpsBJBbz.json'}

exec(code, env_args)
