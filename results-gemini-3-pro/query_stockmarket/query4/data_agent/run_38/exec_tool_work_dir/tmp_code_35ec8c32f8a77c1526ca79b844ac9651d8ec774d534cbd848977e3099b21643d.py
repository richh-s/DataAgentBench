code = """import json

# Load stockinfo results
with open(locals()['var_function-call-18130450125284011666'], 'r') as f:
    stockinfo = json.load(f)

# Load trade tables list
with open(locals()['var_function-call-15651770403221500458'], 'r') as f:
    tables = json.load(f)

tables_set = set(tables)

valid_symbols = []
for entry in stockinfo:
    sym = entry['Symbol']
    if sym in tables_set:
        valid_symbols.append(sym)

# Construct SQL query
sqls = []
for sym in valid_symbols:
    # Avoid triple quotes. Use concatenation or single quotes.
    # Query: SELECT 'SYM' as Symbol, SUM(...) ...
    q = "SELECT '" + sym + "' as Symbol, "
    q += "SUM(CASE WHEN Close > Open THEN 1 ELSE 0 END) as Up, "
    q += "SUM(CASE WHEN Close < Open THEN 1 ELSE 0 END) as Down "
    q += "FROM \"" + sym + "\" "
    q += "WHERE Date >= '2017-01-01' AND Date <= '2017-12-31'"
    sqls.append(q)

full_query = " UNION ALL ".join(sqls)

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
