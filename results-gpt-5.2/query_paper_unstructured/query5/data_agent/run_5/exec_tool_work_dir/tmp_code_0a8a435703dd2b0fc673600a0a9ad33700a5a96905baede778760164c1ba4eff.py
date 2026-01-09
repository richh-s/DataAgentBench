code = """import json, re

def load_maybe_path(v):
    if isinstance(v, str) and v.endswith('.json'):
        with open(v, 'r', encoding='utf-8') as f:
            return json.load(f)
    return v

docs = load_maybe_path(var_call_gTRoysy304z0d0jMDBpm8Hii)

samples=[]
for d in docs:
    text=(d.get('text') or '')
    if 'CHI' in text[:4000] or 'chi' in text[:4000].lower() or 'SIGCHI' in text[:4000]:
        samples.append({'filename':d.get('filename'), 'head':text[:500]})
    if len(samples)>=5:
        break
print('__RESULT__:')
print(json.dumps(samples))"""

env_args = {'var_call_J8txm9Nm7LXRKe115bQZgmuM': 'file_storage/call_J8txm9Nm7LXRKe115bQZgmuM.json', 'var_call_gTRoysy304z0d0jMDBpm8Hii': 'file_storage/call_gTRoysy304z0d0jMDBpm8Hii.json', 'var_call_o7UdNyy6q6k4D0wRTLCPmT1C': {'total_citation_count_for_CHI_papers_cited_in_2020': 0, 'num_CHI_papers_matched': 0}}

exec(code, env_args)
