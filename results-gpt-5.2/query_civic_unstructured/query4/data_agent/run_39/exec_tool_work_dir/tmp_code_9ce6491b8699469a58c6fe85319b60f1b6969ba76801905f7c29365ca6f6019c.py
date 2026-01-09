code = """import json, re, pandas as pd

# Load civic docs query result
path_docs = var_call_doDJq1s9rwUWUOVU3na3B1gf
with open(path_docs, 'r', encoding='utf-8') as f:
    docs = json.load(f)

# Load funding totals per project
path_fund = var_call_SGs0mH129VnZcNiI76ckFcuz
with open(path_fund, 'r', encoding='utf-8') as f:
    fund = json.load(f)

fund_df = pd.DataFrame(fund)
if not fund_df.empty:
    fund_df['Total_Amount'] = pd.to_numeric(fund_df['Total_Amount'], errors='coerce').fillna(0).astype('int64')
fund_map = dict(zip(fund_df['Project_Name'], fund_df['Total_Amount']))

# Parse projects that started in Spring 2022.
# Heuristic: identify project name lines, then within that project block find 'Begin ...: Spring 2022'
start_pat = re.compile(r'\bBegin\s+(?:Construction|Design)\s*:\s*Spring\s*2022\b', re.IGNORECASE)
# project name line: a non-empty line not starting with bullets and not a header, followed by blank line
name_pat = re.compile(r'^[A-Z0-9][A-Za-z0-9\(\)\-\/,\&\s]{2,}$')

projects = set()

for d in docs:
    text = d.get('text','')
    lines = [ln.strip() for ln in text.splitlines()]
    # locate indices with start phrase
    idxs = [i for i,ln in enumerate(lines) if start_pat.search(ln)]
    for i in idxs:
        # search upward for nearest plausible project name line
        name = None
        for j in range(i-1, max(-1,i-80), -1):
            ln = lines[j]
            if not ln:
                continue
            if 'Project Schedule' in ln or 'Estimated Schedule' in ln or 'Updates' in ln or 'Project Description' in ln:
                continue
            if ln.startswith(('(cid', 'Page', 'Agenda', 'Capital', 'Disaster', 'RECOMMENDED', 'DISCUSSION', 'To:', 'Prepared', 'Approved', 'Date prepared', 'Meeting date', 'Subject')):
                continue
            if name_pat.match(ln):
                # avoid generic labels
                if ln.lower() in {'project schedule','estimated schedule','updates','discussion','recommended action'}:
                    continue
                name = ln
                break
        if name:
            projects.add(name)

# Sum funding for those projects (exact match)
amounts = {p: int(fund_map.get(p, 0)) for p in sorted(projects)}
count = len(projects)
total = int(sum(amounts.values()))

out = {
    "spring_2022_started_projects_count": count,
    "total_funding_usd": total,
    "matched_projects": [{"Project_Name": p, "Funding_USD": amounts[p]} for p in sorted(projects)]
}

print('__RESULT__:')
print(json.dumps(out))"""

env_args = {'var_call_XtEzw5AyTsnXaaX8ijHhlrwl': ['Funding'], 'var_call_rb6ikrCfiVg35rh8JoXlANJh': ['civic_docs'], 'var_call_doDJq1s9rwUWUOVU3na3B1gf': 'file_storage/call_doDJq1s9rwUWUOVU3na3B1gf.json', 'var_call_SGs0mH129VnZcNiI76ckFcuz': 'file_storage/call_SGs0mH129VnZcNiI76ckFcuz.json'}

exec(code, env_args)
