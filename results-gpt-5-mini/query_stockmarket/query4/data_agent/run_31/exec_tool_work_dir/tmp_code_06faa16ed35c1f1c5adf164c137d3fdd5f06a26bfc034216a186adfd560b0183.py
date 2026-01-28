code = """import json
nyse_var = var_call_K63MgEF0ck5Q3hnmXh8jEFw7
if isinstance(nyse_var, str):
    with open(nyse_var, 'r') as f:
        nyse_list = json.load(f)
else:
    nyse_list = nyse_var

symbols = [rec['Symbol'] for rec in nyse_list if rec.get('Symbol')]

selects = []
for sym in symbols:
    sel = (
        "SELECT '" + sym + "' AS symbol, "
        "SUM(CASE WHEN \"Close\">\"Open\" THEN 1 ELSE 0 END) AS up, "
        "SUM(CASE WHEN \"Close\"<\"Open\" THEN 1 ELSE 0 END) AS down "
        "FROM \"" + sym + "\" "
        "WHERE \"Date\">= '2017-01-01' AND \"Date\"<= '2017-12-31'"
    )
    selects.append(sel)

if selects:
    union_sql = "\nUNION ALL\n".join(selects)
    sql = "SELECT symbol, up, down FROM (\n" + union_sql + "\n) AS all_counts WHERE up>down ORDER BY up DESC LIMIT 5;"
else:
    sql = ""

print('__RESULT__:')
print(json.dumps(sql))"""

env_args = {'var_call_PMBN6E9T7eI2X9WsQ47LDLpM': 'file_storage/call_PMBN6E9T7eI2X9WsQ47LDLpM.json', 'var_call_KmfEKriY70zObdxCudPoIzlv': 'file_storage/call_KmfEKriY70zObdxCudPoIzlv.json', 'var_call_K63MgEF0ck5Q3hnmXh8jEFw7': 'file_storage/call_K63MgEF0ck5Q3hnmXh8jEFw7.json'}

exec(code, env_args)
