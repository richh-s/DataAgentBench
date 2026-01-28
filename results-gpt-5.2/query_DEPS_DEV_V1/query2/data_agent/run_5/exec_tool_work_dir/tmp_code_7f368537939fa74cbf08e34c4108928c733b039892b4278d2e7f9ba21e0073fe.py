code = """import json, re

def load_records(var):
    if isinstance(var, str):
        with open(var, 'r', encoding='utf-8') as f:
            return json.load(f)
    return var

ppv = load_records(var_call_RrHlFOGiwW9wQ211KgUC4uao)
pi = load_records(var_call_ShNXjAyIbgDoMMm5y2fYcdJF)

projects = set([r.get('ProjectName') for r in ppv if r.get('ProjectName')])

# attempt multiple patterns
patterns = [
    re.compile(r"project\s+(?:is hosted on GitHub under the name\s+|named\s+|)\s*([^\s]+/[^\s,]+).*?(\d[\d,]*)\s+forks", re.IGNORECASE),
]

matches=[]
for rec in pi:
    txt = rec.get('Project_Information') or ''
    pname=None; forks=None
    for pat in patterns:
        m = pat.search(txt)
        if m:
            pname=m.group(1).strip().rstrip('.').rstrip(',')
            forks=int(m.group(2).replace(',',''))
            break
    if pname and pname in projects:
        matches.append((pname,forks))

out={'ppv_projects': len(projects), 'matched': len(matches), 'sample_matches': matches[:20]}
print('__RESULT__:')
print(json.dumps(out))"""

env_args = {'var_call_3m97wNj3g9Tlg0iI8J6uh9Sj': 'file_storage/call_3m97wNj3g9Tlg0iI8J6uh9Sj.json', 'var_call_RrHlFOGiwW9wQ211KgUC4uao': 'file_storage/call_RrHlFOGiwW9wQ211KgUC4uao.json', 'var_call_ShNXjAyIbgDoMMm5y2fYcdJF': 'file_storage/call_ShNXjAyIbgDoMMm5y2fYcdJF.json', 'var_call_uTnLTPDiVgzOQ1DxYMwd9kTe': []}

exec(code, env_args)
