code = """import json, pandas as pd

nyse_path = var_call_YUklvkNSfsVQgYR1c02Ynr1O
with open(nyse_path, 'r') as f:
    nyse = json.load(f)
nyse_df = pd.DataFrame(nyse)

tbl_path = var_call_JtD0SKI6HkrXBgEo4BnEvRkc
with open(tbl_path, 'r') as f:
    tables = json.load(f)
tables_set = set(tables)

symbols = sorted(set(nyse_df['Symbol']).intersection(tables_set))

parts = []
for sym in symbols:
    q = "SELECT '{sym}' AS Symbol, SUM(CASE WHEN Close > Open THEN 1 ELSE 0 END) AS up_days, SUM(CASE WHEN Close < Open THEN 1 ELSE 0 END) AS down_days FROM \"{sym}\" WHERE Date >= '2017-01-01' AND Date < '2018-01-01'".format(sym=sym)
    parts.append(q)

chunk_size = 200
queries = [" UNION ALL ".join(parts[i:i+chunk_size]) for i in range(0, len(parts), chunk_size)]

print('__RESULT__:')
print(json.dumps({'symbols_count': int(len(symbols)), 'queries': queries[:3], 'total_chunks': len(queries)}))"""

env_args = {'var_call_YUklvkNSfsVQgYR1c02Ynr1O': 'file_storage/call_YUklvkNSfsVQgYR1c02Ynr1O.json', 'var_call_JtD0SKI6HkrXBgEo4BnEvRkc': 'file_storage/call_JtD0SKI6HkrXBgEo4BnEvRkc.json'}

exec(code, env_args)
