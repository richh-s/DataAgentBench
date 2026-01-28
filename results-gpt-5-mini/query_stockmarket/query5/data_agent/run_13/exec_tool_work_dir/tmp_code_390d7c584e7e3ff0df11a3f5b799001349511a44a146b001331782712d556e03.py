code = """import json

def load_var(v):
    if isinstance(v, str):
        with open(v, 'r') as f:
            return json.load(f)
    return v

stockinfo = load_var(var_call_obofffwTil0kays857PB0osJ)
trade_tables = load_var(var_call_GWxju3cF897Xt8p4q6hk2Rmi)

symbols_info = [r['Symbol'] for r in stockinfo if r.get('Symbol')]
trade_set = set(trade_tables)

symbols = [s for s in symbols_info if s in trade_set]

# build mapping symbol -> company description
desc = {r['Symbol']: r.get('Company Description', '') for r in stockinfo if r.get('Symbol') in symbols}

out = {'num_symbols': len(symbols), 'symbols': symbols, 'descriptions': desc}
print("__RESULT__:")
print(json.dumps(out))"""

env_args = {'var_call_obofffwTil0kays857PB0osJ': 'file_storage/call_obofffwTil0kays857PB0osJ.json', 'var_call_GWxju3cF897Xt8p4q6hk2Rmi': 'file_storage/call_GWxju3cF897Xt8p4q6hk2Rmi.json'}

exec(code, env_args)
