code = """import json, re

# load funding per project
path_funding = var_call_UCppypxJ9ivCqpPzCKPpOdD5
with open(path_funding, 'r') as f:
    funding = json.load(f)
fund_map = {r['Project_Name']: int(r['total_amount']) for r in funding}

# load civic docs
path_docs = var_call_KrRlBWaEoRWzCOYEfmvlQflO
with open(path_docs, 'r') as f:
    docs = json.load(f)

# helper: extract disaster section projects with start containing 2022
projects_2022 = set()
for d in docs:
    text = d.get('text','')
    # locate disaster section
    m = re.search(r"Disaster Recovery Projects.*?(?:(?:\n\s*Page\s+\d+\s+of\s+\d+)|\Z)", text, flags=re.I|re.S)
    section = m.group(0) if m else text
    # split lines
    lines = [ln.strip() for ln in section.splitlines()]
    # iterate and detect project names as standalone non-bullet lines (no colon, not headers)
    current_project = None
    st_has_2022 = False
    for ln in lines:
        if not ln:
            continue
        # stop at next major header
        if re.match(r"Capital Improvement Projects", ln, flags=re.I):
            continue
        if re.match(r"Disaster Recovery Projects\b", ln, flags=re.I):
            continue
        if re.match(r"\(cid:|Agenda Item|Page \d+ of \d+|RECOMMENDED ACTION|DISCUSSION|Subject:|To:|Prepared by:|Approved by:|Date prepared:|Meeting date:", ln, flags=re.I):
            continue
        # detect schedule lines
        if 'Begin Construction' in ln or re.search(r"\bBegin\b", ln) and 'Construction' in ln:
            if '2022' in ln:
                st_has_2022 = True
        if 'Project Schedule' in ln or 'Estimated Schedule' in ln:
            continue
        # project name line heuristic: line without ':' and not starting with bullet and has letters
        if ':' not in ln and not ln.startswith(('-', '•','(cid')) and re.search(r"[A-Za-z]", ln):
            # if line looks like a project name (not Updates)
            if ln.lower() not in ['updates','project description','project updates'] and 'Updates' not in ln and 'Project Schedule' not in ln:
                # commit previous
                if current_project and st_has_2022:
                    projects_2022.add(current_project)
                current_project = ln
                st_has_2022 = False
                continue
    if current_project and st_has_2022:
        projects_2022.add(current_project)

# Sum funding for those projects that exist in Funding table
matched = [(p, fund_map[p]) for p in sorted(projects_2022) if p in fund_map]
total = sum(a for _,a in matched)

out = {
    'total_funding': total,
    'currency': 'USD',
    'matched_projects_count': len(matched),
    'matched_projects': matched
}

print('__RESULT__:')
print(json.dumps(out))"""

env_args = {'var_call_1RXUbsill3cgLaz2LBxIQUhK': ['Funding'], 'var_call_UCppypxJ9ivCqpPzCKPpOdD5': 'file_storage/call_UCppypxJ9ivCqpPzCKPpOdD5.json', 'var_call_KrRlBWaEoRWzCOYEfmvlQflO': 'file_storage/call_KrRlBWaEoRWzCOYEfmvlQflO.json'}

exec(code, env_args)
