code = """import json, re

path_docs = var_call_EYXYFvFbvN1U9onxzxlLFccl
with open(path_docs,'r',encoding='utf-8') as f:
    docs = json.load(f)

# filter for published year 2016 by copyright/publication year patterns
pub2016 = []
for d in docs:
    txt = d.get('text','')
    if re.search(r'Copyright\s+2016', txt, re.I) or re.search(r'\b2016\b', txt) and re.search(r'(CHI\s*2016|UbiComp\s*2016|CSCW\s*2016|DIS\s*2016|IUI\s*2016|WWW\s*2016|PervasiveHealth\s*2016|OzCHI\s*2016|TEI\s*2016|AH\s*2016)', txt, re.I):
        pub2016.append(d['filename'].replace('.txt',''))

print('__RESULT__:')
print(json.dumps({'pub2016_count': len(pub2016), 'sample': pub2016[:50]}))"""

env_args = {'var_call_kTDdrqkBRqXTBZuUxBPQEHnT': 'file_storage/call_kTDdrqkBRqXTBZuUxBPQEHnT.json', 'var_call_NEWZSHwtzbngeFnBEoPIUOn0': 'file_storage/call_NEWZSHwtzbngeFnBEoPIUOn0.json', 'var_call_z67pkutgTvC3WuHJI9rR80ku': {'candidate_count': 0, 'candidates': []}, 'var_call_Qamalgbo7OGIhnJJXWy4pDnn': 'file_storage/call_Qamalgbo7OGIhnJJXWy4pDnn.json', 'var_call_EYXYFvFbvN1U9onxzxlLFccl': 'file_storage/call_EYXYFvFbvN1U9onxzxlLFccl.json'}

exec(code, env_args)
