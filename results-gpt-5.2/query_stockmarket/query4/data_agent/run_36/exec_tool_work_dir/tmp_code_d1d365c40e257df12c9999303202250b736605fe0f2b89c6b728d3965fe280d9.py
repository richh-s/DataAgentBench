code = """import json, pandas as pd

# Load NYSE non-ETF symbols with names
path = var_call_1KSmw8wTWVRtAfpKPz4Wtunl
with open(path, 'r') as f:
    info = json.load(f)
info_df = pd.DataFrame(info)

# Load trade tables list
path2 = var_call_DYfAOBC3wLroJmA6thnVUubL
with open(path2, 'r') as f:
    tables = json.load(f)
tables_set = set(tables)

# Keep only symbols that actually have a price table
symbols = sorted(set(info_df['Symbol']).intersection(tables_set))

# Build a single DuckDB query that unions per-symbol counts for 2017
# Using table name quoting with double quotes to be safe.
unions = []
for sym in symbols:
    unions.append(
        f"SELECT '{sym}' AS Symbol, "
        f"SUM(CASE WHEN Close > Open THEN 1 ELSE 0 END) AS up_days, "
        f"SUM(CASE WHEN Close < Open THEN 1 ELSE 0 END) AS down_days "
        f"FROM \"{sym}\" WHERE Date >= '2017-01-01' AND Date < '2018-01-01'"
    )

query = "\nUNION ALL\n".join(unions)

# Print query string as JSON so we can send it to query_db next
out = json.dumps({"query": query, "symbol_count": len(symbols)})
print('__RESULT__:')
print(out)"""

env_args = {'var_call_1KSmw8wTWVRtAfpKPz4Wtunl': 'file_storage/call_1KSmw8wTWVRtAfpKPz4Wtunl.json', 'var_call_DYfAOBC3wLroJmA6thnVUubL': 'file_storage/call_DYfAOBC3wLroJmA6thnVUubL.json'}

exec(code, env_args)
