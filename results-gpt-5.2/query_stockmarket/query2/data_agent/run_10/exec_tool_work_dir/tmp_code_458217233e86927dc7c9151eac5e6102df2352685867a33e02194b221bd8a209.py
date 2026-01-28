code = """import json

# load tickers list
x = var_call_PTPvYsotAclTQdV8gDHEdGkj
if isinstance(x, str):
    with open(x, 'r', encoding='utf-8') as f:
        tickers = json.load(f)
else:
    tickers = x

# build a DuckDB SQL statement that unions per-ticker maxima in 2015
# Use double quotes for table names because some could be reserved; tickers here are safe alnum.
selects = []
for t in tickers:
    selects.append(f"SELECT '{t}' AS symbol, MAX(\"Adj Close\") AS max_adj_close_2015 FROM \"{t}\" WHERE \"Date\" >= '2015-01-01' AND \"Date\" < '2016-01-01'")

query = "SELECT symbol, max_adj_close_2015 FROM (" + " UNION ALL ".join(selects) + ") WHERE max_adj_close_2015 > 200 ORDER BY symbol;"
print('__RESULT__:')
print(json.dumps({'query': query, 'n_tickers': len(tickers)}))"""

env_args = {'var_call_6ctMLF9BUUuRXIeIs1vcu4lt': 'file_storage/call_6ctMLF9BUUuRXIeIs1vcu4lt.json', 'var_call_jWYwT4eMqUmqOtH5L0tt2agF': 'file_storage/call_jWYwT4eMqUmqOtH5L0tt2agF.json', 'var_call_PTPvYsotAclTQdV8gDHEdGkj': 'file_storage/call_PTPvYsotAclTQdV8gDHEdGkj.json'}

exec(code, env_args)
