code = """import json, re, pandas as pd

# Load civic docs (may be file path)
cd = var_call_rrITK0lUpo5usLSikqQouxYp
if isinstance(cd, str):
    with open(cd, 'r') as f:
        civic_docs = json.load(f)
else:
    civic_docs = cd

# Load funding totals per project
ft = var_call_PSEZSqWmIRPvYkhDRIsKOJ2Z
if isinstance(ft, str):
    with open(ft, 'r') as f:
        funding_totals = json.load(f)
else:
    funding_totals = ft

fund_df = pd.DataFrame(funding_totals)
if not fund_df.empty:
    fund_df['total_amount'] = pd.to_numeric(fund_df['total_amount'])

# Extract disaster projects and start dates from docs
# Heuristic: In sections titled 'Disaster Recovery Projects', each project appears as a standalone line.
# We'll look for patterns like '\n<Project Name>\n\n' followed nearby by 'Start' or 'Begin' schedule lines.

disaster_projects = {}  # name -> set(start_strings)

for doc in civic_docs:
    text = doc.get('text','')
    if not text:
        continue
    # limit to disaster section if present
    idx = text.lower().find('disaster recovery projects')
    if idx == -1:
        continue
    sec = text[idx:]

    # Candidate project names: lines with Title Case words and not bullets, up to 120 chars
    lines = [ln.strip() for ln in sec.splitlines()]
    # collect names that appear as their own line (not empty, not 'Updates', not 'Project Schedule', not 'Disaster Recovery Projects')
    for i, ln in enumerate(lines):
        if not ln or len(ln) > 140:
            continue
        lnl = ln.lower()
        if lnl in ['disaster recovery projects (design)','disaster recovery projects (construction)','disaster recovery projects','disaster recovery projects (not started)']:
            continue
        if 'updates' in lnl or 'project schedule' in lnl or 'project description' in lnl:
            continue
        if ln.startswith('(') or ln.startswith('cid:') or ln.startswith('agenda') or ln.startswith('page'):
            continue
        # likely a project name if contains letters and not too many punctuation and not a sentence
        if re.search(r'[A-Za-z]', ln) and (ln[0].isalpha() or ln[0].isdigit()):
            # avoid common section headers
            if re.match(r'^(to:|prepared by:|approved by:|date prepared:|meeting date:|subject:|recommended action:|discussion:)$', lnl):
                continue
            # avoid list markers
            if re.match(r'^[\-\u2022\*]', ln):
                continue
            # Require at least two words (or contains parentheses typical of disaster suffix)
            if len(ln.split()) < 2 and '(' not in ln:
                continue
            # Look ahead few lines for 'Begin Construction' or 'Start' date; capture year-bearing strings
            window = '\n'.join(lines[i:i+15])
            starts = set()
            for m in re.finditer(r'(Begin Construction|Start(?: Date)?|Begin)\s*:\s*([^\n]+)', window, flags=re.IGNORECASE):
                starts.add(m.group(2).strip())
            # also capture schedule entries without keyword but formatted like 'st:' not present; try 'Project Schedule:' then next lines
            # We'll just look for any '2022' tokens in window lines containing ':'
            for wln in window.split('\n'):
                if '2022' in wln and ':' in wln:
                    # take rhs
                    rhs = wln.split(':',1)[1].strip()
                    if rhs:
                        starts.add(rhs)
            if starts:
                disaster_projects.setdefault(ln, set()).update(starts)

# Filter those with any start containing '2022'
projects_2022 = [name for name, starts in disaster_projects.items() if any('2022' in s for s in starts)]

# Join with funding totals
sel_fund = fund_df[fund_df['Project_Name'].isin(projects_2022)].copy() if not fund_df.empty else pd.DataFrame(columns=['Project_Name','total_amount'])

answer = {
    'total_funding': int(sel_fund['total_amount'].sum()) if not sel_fund.empty else 0,
    'project_count': int(sel_fund.shape[0]),
    'projects': sel_fund.sort_values('total_amount', ascending=False).to_dict(orient='records')
}

print('__RESULT__:')
print(json.dumps(answer))"""

env_args = {'var_call_RvZ50pS5WKtMq9Ygsv93soeX': ['Funding'], 'var_call_lstHaO2T1fNcM1AkXqdQUIcQ': ['civic_docs'], 'var_call_rrITK0lUpo5usLSikqQouxYp': 'file_storage/call_rrITK0lUpo5usLSikqQouxYp.json', 'var_call_PSEZSqWmIRPvYkhDRIsKOJ2Z': 'file_storage/call_PSEZSqWmIRPvYkhDRIsKOJ2Z.json'}

exec(code, env_args)
