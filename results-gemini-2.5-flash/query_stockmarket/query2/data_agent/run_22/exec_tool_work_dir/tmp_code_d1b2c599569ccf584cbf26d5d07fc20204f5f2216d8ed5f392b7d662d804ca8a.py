code = """import json
import pandas as pd

# Load the list of ETF symbols from the previous tool call result
etf_symbols_json_path = locals()['var_function-call-1441279857627207443']
with open(etf_symbols_json_path, 'r') as f:
    etf_symbols_data = json.load(f)

etf_symbols = [d['Symbol'] for d in etf_symbols_data]

# Construct the UNION ALL query for DuckDB
union_queries = []
for symbol in etf_symbols:
    # Each table is named after the stock symbol
    # Select Symbol and Adj Close for dates in 2015 where Adj Close > 200
    # Note: DuckDB treats table names as case-insensitive usually, but it's good practice to match the exact table name if known.
    # Also, need to ensure the Date column is handled correctly for year extraction.
    union_queries.append(f"SELECT '{symbol}' AS Symbol, "Adj Close" FROM "{symbol}" WHERE SUBSTR(Date, 1, 4) = '2015' AND "Adj Close" > 200")

# Combine all individual queries into a single UNION ALL query
full_query = " UNION ALL ".join(union_queries)

print("__RESULT__:")
print(json.dumps(full_query))"""

env_args = {'var_function-call-2263861411356516965': ['stockinfo'], 'var_function-call-1441279857627207443': 'file_storage/function-call-1441279857627207443.json'}

exec(code, env_args)
