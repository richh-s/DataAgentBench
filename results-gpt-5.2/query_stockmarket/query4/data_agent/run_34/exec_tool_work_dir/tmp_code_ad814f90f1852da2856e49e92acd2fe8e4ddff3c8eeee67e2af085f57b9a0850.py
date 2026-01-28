code = """import json
import pandas as pd

nyse_path = var_call_W9DknPtITkO5E8fVFyGGCP1i
with open(nyse_path, 'r') as f:
    nyse = json.load(f)
nyse_df = pd.DataFrame(nyse)

trade_path = var_call_IkdZGIDgN5BwsY28UnCmseZJ
with open(trade_path, 'r') as f:
    trade_tables = set(json.load(f))

symbols = sorted(set(nyse_df['Symbol']).intersection(trade_tables))

out = {'n_symbols': len(symbols), 'first10': symbols[:10]}
print('__RESULT__:')
print(json.dumps(out))"""

env_args = {'var_call_W9DknPtITkO5E8fVFyGGCP1i': 'file_storage/call_W9DknPtITkO5E8fVFyGGCP1i.json', 'var_call_IkdZGIDgN5BwsY28UnCmseZJ': 'file_storage/call_IkdZGIDgN5BwsY28UnCmseZJ.json', 'var_call_UsFARjzhRdUpjRMozyesZDyT': {'a': 1}}

exec(code, env_args)
