code = """import json, pandas as pd

# Load tickers from stockinfo query (may be stored as file path)
info_src = var_call_W5TuiiyrfPi6o1EtMXMSQu1H
if isinstance(info_src, str):
    with open(info_src, 'r') as f:
        info = json.load(f)
else:
    info = info_src

trade_src = var_call_OYmEXJVMf4LWCZSkuzjovqPJ
if isinstance(trade_src, str):
    with open(trade_src, 'r') as f:
        trade_tables = json.load(f)
else:
    trade_tables = trade_src

info_df = pd.DataFrame(info)
trade_set = set(trade_tables)

# keep only symbols that have a trade table
symbols = [s for s in info_df['Symbol'].tolist() if s in trade_set]

# Build UNION ALL query across all relevant ticker tables to count 2019 days where (High-Low)/Low > 0.2
# Guard against Low <= 0 or NULL
parts = []
for sym in symbols:
    parts.append(
        f"SELECT '{sym}' AS Symbol, COUNT(*) AS days_cnt "
        f"FROM \"{sym}\" "
        f"WHERE Date >= '2019-01-01' AND Date < '2020-01-01' "
        f"AND Low IS NOT NULL AND High IS NOT NULL AND Low > 0 "
        f"AND (High - Low) / Low > 0.2"
    )

query = "\nUNION ALL\n".join(parts)

print('__RESULT__:')
print(json.dumps({'symbols': symbols, 'union_query': query}))"""

env_args = {'var_call_W5TuiiyrfPi6o1EtMXMSQu1H': 'file_storage/call_W5TuiiyrfPi6o1EtMXMSQu1H.json', 'var_call_OYmEXJVMf4LWCZSkuzjovqPJ': 'file_storage/call_OYmEXJVMf4LWCZSkuzjovqPJ.json'}

exec(code, env_args)
