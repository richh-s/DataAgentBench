code = """import json, pandas as pd

def load_json_records(maybe_path_or_list):
    if isinstance(maybe_path_or_list, str):
        with open(maybe_path_or_list, 'r', encoding='utf-8') as f:
            return json.load(f)
    return maybe_path_or_list

etf_arca = pd.DataFrame(load_json_records(var_call_L3QZsJ0Ybio1cEP6tPEvl8TU))
trade_tables = set(load_json_records(var_call_ug2sGvB80yUuHL6Kd0a243vi))

symbols = sorted([s for s in etf_arca['symbol'].dropna().astype(str).unique().tolist() if s in trade_tables])

parts = []
for sym in symbols:
    q = f"SELECT '{sym}' AS symbol, MAX(\"Adj Close\") AS max_adj_close_2015 FROM \"{sym}\" WHERE \"Date\" >= '2015-01-01' AND \"Date\" < '2016-01-01'"
    parts.append(q)

sep = "\nUNION ALL\n"
union_query = sep.join(parts) if parts else "SELECT NULL AS symbol, NULL AS max_adj_close_2015 WHERE 1=0"

out = json.dumps({"n_symbols": len(symbols), "union_query_prefix": union_query[:5000]})
print('__RESULT__:')
print(out)"""

env_args = {'var_call_L3QZsJ0Ybio1cEP6tPEvl8TU': 'file_storage/call_L3QZsJ0Ybio1cEP6tPEvl8TU.json', 'var_call_ug2sGvB80yUuHL6Kd0a243vi': 'file_storage/call_ug2sGvB80yUuHL6Kd0a243vi.json'}

exec(code, env_args)
