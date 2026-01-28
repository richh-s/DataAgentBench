code = """import json, re
import pandas as pd

def load_records(v):
    if isinstance(v, str) and v.endswith('.json'):
        with open(v, 'r', encoding='utf-8') as f:
            return json.load(f)
    return v

docs = load_records(var_call_pp0xZ11F8TmjWNM09HJAXJpg)
funding = load_records(var_call_ODxqSVLA0I92eNyM4qCZtMzd)

fund_df = pd.DataFrame(funding)
if not fund_df.empty:
    fund_df['total_amount'] = pd.to_numeric(fund_df['total_amount'], errors='coerce').fillna(0).astype(int)
fund_map = dict(zip(fund_df['Project_Name'], fund_df['total_amount'])) if not fund_df.empty else {}

park_keywords = ['park','playground','skate','bluffs','legacy','trancas','zuma','point dume']

def is_park_related(name):
    n = (name or '').lower()
    return any(k in n for k in park_keywords)

# Identify park-related projects completed in 2022 by scanning for patterns like:
# "<Project Name>" ... "Construction was completed <Month> 2022"
completed_2022_projects = set()

proj_header_re = re.compile(r'^([A-Z0-9][A-Za-z0-9\-\&\,\'\u2019\s]+?)\s*$' , re.MULTILINE)

for d in docs:
    text = d.get('text','') or ''
    if '2022' not in text:
        continue
    lines = text.splitlines()
    for i, line in enumerate(lines):
        # find completion statements
        if re.search(r'construction\s+was\s+completed.*\b2022\b', line, re.IGNORECASE) or re.search(r'completed\s+\w+\s+2022', line, re.IGNORECASE):
            # look back for nearest plausible project name line within 10 lines
            name = None
            for j in range(i-1, max(-1, i-12), -1):
                cand = lines[j].strip()
                if not cand:
                    continue
                # stop if hit section header
                if re.search(r'Capital Improvement Projects|Disaster Recovery Projects|Project Schedule|Updates', cand, re.IGNORECASE):
                    continue
                m = proj_header_re.match(cand)
                if m:
                    name = m.group(1).strip()
                    break
            if name and is_park_related(name):
                completed_2022_projects.add(name)

# Also handle "Complete Construction: <...2022...>" lines, looking back for project name
for d in docs:
    text = d.get('text','') or ''
    if 'Complete Construction' not in text or '2022' not in text:
        continue
    lines = text.splitlines()
    for i, line in enumerate(lines):
        if re.search(r'Complete\s+Construction\s*:\s*.*\b2022\b', line, re.IGNORECASE):
            name = None
            for j in range(i-1, max(-1, i-12), -1):
                cand = lines[j].strip()
                if not cand:
                    continue
                m = proj_header_re.match(cand)
                if m:
                    name = m.group(1).strip()
                    break
            if name and is_park_related(name):
                completed_2022_projects.add(name)

# Map to funding totals with light normalization

def norm(s):
    return re.sub(r'\s+', ' ', (s or '').strip().lower())

norm_to_key = {norm(k): k for k in fund_map.keys()}

def find_funding(p):
    if p in fund_map:
        return fund_map[p], p
    nk = norm(p)
    if nk in norm_to_key:
        k = norm_to_key[nk]
        return fund_map[k], k
    # strip trailing 'Project'
    p2 = re.sub(r'\s+Project\s*$', '', p, flags=re.IGNORECASE)
    if p2 in fund_map:
        return fund_map[p2], p2
    nk2 = norm(p2)
    if nk2 in norm_to_key:
        k = norm_to_key[nk2]
        return fund_map[k], k
    return None, None

matched = []
unmatched = []
total = 0
for p in sorted(completed_2022_projects):
    amt, matched_name = find_funding(p)
    if amt is None:
        unmatched.append(p)
    else:
        matched.append({'Project_Name_in_docs': p, 'Project_Name_in_funding': matched_name, 'Funding_Total': int(amt)})
        total += int(amt)

result = {
    'total_funding': int(total),
    'projects_count': len(matched),
    'projects': matched,
    'unmatched_projects': unmatched
}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_call_pp0xZ11F8TmjWNM09HJAXJpg': 'file_storage/call_pp0xZ11F8TmjWNM09HJAXJpg.json', 'var_call_ODxqSVLA0I92eNyM4qCZtMzd': 'file_storage/call_ODxqSVLA0I92eNyM4qCZtMzd.json'}

exec(code, env_args)
