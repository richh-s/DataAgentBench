code = """import json, pandas as pd

def load_records(v):
    if isinstance(v, str) and v.endswith('.json'):
        with open(v, 'r') as f:
            return json.load(f)
    return v

nyse = pd.DataFrame(load_records(var_call_yxBJaU3hRrVIBDsSsWUQyRxF))
trade_tables = set(load_records(var_call_55L71prOlGZnGjPd875JYVlS))
nyse = nyse[nyse['symbol'].isin(trade_tables)].copy()
syms = sorted(nyse['symbol'].unique().tolist())
# chunk symbols for later parallel querying strategy
chunks = [syms[i:i+40] for i in range(0, len(syms), 40)]
print('__RESULT__:')
print(json.dumps({'n_symbols': len(syms), 'n_chunks': len(chunks), 'chunk_sizes': [len(c) for c in chunks]}))"""

env_args = {'var_call_55L71prOlGZnGjPd875JYVlS': 'file_storage/call_55L71prOlGZnGjPd875JYVlS.json', 'var_call_yxBJaU3hRrVIBDsSsWUQyRxF': 'file_storage/call_yxBJaU3hRrVIBDsSsWUQyRxF.json', 'var_call_M01LlNsqnyJUUQ9eBPPgmDJV': {'n_symbols': 234, 'sample_symbols': ['AEFC', 'AIN', 'AIV', 'AIZP', 'AJRD', 'AL', 'AMN', 'AMP', 'AMT', 'ARD', 'ARGD', 'ARLO', 'ASG', 'AVA', 'BANC', 'BBU', 'BBVA', 'BDXA', 'BKH', 'BKT']}}

exec(code, env_args)
