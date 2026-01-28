code = """import json
import pandas as pd

# Load NYSE non-ETF symbols from sqlite result (may be file path)
nyse_data = var_call_kNZOFIAS7l658Bla0yhEzoVR
if isinstance(nyse_data, str):
    with open(nyse_data, 'r') as f:
        nyse_data = json.load(f)
nyse_df = pd.DataFrame(nyse_data)
nyse_symbols = set(nyse_df['Symbol'].astype(str))

# Load available trade tables
trade_tables = var_call_JQeLNUauzOkn7Bn3RHEafsPk
if isinstance(trade_tables, str):
    with open(trade_tables, 'r') as f:
        trade_tables = json.load(f)
trade_symbols = set(trade_tables)

symbols = sorted(list(nyse_symbols & trade_symbols))

# Chunk symbols for SQL union query
chunks = [symbols[i:i+80] for i in range(0, len(symbols), 80)]
queries = []
for ch in chunks:
    parts = []
    for t in ch:
        # DuckDB identifier quoting
        parts.append(f"SELECT '{t}' AS Symbol, SUM(CASE WHEN Close>Open THEN 1 ELSE 0 END) AS up_days, SUM(CASE WHEN Close<Open THEN 1 ELSE 0 END) AS down_days FROM \"{t}\" WHERE Date>='2017-01-01' AND Date<='2017-12-31'")
    q = " UNION ALL ".join(parts)
    queries.append(q)

out = {
    'symbols_count': len(symbols),
    'chunks': len(chunks),
    'queries': queries[:3],
    'first_symbols': symbols[:10]
}
print('__RESULT__:')
print(json.dumps(out))"""

env_args = {'var_call_XSjSsb8GS4EPwnO4lroyRna5': ['stockinfo'], 'var_call_kNZOFIAS7l658Bla0yhEzoVR': 'file_storage/call_kNZOFIAS7l658Bla0yhEzoVR.json', 'var_call_JQeLNUauzOkn7Bn3RHEafsPk': 'file_storage/call_JQeLNUauzOkn7Bn3RHEafsPk.json'}

exec(code, env_args)
