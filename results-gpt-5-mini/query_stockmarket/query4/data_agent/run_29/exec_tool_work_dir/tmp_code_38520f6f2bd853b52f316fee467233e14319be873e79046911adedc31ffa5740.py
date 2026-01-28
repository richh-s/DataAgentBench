code = """import json
import os
p1 = var_call_ybrJiY7qN1q4Ht1Y8kc0VNaz
p2 = var_call_oD1ck6ZNbrCkc79DewGoacXv

def load_var(v):
    if isinstance(v, str) and os.path.exists(v):
        with open(v, 'r', encoding='utf-8') as f:
            return json.load(f)
    else:
        return v

stockinfo = load_var(p1)
trade_tables = load_var(p2)

mapping = {}
for rec in stockinfo:
    sym = rec.get('Symbol')
    etf = rec.get('ETF')
    exch = rec.get('Listing Exchange')
    if exch == 'N' and (etf is None or etf != 'Y') and sym:
        mapping[sym] = rec.get('Company Description')

available = set(trade_tables)
symbols = sorted([s for s in mapping.keys() if s in available])

out = {'symbols': symbols, 'symbols_count': len(symbols)}
print("__RESULT__:")
print(json.dumps(out))"""

env_args = {'var_call_ybrJiY7qN1q4Ht1Y8kc0VNaz': 'file_storage/call_ybrJiY7qN1q4Ht1Y8kc0VNaz.json', 'var_call_oD1ck6ZNbrCkc79DewGoacXv': 'file_storage/call_oD1ck6ZNbrCkc79DewGoacXv.json'}

exec(code, env_args)
