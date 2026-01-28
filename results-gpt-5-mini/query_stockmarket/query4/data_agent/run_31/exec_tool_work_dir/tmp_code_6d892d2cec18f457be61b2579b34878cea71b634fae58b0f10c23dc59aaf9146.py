code = """import json
# Load stored results
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

nyse_non_etf = []
for rec in stockinfo:
    sym = rec.get('Symbol')
    if sym in table_list:
        nyse_non_etf.append({'Symbol': sym, 'Company Description': rec.get('Company Description')})

print('__RESULT__:')
print(json.dumps(nyse_non_etf))"""

env_args = {'var_call_PMBN6E9T7eI2X9WsQ47LDLpM': 'file_storage/call_PMBN6E9T7eI2X9WsQ47LDLpM.json', 'var_call_KmfEKriY70zObdxCudPoIzlv': 'file_storage/call_KmfEKriY70zObdxCudPoIzlv.json'}

exec(code, env_args)
