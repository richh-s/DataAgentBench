code = """import json
# Load tool results from storage keys
with open(var_call_PPqOo48KnLzN7VZUluh7p1Pf, 'r') as f:
    stockinfo = json.load(f)
with open(var_call_MxbtFlCKNvwOOD1Kk6AOFzDM, 'r') as f:
    trade_tables = json.load(f)
# Extract symbols from stockinfo (Market Category S results already fetched)
symbols_s = [r['Symbol'] for r in stockinfo]
# trade_tables is list of table names
trade_set = set(trade_tables)
intersection = sorted([s for s in symbols_s if s in trade_set])
output = {'num_stockinfo_S': len(symbols_s), 'num_trade_tables': len(trade_tables), 'num_intersection': len(intersection), 'intersection_sample': intersection[:50], 'intersection_all_count': len(intersection)}
import json
print("__RESULT__:")
print(json.dumps(output))"""

env_args = {'var_call_PPqOo48KnLzN7VZUluh7p1Pf': 'file_storage/call_PPqOo48KnLzN7VZUluh7p1Pf.json', 'var_call_MxbtFlCKNvwOOD1Kk6AOFzDM': 'file_storage/call_MxbtFlCKNvwOOD1Kk6AOFzDM.json'}

exec(code, env_args)
