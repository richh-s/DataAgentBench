code = """import json, re, pandas as pd

def load_records(var):
    if isinstance(var, str) and var.endswith('.json'):
        with open(var, 'r', encoding='utf-8') as f:
            return json.load(f)
    return var

docs = load_records(var_call_fYlaQCxbC6gvt3xOxDbOMMVZ)
fund = load_records(var_call_etwHBg5WL34MY8Y6fOzBJa0F)

# Build funding map
fund_map = {}
for r in fund:
    try:
        amt = int(r['Total_Amount'])
    except Exception:
        amt = 0
    fund_map[r['Project_Name']] = amt

park_completed_2022 = set()

# Heuristic parsing for projects in text blocks
for d in docs:
    text = d.get('text','')
    # quick filter: only consider docs mentioning 2022 and completed and park
    if '2022' not in text or 'completed' not in text.lower() or 'park' not in text.lower():
        continue

    lines = [ln.strip() for ln in text.splitlines()]
    # find sections where updates contain completed and schedule contains 2022 or completion in 2022
    for i, ln in enumerate(lines):
        if not ln:
            continue
        # detect a candidate project name line: not bullet, not header, limited length
        if len(ln) > 2 and len(ln) < 120 and not ln.lower().startswith(('page','agenda','item','to:','prepared','approved','date','meeting','subject','recommended','discussion','capital improvement','disaster recovery','project schedule','updates','estimated schedule')):
            # If line includes park keyword
            if re.search(r'\bpark\b', ln, flags=re.IGNORECASE):
                # scan next ~25 lines for completion info with 2022
                window = '\n'.join(lines[i:i+30])
                if re.search(r'completed\s+\w+\s*2022', window, flags=re.IGNORECASE) or re.search(r'completed\s*,?\s*\w+\s*2022', window, flags=re.IGNORECASE) or re.search(r'construction\s+was\s+completed\s+\w+\s*2022', window, flags=re.IGNORECASE) or re.search(r'complete\s+construction\s*:\s*.*2022', window, flags=re.IGNORECASE) or re.search(r'completed\s+in\s+2022', window, flags=re.IGNORECASE):
                    park_completed_2022.add(ln)

# Sum funding for these projects (exact match)
total = sum(fund_map.get(name, 0) for name in park_completed_2022)

out = {
    'total_funding_completed_2022_park_related': total,
    'matched_project_count': len(park_completed_2022),
    'matched_projects': sorted(list(park_completed_2022))
}

print('__RESULT__:')
print(json.dumps(out))"""

env_args = {'var_call_6BNQfQ3PAhFsDjXvqPUGsuWn': ['Funding'], 'var_call_lcQWSl1OPhYFV2OKomSr07FD': ['civic_docs'], 'var_call_fYlaQCxbC6gvt3xOxDbOMMVZ': 'file_storage/call_fYlaQCxbC6gvt3xOxDbOMMVZ.json', 'var_call_etwHBg5WL34MY8Y6fOzBJa0F': 'file_storage/call_etwHBg5WL34MY8Y6fOzBJa0F.json'}

exec(code, env_args)
