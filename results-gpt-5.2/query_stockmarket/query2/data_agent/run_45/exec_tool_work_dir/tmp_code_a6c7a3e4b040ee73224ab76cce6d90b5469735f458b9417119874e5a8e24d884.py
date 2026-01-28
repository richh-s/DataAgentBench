code = """import json
import pandas as pd

etf_path = var_call_QithJaJqsmFZRHfXOHGy4hET
with open(etf_path, 'r') as f:
    etfs = json.load(f)

trade_path = var_call_czITr5fOMcSV0ks2Q3JHJxdB
with open(trade_path, 'r') as f:
    tables = set(json.load(f))

symbols = [r['symbol'] for r in etfs if r.get('symbol') in tables]
chunks = [symbols[i:i+200] for i in range(0, len(symbols), 200)]
result_frames = []

for chunk in chunks:
    parts = []
    for sym in chunk:
        parts.append("SELECT '{0}' AS symbol, MAX(\"Adj Close\") AS max_adj_close_2015 FROM \"{0}\" WHERE \"Date\" >= '2015-01-01' AND \"Date\" <= '2015-12-31'".format(sym))
    q = " UNION ALL ".join(parts)
    res = functions.query_db(db_name='stocktrade_database', query=q)
    result_frames.append(pd.DataFrame(res))

if result_frames:
    df = pd.concat(result_frames, ignore_index=True)
else:
    df = pd.DataFrame(columns=['symbol','max_adj_close_2015'])

if not df.empty:
    df['max_adj_close_2015'] = pd.to_numeric(df['max_adj_close_2015'], errors='coerce')

hits = df[df['max_adj_close_2015'] > 200].copy()
info_df = pd.DataFrame(etfs)
hits = hits.merge(info_df, on='symbol', how='left')
hits = hits.sort_values('symbol')

answer = {
    'total_etfs': int(hits.shape[0]),
    'etfs': hits[['symbol','company_description','max_adj_close_2015']].to_dict(orient='records')
}

print('__RESULT__:')
print(json.dumps(answer))"""

env_args = {'var_call_QithJaJqsmFZRHfXOHGy4hET': 'file_storage/call_QithJaJqsmFZRHfXOHGy4hET.json', 'var_call_czITr5fOMcSV0ks2Q3JHJxdB': 'file_storage/call_czITr5fOMcSV0ks2Q3JHJxdB.json'}

exec(code, env_args)
