code = """import json
selected = json.load(open('selected_syms.json'))
queries = []
for s in selected:
    q = f"SELECT '{s}' AS Symbol, Date, Open, Close FROM '{s}' WHERE Date LIKE '2017-%';"
    queries.append(q)
print('__RESULT__:')
print(json.dumps(queries))"""

env_args = {'var_call_LZrArnqQ3hWDEAwcrfaZCoM5': 'file_storage/call_LZrArnqQ3hWDEAwcrfaZCoM5.json', 'var_call_NtV0ylhLgiw0Jdmpd0RZCe9O': 'file_storage/call_NtV0ylhLgiw0Jdmpd0RZCe9O.json', 'var_call_H5aYOjUvCTaidF3bIXwo8Jln': {'count': 234, 'sample': ['AEFC', 'AIN', 'AIV', 'AIZP', 'AJRD', 'AL', 'AMN', 'AMP', 'AMT', 'ARD']}}

exec(code, env_args)
