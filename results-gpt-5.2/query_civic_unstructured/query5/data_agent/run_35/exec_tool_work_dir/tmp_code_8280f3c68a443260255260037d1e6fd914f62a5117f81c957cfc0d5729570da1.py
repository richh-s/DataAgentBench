code = """import json, re
import pandas as pd

# Load funding totals per project
path_funding = var_call_RulML30xUVm7z6HjS6Vlheqd
with open(path_funding, 'r', encoding='utf-8') as f:
    funding_totals = json.load(f)
fund_df = pd.DataFrame(funding_totals)
if not fund_df.empty:
    fund_df['total_amount'] = pd.to_numeric(fund_df['total_amount'], errors='coerce').fillna(0).astype(int)

# Load relevant civic docs
path_docs = var_call_GnrTK04YJ2K9l5O71wRnwMs4
with open(path_docs, 'r', encoding='utf-8') as f:
    docs = json.load(f)

# Heuristic extraction: parse 'Disaster Recovery Projects' section and capture project names with schedule lines.
# We identify disaster projects by lines that include FEMA/CalOES/CalJPIA or are under the 'Disaster Recovery Projects' header.

def extract_disaster_projects_started_2022(text):
    lines = [ln.strip() for ln in text.splitlines()]
    projects = []
    in_disaster = False
    current = None
    for i, ln in enumerate(lines):
        if re.search(r'^Disaster Recovery Projects', ln, flags=re.I):
            in_disaster = True
            current = None
            continue
        if in_disaster and re.search(r'^Capital Improvement Projects', ln, flags=re.I):
            in_disaster = False
            current = None
            continue
        # project name lines: not empty, not bullets, and followed by an Updates or Project Schedule line nearby
        if in_disaster:
            if ln and not re.match(r'^[\(\[]?cid', ln, flags=re.I) and not re.search(r'^(Updates|Project Schedule|Estimated Schedule|Project Description)\b', ln, flags=re.I):
                # candidate names often have parenthetical project types
                if len(ln) < 120 and not re.search(r'Agenda Item|Page \d+ of \d+|RECOMMENDED ACTION|DISCUSSION|To:|Prepared by:|Approved by:|Date prepared:|Meeting date:|Subject:', ln, flags=re.I):
                    # treat as new project name if next few lines contain Updates or Schedule
                    window = ' '.join(lines[i:i+5])
                    if re.search(r'Updates|Project Schedule|Estimated Schedule', window, flags=re.I):
                        current = ln
                        projects.append({'Project_Name': current, 'context': window})
    # Determine start in 2022: look for 'Begin Construction' or 'Advertise' or 'Start' with 2022 in same context
    started_2022 = set()
    for p in projects:
        ctx = p['context']
        if re.search(r'(Begin Construction|Start|Advertise)\s*:\s*[^\n]*2022', ctx, flags=re.I):
            started_2022.add(p['Project_Name'])
    return started_2022

started_2022_projects = set()
for d in docs:
    started_2022_projects |= extract_disaster_projects_started_2022(d.get('text',''))

# Fallback: many disaster projects might not be under header in these docs. Use name-based signals and find any 2022 begin/start in nearby text around the name.
# Build regex patterns for known funding project names containing FEMA/CalOES/CalJPIA.
disaster_names = fund_df[fund_df['Project_Name'].str.contains(r'\(FEMA|CalOES|CalJPIA', regex=True, na=False)]['Project_Name'].tolist()

for d in docs:
    text = d.get('text','')
    for name in disaster_names:
        if name in text:
            # search within +/- 400 chars for start indicators with 2022
            for m in re.finditer(re.escape(name), text):
                start = max(0, m.start()-400)
                end = min(len(text), m.end()+400)
                snippet = text[start:end]
                if re.search(r'(Begin Construction|Start|Advertise)\s*:\s*[^\n]*2022', snippet, flags=re.I):
                    started_2022_projects.add(name)

# Join with funding totals
if started_2022_projects:
    sel = fund_df[fund_df['Project_Name'].isin(sorted(started_2022_projects))]
    total_funding = int(sel['total_amount'].sum())
else:
    total_funding = 0

out = {
    'total_funding_disaster_projects_started_in_2022': total_funding,
    'matched_projects_count': int(len(started_2022_projects)),
    'matched_projects': sorted(started_2022_projects)[:50]
}
print('__RESULT__:')
print(json.dumps(out))"""

env_args = {'var_call_YJ2uK7IC5YUxvFQ5GSnMFfDn': ['Funding'], 'var_call_dEt2skTiWFH9rCHgKtKznCXX': ['civic_docs'], 'var_call_RulML30xUVm7z6HjS6Vlheqd': 'file_storage/call_RulML30xUVm7z6HjS6Vlheqd.json', 'var_call_GnrTK04YJ2K9l5O71wRnwMs4': 'file_storage/call_GnrTK04YJ2K9l5O71wRnwMs4.json'}

exec(code, env_args)
