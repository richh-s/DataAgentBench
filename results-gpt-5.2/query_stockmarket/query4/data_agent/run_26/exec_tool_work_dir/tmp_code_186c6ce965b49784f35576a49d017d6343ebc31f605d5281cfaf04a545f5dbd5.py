code = """import json, pandas as pd

# Load NYSE non-ETF symbols
nyse_path = var_call_YUklvkNSfsVQgYR1c02Ynr1O
with open(nyse_path, 'r') as f:
    nyse = json.load(f)
nyse_df = pd.DataFrame(nyse)

# Load available trade tables
tbl_path = var_call_JtD0SKI6HkrXBgEo4BnEvRkc
with open(tbl_path, 'r') as f:
    tables = json.load(f)
tables_set = set(tables)

# Intersect to those with price tables
symbols = sorted(set(nyse_df['Symbol']).intersection(tables_set))

# Build a single UNION ALL query to compute up/down days for 2017 per symbol
parts = []
for sym in symbols:
    # table names are tickers; quote with double quotes for DuckDB
    parts.append(
        f"SELECT '{sym}' AS Symbol, "
        f"SUM(CASE WHEN Close > Open THEN 1 ELSE 0 END) AS up_days, "
        f"SUM(CASE WHEN Close < Open THEN 1 ELSE 0 END) AS down_days "
        f"FROM \"{sym}\" WHERE Date >= '2017-01-01' AND Date < '2018-01-01'"
    )

# Chunk to avoid overly large query strings
chunk_size = 200
chunks = [parts[i:i+chunk_size] for i in range(0, len(parts), chunk_size)]
queries = [" UNION ALL ".join(ch) for ch in chunks]

result = {
    'symbols_count': int(len(symbols)),
    'queries': queries
}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_call_YUklvkNSfsVQgYR1c02Ynr1O': 'file_storage/call_YUklvkNSfsVQgYR1c02Ynr1O.json', 'var_call_JtD0SKI6HkrXBgEo4BnEvRkc': 'file_storage/call_JtD0SKI6HkrXBgEo4BnEvRkc.json'}

exec(code, env_args)
