code = """import json, re
import pandas as pd

def load_records(var):
    if isinstance(var, str) and var.endswith('.json'):
        with open(var, 'r', encoding='utf-8') as f:
            return json.load(f)
    return var

docs = load_records(var_call_pp0xZ11F8TmjWNM09HJAXJpg)
funding = load_records(var_call_ODxqSVLA0I92eNyM4qCZtMzd)

# Build a lookup for funding totals by project name
fund_df = pd.DataFrame(funding)
if not fund_df.empty:
    fund_df['total_amount'] = pd.to_numeric(fund_df['total_amount'], errors='coerce').fillna(0).astype(int)

# Extract project blocks from documents: look for 'Project Schedule' or 'Estimated Schedule' with 'Complete Construction' lines.
# We'll identify completed-in-2022 projects that are park-related.

park_keywords = [
    'park', 'playground', 'skate', 'bluffs', 'legacy', 'trancas', 'zuma', 'point dume'
]

def is_park_related(name):
    n = (name or '').lower()
    return any(k in n for k in park_keywords)

# Collect completions info
completed_2022_projects = set()

# Regex patterns
re_complete = re.compile(r'^(?P<name>.+?)\s*(?:\r?\n)+\s*(?:\(.*?\)\s*)?(?:Updates:.*?\n)?\s*.*?Complete\s+Construction\s*:\s*(?P<date>.+)$', re.IGNORECASE | re.MULTILINE)
# More direct pattern: project name line then later 'Construction was completed <Month> 2022' or 'completed <Month> 2022'
re_completed_sentence = re.compile(r'^(?P<name>[A-Z0-9][^\n]{2,120})\n\s*(?:\(cid:190\)\s*)?Updates:\s*(?P<upd>.*?)(?:\n\s*(?:\(cid:190\)|Page|Agenda Item|\Z))', re.IGNORECASE | re.MULTILINE | re.DOTALL)

# Helper to parse update chunk for completion year 2022
re_year2022 = re.compile(r'\b2022\b')
re_completed = re.compile(r'\b(completed|complete)\b', re.IGNORECASE)

for d in docs:
    text = d.get('text','') or ''
    # From update chunks
    for m in re_completed_sentence.finditer(text):
        name = m.group('name').strip()
        upd = m.group('upd') or ''
        if re_year2022.search(upd) and re_completed.search(upd):
            # ensure it's construction completion not design etc, but keep if indicates construction was completed
            if re.search(r'construction\s+was\s+completed', upd, re.IGNORECASE) or re.search(r'notice of completion', upd, re.IGNORECASE) or re.search(r'completed\s+\w+\s+2022', upd, re.IGNORECASE):
                if is_park_related(name):
                    completed_2022_projects.add(name)
    # From explicit Complete Construction lines
    for m in re_complete.finditer(text):
        name = m.group('name').strip()
        date = (m.group('date') or '').strip()
        if '2022' in date and is_park_related(name):
            completed_2022_projects.add(name)

# Join with funding totals; if exact name not found, try minor normalization
fund_map = dict(zip(fund_df['Project_Name'], fund_df['total_amount'])) if not fund_df.empty else {}

def norm(s):
    return re.sub(r'\s+', ' ', (s or '').strip().lower())

norm_to_actual = {norm(k): k for k in fund_map.keys()}

total = 0
matched = []
unmatched = []
for p in sorted(completed_2022_projects):
    amt = fund_map.get(p)
    if amt is None:
        nk = norm(p)
        if nk in norm_to_actual:
            amt = fund_map[norm_to_actual[nk]]
    if amt is None:
        # try stripping trailing words like 'Project'
        p2 = re.sub(r'\s+Project\s*$', '', p, flags=re.IGNORECASE)
        amt = fund_map.get(p2)
        if amt is None:
            nk = norm(p2)
            if nk in norm_to_actual:
                amt = fund_map[norm_to_actual[nk]]
    if amt is None:
        unmatched.append(p)
    else:
        matched.append({'Project_Name': p, 'Funding_Total': int(amt)})
        total += int(amt)

out = {
    'total_funding_completed_2022_park_related': int(total),
    'matched_projects': matched,
    'unmatched_projects': unmatched
}

print('__RESULT__:')
print(json.dumps(out))"""

env_args = {'var_call_pp0xZ11F8TmjWNM09HJAXJpg': 'file_storage/call_pp0xZ11F8TmjWNM09HJAXJpg.json', 'var_call_ODxqSVLA0I92eNyM4qCZtMzd': 'file_storage/call_ODxqSVLA0I92eNyM4qCZtMzd.json'}

exec(code, env_args)
