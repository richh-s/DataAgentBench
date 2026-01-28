code = """import json, re
path_docs = var_call_h1mBTWtOiYwb2M6jHJYUJtJl
with open(path_docs,'r',encoding='utf-8') as f:
    docs=json.load(f)

hits=[]
for d in docs:
    t=d.get('text','') or ''
    if re.search(r'Disaster Recovery Projects', t, re.IGNORECASE):
        hits.append(d['filename'])

print('__RESULT__:')
print(json.dumps({'count':len(hits),'filenames':hits[:50]}))"""

env_args = {'var_call_9LRTw9p8CQH1knoR8Etwuoh7': 'file_storage/call_9LRTw9p8CQH1knoR8Etwuoh7.json', 'var_call_h1mBTWtOiYwb2M6jHJYUJtJl': 'file_storage/call_h1mBTWtOiYwb2M6jHJYUJtJl.json', 'var_call_QAfQ96K2TyjqYPSUtKzbHIiG': ['Funding'], 'var_call_cxMIsGphe9S0zjJQjPqUmEqF': ['civic_docs'], 'var_call_k18HwFeQpdk4KH2OgFfcZ80W': {'total_funding': 0, 'project_count_with_funding': 0, 'projects_with_funding': []}}

exec(code, env_args)
