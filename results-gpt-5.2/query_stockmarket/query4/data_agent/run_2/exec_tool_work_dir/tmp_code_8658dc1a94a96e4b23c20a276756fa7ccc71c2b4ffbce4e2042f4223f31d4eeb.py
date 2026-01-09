code = """import json
import pandas as pd

def load_var(v):
    if isinstance(v, str) and v.endswith('.json'):
        with open(v, 'r') as f:
            return json.load(f)
    return v

stocks = load_var(var_call_HA7aZkk6ej0IlGua67UFhxLm)
trade_tables = set(load_var(var_call_KS9toGYpPJHCYGzuWhO10tQ3))

symbols = [r['Symbol'] for r in stocks if r['Symbol'] in trade_tables]
symbols = symbols[:500]

parts = []
for s in symbols:
    parts.append("SELECT '{sym}' AS Symbol, SUM(CASE WHEN Close>Open THEN 1 ELSE 0 END) AS up_days, SUM(CASE WHEN Close<Open THEN 1 ELSE 0 END) AS down_days FROM \"{sym}\" WHERE Date >= '2017-01-01' AND Date < '2018-01-01'".format(sym=s.replace("'","''")))

sql = " UNION ALL ".join(parts)

print('__RESULT__:')
print(json.dumps({'sql': sql, 'n_symbols': len(symbols)}))"""

env_args = {'var_call_HA7aZkk6ej0IlGua67UFhxLm': 'file_storage/call_HA7aZkk6ej0IlGua67UFhxLm.json', 'var_call_KS9toGYpPJHCYGzuWhO10tQ3': 'file_storage/call_KS9toGYpPJHCYGzuWhO10tQ3.json'}

exec(code, env_args)
