code = """import json, re
path_docs = var_call_h1mBTWtOiYwb2M6jHJYUJtJl
with open(path_docs,'r',encoding='utf-8') as f:
    docs=json.load(f)

target='malibucity_agenda__01262022-1835.txt'
text = next(d['text'] for d in docs if d['filename']==target)
lines=[ln.rstrip() for ln in text.splitlines()]
idx=[i for i,ln in enumerate(lines) if re.search(r'^Disaster Recovery Projects', ln, re.IGNORECASE)]
if not idx:
    snippet='NO HEADER'
else:
    i=idx[0]
    snippet='\\n'.join(lines[i:i+120])

print('__RESULT__:')
print(json.dumps({'snippet':snippet[:9500]}))"""

env_args = {'var_call_9LRTw9p8CQH1knoR8Etwuoh7': 'file_storage/call_9LRTw9p8CQH1knoR8Etwuoh7.json', 'var_call_h1mBTWtOiYwb2M6jHJYUJtJl': 'file_storage/call_h1mBTWtOiYwb2M6jHJYUJtJl.json', 'var_call_QAfQ96K2TyjqYPSUtKzbHIiG': ['Funding'], 'var_call_cxMIsGphe9S0zjJQjPqUmEqF': ['civic_docs'], 'var_call_k18HwFeQpdk4KH2OgFfcZ80W': {'total_funding': 0, 'project_count_with_funding': 0, 'projects_with_funding': []}, 'var_call_C3Rd9w4T8IQbs1R4iKJRLEjH': {'count': 19, 'filenames': ['malibucity_agenda_03222023-2060.txt', 'malibucity_agenda__01262022-1835.txt', 'malibucity_agenda__01272021-1626.txt', 'malibucity_agenda__03022021-1648.txt', 'malibucity_agenda__03232022-1869.txt', 'malibucity_agenda__03242021-1665.txt', 'malibucity_agenda__04282021-1687.txt', 'malibucity_agenda__05262021-1701.txt', 'malibucity_agenda__06222022-1919.txt', 'malibucity_agenda__06232021-1714.txt', 'malibucity_agenda__06282023-2116.txt', 'malibucity_agenda__07272022-1939.txt', 'malibucity_agenda__07282021-1732.txt', 'malibucity_agenda__08252021-1746.txt', 'malibucity_agenda__09222021-1765.txt', 'malibucity_agenda__09272023-2155.txt', 'malibucity_agenda__10272021-1779.txt', 'malibucity_agenda__11102022-1995.txt', 'malibucity_agenda__12142021-1808.txt']}}

exec(code, env_args)
