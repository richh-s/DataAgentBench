code = """import json, re
import pandas as pd

def load_mongo(path_or_obj):
    if isinstance(path_or_obj, str) and path_or_obj.endswith('.json'):
        with open(path_or_obj, 'r', encoding='utf-8') as f:
            return json.load(f)
    return path_or_obj

docs = load_mongo(var_call_ZUCDDdG0SXoMt4kmuU3viNnj)

# Parse projects from text blocks in agendas.
projects = []
for d in docs:
    text = d.get('text','')
    # Identify blocks by status headings
    for status in ['Design','Construction','Not Started','Completed']:
        # capture section text after heading until next heading or end
        pattern = re.compile(rf"Capital Improvement Projects \({re.escape(status)}\)\s*(.*?)\n\n(?=Capital Improvement Projects \(|Disaster Recovery Projects|$)", re.S|re.I)
        for m in pattern.finditer(text):
            sec = m.group(1)
            # project names appear as lines not starting with bullets and followed by updates
            lines = [ln.strip() for ln in sec.splitlines() if ln.strip()]
            # heuristic: project name line is followed by '(cid' bullet or '•' or 'Updates'
            for i, ln in enumerate(lines):
                if re.match(r"^(cid:190)|^•|^\(cid", ln):
                    continue
                if ln.lower().startswith(('updates','project schedule','estimated schedule','project description','project updates','page ')):
                    continue
                # exclude generic headings
                if 'Capital Improvement Projects' in ln:
                    continue
                # likely name if next non-empty line contains 'Updates' or bullet marker
                nxt = lines[i+1].lower() if i+1 < len(lines) else ''
                if 'updates' in nxt or nxt.startswith('(cid') or nxt.startswith('•'):
                    projects.append({'Project_Name': ln, 'status': status.lower(), 'section':'capital'})

# Also parse Disaster Recovery Projects sections if they include completed; focus is parks so capital likely.

# Derive topic park-related by name containing park/playground/bluffs/legacy
for p in projects:
    name_l = p['Project_Name'].lower()
    p['is_park_related'] = bool(re.search(r"\bpark\b|playground|bluffs|skate|legacy park", name_l))

# Determine completion year from any occurrences near project? Using overall docs: for completed projects, infer year from 'completed' sentences include month/year.
# We'll look for sentences containing project name and 'completed' and '2022' in full text.
for p in projects:
    p['completed_2022'] = False

for d in docs:
    text = d.get('text','')
    low = text.lower()
    for p in projects:
        if not p['is_park_related']:
            continue
        nm = p['Project_Name']
        nml = nm.lower()
        if nml in low:
            # window around name
            idx = low.find(nml)
            window = low[max(0, idx-400): idx+800]
            if 'completed' in window and '2022' in window:
                p['completed_2022'] = True

# In addition, some docs list as Construction and say completed Nov 2022. Include those even if status not completed.
# We'll include any park-related project with completion mention 2022.
park_completed_names = sorted({p['Project_Name'] for p in projects if p['is_park_related'] and p['completed_2022']})

fund = load_mongo(var_call_lHgXzv8V5PNkATE07UWgYxoP)
df_f = pd.DataFrame(fund)
if not df_f.empty:
    df_f['total_amount'] = pd.to_numeric(df_f['total_amount'])

# Sum funding for matched projects
matched = df_f[df_f['Project_Name'].isin(park_completed_names)]

total = int(matched['total_amount'].sum()) if not matched.empty else 0

out = {'total_funding': total, 'projects': park_completed_names, 'matched_funding_rows': matched.to_dict(orient='records')}
print('__RESULT__:')
print(json.dumps(out))"""

env_args = {'var_call_33hmIpX4fm9R354cWlcPlxP0': ['Funding'], 'var_call_9hYeWZ1GktsnA3KhmBLFySCc': ['civic_docs'], 'var_call_ZUCDDdG0SXoMt4kmuU3viNnj': 'file_storage/call_ZUCDDdG0SXoMt4kmuU3viNnj.json', 'var_call_lHgXzv8V5PNkATE07UWgYxoP': 'file_storage/call_lHgXzv8V5PNkATE07UWgYxoP.json'}

exec(code, env_args)
