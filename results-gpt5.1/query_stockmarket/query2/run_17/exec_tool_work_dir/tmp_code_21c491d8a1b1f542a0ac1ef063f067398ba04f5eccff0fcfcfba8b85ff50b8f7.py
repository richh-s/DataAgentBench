code = """import json
import pandas as pd

# Load ETF symbols listed on NYSE Arca
file_path = var_call_OBOcCkedgKAL1oJt9GjG911c
with open(file_path, 'r') as f:
    etf_records = json.load(f)

etf_symbols = sorted({rec['Symbol'] for rec in etf_records})

# Prepare DuckDB SQL to scan only these ETF tables and find those with Adj Close > 200 in 2015
# We'll build a UNION ALL query across all symbols that exist as tables in stocktrade_database.

# Load list of all tables in stocktrade_database
trade_tables_file = var_call_gRAt9zifotekgqiw2SRtcTJT
with open(trade_tables_file, 'r') as f:
    all_tables = json.load(f)

all_tables_set = set(all_tables)

symbols_to_use = sorted(sym for sym in etf_symbols if sym in all_tables_set)

parts = []
for sym in symbols_to_use:
    # DuckDB: need to quote table and column names that have spaces; table names are simple
    part = f"SELECT '{sym}' AS Symbol FROM '{sym}' WHERE CAST(Date AS DATE) BETWEEN DATE '2015-01-01' AND DATE '2015-12-31' AND ""Adj Close"" > 200"
    parts.append(part)

if parts:
    union_query = " UNION ALL ".join(parts)
    final_query = f"SELECT DISTINCT Symbol FROM ({union_query});"
else:
    final_query = "SELECT 'NONE' AS Symbol WHERE 1=0;"

result = {
    'duckdb_query': final_query,
    'symbol_count_considered': len(symbols_to_use)
}

out = json.dumps(result)
print("__RESULT__:")
print(out)"""

env_args = {'var_call_OBOcCkedgKAL1oJt9GjG911c': 'file_storage/call_OBOcCkedgKAL1oJt9GjG911c.json', 'var_call_gRAt9zifotekgqiw2SRtcTJT': 'file_storage/call_gRAt9zifotekgqiw2SRtcTJT.json'}

exec(code, env_args)
