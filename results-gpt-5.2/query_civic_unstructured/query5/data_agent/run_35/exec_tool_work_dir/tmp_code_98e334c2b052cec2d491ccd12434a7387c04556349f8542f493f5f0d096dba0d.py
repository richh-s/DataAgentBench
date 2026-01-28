code = """import json, re
import pandas as pd

path_funding = var_call_RulML30xUVm7z6HjS6Vlheqd
with open(path_funding, 'r', encoding='utf-8') as f:
    funding_totals = json.load(f)
fund_df = pd.DataFrame(funding_totals)
if not fund_df.empty:
    fund_df['total_amount'] = pd.to_numeric(fund_df['total_amount'], errors='coerce').fillna(0).astype(int)

path_docs = var_call_GnrTK04YJ2K9l5O71wRnwMs4
with open(path_docs, 'r', encoding='utf-8') as f:
    docs = json.load(f)

def extract_disaster_projects_started_2022(text):
    lines = [ln.strip() for ln in text.splitlines()]
    projects = []
    in_disaster = False
    for i, ln in enumerate(lines):
        if re.search(r'^Disaster Recovery Projects', ln, flags=re.I):
            in_disaster = True
            continue
        if in_disaster and re.search(r'^Capital Improvement Projects', ln, flags=re.I):
            in_disaster = False
            continue
        if in_disaster:
            if ln and not re.match(r'^[\(\[]?cid', ln, flags=re.I) and not re.search(r'^(Updates|Project Schedule|Estimated Schedule|Project Description)\b', ln, flags=re.I):
                if len(ln) < 120 and not re.search(r'Agenda Item|Page \d+ of \d+|RECOMMENDED ACTION|DISCUSSION|To:|Prepared by:|Approved by:|Date prepared:|Meeting date:|Subject:', ln, flags=re.I):
                    window = ' '.join(lines[i:i+5])
                    if re.search(r'Updates|Project Schedule|Estimated Schedule', window, flags=re.I):
                        projects.append({'Project_Name': ln, 'context': window})
    started_2022 = set()
    for p in projects:
        ctx = p['context']
        if re.search(r'(Begin Construction|Start|Advertise)\s*:\s*[^\n]*2022', ctx, flags=re.I):
            started_2022.add(p['Project_Name'])
    return started_2022

started_2022_projects = set()
for d in docs:
    started_2022_projects |= extract_disaster_projects_started_2022(d.get('text',''))

# fallback search around known disaster-type names (contain FEMA/CalOES/CalJPIA)
disaster_names = fund_df[fund_df['Project_Name'].str.contains(r'\((FEMA|CalOES|CalJPIA)', regex=True, na=False)]['Project_Name'].tolist()

for d in docs:
    text = d.get('text','')
    for name in disaster_names:
        if name in text:
            for m in re.finditer(re.escape(name), text):
                s = max(0, m.start()-400)
                e = min(len(text), m.end()+400)
                snippet = text[s:e]
                if re.search(r'(Begin Construction|Start|Advertise)\s*:\s*[^\n]*2022', snippet, flags=re.I):
                    started_2022_projects.add(name)

sel = fund_df[fund_df['Project_Name'].isin(sorted(started_2022_projects))] if started_2022_projects else fund_df.iloc[0:0]

total_funding = int(sel['total_amount'].sum()) if not sel.empty else 0
out = {
    'total_funding_disaster_projects_started_in_2022': total_funding,
    'matched_projects_count': int(len(started_2022_projects)),
    'matched_projects': sorted(started_2022_projects)
}
print('__RESULT__:')
print(json.dumps(out))"""

env_args = {'var_call_YJ2uK7IC5YUxvFQ5GSnMFfDn': ['Funding'], 'var_call_dEt2skTiWFH9rCHgKtKznCXX': ['civic_docs'], 'var_call_RulML30xUVm7z6HjS6Vlheqd': 'file_storage/call_RulML30xUVm7z6HjS6Vlheqd.json', 'var_call_GnrTK04YJ2K9l5O71wRnwMs4': 'file_storage/call_GnrTK04YJ2K9l5O71wRnwMs4.json'}

exec(code, env_args)
