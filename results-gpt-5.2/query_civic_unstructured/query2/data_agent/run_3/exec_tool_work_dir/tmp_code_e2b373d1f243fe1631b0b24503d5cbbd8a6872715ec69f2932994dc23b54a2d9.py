code = """import json, re, pandas as pd

civic_src = var_call_Zj7izuAdJg70VarE2FUTw5PV
if isinstance(civic_src, str) and civic_src.endswith('.json'):
    with open(civic_src, 'r', encoding='utf-8') as f:
        civic_docs = json.load(f)
else:
    civic_docs = civic_src

fund_src = var_call_5sEAXb97vC8e9fiBLFNcSwZd
if isinstance(fund_src, str) and fund_src.endswith('.json'):
    with open(fund_src, 'r', encoding='utf-8') as f:
        fund_rows = json.load(f)
else:
    fund_rows = fund_src

fund_df = pd.DataFrame(fund_rows)
if not fund_df.empty:
    fund_df['Total_Amount'] = pd.to_numeric(fund_df['Total_Amount'])

park_kw = re.compile(r'\bpark\b|playground|skate\s*park|bluffs\s*park|legacy\s*park', re.I)
completed_kw = re.compile(r'completed', re.I)
y2022_kw = re.compile(r'2022')

projects=set()

def is_heading(line: str) -> bool:
    if not line or len(line) > 140:
        return False
    bad_starts = ('(', 'cid', 'Page', 'Agenda', 'To:', 'Prepared', 'Approved', 'Date', 'Meeting', 'Subject',
                  'RECOMMENDED', 'DISCUSSION', 'Capital', 'Storm', 'Project', 'Updates', 'Estimated',
                  'Complete', 'Begin', 'Advertise')
    if line.startswith(bad_starts):
        return False
    return re.fullmatch(r"[A-Za-z0-9&\-\/'\(\)\s\.]+", line) is not None

for doc in civic_docs:
    text = doc.get('text','') or ''
    if not text:
        continue
    lines = [ln.strip() for ln in text.splitlines()]
    for i, ln in enumerate(lines):
        if not is_heading(ln):
            continue
        if not park_kw.search(ln):
            continue
        window = "\n".join(lines[i:i+15])
        if completed_kw.search(window) and y2022_kw.search(window):
            projects.add(ln)

for doc in civic_docs:
    text = doc.get('text','') or ''
    lines = [ln.strip() for ln in text.splitlines()]
    for i, ln in enumerate(lines):
        if 'completed' in ln.lower() and '2022' in ln:
            for j in range(max(0, i-10), i):
                h = lines[j]
                if is_heading(h) and park_kw.search(h):
                    projects.add(h)

projects_list = sorted(projects)

matched=[]
if not fund_df.empty and projects_list:
    matched_df = fund_df[fund_df['Project_Name'].isin(projects_list)].copy()
    total = int(matched_df['Total_Amount'].sum())
    matched = matched_df.sort_values('Project_Name')[['Project_Name','Total_Amount']].to_dict(orient='records')
else:
    total = 0

out = {'park_completed_2022_projects': projects_list,
       'matched_funding_rows': matched,
       'total_funding': total}

print('__RESULT__:')
print(json.dumps(out))"""

env_args = {'var_call_FqGqUBynRMTN7hnb6BMaKmbM': ['Funding'], 'var_call_JaXA1PXUx5YjvhO7ozSmjRfS': ['civic_docs'], 'var_call_Zj7izuAdJg70VarE2FUTw5PV': 'file_storage/call_Zj7izuAdJg70VarE2FUTw5PV.json', 'var_call_5sEAXb97vC8e9fiBLFNcSwZd': 'file_storage/call_5sEAXb97vC8e9fiBLFNcSwZd.json'}

exec(code, env_args)
