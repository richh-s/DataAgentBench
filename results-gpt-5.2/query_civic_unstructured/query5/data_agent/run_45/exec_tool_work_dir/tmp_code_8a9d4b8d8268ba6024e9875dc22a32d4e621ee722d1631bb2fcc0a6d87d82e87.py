code = """import json, re, pandas as pd
from pathlib import Path

p = Path(var_call_iWlvf1w9K4H2EEJVqj4PDnhd)
funding = json.loads(p.read_text())
df_f = pd.DataFrame(funding)
df_f['total_amount'] = pd.to_numeric(df_f['total_amount'])

p2 = Path(var_call_VY1KuUzWSgOAlthz2fEG5f9x)
docs = json.loads(p2.read_text())

disaster_projects = {}

pattern_block = re.compile(r'(?is)Disaster Recovery Projects\b(.*?)(?:\n\s*Capital Improvement Projects\b|\Z)')

for d in docs:
    t = d.get('text','').replace('\r','\n')
    for m in pattern_block.finditer(t):
        block = m.group(1)
        lines = [ln.strip() for ln in block.split('\n') if ln.strip()]
        candidates = []
        for ln in lines:
            if len(ln) < 3:
                continue
            if re.match(r'^[\(\[\{\*\-\u2022\u00b7\u00a7\u00b6]', ln):
                continue
            if ':' in ln:
                continue
            if re.search(r'^(Updates|Project Schedule|Estimated Schedule|Project Description|Page\s+\d+|Agenda Item)', ln, flags=re.I):
                continue
            if re.search(r'Disaster Recovery Projects', ln, flags=re.I):
                continue
            if re.search(r'[A-Za-z]', ln):
                candidates.append(ln)
        seen=set(); cand=[]
        for c in candidates:
            if c not in seen:
                seen.add(c); cand.append(c)
        for name in cand:
            for nm in re.finditer(re.escape(name), block):
                window = block[nm.start(): min(len(block), nm.end()+1200)]
                has_2022 = bool(re.search(r'(?i)(Begin|Start)(?:\s+\w+){0,3}\s*:?\s*[^\n]*2022', window)) or bool(re.search(r'(?i)2022[^\n]*(Begin|Start)', window))
                if has_2022:
                    disaster_projects[name] = True
                else:
                    disaster_projects.setdefault(name, False)

start_2022_projects = [k for k,v in disaster_projects.items() if v]
df_join = df_f[df_f['Project_Name'].isin(start_2022_projects)]
total = int(df_join['total_amount'].sum())

out = {
    'total_funding_disaster_projects_started_2022': total,
    'matched_projects_count': int(len(start_2022_projects)),
    'matched_projects': sorted(start_2022_projects)[:50]
}

print('__RESULT__:')
print(json.dumps(out))"""

env_args = {'var_call_1ebOZ15ayV0lFyqWtJ57nNZo': ['Funding'], 'var_call_fE7quFsgt4sJz0LUfYJgwzqP': ['civic_docs'], 'var_call_iWlvf1w9K4H2EEJVqj4PDnhd': 'file_storage/call_iWlvf1w9K4H2EEJVqj4PDnhd.json', 'var_call_VY1KuUzWSgOAlthz2fEG5f9x': 'file_storage/call_VY1KuUzWSgOAlthz2fEG5f9x.json'}

exec(code, env_args)
