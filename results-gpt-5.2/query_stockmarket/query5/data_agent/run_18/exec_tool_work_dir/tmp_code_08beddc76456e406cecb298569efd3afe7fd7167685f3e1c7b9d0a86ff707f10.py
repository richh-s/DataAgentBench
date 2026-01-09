code = """import json, pandas as pd

# Load symbols/company names
path = var_call_COIkrGN9cWpnuc7Vnq57yeIM
with open(path, 'r', encoding='utf-8') as f:
    info = json.load(f)

df_info = pd.DataFrame(info)
symbols = df_info['Symbol'].dropna().unique().tolist()

# Prepare UNION ALL query over only tables that exist in stocktrade_database
# We need list of tables first
print('__RESULT__:')
print(json.dumps({'n_symbols': len(symbols)}))"""

env_args = {'var_call_COIkrGN9cWpnuc7Vnq57yeIM': 'file_storage/call_COIkrGN9cWpnuc7Vnq57yeIM.json'}

exec(code, env_args)
