code = """import json, os
path = var_call_XbZPXxjiSVAG8ZgkztPKNSs7
with open(path, 'r', encoding='utf-8') as f:
    docs = json.load(f)

titles = []
for d in docs:
    fn = d.get('filename','')
    if fn.lower().endswith('.txt'):
        title = fn[:-4]
    else:
        title = fn
    titles.append(title)
# dedupe and sort
titles = sorted(list(dict.fromkeys(titles)))
print('__RESULT__:')
print(json.dumps(titles))"""

env_args = {'var_call_9LUcJa07UacZD6oGJc9q86b9': 'file_storage/call_9LUcJa07UacZD6oGJc9q86b9.json', 'var_call_rxiPijACM8fM6xdYrma1UYHi': [], 'var_call_NDKCw76JURjoKqfcSWAerO58': 'file_storage/call_NDKCw76JURjoKqfcSWAerO58.json', 'var_call_XbZPXxjiSVAG8ZgkztPKNSs7': 'file_storage/call_XbZPXxjiSVAG8ZgkztPKNSs7.json'}

exec(code, env_args)
