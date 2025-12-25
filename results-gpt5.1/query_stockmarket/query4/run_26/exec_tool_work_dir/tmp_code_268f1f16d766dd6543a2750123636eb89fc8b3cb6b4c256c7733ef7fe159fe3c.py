code = """import json, duckdb, pandas as pd

with open(var_call_DEjav8jqQx1PKztE1bMdBHQq) as f:
    nyse_meta = json.load(f)

symbol_to_name = {r['Symbol']: r['name'] for r in nyse_meta}

con = duckdb.connect(database='stocktrade_database', read_only=True)

results = []
for symbol in symbol_to_name.keys():
    try:
        query = 'SELECT Date, Open, Close FROM "' + symbol + '" WHERE Date >= "2017-01-01" AND Date <= "2017-12-31"'
        df = con.execute(query).fetch_df()
    except Exception:
        continue
    if df.empty:
        continue
    up_days = int((df['Close'] > df['Open']).sum())
    down_days = int((df['Close'] < df['Open']).sum())
    if up_days > down_days:
        results.append({'Symbol': symbol, 'up_days': up_days, 'down_days': down_days})

results_sorted = sorted(results, key=lambda x: (x['up_days']-x['down_days'], x['up_days'], x['Symbol']), reverse=True)

top5 = results_sorted[:5]

names = [symbol_to_name.get(r['Symbol']) for r in top5]

out = json.dumps(names)
print("__RESULT__:")
print(out)"""

env_args = {'var_call_43EfGfzYPRdd2AGYdPp6tHwR': 'file_storage/call_43EfGfzYPRdd2AGYdPp6tHwR.json', 'var_call_DEjav8jqQx1PKztE1bMdBHQq': 'file_storage/call_DEjav8jqQx1PKztE1bMdBHQq.json'}

exec(code, env_args)
