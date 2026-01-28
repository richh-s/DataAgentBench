code = """import json
# Load the stored query results
with open(var_call_Lj8XAxsX7AT97Di1xIKGsn9F, 'r') as f:
    stockinfo = json.load(f)
with open(var_call_EmUNNKSWKE7BeUlKNfhNkVnb, 'r') as f:
    trade_tables = json.load(f)

# Extract symbols from stockinfo (ETF symbols listed on NYSE Arca)
etf_symbols = [r['Symbol'] for r in stockinfo]
# trade_tables is a list of table names
trade_set = set(trade_tables)

# Keep only symbols that have a corresponding table in the trade database
symbols_with_table = [s for s in etf_symbols if s in trade_set]

# Build a union SQL that computes max adj close in 2015 per symbol and returns those with max>200
sql_parts = []
for s in symbols_with_table:
    part = f"SELECT '{s}' AS Symbol, MAX(\"Adj Close\") AS max_adj FROM \"{s}\" WHERE Date >= '2015-01-01' AND Date <= '2015-12-31' GROUP BY Symbol HAVING MAX(\"Adj Close\") > 200"
    sql_parts.append(part)

if not sql_parts:
    final_sql = "SELECT NULL WHERE FALSE;"
else:
    final_sql = " UNION ALL ".join(sql_parts) + ";"

result = {
    'sql': final_sql,
    'symbols_count_checked': len(symbols_with_table),
    'symbols_checked_sample': symbols_with_table[:50]
}

import json
print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_Lj8XAxsX7AT97Di1xIKGsn9F': 'file_storage/call_Lj8XAxsX7AT97Di1xIKGsn9F.json', 'var_call_EmUNNKSWKE7BeUlKNfhNkVnb': 'file_storage/call_EmUNNKSWKE7BeUlKNfhNkVnb.json'}

exec(code, env_args)
