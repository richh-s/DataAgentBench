code = """import json
import os
# load the two previous tool results
p1 = var_call_ybrJiY7qN1q4Ht1Y8kc0VNaz
p2 = var_call_oD1ck6ZNbrCkc79DewGoacXv

# helper to load either direct list or filepath
def load_var(v):
    if isinstance(v, str) and os.path.exists(v):
        with open(v, 'r', encoding='utf-8') as f:
            return json.load(f)
    else:
        return v

stockinfo = load_var(p1)
trade_tables = load_var(p2)

# build mapping of symbol -> company description for NYSE non-ETF
mapping = {}
for rec in stockinfo:
    sym = rec.get('Symbol')
    etf = rec.get('ETF')
    exch = rec.get('Listing Exchange')
    if exch == 'N' and (etf is None or etf != 'Y') and sym:
        mapping[sym] = rec.get('Company Description')

# intersect with available trade tables
available = set(trade_tables)
symbols = sorted([s for s in mapping.keys() if s in available])

# build SQL union for 2017 counts
parts = []
for s in symbols:
    part = f"SELECT '{s}' AS symbol, SUM(CASE WHEN \"Close\">\"Open\" THEN 1 ELSE 0 END) AS up_count, SUM(CASE WHEN \"Close\"<\"Open\" THEN 1 ELSE 0 END) AS down_count FROM \"{s}\" WHERE \"Date\" >= '2017-01-01' AND \"Date\" <= '2017-12-31'"
    parts.append(part)
sql = " UNION ALL ".join(parts) + ";"

out = {'sql': sql, 'mapping': mapping, 'symbols_count': len(symbols)}
print("__RESULT__:")
print(json.dumps(out))"""

env_args = {'var_call_ybrJiY7qN1q4Ht1Y8kc0VNaz': 'file_storage/call_ybrJiY7qN1q4Ht1Y8kc0VNaz.json', 'var_call_oD1ck6ZNbrCkc79DewGoacXv': 'file_storage/call_oD1ck6ZNbrCkc79DewGoacXv.json'}

exec(code, env_args)
