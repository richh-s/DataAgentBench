code = """import json, re, pandas as pd

# Load funding per project
funding_path = var_call_POnMSnCxvKJodwURvENF1OP4
with open(funding_path, 'r', encoding='utf-8') as f:
    funding = json.load(f)
fund_df = pd.DataFrame(funding)
fund_df['total_amount'] = pd.to_numeric(fund_df['total_amount'])

# Load civic docs
docs_path = var_call_IegVeO7iEQ8LuDVQdQO2qcWC
with open(docs_path, 'r', encoding='utf-8') as f:
    docs = json.load(f)

# Heuristic extraction from status reports: find Disaster Recovery Projects section and parse names + optional schedule lines

def extract_disaster_projects_started_2022(text):
    out = []
    # locate disaster section
    m = re.search(r"Disaster Recovery Projects Status\s*Report|Disaster Recovery Projects", text, flags=re.I)
    if not m:
        return out
    # take tail from first mention
    tail = text[m.start():]
    # stop at next major section if present
    # We'll keep whole tail.
    lines = [ln.strip() for ln in tail.splitlines()]
    current = None
    started_2022 = set()

    # project name lines are usually standalone without bullets, and not headings
    heading_patterns = re.compile(r"^(Disaster Recovery Projects|Capital Improvement Projects|Page \d+ of \d+|Agenda Item|RECOMMENDED ACTION|DISCUSSION|Project Schedule|Updates|Project Description|Estimated Schedule|\(cid:|To:|Prepared by:|Approved by:|Date prepared|Meeting date|Subject:)\b", re.I)

    for i, ln in enumerate(lines):
        if not ln:
            continue
        if heading_patterns.search(ln):
            continue
        # likely a project name if it has letters and no colon and is not too long
        if ':' in ln:
            continue
        if len(ln) > 120:
            continue
        # ignore common words
        if ln.lower() in {'updates', 'project schedule', 'estimated schedule'}:
            continue
        # detect schedule lines following containing begin/start
        # if this line looks like a project name, set current
        # project names often have Title Case and words like Road, Culvert, Repairs, (FEMA Project)
        if re.search(r"[A-Za-z]", ln) and not re.match(r"^\d+[\.)]", ln):
            current = ln
            # check subsequent few lines for Begin Construction/Start/etc containing 2022
            window = " \n".join(lines[i:i+8])
            if re.search(r"\b(Begin|Start)(?:\s+\w+){0,3}\s+(?:Construction|Design)?\s*:?\s*.*2022", window, flags=re.I) or re.search(r"\b2022\b", window) and re.search(r"\b(Begin|Start)\b", window, flags=re.I):
                started_2022.add(current)
    return list(started_2022)

started_2022_projects = set()
for d in docs:
    txt = d.get('text','')
    for p in extract_disaster_projects_started_2022(txt):
        started_2022_projects.add(p)

# If heuristic fails, fallback: any project with FEMA/CalOES/CalJPIA in name and a nearby 'Start'/'Begin' in 2022
if not started_2022_projects:
    for d in docs:
        txt = d.get('text','')
        if '2022' not in txt:
            continue
        for m in re.finditer(r"\n([A-Z][^\n]{3,100}?(?:\(FEMA[^\)]*\)|\(CalOES[^\)]*\)|\(CalJPIA[^\)]*\)))\s*\n", txt):
            name = m.group(1).strip()
            ctx = txt[m.start():m.start()+600]
            if re.search(r"\b(Begin|Start)\b[^\n]*2022", ctx, flags=re.I):
                started_2022_projects.add(name)

# Join with funding totals by exact Project_Name match
fund_started = fund_df[fund_df['Project_Name'].isin(started_2022_projects)].copy()

total_funding = int(fund_started['total_amount'].sum())

result = {
    "total_funding": total_funding,
    "num_projects": int(fund_started.shape[0]),
    "projects": fund_started.sort_values('total_amount', ascending=False).to_dict(orient='records')
}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_call_POnMSnCxvKJodwURvENF1OP4': 'file_storage/call_POnMSnCxvKJodwURvENF1OP4.json', 'var_call_IegVeO7iEQ8LuDVQdQO2qcWC': 'file_storage/call_IegVeO7iEQ8LuDVQdQO2qcWC.json'}

exec(code, env_args)
