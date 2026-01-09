code = """import json, re
import pandas as pd

# Load civic docs
civic_src = var_call_YP40XOl6RYtUWabTBpSKX6gV
if isinstance(civic_src, str) and civic_src.endswith('.json'):
    with open(civic_src, 'r', encoding='utf-8') as f:
        civic_docs = json.load(f)
else:
    civic_docs = civic_src

# Load funding aggregated
fund_src = var_call_jtGag2yJysDMXLV2Yhr0Vdw2
if isinstance(fund_src, str) and fund_src.endswith('.json'):
    with open(fund_src, 'r', encoding='utf-8') as f:
        funding_rows = json.load(f)
else:
    funding_rows = fund_src

fund_df = pd.DataFrame(funding_rows)
if not fund_df.empty:
    fund_df['total_amount'] = pd.to_numeric(fund_df['total_amount'])

# Extract projects whose schedule includes "Start" or "Begin" with Spring 2022
spring_pattern = re.compile(r'(?i)(?:\b(?:Start|Begin)\b\s*(?:Construction|Design)?\s*:?\s*)(Spring\s*2022|2022\s*Spring|Spring\s*,?\s*2022)')

projects = set()

for doc in civic_docs:
    text = doc.get('text','')
    # find occurrences and then backtrack to nearest project title line
    for m in spring_pattern.finditer(text):
        idx = m.start()
        # take previous 800 chars, split lines, find last non-empty line that is not a bullet/schedule label
        window = text[max(0, idx-1200):idx]
        lines = [ln.strip() for ln in window.splitlines() if ln.strip()]
        # heuristics: project title lines are not starting with '(' or 'cid' or 'Project Schedule' or 'Updates' and not containing ':'
        title = None
        for ln in reversed(lines):
            low = ln.lower()
            if any(k in low for k in ['project schedule', 'estimated schedule', 'updates', 'complete design', 'advertise', 'begin construction', 'begin design', 'start construction', 'start design']):
                continue
            if ln.startswith('(') or ln.startswith('cid'):
                continue
            if ln.endswith('.') and len(ln.split())<=4:
                continue
            # likely header
            if len(ln) >= 4 and len(ln) <= 120 and ':' not in ln:
                title = ln
                break
        if title:
            projects.add(title)

# Join with funding
proj_list = sorted(projects)
if len(proj_list)==0:
    out = {"spring_2022_projects_started_count": 0, "spring_2022_projects_total_funding": 0, "projects": []}
else:
    match_df = fund_df[fund_df['Project_Name'].isin(proj_list)].copy() if not fund_df.empty else pd.DataFrame(columns=['Project_Name','total_amount'])
    total_funding = int(match_df['total_amount'].sum()) if not match_df.empty else 0
    out = {
        "spring_2022_projects_started_count": int(len(proj_list)),
        "spring_2022_projects_total_funding": int(total_funding),
        "projects": proj_list,
        "projects_with_funding_records": match_df[['Project_Name','total_amount']].sort_values('Project_Name').to_dict('records')
    }

print('__RESULT__:')
print(json.dumps(out))"""

env_args = {'var_call_7eZ5PDTtR6rRioHc1hyH4MtR': ['Funding'], 'var_call_YP40XOl6RYtUWabTBpSKX6gV': 'file_storage/call_YP40XOl6RYtUWabTBpSKX6gV.json', 'var_call_jtGag2yJysDMXLV2Yhr0Vdw2': 'file_storage/call_jtGag2yJysDMXLV2Yhr0Vdw2.json'}

exec(code, env_args)
