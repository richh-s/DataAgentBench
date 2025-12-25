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

valid_symbols.sort()

# Batch 1: 0 to 60
batch_symbols = valid_symbols[0:60]

sqls = []
for sym in batch_symbols:
    q = "SELECT '" + sym + "' as Symbol, "
    q += "SUM(CASE WHEN Close > Open THEN 1 ELSE 0 END) as Up, "
    q += "SUM(CASE WHEN Close < Open THEN 1 ELSE 0 END) as Down "
    q += "FROM \"" + sym + "\" "
    q += "WHERE Date >= '2017-01-01' AND Date <= '2017-12-31'"
    sqls.append(q)

full_query = " UNION ALL ".join(sqls)

print("__RESULT__:")
print(full_query)"""

env_args = {'var_function-call-18130450125284011666': 'file_storage/function-call-18130450125284011666.json', 'var_function-call-15651770403221500458': 'file_storage/function-call-15651770403221500458.json', 'var_function-call-6132161649174360652': [{'Date': '2018-08-15', 'Open': '11.84000015258789', 'High': '11.84000015258789', 'Low': '11.739999771118164', 'Close': '11.739999771118164', 'Adj Close': '11.739999771118164', 'Volume': '27300'}], 'var_function-call-10399904514394169553': 'file_storage/function-call-10399904514394169553.json', 'var_function-call-5034726085254749822': 'file_storage/function-call-5034726085254749822.json'}

exec(code, env_args)
