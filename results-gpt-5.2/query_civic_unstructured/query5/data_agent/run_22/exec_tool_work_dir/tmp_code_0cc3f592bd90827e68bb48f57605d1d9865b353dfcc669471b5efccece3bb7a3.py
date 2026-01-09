code = """import json, pandas as pd

def load_records(v):
    if isinstance(v, str) and v.endswith('.json'):
        with open(v, 'r', encoding='utf-8') as f:
            return json.load(f)
    return v

docs = load_records(var_call_pvJShtqIdgjHoyyWmysUP8iU)

# show first 30 unique lines after 'Disaster Recovery Projects'
lines_out=[]
for d in docs:
    t=d.get('text','')
    if 'Disaster Recovery Projects' not in t:
        continue
    lines=[ln.strip() for ln in t.splitlines()]
    for i,ln in enumerate(lines):
        if ln.startswith('Disaster Recovery Projects'):
            lines_out.extend(lines[i:i+40])
            break
    if len(lines_out)>200:
        break
out=lines_out[:120]
print('__RESULT__:')
print(json.dumps(out))"""

env_args = {'var_call_WforWNGckDLZNcgvbG8AKAU6': ['Funding'], 'var_call_QfAvDZ3qPtBCuw0ojwVBpNT6': ['civic_docs'], 'var_call_pvJShtqIdgjHoyyWmysUP8iU': 'file_storage/call_pvJShtqIdgjHoyyWmysUP8iU.json', 'var_call_9cXbeBzbNaOXIHYfXpfQYeX9': 'file_storage/call_9cXbeBzbNaOXIHYfXpfQYeX9.json'}

exec(code, env_args)
