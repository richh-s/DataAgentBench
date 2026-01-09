code = """import json, pandas as pd

def load_json_records(maybe_path_or_list):
    if isinstance(maybe_path_or_list, str):
        with open(maybe_path_or_list, 'r', encoding='utf-8') as f:
            return json.load(f)
    return maybe_path_or_list

etf_arca = pd.DataFrame(load_json_records(var_call_L3QZsJ0Ybio1cEP6tPEvl8TU))
trade_tables = set(load_json_records(var_call_ug2sGvB80yUuHL6Kd0a243vi))

symbols = sorted([s for s in etf_arca['symbol'].dropna().astype(str).unique().tolist() if s in trade_tables])

out = json.dumps({"n_symbols": len(symbols), "sample_symbols": symbols[:20]})
print('__RESULT__:')
print(out)"""

env_args = {'var_call_L3QZsJ0Ybio1cEP6tPEvl8TU': 'file_storage/call_L3QZsJ0Ybio1cEP6tPEvl8TU.json', 'var_call_ug2sGvB80yUuHL6Kd0a243vi': 'file_storage/call_ug2sGvB80yUuHL6Kd0a243vi.json'}

exec(code, env_args)
