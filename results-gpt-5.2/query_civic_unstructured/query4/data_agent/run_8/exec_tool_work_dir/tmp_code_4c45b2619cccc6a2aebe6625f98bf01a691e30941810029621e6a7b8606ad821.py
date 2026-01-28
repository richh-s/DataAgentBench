code = """import json, re
import pandas as pd

def load_maybe_path(v):
    if isinstance(v, str) and v.endswith('.json'):
        with open(v, 'r', encoding='utf-8') as f:
            return json.load(f)
    return v

docs = load_maybe_path(var_call_dGtesJIXNNNsfONCBsfnBBgu)
funding = load_maybe_path(var_call_GDGSfAI3qBmWEhKepTKF28OD)

# Build funding map
fund_df = pd.DataFrame(funding)
if not fund_df.empty:
    fund_df['total_amount'] = pd.to_numeric(fund_df['total_amount'], errors='coerce').fillna(0).astype(int)
fund_map = dict(zip(fund_df['Project_Name'], fund_df['total_amount']))

# Extract candidate project blocks from text and look for start in Spring 2022
# Heuristic: project name line (not bullet) followed nearby by 'Begin'/'Start' and 'Spring 2022' or '2022-Spring'
name_pat = re.compile(r'^(?!\s*(?:\(cid:|Page\s+\d+\s+of\s+\d+|Agenda\s+Item|RECOMMENDED\s+ACTION|DISCUSSION|Capital\s+Improvement\s+Projects|Disaster\s+Recovery\s+Projects)\b)([A-Z0-9][A-Za-z0-9/&\-\u2019\'\u201c\u201d\u2014\u2013\.,\(\) ]{3,})\s*$')
start_spring_pat = re.compile(r'(?:Begin\s+Construction|Begin\s+construction|Begin\s+Design|Begin\s+design|Begin|Start|Started)\s*:\s*(?:Spring\s+2022|2022\s*[-/]\s*Spring)', re.IGNORECASE)
any_spring2022_pat = re.compile(r'\b(Spring\s+2022|2022\s*[-/]\s*Spring)\b', re.IGNORECASE)

projects_spring2022 = set()

for d in docs:
    text = d.get('text','') or ''
    lines = [ln.rstrip() for ln in text.splitlines()]
    # index all possible names
    for i, ln in enumerate(lines):
        m = name_pat.match(ln.strip())
        if not m:
            continue
        name = m.group(1).strip()
        # lookahead window
        window = "\n".join(lines[i:i+15])
        if start_spring_pat.search(window):
            projects_spring2022.add(name)
        else:
            # fallback: if line contains project schedule and spring 2022 nearby with begin keyword
            if any_spring2022_pat.search(window) and re.search(r'\b(Begin|Start|Started)\b', window, re.IGNORECASE):
                projects_spring2022.add(name)

# Join with funding where available (exact match)
matched = []
missing_funding = []
for p in sorted(projects_spring2022):
    amt = fund_map.get(p)
    if amt is None:
        missing_funding.append(p)
    else:
        matched.append({'Project_Name': p, 'Amount': int(amt)})

total_projects = len(projects_spring2022)
matched_count = len(matched)
fund_total = sum(x['Amount'] for x in matched)

result = {
    'projects_started_spring_2022_count': total_projects,
    'total_funding_matched_usd': fund_total,
    'projects_with_funding_count': matched_count,
    'projects_missing_funding_count': len(missing_funding),
    'projects_started_spring_2022': sorted(projects_spring2022)
}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_call_dGtesJIXNNNsfONCBsfnBBgu': 'file_storage/call_dGtesJIXNNNsfONCBsfnBBgu.json', 'var_call_GDGSfAI3qBmWEhKepTKF28OD': 'file_storage/call_GDGSfAI3qBmWEhKepTKF28OD.json'}

exec(code, env_args)
