code = """import json
# Load the previous query results from storage files
with open(var_call_d6OF5lNHFpCkdROe3WXhSEIn, 'r') as f:
    etf_list = json.load(f)
with open(var_call_pWaf7Rt5WZqXxRrWb0Xhaa1p, 'r') as f:
    trade_tables = json.load(f)

# Extract symbols from etf_list
etf_symbols = [r['Symbol'] for r in etf_list]
# trade_tables is a list of table names
trade_set = set(trade_tables)

# Compute intersection of symbols present in trade DB
common_symbols = [s for s in etf_symbols if s in trade_set]

# Build a UNION ALL SQL that checks each table for any 2015 adj close > 200
selects = []
for s in common_symbols:
    # Sanitize symbol for use in SQL literal and identifier
    lit = s.replace("'","''")
    # Table identifier: wrap in double quotes to handle special names
    sel = f"(SELECT '{lit}' AS Symbol FROM \"{s}\" WHERE Date >= '2015-01-01' AND Date <= '2015-12-31' AND \"Adj Close\" > 200 LIMIT 1)"
    selects.append(sel)

if not selects:
    sql = "SELECT NULL::VARCHAR AS Symbol WHERE false;"
else:
    sql = "\nUNION ALL\n".join(selects) + "\nORDER BY Symbol;"

out = {'sql': sql, 'candidate_count': len(common_symbols)}
import json
print("__RESULT__:")
print(json.dumps(out))"""

env_args = {'var_call_d6OF5lNHFpCkdROe3WXhSEIn': 'file_storage/call_d6OF5lNHFpCkdROe3WXhSEIn.json', 'var_call_pWaf7Rt5WZqXxRrWb0Xhaa1p': 'file_storage/call_pWaf7Rt5WZqXxRrWb0Xhaa1p.json'}

exec(code, env_args)
