code = """import json, pandas as pd

# Load NYSE Arca ETFs list
path = var_call_IIzelB2aZqN6Arw9eX5Xcqia
with open(path, 'r') as f:
    etfs = json.load(f)

symbols = [r['Symbol'] for r in etfs]

# Load available trade tables
path2 = var_call_xPgeMOXLTvmuFt8SHsxsB5Pb
with open(path2, 'r') as f:
    trade_tables = set(json.load(f))

symbols_in_trade = [s for s in symbols if s in trade_tables]

# Prepare batch list for SQL IN clause
# DuckDB identifiers: use double quotes for table names
batches = []
batch = []
for s in symbols_in_trade:
    batch.append(s)
    if len(batch) >= 200:
        batches.append(batch)
        batch = []
if batch:
    batches.append(batch)

out = {
    'symbols_total_nyse_arca_etf': len(symbols),
    'symbols_with_trade_table': len(symbols_in_trade),
    'batches': batches
}

print('__RESULT__:')
print(json.dumps(out))"""

env_args = {'var_call_7un3cbfUYFXu1BEzO9lTedgP': ['stockinfo'], 'var_call_xPgeMOXLTvmuFt8SHsxsB5Pb': 'file_storage/call_xPgeMOXLTvmuFt8SHsxsB5Pb.json', 'var_call_IIzelB2aZqN6Arw9eX5Xcqia': 'file_storage/call_IIzelB2aZqN6Arw9eX5Xcqia.json'}

exec(code, env_args)
