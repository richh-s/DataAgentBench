code = """import json, duckdb, pandas as pd
from pathlib import Path

symbols_file = var_call_UvVeUGBkvhTsBG5rF8CU1mEZ
with open(symbols_file, 'r') as f:
    all_symbols = json.load(f)

info_file = var_call_85VW3ZBAdume3gcpttrk5oaU
with open(info_file, 'r') as f:
    nyse_info = json.load(f)

nyse_symbols = {row['Symbol']: row['Company Description'] for row in nyse_info if row['Symbol'] in all_symbols}

con = duckdb.connect(database='stocktrade_database', read_only=True)

results = []
for symbol, name in nyse_symbols.items():
    try:
        df = con.execute(f"SELECT Date, Open, Close FROM '{symbol}' WHERE Date >= '2017-01-01' AND Date <= '2017-12-31'").df()
    except Exception:
        continue
    if df.empty:
        continue
    up_days = (df['Close'] > df['Open']).sum()
    down_days = (df['Close'] < df['Open']).sum()
    if up_days > down_days:
        results.append({'Symbol': symbol, 'Name': name, 'UpDays': int(up_days), 'DownDays': int(down_days)})

res_df = pd.DataFrame(results)
res_df['Diff'] = res_df['UpDays'] - res_df['DownDays']
res_df = res_df.sort_values(['Diff','UpDays'], ascending=[False, False]).head(5)

answer_names = res_df['Name'].tolist()

out = json.dumps(answer_names)
print('__RESULT__:')
print(out)"""

env_args = {'var_call_UvVeUGBkvhTsBG5rF8CU1mEZ': 'file_storage/call_UvVeUGBkvhTsBG5rF8CU1mEZ.json', 'var_call_85VW3ZBAdume3gcpttrk5oaU': 'file_storage/call_85VW3ZBAdume3gcpttrk5oaU.json'}

exec(code, env_args)
