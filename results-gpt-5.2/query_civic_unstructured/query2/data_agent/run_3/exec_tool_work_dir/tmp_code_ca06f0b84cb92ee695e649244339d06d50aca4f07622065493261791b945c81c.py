code = """import json, re, pandas as pd

# load civic docs
civic_src = var_call_Zj7izuAdJg70VarE2FUTw5PV
if isinstance(civic_src, str) and civic_src.endswith('.json'):
    with open(civic_src, 'r', encoding='utf-8') as f:
        civic_docs = json.load(f)
else:
    civic_docs = civic_src

# load funding grouped totals
fund_src = var_call_5sEAXb97vC8e9fiBLFNcSwZd
if isinstance(fund_src, str) and fund_src.endswith('.json'):
    with open(fund_src, 'r', encoding='utf-8') as f:
        fund_rows = json.load(f)
else:
    fund_rows = fund_src

fund_df = pd.DataFrame(fund_rows)
if not fund_df.empty:
    fund_df['Total_Amount'] = pd.to_numeric(fund_df['Total_Amount'])

# Identify park-related completed in 2022 projects by scanning documents
# Heuristic: a section line (project name) followed by an 'Updates' block containing 'completed' and '2022'
# and project name itself contains 'Park' or 'Bluffs Park' or 'Playground' or other park keywords.
park_kw = re.compile(r'\bpark\b|playground|skate\s*park|bluffs\s*park|legacy\s*park', re.I)
completed_2022_kw = re.compile(r'completed', re.I)
y2022_kw = re.compile(r'2022')

projects=set()

# parse candidate project headings: lines with Title Case and not bullet lines
for doc in civic_docs:
    text = doc.get('text','')
    if not text:
        continue
    lines = [ln.strip() for ln in text.splitlines()]
    for i, ln in enumerate(lines):
        if not ln or len(ln) > 120:
            continue
        if ln.startswith(('(', 'cid', 'Page', 'Agenda', 'To:', 'Prepared', 'Approved', 'Date', 'Meeting', 'Subject', 'RECOMMENDED', 'DISCUSSION', 'Capital', 'Storm', 'Project', 'Updates', 'Estimated', 'Complete', 'Begin', 'Advertise')):
            continue
        # keep lines with letters and spaces and some punctuation
        if re.fullmatch(r"[A-Za-z0-9&\-\/'\(\)\s\.]+", ln) is None:
            continue
        if not park_kw.search(ln):
            continue
        # window of next 12 lines
        window = "\n".join(lines[i:i+15])
        if completed_2022_kw.search(window) and y2022_kw.search(window):
            projects.add(ln)

# also catch instances like 'Construction was completed November 2022' under a heading that may not include park keyword
# We'll search for completed Nov 2022 lines and look back for nearest heading containing park keyword within 10 lines
for doc in civic_docs:
    text = doc.get('text','')
    lines = [ln.strip() for ln in text.splitlines()]
    for i, ln in enumerate(lines):
        if 'completed' in ln.lower() and '2022' in ln:
            # look back
            for j in range(max(0,i-10), i):
                h = lines[j]
                if park_kw.search(h) and re.fullmatch(r"[A-Za-z0-9&\-\/'\(\)\s\.]+", h or ''):
                    projects.add(h)

projects_list = sorted(projects)

# Join with funding totals for these projects (exact match)
if fund_df.empty:
    total = 0
    matched=[]
else:
    matched_df = fund_df[fund_df['Project_Name'].isin(projects_list)].copy()
    total = int(matched_df['Total_Amount'].sum())
    matched = matched_df.sort_values('Project_Name')[['Project_Name','Total_Amount']].to_dict(orient='records')

out = {
    'park_completed_2022_projects': projects_list,
    'matched_funding_rows': matched,
    'total_funding': total
}

print('__RESULT__:')
print(json.dumps(out))"""

env_args = {'var_call_FqGqUBynRMTN7hnb6BMaKmbM': ['Funding'], 'var_call_JaXA1PXUx5YjvhO7ozSmjRfS': ['civic_docs'], 'var_call_Zj7izuAdJg70VarE2FUTw5PV': 'file_storage/call_Zj7izuAdJg70VarE2FUTw5PV.json', 'var_call_5sEAXb97vC8e9fiBLFNcSwZd': 'file_storage/call_5sEAXb97vC8e9fiBLFNcSwZd.json'}

exec(code, env_args)
