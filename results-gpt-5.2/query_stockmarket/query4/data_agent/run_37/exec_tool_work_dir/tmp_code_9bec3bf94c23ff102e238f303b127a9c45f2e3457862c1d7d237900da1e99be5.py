code = """import json, pandas as pd

# load nyse non-etf symbols + names
sym_path = var_call_tw1ITfOp97oQbfqVeKzARqzi
with open(sym_path,'r') as f:
    symrecs = json.load(f)
df_sym = pd.DataFrame(symrecs)

# load available trade tables
trade_path = var_call_5rrCVPu8sti9lypppss1B3Br
with open(trade_path,'r') as f:
    tabrecs = json.load(f)
df_tabs = pd.DataFrame(tabrecs)

symbols = sorted(set(df_sym['Symbol']).intersection(set(df_tabs['name'])))

# create a single union query to count up/down days in 2017 for each symbol
parts = []
for s in symbols:
    # quote identifier with double quotes for DuckDB
    parts.append(
        f"SELECT '{s}' AS Symbol, "
        f"SUM(CASE WHEN Close > Open THEN 1 ELSE 0 END) AS up_days, "
        f"SUM(CASE WHEN Close < Open THEN 1 ELSE 0 END) AS down_days "
        f"FROM \"{s}\" WHERE Date >= '2017-01-01' AND Date < '2018-01-01'"
    )
union_sql = "\nUNION ALL\n".join(parts)
final_sql = f"WITH counts AS ({union_sql}) SELECT * FROM counts;"

print('__RESULT__:')
print(json.dumps({'symbols_n': len(symbols), 'sql': final_sql[:9000]}))"""

env_args = {'var_call_MIfIdCZXA2HzZYAVj8h4hV89': ['stockinfo'], 'var_call_tw1ITfOp97oQbfqVeKzARqzi': 'file_storage/call_tw1ITfOp97oQbfqVeKzARqzi.json', 'var_call_5rrCVPu8sti9lypppss1B3Br': 'file_storage/call_5rrCVPu8sti9lypppss1B3Br.json'}

exec(code, env_args)
