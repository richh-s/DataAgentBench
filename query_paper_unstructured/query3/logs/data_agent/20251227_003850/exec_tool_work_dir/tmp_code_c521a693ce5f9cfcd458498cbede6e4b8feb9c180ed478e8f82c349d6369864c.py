code = """import json

with open(var_call_WPw67wgXaskTYVaZBay2hrci, 'r', encoding='utf-8') as f:
    docs = json.load(f)

sample = []
for i, d in enumerate(docs[:50]):
    fn = d.get('filename')
    text = (d.get('text') or '')
    sample.append({
        'filename': fn,
        'head': text[:200].replace('\n',' '),
        'contains_empirical': ('empirical' in (text.lower()))
    })

print('__RESULT__:')
print(json.dumps(sample))"""

env_args = {'var_call_WPw67wgXaskTYVaZBay2hrci': 'file_storage/call_WPw67wgXaskTYVaZBay2hrci.json', 'var_call_1ntqvKIgCKBFjh2PBN0ocFX8': 'file_storage/call_1ntqvKIgCKBFjh2PBN0ocFX8.json', 'var_call_mYMhTkK3uSl7cJInG6UsluoL': [], 'var_call_lk7wSCfnHF8Qhr71426NHQZw': [], 'var_call_B6tTsBXqGYIrbqBYA3iowVR1': []}

exec(code, env_args)
