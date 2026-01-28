code = """import json
# Load the results from previous queries which are stored as file paths in the provided variable names
with open(var_call_PVAfm8uVITZvm5Qg3urNUhRO, 'r') as f:
    stockinfo_records = json.load(f)
with open(var_call_wtLJ5gytvW712GxaYrXyCriN, 'r') as f:
    trade_tables = json.load(f)

# stockinfo_records is a list of dicts with keys Symbol, Company Description, Market Category
# trade_tables is a list of table names (symbols)

# Build a mapping for company descriptions and filter symbols that also exist in trade_tables
company_map = {}
symbols = []
for rec in stockinfo_records:
    sym = rec.get('Symbol')
    desc = rec.get('Company Description')
    if sym in trade_tables:
        symbols.append(sym)
        company_map[sym] = desc

output = {'symbols': symbols, 'company_map': company_map}

print("__RESULT__:")
print(json.dumps(output))"""

env_args = {'var_call_PVAfm8uVITZvm5Qg3urNUhRO': 'file_storage/call_PVAfm8uVITZvm5Qg3urNUhRO.json', 'var_call_wtLJ5gytvW712GxaYrXyCriN': 'file_storage/call_wtLJ5gytvW712GxaYrXyCriN.json'}

exec(code, env_args)
