code = """import json

# Load stockinfo results
with open(locals()['var_function-call-18130450125284011666'], 'r') as f:
    stockinfo = json.load(f)

# Load trade tables list
with open(locals()['var_function-call-15651770403221500458'], 'r') as f:
    tables = json.load(f)

# Create a set of available tables
tables_set = set(tables)

# Filter stockinfo
valid_symbols = []
for entry in stockinfo:
    sym = entry['Symbol']
    if sym in tables_set:
        valid_symbols.append(sym)

print(f"DEBUG: Found {len(valid_symbols)} valid symbols out of {len(stockinfo)} candidates.")

# Construct SQL query
# We need UpDays and DownDays for 2017.
# Query: SELECT 'SYM' as Symbol, SUM(CASE...) as Up, SUM(CASE...) as Down FROM "SYM" WHERE Date LIKE '2017-%'
# UNION ALL ...

sqls = []
for sym in valid_symbols:
    # Use double quotes for table name in case of reserved words or special chars
    # Ensure safe strings
    sqls.append(f"""SELECT '{sym}' as Symbol, 
       SUM(CASE WHEN Close > Open THEN 1 ELSE 0 END) as Up, 
       SUM(CASE WHEN Close < Open THEN 1 ELSE 0 END) as Down 
       FROM "{sym}" 
       WHERE Date >= '2017-01-01' AND Date <= '2017-12-31'""")

full_query = " UNION ALL ".join(sqls)

# Check length
print(f"DEBUG: Query length is {len(full_query)}")

# If length is reasonable, we return it. If too large, we might need a strategy.
# But for now, let's just output the symbols and the query size to decide.
# I'll return the full query if it's < 100000 chars.
# If it's larger, I'll return a split.

# To be safe, I'll return the list of symbols and names as well so I can map later.
symbol_name_map = {entry['Symbol']: entry['Company Description'] for entry in stockinfo if entry['Symbol'] in valid_symbols}

print("__RESULT__:")
print(json.dumps({
    "count": len(valid_symbols),
    "query_len": len(full_query),
    "query": full_query if len(full_query) < 200000 else "TOO_LARGE",
    "names": symbol_name_map
}))"""

env_args = {'var_function-call-18130450125284011666': 'file_storage/function-call-18130450125284011666.json', 'var_function-call-15651770403221500458': 'file_storage/function-call-15651770403221500458.json', 'var_function-call-6132161649174360652': [{'Date': '2018-08-15', 'Open': '11.84000015258789', 'High': '11.84000015258789', 'Low': '11.739999771118164', 'Close': '11.739999771118164', 'Adj Close': '11.739999771118164', 'Volume': '27300'}]}

exec(code, env_args)
