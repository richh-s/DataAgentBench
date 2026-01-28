code = """import json
nyse_var = var_call_K63MgEF0ck5Q3hnmXh8jEFw7
if isinstance(nyse_var, str):
    with open(nyse_var, 'r') as f:
        nyse_list = json.load(f)
else:
    nyse_list = nyse_var

tool_uses = []
for rec in nyse_list:
    sym = rec.get('Symbol')
    if not sym:
        continue
    query = f'SELECT "{sym}" AS symbol, SUM(CASE WHEN "Close">"Open" THEN 1 ELSE 0 END) AS up, SUM(CASE WHEN "Close"<"Open" THEN 1 ELSE 0 END) AS down FROM "{sym}" WHERE "Date">=\'2017-01-01\' AND "Date"<=\'2017-12-31\''
    # wrap in dict for multi_tool_use
    tool_uses.append({
        'recipient_name': 'functions.query_db',
        'parameters': {
            'db_name': 'stocktrade_database',
            'query': query
        }
    })

print('__RESULT__:')
print(json.dumps(tool_uses))"""

env_args = {'var_call_PMBN6E9T7eI2X9WsQ47LDLpM': 'file_storage/call_PMBN6E9T7eI2X9WsQ47LDLpM.json', 'var_call_KmfEKriY70zObdxCudPoIzlv': 'file_storage/call_KmfEKriY70zObdxCudPoIzlv.json', 'var_call_K63MgEF0ck5Q3hnmXh8jEFw7': 'file_storage/call_K63MgEF0ck5Q3hnmXh8jEFw7.json'}

exec(code, env_args)
