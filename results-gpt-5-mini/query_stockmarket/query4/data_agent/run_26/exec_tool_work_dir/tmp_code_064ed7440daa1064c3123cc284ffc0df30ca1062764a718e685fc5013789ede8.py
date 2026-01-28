code = """import json
import pandas as pd
# Load the stored JSON files from the previous query_db and list_db calls
path_stockinfo = var_call_rXv6uZ0DDNksTWfPiVrfTqtu
path_tables = var_call_5jcJoDfvBouMTBJgTuzgin4N
with open(path_stockinfo, 'r') as f:
    stockinfo_records = json.load(f)
with open(path_tables, 'r') as f:
    tables = json.load(f)

df = pd.DataFrame(stockinfo_records)
# Filter rows where Listing Exchange = 'N' and ETF is not 'Y' (or is null)
# Note: The original SQL already filtered Listing Exchange = 'N' and ETF != 'Y', but we re-check if ETF is null or not 'Y'
if 'Listing Exchange' in df.columns:
    df = df[df['Listing Exchange'] == 'N']
# Consider ETF values: include if ETF is None or not 'Y'
if 'ETF' in df.columns:
    df = df[(df['ETF'].isnull()) | (df['ETF'] != 'Y')]
# Ensure Symbol column exists
if 'Symbol' not in df.columns:
    symbols = []
else:
    df = df.dropna(subset=['Symbol'])
    df['Symbol'] = df['Symbol'].astype(str)
    tables_set = set(tables)
    df['in_trade_db'] = df['Symbol'].apply(lambda s: s in tables_set)
    df = df[df['in_trade_db'] == True]
    symbols = df['Symbol'].tolist()
    mapping = dict(zip(df['Symbol'].tolist(), df['Company Description'].tolist()))

result = {'num_symbols': len(symbols), 'symbols': symbols, 'mapping_sample': {k: mapping[k] for k in list(mapping)[:20]}}
print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_call_rXv6uZ0DDNksTWfPiVrfTqtu': 'file_storage/call_rXv6uZ0DDNksTWfPiVrfTqtu.json', 'var_call_5jcJoDfvBouMTBJgTuzgin4N': 'file_storage/call_5jcJoDfvBouMTBJgTuzgin4N.json'}

exec(code, env_args)
