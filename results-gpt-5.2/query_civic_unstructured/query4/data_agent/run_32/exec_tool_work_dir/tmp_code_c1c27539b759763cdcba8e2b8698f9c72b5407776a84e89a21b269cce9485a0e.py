code = """import json, re
import pandas as pd

def load_records(maybe_path):
    if isinstance(maybe_path, str) and maybe_path.endswith('.json'):
        with open(maybe_path, 'r', encoding='utf-8') as f:
            return json.load(f)
    return maybe_path

docs = load_records(var_call_FbPs2UpiOvBqbJZlsxBx3bFx)
fund = load_records(var_call_soeirc9Z1ELJ01wWJlLpA9jV)
fund_map = {r['Project_Name']: float(r['total_amount']) for r in fund}

projects = []
for d in docs:
    text = d.get('text','')
    lines = [ln.strip() for ln in text.splitlines()]
    for i, ln in enumerate(lines):
        if not ln or len(ln) > 140:
            continue
        if ln.endswith(':'):
            continue
        if ln.lower() in {'updates','project schedule','estimated schedule','project description','project updates','discussion','recommended action'}:
            continue
        if re.search(r'^(page \d+ of \d+|agenda item|to:|prepared by:|approved by:|date prepared|meeting date|subject:)$', ln, re.I):
            continue
        window = "\n".join(lines[i:i+40])
        if re.search(r'Project Schedule', window, re.I) and re.search(r'Begin( Construction)?:\s*Spring\s+2022', window, re.I):
            projects.append(ln)

proj_unique = sorted(set(projects))
matched = [p for p in proj_unique if p in fund_map]

total_funding = sum(fund_map[p] for p in matched)

result = {
    'projects_started_spring_2022_count': len(proj_unique),
    'projects_with_funding_match_count': len(matched),
    'total_funding_matched_usd': int(total_funding),
    'projects_started_spring_2022': proj_unique,
    'funding_matched_by_project': [{"Project_Name": p, "Funding_USD": int(fund_map[p])} for p in matched]
}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_call_FbPs2UpiOvBqbJZlsxBx3bFx': 'file_storage/call_FbPs2UpiOvBqbJZlsxBx3bFx.json', 'var_call_soeirc9Z1ELJ01wWJlLpA9jV': 'file_storage/call_soeirc9Z1ELJ01wWJlLpA9jV.json'}

exec(code, env_args)
