code = """import json
# Load the large results from previous tool calls stored as files
with open(var_call_cOi9OMUYcXvqMM1mSCci0y6k, 'r') as f:
    stockinfo = json.load(f)
with open(var_call_ppF3FrkgSKRwnihegO5SvHTe, 'r') as f:
    tables = json.load(f)

# Extract symbols from stockinfo where Market Category is 'S'
symbols_s = [rec['Symbol'] for rec in stockinfo if rec.get('Market Category') == 'S']
# Ensure uppercase and strip
symbols_s = [s.strip() for s in symbols_s]

# Available tables
tables_set = set(tables)

# Intersection
symbols_to_query = [s for s in symbols_s if s in tables_set]
symbols_to_query = sorted(symbols_to_query)

# Build UNION ALL SQL for 2019 days where (High - Low) > 0.2 * Low
# If no symbols, produce a harmless query
if not symbols_to_query:
    sql = "SELECT '' as Symbol, 0 as days LIMIT 0;"
else:
    parts = []
    for s in symbols_to_query:
        part = f"SELECT '{s}' AS Symbol, \"Date\", \"High\", \"Low\" FROM \"{s}\" WHERE \"Date\" LIKE '2019-%' AND (\"High\" - \"Low\") > 0.2 * \"Low\""
        parts.append(part)
    union_sql = "\nUNION ALL\n".join(parts)
    sql = f"SELECT Symbol, COUNT(*) as days FROM (\n{union_sql}\n) t GROUP BY Symbol ORDER BY days DESC LIMIT 5;"

result = {"sql": sql, "symbols_count": len(symbols_to_query)}
print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_call_cOi9OMUYcXvqMM1mSCci0y6k': 'file_storage/call_cOi9OMUYcXvqMM1mSCci0y6k.json', 'var_call_ppF3FrkgSKRwnihegO5SvHTe': 'file_storage/call_ppF3FrkgSKRwnihegO5SvHTe.json'}

exec(code, env_args)
