code = """import json, pandas as pd
from pathlib import Path

# load stock list and NYSE non-ETF list
with open(var_call_HKeVuwWBiF5EBM36pXyqZcqi, 'r') as f:
    all_symbols = json.load(f)
with open(var_call_NuB5KLQc8zdr7taZCP7chJVc, 'r') as f:
    nyse_meta = json.load(f)

nyse_df = pd.DataFrame(nyse_meta)
nyse_df = nyse_df.rename(columns={'Symbol':'symbol', 'Company Description':'company'})

# filter symbols to NYSE non-ETF that exist in trade db
trade_set = set(all_symbols)
nyse_df = nyse_df[nyse_df['symbol'].isin(trade_set)].reset_index(drop=True)

# sample up to, say, 400 symbols to keep runtime reasonable
symbols = nyse_df['symbol'].tolist()

result = json.dumps({'symbols': symbols[:400]})
print("__RESULT__:")
print(result)"""

env_args = {'var_call_HKeVuwWBiF5EBM36pXyqZcqi': 'file_storage/call_HKeVuwWBiF5EBM36pXyqZcqi.json', 'var_call_NuB5KLQc8zdr7taZCP7chJVc': 'file_storage/call_NuB5KLQc8zdr7taZCP7chJVc.json'}

exec(code, env_args)
