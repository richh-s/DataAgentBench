code = """import json
# Load the previous tool results from storage file paths
p1 = var_call_Lb6wOudI1vGIvlWeFmRfaMcq
p2 = var_call_DT0diiPjDs1dAAdc2zRjJVxt
with open(p1, 'r') as f:
    stockinfo = json.load(f)
with open(p2, 'r') as f:
    trade_tables = json.load(f)

# Extract symbols from stockinfo (list of dicts with 'Symbol')
stockinfo_syms = [rec['Symbol'] for rec in stockinfo]
trade_syms = list(trade_tables)

# Intersection: symbols that are ETFs listed on NYSE Arca and have trade tables
common_syms = sorted(list(set(stockinfo_syms).intersection(set(trade_syms))))

# Build a UNION ALL SQL query to get max adj close in 2015 for each symbol
parts = []
for sym in common_syms:
    # Escape double quotes in sym if any (unlikely)
    parts.append(f"SELECT '{sym}' AS Symbol, MAX(\"Adj Close\") AS maxadj FROM \"{sym}\" WHERE Date >= '2015-01-01' AND Date <= '2015-12-31'")
sql = '\nUNION ALL\n'.join(parts) + ';'

# Output the SQL string as JSON-serializable string
output = json.dumps(sql)
print("__RESULT__:")
print(output)"""

env_args = {'var_call_Lb6wOudI1vGIvlWeFmRfaMcq': 'file_storage/call_Lb6wOudI1vGIvlWeFmRfaMcq.json', 'var_call_DT0diiPjDs1dAAdc2zRjJVxt': 'file_storage/call_DT0diiPjDs1dAAdc2zRjJVxt.json'}

exec(code, env_args)
