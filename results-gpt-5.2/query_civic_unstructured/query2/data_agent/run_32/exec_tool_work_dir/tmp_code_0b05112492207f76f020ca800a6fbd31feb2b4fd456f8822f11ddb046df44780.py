code = """import json, re
import pandas as pd

def load_records(v):
    if isinstance(v, str) and v.endswith('.json'):
        with open(v, 'r', encoding='utf-8') as f:
            return json.load(f)
    return v

docs = load_records(var_call_rBZwuDjTsXSCOOMA47fnyCya)
fund = load_records(var_call_ECOXYDdx7UyF66cFrhDhAtkw)

# Heuristic extraction from docs: project blocks separated by blank lines, detect Project Name as a line title.
# We'll focus on identifying projects that (a) are park-related and (b) completed in 2022.
park_completed_2022 = set()

park_keywords = [
    'park', 'playground', 'skate', 'bluffs', 'legacy', 'trancas', 'point dume walkway', 'shade structure'
]

# patterns to find completion statements with 2022
comp_2022_pat = re.compile(r'completed[^\n\.]*\b(2022)\b', re.IGNORECASE)
# also handle "Construction was completed November 2022"

for d in docs:
    text = d.get('text','')
    # split into lines
    lines = [ln.strip() for ln in text.splitlines()]
    # Find candidate project name lines: non-empty, not bullets, not headers, title case-ish
    # We'll scan for lines followed soon by an Updates section containing completed ... 2022
    for i, ln in enumerate(lines):
        if not ln:
            continue
        # skip obvious headings
        if ln.lower().startswith(('public works', 'agenda', 'to:', 'prepared by', 'approved by', 'date prepared', 'meeting date', 'subject', 'recommended action', 'discussion', 'capital improvement projects', 'disaster recovery projects', 'page ')):
            continue
        if len(ln) > 120:
            continue
        # exclude lines with ':' as they are labels
        if ':' in ln:
            continue
        # candidate must contain letters
        if not re.search(r'[A-Za-z]', ln):
            continue

        window = '\n'.join(lines[i:i+40])
        if comp_2022_pat.search(window):
            lname = ln.lower()
            if any(k in lname for k in park_keywords):
                park_completed_2022.add(ln)

# Also scan for park-related projects where completion date line includes 2022 but project name appears earlier in same section
# Simple additional extraction: if a completion line exists, backtrack to nearest preceding non-empty line that looks like a project title.
for d in docs:
    lines = [ln.strip() for ln in d.get('text','').splitlines()]
    for idx, ln in enumerate(lines):
        if comp_2022_pat.search(ln):
            # backtrack up to 10 lines for title
            for j in range(1, 15):
                if idx-j < 0: break
                cand = lines[idx-j]
                if not cand: continue
                if ':' in cand: continue
                if cand.lower().startswith(('updates', '(cid', 'project schedule', 'estimated schedule', 'capital improvement projects', 'disaster recovery projects', 'project description', 'project updates')):
                    continue
                if len(cand) > 120: continue
                if any(k in cand.lower() for k in park_keywords):
                    park_completed_2022.add(cand)
                    break

# Now join to funding totals
fund_df = pd.DataFrame(fund)
# normalize to string keys
fund_df['Project_Name_norm'] = fund_df['Project_Name'].astype(str).str.strip().str.lower()
fund_df['total_amount'] = pd.to_numeric(fund_df['total_amount'], errors='coerce').fillna(0)

park_list = sorted(park_completed_2022)
park_norm = [p.strip().lower() for p in park_list]

matched = fund_df[fund_df['Project_Name_norm'].isin(park_norm)].copy()

total = float(matched['total_amount'].sum())

out = {
    'park_completed_2022_projects': park_list,
    'matched_funding_projects': matched[['Project_Name','total_amount']].to_dict(orient='records'),
    'total_funding': int(total)
}

print('__RESULT__:')
print(json.dumps(out))"""

env_args = {'var_call_smXPOBk8I2nHR1Q7DTEhBVE7': ['Funding'], 'var_call_rBZwuDjTsXSCOOMA47fnyCya': 'file_storage/call_rBZwuDjTsXSCOOMA47fnyCya.json', 'var_call_ECOXYDdx7UyF66cFrhDhAtkw': 'file_storage/call_ECOXYDdx7UyF66cFrhDhAtkw.json'}

exec(code, env_args)
