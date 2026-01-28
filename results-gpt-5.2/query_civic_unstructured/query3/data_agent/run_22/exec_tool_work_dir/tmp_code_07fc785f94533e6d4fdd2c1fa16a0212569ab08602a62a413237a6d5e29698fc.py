code = """import json, re, pandas as pd

# Load civic docs (may be file path)
docs = var_call_0NxPrbwyuGdFf83H0WzG8QVN
if isinstance(docs, str) and docs.endswith('.json'):
    with open(docs, 'r', encoding='utf-8') as f:
        docs = json.load(f)

fund = var_call_OFVqNgOlPQ2HaSZl0rQqIF7N
if isinstance(fund, str) and fund.endswith('.json'):
    with open(fund, 'r', encoding='utf-8') as f:
        fund = json.load(f)

# Parse project statuses from documents: look for headings and project blocks with 'Updates:'
status_map = {}

# helper to infer status from nearby section heading
section_to_status = {
    'design':'design',
    'construction':'design',
    'not started':'not started',
    'completed':'completed'
}

for d in docs:
    text = d.get('text','')
    # normalize
    lines = [ln.strip() for ln in text.splitlines()]
    current_status = None
    for i, ln in enumerate(lines):
        lnl = ln.lower()
        if 'capital improvement projects' in lnl or 'disaster recovery projects' in lnl:
            # do nothing
            pass
        # detect status section headings
        m = re.search(r'\b(Design|Construction|Not Started|Completed)\b', ln)
        if m and ('Capital Improvement Projects' in ln or ln.strip() in ['Capital Improvement Projects (Design)','Capital Improvement Projects (Construction)','Capital Improvement Projects (Not Started)','Disaster Recovery Projects (Design)','Disaster Recovery Projects (Construction)','Disaster Recovery Projects (Not Started)','Disaster Recovery Projects (Completed)']):
            current_status = section_to_status.get(m.group(1).lower(), current_status)

        # detect project name line: a non-empty line followed by 'Updates:' within next 3 lines
        if ln and (i+1) < len(lines):
            # skip obvious non-project lines
            if any(k in lnl for k in ['agenda', 'page ', 'item', 'recommended action', 'discussion', 'project schedule', 'updates:', 'estimated schedule', 'project description']):
                continue
            nxt = '\n'.join(lines[i+1:i+4]).lower()
            if 'updates' in nxt:
                pname = ln
                # reduce artifacts
                pname = re.sub(r'\s{2,}',' ',pname).strip()
                # keep only plausible names
                if len(pname) >= 4 and len(pname) <= 120:
                    status_map.setdefault(pname, current_status)

# Build funding df and filter to emergency/FEMA related projects
fdf = pd.DataFrame(fund)
# ensure numeric amount
if 'Amount' in fdf.columns:
    fdf['Amount'] = pd.to_numeric(fdf['Amount'], errors='coerce')

mask = fdf['Project_Name'].str.contains(r'(FEMA|Emergency)', case=False, na=False) | fdf['Funding_Source'].str.contains(r'(FEMA|Emergency)', case=False, na=False)
rel = fdf[mask].copy()

# attach status via exact match, else try fuzzy by stripping suffixes in parentheses

def canon(name):
    return re.sub(r'\s*\([^)]*\)\s*','', name).strip().lower()

canon_to_status = {}
for k,v in status_map.items():
    canon_to_status.setdefault(canon(k), v)

statuses = []
for pn in rel['Project_Name'].fillna(''):
    st = status_map.get(pn)
    if st is None:
        st = canon_to_status.get(canon(pn))
    statuses.append(st)
rel['Status'] = statuses

# Keep relevant columns and sort
out = rel[['Project_Name','Funding_Source','Amount','Status']].sort_values(['Project_Name','Funding_Source']).reset_index(drop=True)

# Convert to plain text table
out_fill = out.fillna('')
# format amount
out_fill['Amount'] = out_fill['Amount'].apply(lambda x: '' if pd.isna(x) else f"${int(x):,}")

# produce output records
records = out_fill.to_dict(orient='records')

print('__RESULT__:')
print(json.dumps(records))"""

env_args = {'var_call_0NxPrbwyuGdFf83H0WzG8QVN': 'file_storage/call_0NxPrbwyuGdFf83H0WzG8QVN.json', 'var_call_OFVqNgOlPQ2HaSZl0rQqIF7N': 'file_storage/call_OFVqNgOlPQ2HaSZl0rQqIF7N.json'}

exec(code, env_args)
