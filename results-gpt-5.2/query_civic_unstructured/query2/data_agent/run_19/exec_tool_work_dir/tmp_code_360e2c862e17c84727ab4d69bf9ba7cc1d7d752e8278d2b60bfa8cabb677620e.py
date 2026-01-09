code = """import json, re

def load_records(var):
    if isinstance(var, str) and var.endswith('.json'):
        with open(var, 'r', encoding='utf-8') as f:
            return json.load(f)
    return var

docs = load_records(var_call_fYlaQCxbC6gvt3xOxDbOMMVZ)
fund = load_records(var_call_etwHBg5WL34MY8Y6fOzBJa0F)

fund_map = {}
for r in fund:
    try:
        amt = int(r.get('Total_Amount', 0))
    except Exception:
        amt = 0
    fund_map[r.get('Project_Name')] = amt

park_completed_2022 = set()

for d in docs:
    text = d.get('text','')
    low = text.lower()
    if '2022' not in text or 'completed' not in low or 'park' not in low:
        continue
    lines = [ln.strip() for ln in text.splitlines()]
    for i, ln in enumerate(lines):
        if not ln:
            continue
        lln = ln.lower()
        if len(ln) < 3 or len(ln) > 140:
            continue
        if lln.startswith(('page','agenda','item','to:','prepared','approved','date','meeting','subject','recommended','discussion','capital improvement','disaster recovery','project schedule','updates','estimated schedule')):
            continue
        if re.search(r'\bpark\b', ln, flags=re.IGNORECASE):
            window = '\n'.join(lines[i:i+35])
            if re.search(r'construction\s+was\s+completed\s+[^\n]*2022', window, flags=re.IGNORECASE) or re.search(r'completed\s+[^\n]*2022', window, flags=re.IGNORECASE) or re.search(r'complete\s+construction\s*:\s*[^\n]*2022', window, flags=re.IGNORECASE):
                park_completed_2022.add(ln)

total = sum(fund_map.get(name, 0) for name in park_completed_2022 if name in fund_map)

out = {
    'total_funding_completed_2022_park_related': total,
    'matched_project_count': len([n for n in park_completed_2022 if n in fund_map]),
    'matched_projects': sorted([n for n in park_completed_2022 if n in fund_map])
}

print('__RESULT__:')
print(json.dumps(out))"""

env_args = {'var_call_6BNQfQ3PAhFsDjXvqPUGsuWn': ['Funding'], 'var_call_lcQWSl1OPhYFV2OKomSr07FD': ['civic_docs'], 'var_call_fYlaQCxbC6gvt3xOxDbOMMVZ': 'file_storage/call_fYlaQCxbC6gvt3xOxDbOMMVZ.json', 'var_call_etwHBg5WL34MY8Y6fOzBJa0F': 'file_storage/call_etwHBg5WL34MY8Y6fOzBJa0F.json'}

exec(code, env_args)
