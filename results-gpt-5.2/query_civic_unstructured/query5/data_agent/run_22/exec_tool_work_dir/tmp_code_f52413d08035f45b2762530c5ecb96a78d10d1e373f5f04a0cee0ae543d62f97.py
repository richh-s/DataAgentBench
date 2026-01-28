code = """import json, re

def load_records(v):
    if isinstance(v, str) and v.endswith('.json'):
        with open(v, 'r', encoding='utf-8') as f:
            return json.load(f)
    return v

docs = load_records(var_call_pvJShtqIdgjHoyyWmysUP8iU)
# find first doc that contains 'Disaster Recovery Projects' and return filename
for d in docs:
    t=d.get('text','')
    if re.search(r'Disaster Recovery Projects', t):
        out={'filename':d.get('filename'), 'has_phrase':True, 'snippet':t[t.find('Disaster Recovery Projects'):t.find('Disaster Recovery Projects')+500]}
        break
else:
    out={'found':False}
print('__RESULT__:')
print(json.dumps(out))"""

env_args = {'var_call_WforWNGckDLZNcgvbG8AKAU6': ['Funding'], 'var_call_QfAvDZ3qPtBCuw0ojwVBpNT6': ['civic_docs'], 'var_call_pvJShtqIdgjHoyyWmysUP8iU': 'file_storage/call_pvJShtqIdgjHoyyWmysUP8iU.json', 'var_call_9cXbeBzbNaOXIHYfXpfQYeX9': 'file_storage/call_9cXbeBzbNaOXIHYfXpfQYeX9.json', 'var_call_SQoTkmoTWIbOJzh1MoSBeDNQ': []}

exec(code, env_args)
