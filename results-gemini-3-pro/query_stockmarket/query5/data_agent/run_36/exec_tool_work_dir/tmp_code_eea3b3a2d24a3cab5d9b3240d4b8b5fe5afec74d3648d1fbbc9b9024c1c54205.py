code = """import json
import pandas as pd

# Load stockinfo result
with open(locals()['var_function-call-12648435365939612161'], 'r') as f:
    stockinfo_data = json.load(f)

# Load stocktrade table list
with open(locals()['var_function-call-16816668521200579530'], 'r') as f:
    table_list = json.load(f)

# Convert to DataFrame
df_stockinfo = pd.DataFrame(stockinfo_data)
# Filter symbols that exist in table_list
# table_list contains strings.
tables_set = set(table_list)

# Find symbols in stockinfo that are in stocktrade tables
valid_symbols = []
symbol_map = {} # To store Company Description

for index, row in df_stockinfo.iterrows():
    sym = row['Symbol']
    if sym in tables_set:
        valid_symbols.append(sym)
        symbol_map[sym] = row['Company Description']

print(f"Total valid symbols: {len(valid_symbols)}")
print("__RESULT__:")
print(json.dumps({"valid_symbols": valid_symbols, "symbol_map": symbol_map}))"""

env_args = {'var_function-call-12648435365939612161': 'file_storage/function-call-12648435365939612161.json', 'var_function-call-16816668521200579530': 'file_storage/function-call-16816668521200579530.json'}

exec(code, env_args)
