code = """import json

# Load stock info results
with open(locals()['var_function-call-2176412617243161922'], 'r') as f:
    target_stocks = json.load(f)

# Load available tables in stocktrade_database
with open(locals()['var_function-call-11082574715617122511'], 'r') as f:
    available_tables = set(json.load(f))

# Filter symbols
valid_symbols = []
company_names = {}
for stock in target_stocks:
    sym = stock['Symbol']
    if sym in available_tables:
        valid_symbols.append(sym)
        company_names[sym] = stock['Company Description']

print(f"Total target symbols: {len(target_stocks)}")
print(f"Valid symbols with data: {len(valid_symbols)}")
print(f"Valid symbols list: {valid_symbols}")
print("__RESULT__:")
print(json.dumps({"valid_symbols": valid_symbols, "company_names": company_names}))"""

env_args = {'var_function-call-2176412617243161922': 'file_storage/function-call-2176412617243161922.json', 'var_function-call-11082574715617122511': 'file_storage/function-call-11082574715617122511.json'}

exec(code, env_args)
