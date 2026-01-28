code = """import json, re
path_docs=var_call_bRlNzZZ72IqhjANul1A5ti3D
with open(path_docs,'r',encoding='utf-8') as f:
    docs=json.load(f)
text=None
fn=None
for d in docs:
    if 'Capital Improvement Projects (Construction)' in d.get('text',''):
        text=d['text']; fn=d['filename']; break
lines=[ln.strip() for ln in text.splitlines()]
# locate the index
idx=[i for i,ln in enumerate(lines) if re.search(r'Capital Improvement Projects \(Construction\)', ln, re.I)][0]
segment=lines[idx:idx+80]
print('__RESULT__:')
print(json.dumps({'filename':fn,'segment':segment}))"""

env_args = {'var_call_EwJRJJ2BDH1bM1CyPdScGWSH': ['Funding'], 'var_call_y86nrVdqSPdR9vmjn1tZzarh': ['civic_docs'], 'var_call_bRlNzZZ72IqhjANul1A5ti3D': 'file_storage/call_bRlNzZZ72IqhjANul1A5ti3D.json', 'var_call_tSW7bYfRh9pqlIqOF2V66jZM': 'file_storage/call_tSW7bYfRh9pqlIqOF2V66jZM.json', 'var_call_9wzPbJn4pIo9IAPXQeBcNCYw': {'doc_count': 19, 'sample_keys': ['filename', 'text']}, 'var_call_EmngWz2UM1sSupaha8csJxcu': {'rows': 0, 'cols': [], 'head': []}, 'var_call_FZY50vlgyNKOysQy9D5bHi50': {'filename': 'malibucity_agenda_03222023-2060.txt', 'hits': ['Capital Improvement Projects and Disaster Recovery Projects Status', 'upcoming Capital Improvement Projects and Disaster Recovery Projects.', 'Fiscal Year 2022-2023 Capital Improvement Program:', 'Capital Improvement Projects (Design)', 'Capital Improvement Projects (Construction)', 'Capital Improvement Projects (Not Started)']}}

exec(code, env_args)
