code = """import json
import pandas as pd
# load list of all trade tables
with open(var_call_81EOLJGEHfF155klz6RD5tvw, 'r') as f:
    all_tables = json.load(f)
# load nasdaq capital market symbols
ncm_records = var_call_SuLYyzDLn95dtXzf8RJtyegT
ncm_df = pd.DataFrame(ncm_records)
syms = set(ncm_df['Symbol'])
# intersect with tables actually having price data
tickers = sorted(list(syms.intersection(set(all_tables))))
result = json.dumps(tickers)
print("__RESULT__:")
print(result)"""

env_args = {'var_call_81EOLJGEHfF155klz6RD5tvw': 'file_storage/call_81EOLJGEHfF155klz6RD5tvw.json', 'var_call_SuLYyzDLn95dtXzf8RJtyegT': 'file_storage/call_SuLYyzDLn95dtXzf8RJtyegT.json'}

exec(code, env_args)
