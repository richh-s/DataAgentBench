code = """import json, re, pandas as pd

def load_records(maybe_path_or_list):
    if isinstance(maybe_path_or_list, str) and maybe_path_or_list.endswith('.json'):
        with open(maybe_path_or_list, 'r', encoding='utf-8') as f:
            return json.load(f)
    return maybe_path_or_list

docs = load_records(var_call_zx7EwMgF9LnPQvNwKoE3ceX4)
fund = load_records(var_call_4DE6bKcGZYB2eTT9vOkVesJT)

# Build funding map
fund_map = {}
for r in fund:
    name = r.get('Project_Name')
    if name is None: 
        continue
    amt = r.get('total_amount')
    try:
        amt_i = int(amt)
    except Exception:
        try:
            amt_i = int(float(amt))
        except Exception:
            amt_i = 0
    fund_map[name.strip()] = amt_i

spring2022_projects = set()

# Heuristic parsing: in these agenda reports, projects appear as standalone lines.
# We consider a project 'started in Spring 2022' if within its nearby context we see 'Start'/'Begin' with 'Spring 2022' or schedule line 'Start: Spring 2022'.
# We'll scan line by line, keep current candidate project heading.
start_pat = re.compile(r'\b(start|begin|started|begin construction|start construction)\b', re.I)
season_pat = re.compile(r'\bSpring\s+2022\b', re.I)

for d in docs:
    text = d.get('text','') or ''
    lines = [re.sub(r'\s+', ' ', ln).strip() for ln in text.splitlines()]
    lines = [ln for ln in lines if ln]
    current_project = None
    for i, ln in enumerate(lines):
        # detect project headings: must match a known funded project name exactly
        if ln in fund_map:
            current_project = ln
        # if schedule line mentions Spring 2022 and start/begin, attribute to current_project if exists
        if season_pat.search(ln) and (start_pat.search(ln) or 'Project Schedule' in ln or 'Estimated Schedule' in ln or 'Schedule' in ln):
            if current_project:
                spring2022_projects.add(current_project)
        # also check window +/-2 lines when line is exactly 'Spring 2022'
        if season_pat.search(ln) and not start_pat.search(ln):
            window = ' '.join(lines[max(0,i-2):min(len(lines), i+3)])
            if start_pat.search(window) and current_project:
                spring2022_projects.add(current_project)

# compute totals
count = len(spring2022_projects)
amount_total = sum(fund_map.get(p,0) for p in spring2022_projects)

out = {
    "spring_2022_project_count": count,
    "spring_2022_total_funding": amount_total,
    "projects": sorted(spring2022_projects)
}
print('__RESULT__:')
print(json.dumps(out))"""

env_args = {'var_call_zx7EwMgF9LnPQvNwKoE3ceX4': 'file_storage/call_zx7EwMgF9LnPQvNwKoE3ceX4.json', 'var_call_4DE6bKcGZYB2eTT9vOkVesJT': 'file_storage/call_4DE6bKcGZYB2eTT9vOkVesJT.json'}

exec(code, env_args)
