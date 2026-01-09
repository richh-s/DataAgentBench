code = """import json
import pandas as pd

nyse_data = var_call_kNZOFIAS7l658Bla0yhEzoVR
if isinstance(nyse_data, str):
    with open(nyse_data, 'r') as f:
        nyse_data = json.load(f)
nyse_df = pd.DataFrame(nyse_data)
nyse_symbols = set(nyse_df['Symbol'].astype(str))

trade_tables = var_call_JQeLNUauzOkn7Bn3RHEafsPk
if isinstance(trade_tables, str):
    with open(trade_tables, 'r') as f:
        trade_tables = json.load(f)
trade_symbols = set(trade_tables)

symbols = sorted(nyse_symbols & trade_symbols)
chunks = [symbols[i:i+80] for i in range(0, len(symbols), 80)]
queries = []
for ch in chunks:
    parts = []
    for t in ch:
        part = (
            "SELECT '{sym}' AS Symbol, "
            "SUM(CASE WHEN Close>Open THEN 1 ELSE 0 END) AS up_days, "
            "SUM(CASE WHEN Close<Open THEN 1 ELSE 0 END) AS down_days "
            "FROM \"{sym}\" "
            "WHERE Date>='2017-01-01' AND Date<='2017-12-31'"
        ).format(sym=t)
        parts.append(part)
    queries.append(" UNION ALL ".join(parts))

out = {'symbols_count': len(symbols), 'chunks': len(chunks), 'first_symbols': symbols[:10]}
print('__RESULT__:')
print(json.dumps(out))"""

env_args = {'var_call_XSjSsb8GS4EPwnO4lroyRna5': ['stockinfo'], 'var_call_kNZOFIAS7l658Bla0yhEzoVR': 'file_storage/call_kNZOFIAS7l658Bla0yhEzoVR.json', 'var_call_JQeLNUauzOkn7Bn3RHEafsPk': 'file_storage/call_JQeLNUauzOkn7Bn3RHEafsPk.json'}

exec(code, env_args)
