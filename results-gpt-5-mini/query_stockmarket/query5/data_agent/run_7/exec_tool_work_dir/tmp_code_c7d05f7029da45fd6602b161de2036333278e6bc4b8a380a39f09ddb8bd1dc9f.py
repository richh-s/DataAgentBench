code = """import json
# load stockinfo query_db result
val1 = var_call_g29DMfGZ1F5iPmMFwe0rGJmZ
if isinstance(val1, str) and val1.endswith('.json'):
    with open(val1, 'r') as f:
        stockinfo = json.load(f)
else:
    stockinfo = val1
# load stocktrade list_db result
val2 = var_call_NxAzjzgAprbtYGql6TUtUGiP
if isinstance(val2, str) and val2.endswith('.json'):
    with open(val2, 'r') as f:
        trade_tables = json.load(f)
else:
    trade_tables = val2

# build set of symbols in market category S
symbols_s = [rec['Symbol'] for rec in stockinfo if rec.get('Symbol')]
trade_set = set(trade_tables)
common = [s for s in symbols_s if s in trade_set]

# construct SQL union query
parts = []
for s in common:
    # Quote table name by doubling any double quotes
    t = s.replace('"', '""')
    part = f"SELECT '{s}' AS Symbol, COUNT(*) AS cnt FROM \"{t}\" WHERE Date >= '2019-01-01' AND Date <= '2019-12-31' AND High > 1.2 * Low"
    parts.append(part)

if parts:
    sql = "\nUNION ALL\n".join(parts) + "\nORDER BY cnt DESC;"
else:
    sql = ''

print("__RESULT__:")
print(json.dumps(sql))"""

env_args = {'var_call_g29DMfGZ1F5iPmMFwe0rGJmZ': 'file_storage/call_g29DMfGZ1F5iPmMFwe0rGJmZ.json', 'var_call_NxAzjzgAprbtYGql6TUtUGiP': 'file_storage/call_NxAzjzgAprbtYGql6TUtUGiP.json'}

exec(code, env_args)
