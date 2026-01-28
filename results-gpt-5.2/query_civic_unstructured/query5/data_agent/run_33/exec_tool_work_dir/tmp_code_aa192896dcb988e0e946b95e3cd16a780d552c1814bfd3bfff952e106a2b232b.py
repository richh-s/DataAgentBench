code = """import json, re
from pathlib import Path

def load_records(x):
    if isinstance(x, str) and x.endswith('.json'):
        return json.loads(Path(x).read_text())
    return x

civic_recs = load_records(var_call_ZYtrRg6YQuqLcxt7slVcKrb9)

def extract_disaster_projects_started_2022(text):
    lines = text.splitlines()
    start_idx = None
    for i, l in enumerate(lines):
        if re.search(r'Disaster Recovery Projects', l, re.I):
            start_idx = i
            break
    if start_idx is None:
        return []
    window = lines[start_idx:start_idx+800]
    projects = []
    for i, l in enumerate(window):
        name = l.strip()
        if not name or len(name) > 120:
            continue
        if name.startswith(('(cid', 'Page', 'Agenda', 'To:', 'Prepared', 'Approved', 'Date', 'Meeting', 'Subject', 'RECOMMENDED', 'DISCUSSION', 'Capital Improvement')):
            continue
        if re.match(r'^(Updates|Project Schedule|Estimated Schedule|Project Description)\b', name, re.I):
            continue
        chunk = "\n".join([w.strip() for w in window[i:i+35]])
        if re.search(r'Project Schedule', chunk, re.I) and re.search(r'Begin (Construction|Design)\s*:', chunk, re.I):
            m = re.search(r'Begin (?:Construction|Design)\s*:\s*([^\n\r]+)', chunk, re.I)
            begin = m.group(1).strip() if m else ''
            projects.append((name, begin))
    out = []
    for name, begin in projects:
        if '2022' in begin:
            out.append(name)
    # unique preserve order
    seen=set(); uniq=[]
    for n in out:
        if n not in seen:
            seen.add(n); uniq.append(n)
    return uniq

projects_2022=set()
for rec in civic_recs:
    for p in extract_disaster_projects_started_2022(rec.get('text','')):
        projects_2022.add(p)

print('__RESULT__:')
print(json.dumps({'projects_started_2022_disaster': sorted(projects_2022)}))"""

env_args = {'var_call_mfWaEFrfiY7eOT37QkwDcsbv': ['Funding'], 'var_call_2XFv5yYihjWlW1Gp9BKjtyGo': [{'total_funding': '1410000'}], 'var_call_mWWzHlltBpzVXGUApq0UA9q2': ['civic_docs'], 'var_call_ZYtrRg6YQuqLcxt7slVcKrb9': 'file_storage/call_ZYtrRg6YQuqLcxt7slVcKrb9.json'}

exec(code, env_args)
