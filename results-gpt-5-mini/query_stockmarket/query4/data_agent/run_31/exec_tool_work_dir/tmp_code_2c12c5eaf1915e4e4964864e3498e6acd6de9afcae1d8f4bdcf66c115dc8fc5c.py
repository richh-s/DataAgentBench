code = """import json
# Load variables from storage
table_list_var = var_call_PMBN6E9T7eI2X9WsQ47LDLpM
stockinfo_var = var_call_KmfEKriY70zObdxCudPoIzlv

# If these are file paths, open and load JSON
if isinstance(table_list_var, str):
    with open(table_list_var, 'r') as f:
        table_list = json.load(f)
else:
    table_list = table_list_var

if isinstance(stockinfo_var, str):
    with open(stockinfo_var, 'r') as f:
        stockinfo = json.load(f)
else:
    stockinfo = stockinfo_var

# Build list of NYSE non-ETF symbols and mapping to company description
symbols = []
mapping = {}
for rec in stockinfo:
    sym = rec.get('Symbol')
    desc = rec.get('Company Description')
    # ensure symbol in trade database tables
    if sym in table_list:
        symbols.append(sym)
        mapping[sym] = desc

# Build SQL that computes up and down counts for 2017 for each symbol
selects = []
for sym in symbols:
    # safe table and column quoting
    sel = f"SELECT '{sym}' AS symbol, SUM(CASE WHEN \"Close\">\"Open\" THEN 1 ELSE 0 END) AS up, SUM(CASE WHEN \"Close\"<\"Open\" THEN 1 ELSE 0 END) AS down FROM \"{sym}\" WHERE \"Date\">='2017-01-01' AND \"Date\"<='2017-12-31'"
    selects.append(sel)

if not selects:
    sql = ''
else:
    sql = '\nUNION ALL\n'.join(selects) + ';'

output = {'sql': sql, 'mapping': mapping, 'symbols_count': len(symbols)}

print('__RESULT__:')
print(json.dumps(output))"""

env_args = {'var_call_PMBN6E9T7eI2X9WsQ47LDLpM': 'file_storage/call_PMBN6E9T7eI2X9WsQ47LDLpM.json', 'var_call_KmfEKriY70zObdxCudPoIzlv': 'file_storage/call_KmfEKriY70zObdxCudPoIzlv.json'}

exec(code, env_args)
