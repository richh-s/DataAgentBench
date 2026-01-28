code = """import json
# Load the large results from previous tool calls
p1 = var_call_obofffwTil0kays857PB0osJ
p2 = var_call_GWxju3cF897Xt8p4q6hk2Rmi

# Helper to load if it's a filepath
def load_var(v):
    if isinstance(v, str):
        with open(v, 'r') as f:
            return json.load(f)
    return v

stockinfo = load_var(p1)
trade_tables = load_var(p2)

# Get symbols from stockinfo where Market Category was 'S' (already filtered in the query)
symbols_info = [r['Symbol'] for r in stockinfo if r.get('Symbol')]
trade_set = set(trade_tables)

# Intersection
symbols = [s for s in symbols_info if s in trade_set]

# Build SQL by unioning selects per table
sql_parts = []
for s in symbols:
    # skip problematic symbols containing double quote
    if '"' in s:
        continue
    part = f"SELECT '{s}' AS Symbol, COUNT(*) AS cnt FROM \"{s}\" WHERE Date >= '2019-01-01' AND Date <= '2019-12-31' AND (\"High\" - \"Low\") > 0.2 * \"Low\""
    sql_parts.append(part)

if not sql_parts:
    sql = ''
else:
    sql = "\nUNION ALL\n".join(sql_parts) + "\nORDER BY cnt DESC;"

out = {'sql': sql, 'num_symbols': len(symbols)}
print("__RESULT__:")
print(json.dumps(out))"""

env_args = {'var_call_obofffwTil0kays857PB0osJ': 'file_storage/call_obofffwTil0kays857PB0osJ.json', 'var_call_GWxju3cF897Xt8p4q6hk2Rmi': 'file_storage/call_GWxju3cF897Xt8p4q6hk2Rmi.json'}

exec(code, env_args)
