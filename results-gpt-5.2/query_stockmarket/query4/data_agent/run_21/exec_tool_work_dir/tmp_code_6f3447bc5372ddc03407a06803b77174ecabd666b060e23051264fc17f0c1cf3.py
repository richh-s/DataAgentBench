code = """import json, pandas as pd

# load nyse non-etf symbols
nyse_path = var_call_VroXjKZTSWYofoKRExj4rRXj
with open(nyse_path, 'r') as f:
    nyse = json.load(f)
nyse_df = pd.DataFrame(nyse)
nyse_symbols = set(nyse_df['Symbol'].astype(str))

# load available trade tables
trade_path = var_call_YNzH1kydC4Z3f3E2u8H6XzeS
with open(trade_path, 'r') as f:
    trade_tables = json.load(f)
trade_set = set(trade_tables)

symbols = sorted(list(nyse_symbols & trade_set))

# helper to safely quote duckdb identifiers
# double-quote and escape embedded quotes by doubling them

def qident(name: str) -> str:
    return '"' + name.replace('"','""') + '"'

# build one UNION ALL query to compute up/down counts in 2017 for all symbols
selects = []
for s in symbols:
    t = qident(s)
    # Date is string; compare string range for 2017
    sel = f"SELECT '{s}' AS Symbol, "\
          f"SUM(CASE WHEN Close > Open THEN 1 ELSE 0 END) AS up_days, "\
          f"SUM(CASE WHEN Close < Open THEN 1 ELSE 0 END) AS down_days "\
          f"FROM {t} WHERE Date >= '2017-01-01' AND Date <= '2017-12-31'"
    selects.append(sel)

# chunk if too large
chunks = []
chunk = []
max_len = 900000  # keep query size reasonable
cur_len = 0
for sel in selects:
    if cur_len + len(sel) + 12 > max_len and chunk:
        chunks.append(chunk)
        chunk = [sel]
        cur_len = len(sel)
    else:
        chunk.append(sel)
        cur_len += len(sel) + 12
if chunk:
    chunks.append(chunk)

out = {
    'symbols': symbols,
    'chunks': [' UNION ALL '.join(c) for c in chunks]
}

print('__RESULT__:')
print(json.dumps(out))"""

env_args = {'var_call_VroXjKZTSWYofoKRExj4rRXj': 'file_storage/call_VroXjKZTSWYofoKRExj4rRXj.json', 'var_call_YNzH1kydC4Z3f3E2u8H6XzeS': 'file_storage/call_YNzH1kydC4Z3f3E2u8H6XzeS.json'}

exec(code, env_args)
