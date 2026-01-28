code = """import json
# load query result and company map
res = var_call_EGPVvVAe8H6qZ9Iz9KveEDWz
with open(var_call_T5JxIIzn9gW9I1SYPaYm57Rh, 'r') as f:
    data = json.load(f)
company_map = data['company_map']

# Map symbols to company descriptions
out_list = []
for r in res:
    sym = r['symbol']
    desc = company_map.get(sym, None)
    out_list.append({'symbol': sym, 'company': desc, 'count': float(r['cnt'])})

print('__RESULT__:')
print(json.dumps(out_list))"""

env_args = {'var_call_QB0CCR1hatdVEWXkYN8q4fGL': 'file_storage/call_QB0CCR1hatdVEWXkYN8q4fGL.json', 'var_call_5zfSoW9T2RnNqppz3xCdHJon': 'file_storage/call_5zfSoW9T2RnNqppz3xCdHJon.json', 'var_call_T5JxIIzn9gW9I1SYPaYm57Rh': 'file_storage/call_T5JxIIzn9gW9I1SYPaYm57Rh.json', 'var_call_EGPVvVAe8H6qZ9Iz9KveEDWz': [{'symbol': 'SES', 'cnt': '51.0'}, {'symbol': 'GLG', 'cnt': '42.0'}, {'symbol': 'TMSR', 'cnt': '40.0'}, {'symbol': 'VERB', 'cnt': '38.0'}, {'symbol': 'SNSS', 'cnt': '32.0'}]}

exec(code, env_args)
