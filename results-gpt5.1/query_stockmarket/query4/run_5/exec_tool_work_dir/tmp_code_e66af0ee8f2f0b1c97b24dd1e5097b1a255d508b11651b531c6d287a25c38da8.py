code = """import json, pandas as pd
from datetime import datetime

symbols_info = pd.DataFrame(var_call_EjUTnrPq1QHzlKOfrUBo2KWt)

trade_tables = json.load(open(var_call_5maOYjT5bSYo820Cen1eByBj))

nyse_syms = set(symbols_info['Symbol'])
common_syms = sorted(list(nyse_syms.intersection(trade_tables)))

results = []
start = datetime(2017,1,1)
end = datetime(2017,12,31)

for sym in common_syms:
    q = f'SELECT Date, Open, Close FROM "{sym}" WHERE Date >= "2017-01-01" AND Date <= "2017-12-31";'
    res = query_db({"db_name": "stocktrade_database", "query": q})
    df = pd.DataFrame(res)
    if df.empty:
        continue
    up = (df['Close'] > df['Open']).sum()
    down = (df['Close'] < df['Open']).sum()
    if up > down:
        results.append({"Symbol": sym, "UpDays": int(up), "DownDays": int(down)})

res_df = pd.DataFrame(results)
if not res_df.empty:
    res_df = res_df.sort_values('UpDays', ascending=False).head(5)
    merged = res_df.merge(symbols_info[['Symbol','Company Description']], on='Symbol', how='left')
    out = merged[['Symbol','Company Description','UpDays','DownDays']]
    result_json = out.to_json(orient='records')
else:
    result_json = json.dumps([])

print("__RESULT__:")
print(result_json)"""

env_args = {'var_call_5maOYjT5bSYo820Cen1eByBj': 'file_storage/call_5maOYjT5bSYo820Cen1eByBj.json', 'var_call_EjUTnrPq1QHzlKOfrUBo2KWt': 'file_storage/call_EjUTnrPq1QHzlKOfrUBo2KWt.json'}

exec(code, env_args)
