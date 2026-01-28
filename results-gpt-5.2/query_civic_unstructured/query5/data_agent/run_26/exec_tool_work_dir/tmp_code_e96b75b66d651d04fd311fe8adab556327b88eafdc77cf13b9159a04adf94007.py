code = """import json, re

path_funding = var_call_UCppypxJ9ivCqpPzCKPpOdD5
with open(path_funding, 'r') as f:
    funding = json.load(f)
fund_map = {r['Project_Name']: int(r['total_amount']) for r in funding}

path_docs = var_call_KrRlBWaEoRWzCOYEfmvlQflO
with open(path_docs, 'r') as f:
    docs = json.load(f)

projects_2022 = set()
ignore_pat = re.compile(r"^(\(cid:|Agenda Item|Page \d+ of \d+|RECOMMENDED ACTION|DISCUSSION|Subject:|To:|Prepared by:|Approved by:|Date prepared:|Meeting date:)", re.I)

for d in docs:
    text = d.get('text','')
    m = re.search(r"Disaster Recovery Projects.*?(?:(?:\n\s*Page\s+\d+\s+of\s+\d+)|\Z)", text, flags=re.I|re.S)
    section = m.group(0) if m else text
    lines = [ln.strip() for ln in section.splitlines()]

    current_project = None
    st_has_2022 = False

    for ln in lines:
        if not ln:
            continue
        if ignore_pat.match(ln):
            continue
        if re.match(r"Capital Improvement Projects", ln, re.I):
            continue
        if re.match(r"Disaster Recovery Projects\b", ln, re.I):
            continue

        if "Begin Construction" in ln and "2022" in ln:
            st_has_2022 = True

        if ':' not in ln and not ln.startswith(('-', '•')) and re.search(r"[A-Za-z]", ln):
            if ln.lower() in ["updates", "project description", "project updates"]:
                continue
            if "Project Schedule" in ln or "Estimated Schedule" in ln:
                continue
            if "Updates" in ln:
                continue

            if current_project and st_has_2022:
                projects_2022.add(current_project)
            current_project = ln
            st_has_2022 = False

    if current_project and st_has_2022:
        projects_2022.add(current_project)

matched = [(p, fund_map[p]) for p in sorted(projects_2022) if p in fund_map]
total = sum(a for _, a in matched)

out = {"total_funding": total, "currency": "USD", "matched_projects_count": len(matched), "matched_projects": matched}

print('__RESULT__:')
print(json.dumps(out))"""

env_args = {'var_call_1RXUbsill3cgLaz2LBxIQUhK': ['Funding'], 'var_call_UCppypxJ9ivCqpPzCKPpOdD5': 'file_storage/call_UCppypxJ9ivCqpPzCKPpOdD5.json', 'var_call_KrRlBWaEoRWzCOYEfmvlQflO': 'file_storage/call_KrRlBWaEoRWzCOYEfmvlQflO.json'}

exec(code, env_args)
