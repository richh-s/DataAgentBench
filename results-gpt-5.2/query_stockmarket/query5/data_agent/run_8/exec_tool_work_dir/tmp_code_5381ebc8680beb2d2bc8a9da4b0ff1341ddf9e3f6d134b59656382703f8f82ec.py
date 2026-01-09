code = """import json, pandas as pd

# load tickers list from stockinfo result file
path = var_call_Kpm5Gsm2fwj4Ln8qQyOEmDvn
with open(path, 'r') as f:
    info = json.load(f)
info_df = pd.DataFrame(info)
info_df['Symbol'] = info_df['Symbol'].astype(str)

# load available trade tables
path2 = var_call_Xwr045cIACRdwbk2QikswdHt
with open(path2, 'r') as f:
    tables = json.load(f)
tables_set = set(tables)

# keep only symbols that have a trade table
symbols = [s for s in info_df['Symbol'].tolist() if s in tables_set]

print('__RESULT__:')
print(json.dumps({'symbols': symbols, 'n': len(symbols)}))"""

env_args = {'var_call_Kpm5Gsm2fwj4Ln8qQyOEmDvn': 'file_storage/call_Kpm5Gsm2fwj4Ln8qQyOEmDvn.json', 'var_call_Xwr045cIACRdwbk2QikswdHt': 'file_storage/call_Xwr045cIACRdwbk2QikswdHt.json'}

exec(code, env_args)
