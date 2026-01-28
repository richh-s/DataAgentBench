code = """import json

# load symbols/company mapping
src = var_call_xlmV46fzXoRjDCNE5tWJWBSV
if isinstance(src, str):
    with open(src,'r') as f:
        payload = json.load(f)
else:
    payload = src
symbols = payload['symbols']
company = payload['company']

# load table names
tbl_src = var_call_p9dolxokJW8AiTJj0fYLpxbg
if isinstance(tbl_src, str):
    with open(tbl_src,'r') as f:
        tbl_recs = json.load(f)
else:
    tbl_recs = tbl_src
available = {r['table_name'] for r in tbl_recs}

symbols_avail = [s for s in symbols if s in available]

out = json.dumps({'symbols_avail': symbols_avail, 'company': company})
print('__RESULT__:')
print(out)"""

env_args = {'var_call_5NexJwt9r8tmm7M3boorcoK4': 'file_storage/call_5NexJwt9r8tmm7M3boorcoK4.json', 'var_call_xlmV46fzXoRjDCNE5tWJWBSV': 'file_storage/call_xlmV46fzXoRjDCNE5tWJWBSV.json', 'var_call_p9dolxokJW8AiTJj0fYLpxbg': 'file_storage/call_p9dolxokJW8AiTJj0fYLpxbg.json'}

exec(code, env_args)
