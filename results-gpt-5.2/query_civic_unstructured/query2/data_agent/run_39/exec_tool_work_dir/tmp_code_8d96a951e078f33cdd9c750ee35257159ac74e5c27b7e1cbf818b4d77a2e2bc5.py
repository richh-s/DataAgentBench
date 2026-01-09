code = """import json, re
import pandas as pd

def load_json(path_or_obj):
    if isinstance(path_or_obj, str) and path_or_obj.endswith('.json'):
        with open(path_or_obj, 'r', encoding='utf-8') as f:
            return json.load(f)
    return path_or_obj

docs = load_json(var_call_ZUCDDdG0SXoMt4kmuU3viNnj)

projects = []
status_list = ['Design','Construction','Not Started','Completed']
for d in docs:
    text = d.get('text','')
    for status in status_list:
        pat = re.compile(r"Capital Improvement Projects \(" + re.escape(status) + r"\)\s*(.*?)\n\n(?=Capital Improvement Projects \(|Disaster Recovery Projects|$)", re.S|re.I)
        for m in pat.finditer(text):
            sec = m.group(1)
            lines = [ln.strip() for ln in sec.splitlines() if ln.strip()]
            for i, ln in enumerate(lines):
                if re.match(r"^(cid:190)|^•|^\(cid", ln):
                    continue
                if ln.lower().startswith(('updates','project schedule','estimated schedule','project description','project updates','page ')):
                    continue
                if 'capital improvement projects' in ln.lower():
                    continue
                nxt = lines[i+1].lower() if i+1 < len(lines) else ''
                if ('updates' in nxt) or nxt.startswith('(cid') or nxt.startswith('•'):
                    projects.append({'Project_Name': ln, 'status': status.lower()})

# de-dup
seen=set(); uniq=[]
for p in projects:
    k=(p['Project_Name'], p['status'])
    if k in seen: continue
    seen.add(k); uniq.append(p)
projects=uniq

for p in projects:
    name_l = p['Project_Name'].lower()
    p['is_park_related'] = bool(re.search(r"\bpark\b|playground|bluffs|skate|legacy park", name_l))
    p['completed_2022'] = False

for d in docs:
    low = d.get('text','').lower()
    for p in projects:
        if not p['is_park_related']:
            continue
        nml = p['Project_Name'].lower()
        idx = low.find(nml)
        if idx == -1:
            continue
        window = low[max(0, idx-500): idx+1000]
        if 'completed' in window and '2022' in window:
            p['completed_2022'] = True

park_completed_names = sorted({p['Project_Name'] for p in projects if p['is_park_related'] and p['completed_2022']})

fund = load_json(var_call_lHgXzv8V5PNkATE07UWgYxoP)
df_f = pd.DataFrame(fund)
if not df_f.empty:
    df_f['total_amount'] = pd.to_numeric(df_f['total_amount'])

matched = df_f[df_f['Project_Name'].isin(park_completed_names)]
total = int(matched['total_amount'].sum()) if not matched.empty else 0

out = {'total_funding': total, 'project_count': len(park_completed_names), 'projects': park_completed_names}
print('__RESULT__:')
print(json.dumps(out))"""

env_args = {'var_call_33hmIpX4fm9R354cWlcPlxP0': ['Funding'], 'var_call_9hYeWZ1GktsnA3KhmBLFySCc': ['civic_docs'], 'var_call_ZUCDDdG0SXoMt4kmuU3viNnj': 'file_storage/call_ZUCDDdG0SXoMt4kmuU3viNnj.json', 'var_call_lHgXzv8V5PNkATE07UWgYxoP': 'file_storage/call_lHgXzv8V5PNkATE07UWgYxoP.json'}

exec(code, env_args)
