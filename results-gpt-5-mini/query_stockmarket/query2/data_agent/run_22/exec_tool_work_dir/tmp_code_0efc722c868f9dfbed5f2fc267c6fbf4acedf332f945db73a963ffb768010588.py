code = """import json, os
data_key = var_call_X4n0M9LafRIoQ3LmMntBQPH6
if isinstance(data_key, str) and os.path.exists(data_key):
    with open(data_key, 'r', encoding='utf-8') as f:
        symbols = json.load(f)
else:
    symbols = data_key
# build union all SQL in chunks to avoid extremely long single line
selects = []
for s in symbols:
    # sanitize symbol: assume valid
    selects.append(f"SELECT '{s}' AS Symbol, MAX(\"Adj Close\") AS max_adj FROM \"{s}\" WHERE \"Date\" >= '2015-01-01' AND \"Date\" <= '2015-12-31'")
sql = " UNION ALL ".join(selects)
full_sql = f"SELECT Symbol, max_adj FROM ({sql}) WHERE max_adj > 200 ORDER BY Symbol;"
print("__RESULT__:")
print(json.dumps(full_sql))"""

env_args = {'var_call_qPWkYeKXPqjNVSXJnmDnWape': 'file_storage/call_qPWkYeKXPqjNVSXJnmDnWape.json', 'var_call_DG3QOs7vOSoK4UcA4sepoE72': 'file_storage/call_DG3QOs7vOSoK4UcA4sepoE72.json', 'var_call_IZXraRyNaZHsPImlQfrnZ3PY': 'file_storage/call_IZXraRyNaZHsPImlQfrnZ3PY.json', 'var_call_X4n0M9LafRIoQ3LmMntBQPH6': 'file_storage/call_X4n0M9LafRIoQ3LmMntBQPH6.json', 'var_call_GWoVrMQVfNw3fsGNtNACDRbY': [], 'var_call_7r0CFhj04VecRsHT4pFd10NK': [], 'var_call_rOa0xl74wwIxyrOrhYUvt28Q': [], 'var_call_E41dxzggIuMzZZ9t8W8KRcjf': [{'max_adj': '193.3121490478516'}], 'var_call_kJ0JanfXBgygjuWtfR1mud76': {'count': 1435}}

exec(code, env_args)
