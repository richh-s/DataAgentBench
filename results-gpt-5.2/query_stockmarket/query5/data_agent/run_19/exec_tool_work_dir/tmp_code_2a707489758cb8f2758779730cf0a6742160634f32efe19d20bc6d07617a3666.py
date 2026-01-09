code = """import json

# top5 from trade query
rows = var_call_Y1YnAexsdlO12PXqHxQwxc9u

# company mapping
src = var_call_WHVSnajTliQHiGgfimhz4muQ
if isinstance(src, str):
    with open(src,'r') as f:
        payload = json.load(f)
else:
    payload = src
company = payload['company']

names = [company.get(r['symbol'], r['symbol']) for r in rows]

print('__RESULT__:')
print(json.dumps(names))"""

env_args = {'var_call_5NexJwt9r8tmm7M3boorcoK4': 'file_storage/call_5NexJwt9r8tmm7M3boorcoK4.json', 'var_call_xlmV46fzXoRjDCNE5tWJWBSV': 'file_storage/call_xlmV46fzXoRjDCNE5tWJWBSV.json', 'var_call_p9dolxokJW8AiTJj0fYLpxbg': 'file_storage/call_p9dolxokJW8AiTJj0fYLpxbg.json', 'var_call_WHVSnajTliQHiGgfimhz4muQ': 'file_storage/call_WHVSnajTliQHiGgfimhz4muQ.json', 'var_call_rMrKNYNDYaKxbxsnoGSlPXVv': 'file_storage/call_rMrKNYNDYaKxbxsnoGSlPXVv.json', 'var_call_Y1YnAexsdlO12PXqHxQwxc9u': [{'symbol': 'SES', 'days': '51'}, {'symbol': 'GLG', 'days': '42'}, {'symbol': 'TMSR', 'days': '40'}, {'symbol': 'VERB', 'days': '38'}, {'symbol': 'SNSS', 'days': '32'}]}

exec(code, env_args)
