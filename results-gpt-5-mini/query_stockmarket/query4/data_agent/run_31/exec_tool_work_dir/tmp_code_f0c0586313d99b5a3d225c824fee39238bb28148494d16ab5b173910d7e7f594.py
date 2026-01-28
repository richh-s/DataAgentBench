code = """import json
table_list_var = var_call_PMBN6E9T7eI2X9WsQ47LDLpM
stockinfo_var = var_call_KmfEKriY70zObdxCudPoIzlv

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

symbols = []
mapping = {}
for rec in stockinfo:
    sym = rec.get('Symbol')
    desc = rec.get('Company Description')
    if sym in table_list:
        symbols.append(sym)
        mapping[sym] = desc

selects = []
for sym in symbols:
    sel = ("SELECT '{}' AS symbol, SUM(CASE WHEN \"Close\">\"Open\" THEN 1 ELSE 0 END) AS up, "
           "SUM(CASE WHEN \"Close\"<\"Open\" THEN 1 ELSE 0 END) AS down FROM \"{}\" "
           "WHERE \"Date\">='2017-01-01' AND \"Date\"<='2017-12-31'").format(sym, sym)
    selects.append(sel)

sql = ''
if selects:
    sql = "\nUNION ALL\n".join(selects) + ';'

output = {'sql': sql, 'mapping': mapping, 'symbols_count': len(symbols)}
print('__RESULT__:')
print(json.dumps(output))"""

env_args = {'var_call_PMBN6E9T7eI2X9WsQ47LDLpM': 'file_storage/call_PMBN6E9T7eI2X9WsQ47LDLpM.json', 'var_call_KmfEKriY70zObdxCudPoIzlv': 'file_storage/call_KmfEKriY70zObdxCudPoIzlv.json'}

exec(code, env_args)
