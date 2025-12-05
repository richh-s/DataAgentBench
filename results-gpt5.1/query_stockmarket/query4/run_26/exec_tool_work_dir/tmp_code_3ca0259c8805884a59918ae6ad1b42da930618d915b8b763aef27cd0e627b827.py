code = """import json, duckdb, pandas as pd

# load symbol -> name mapping
with open(var_call_DEjav8jqQx1PKztE1bMdBHQq) as f:
    nyse_meta = json.load(f)

symbol_to_name = {r['Symbol']: r['name'] for r in nyse_meta}

# connect to duckdb file
con = duckdb.connect(database='stocktrade_database', read_only=True)

results = []
for symbol in symbol_to_name.keys():
    try:
        df = con.execute(f"""SELECT Date, Open, Close FROM "{symbol}" WHERE Date >= '2017-01-01' AND Date <= '2017-12-31'""").fetch_df()
    except Exception:
        continue
    if df.empty:
        continue
    up_days = (df['Close'] > df['Open']).sum()
    down_days = (df['Close'] < df['Open']).sum()
    if up_days > down_days:
        results.append({'Symbol': symbol, 'up_days': int(up_days), 'down_days': int(down_days)})

# sort by (up_days - down_days) desc, then up_days desc, then symbol
results_sorted = sorted(results, key=lambda x: (x['up_days']-x['down_days'], x['up_days'], x['Symbol']), reverse=True)

top5 = results_sorted[:5]

# attach names
for r in top5:
    r['name'] = symbol_to_name.get(r['Symbol'], None)

out = [r['name'] for r in top5]

res_json = json.dumps(out)
print("__RESULT__:")
print(res_json)"""

env_args = {'var_call_43EfGfzYPRdd2AGYdPp6tHwR': 'file_storage/call_43EfGfzYPRdd2AGYdPp6tHwR.json', 'var_call_DEjav8jqQx1PKztE1bMdBHQq': 'file_storage/call_DEjav8jqQx1PKztE1bMdBHQq.json'}

exec(code, env_args)
