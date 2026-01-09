code = """import json
from pathlib import Path

p = Path(var_call_G47btGjm15K0WsPRavoAXJ2R)
with p.open() as f:
    d = json.load(f)
syms = d['arca_etf_symbols']

parts = []
for s in syms:
    tbl = s.replace('"','""')
    part = f'SELECT \'{s}\' AS symbol, MAX("Adj Close") AS max_adj_close_2015 FROM main."{tbl}" WHERE "Date" >= \'2015-01-01\' AND "Date" < \'2016-01-01\''
    parts.append(part)
query = "\nUNION ALL\n".join(parts)

print('__RESULT__:')
print(json.dumps({'query': query, 'n_parts': len(parts)}))"""

env_args = {'var_call_4zvnEpy4TcgDPxNN3yfwUgQc': 'file_storage/call_4zvnEpy4TcgDPxNN3yfwUgQc.json', 'var_call_PK2VWvd4xur6MI6L2CYBTa7J': 'file_storage/call_PK2VWvd4xur6MI6L2CYBTa7J.json', 'var_call_G47btGjm15K0WsPRavoAXJ2R': 'file_storage/call_G47btGjm15K0WsPRavoAXJ2R.json'}

exec(code, env_args)
