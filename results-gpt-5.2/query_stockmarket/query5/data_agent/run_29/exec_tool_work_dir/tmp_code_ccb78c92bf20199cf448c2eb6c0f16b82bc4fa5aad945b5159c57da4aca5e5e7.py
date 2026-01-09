code = """import json, pandas as pd

# load stockinfo result
path = var_call_t6qYTgEhLW52YPNGHQeKk6oL
with open(path, 'r') as f:
    info = json.load(f)
info_df = pd.DataFrame(info)

# load list of trade tables
path2 = var_call_1gtyyeTNjea4vCWTo20aow0w
with open(path2, 'r') as f:
    tables = set(json.load(f))

# keep only tickers that exist as tables
info_df = info_df[info_df['Symbol'].isin(tables)].copy()

# sample limit for output to use in next step (tickers list)
tickers = info_df['Symbol'].tolist()

print('__RESULT__:')
print(json.dumps({'n_tickers': len(tickers), 'tickers': tickers}))"""

env_args = {'var_call_t6qYTgEhLW52YPNGHQeKk6oL': 'file_storage/call_t6qYTgEhLW52YPNGHQeKk6oL.json', 'var_call_1gtyyeTNjea4vCWTo20aow0w': 'file_storage/call_1gtyyeTNjea4vCWTo20aow0w.json'}

exec(code, env_args)
