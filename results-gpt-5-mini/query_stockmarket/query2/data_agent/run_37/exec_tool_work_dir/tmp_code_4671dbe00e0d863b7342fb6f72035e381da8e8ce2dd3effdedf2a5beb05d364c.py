code = """import json
# Load the two large results from previous tool calls
path_stockinfo = var_call_uaaUjkgCkmEkiZqaNlFP7iBq
path_trade_tables = var_call_V3UlhusiiMVsL0D2qHUs1Des
with open(path_stockinfo, 'r') as f:
    stockinfo = json.load(f)
with open(path_trade_tables, 'r') as f:
    trade_tables = json.load(f)
# Extract symbols from stockinfo result
symbols_stockinfo = [rec['Symbol'] for rec in stockinfo]
# trade_tables is a list of table names
symbols_trade = trade_tables
# Intersection (symbols that are ETF on NYSE Arca and have trade data)
symbols = [s for s in symbols_stockinfo if s in symbols_trade]
symbols = sorted(symbols)
# Build a UNION ALL SQL that computes max Adj Close in 2015 for each symbol
# Use double quotes around table and column names
parts = []
for s in symbols:
    part = f"SELECT '{s}' AS Symbol, (SELECT MAX(\"Adj Close\") FROM \"{s}\" WHERE \"Date\">='2015-01-01' AND \"Date\"<='2015-12-31') AS max_adj"
    parts.append(part)
if parts:
    union_sql = "\nUNION ALL\n".join(parts)
    final_sql = f"SELECT Symbol, max_adj FROM (\n{union_sql}\n) WHERE max_adj IS NOT NULL AND max_adj > 200 ORDER BY Symbol;"
else:
    final_sql = "SELECT NULL AS Symbol, NULL AS max_adj WHERE 1=0;"
# Output the SQL query as JSON string
print("__RESULT__:")
print(json.dumps(final_sql))"""

env_args = {'var_call_uaaUjkgCkmEkiZqaNlFP7iBq': 'file_storage/call_uaaUjkgCkmEkiZqaNlFP7iBq.json', 'var_call_V3UlhusiiMVsL0D2qHUs1Des': 'file_storage/call_V3UlhusiiMVsL0D2qHUs1Des.json'}

exec(code, env_args)
