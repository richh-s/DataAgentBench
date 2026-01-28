code = """import json, re, pandas as pd

# Load civic docs
civic_src = var_call_Zjzr6BMRozQbZ5KvFdDjRRjp
if isinstance(civic_src, str):
    with open(civic_src, 'r', encoding='utf-8') as f:
        civic_docs = json.load(f)
else:
    civic_docs = civic_src

# Load funding aggregated by project
fund_src = var_call_f8u0g3dkEM1CDgRlQB0OcIdZ
if isinstance(fund_src, str):
    with open(fund_src, 'r', encoding='utf-8') as f:
        fund_rows = json.load(f)
else:
    fund_rows = fund_src
fund_df = pd.DataFrame(fund_rows)
if not fund_df.empty:
    fund_df['total_amount'] = pd.to_numeric(fund_df['total_amount'], errors='coerce').fillna(0).astype(int)

# Pattern: project name line followed soon by Begin Construction: Spring 2022
begin_pat = re.compile(r"Begin Construction:\s*Spring\s*2022", re.IGNORECASE)

# Candidate project name line: non-empty, not bullet headers, limited length
exclude_prefixes = (
    'capital improvement projects', 'disaster recovery projects', 'project schedule', 'updates',
    'discussion', 'recommended action', 'page ', 'agenda item', 'subject', 'to:', 'prepared by',
    'approved by', 'date prepared', 'meeting date'
)

def extract_projects_from_text(text):
    projects = set()
    # Find all begin construction spring 2022 occurrences
    for m in begin_pat.finditer(text):
        start = max(0, m.start() - 800)  # look back window
        window = text[start:m.start()]
        lines = [ln.strip() for ln in window.splitlines() if ln.strip()]
        # walk backwards to find plausible project name
        for ln in reversed(lines):
            low = ln.lower()
            if any(low.startswith(p) for p in exclude_prefixes):
                continue
            if low.startswith('(cid') or low.startswith('cid:'):
                continue
            if low.startswith('(') and low.endswith(')') and len(ln) < 40:
                continue
            if ':' in ln and len(ln) < 50:
                # likely header like 'Updates:'
                if low.endswith(':') or low.split(':',1)[0] in ['updates','project schedule','estimated schedule','project description']:
                    continue
            # avoid schedule lines
            if re.search(r"(complete design|advertise|final design|complete construction|bids|due on|notice of completion)", low):
                continue
            # likely project name: mostly letters/numbers/& and not too long
            if 3 <= len(ln) <= 120 and re.search(r"[A-Za-z]", ln):
                # remove trailing punctuation
                proj = re.sub(r"\s+$", "", ln)
                proj = re.sub(r"\s{2,}", " ", proj)
                projects.add(proj)
                break
    return projects

spring2022_projects = set()
for doc in civic_docs:
    txt = doc.get('text','') or ''
    if 'Spring 2022' not in txt and 'spring 2022' not in txt:
        continue
    spring2022_projects |= extract_projects_from_text(txt)

# Join to funding (exact match)
if spring2022_projects:
    proj_df = pd.DataFrame({'Project_Name': sorted(spring2022_projects)})
    merged = proj_df.merge(fund_df, on='Project_Name', how='left')
    merged['total_amount'] = merged['total_amount'].fillna(0).astype(int)
    total_funding = int(merged['total_amount'].sum())
    count_projects = int(len(proj_df))
else:
    count_projects = 0
    total_funding = 0

out = {'projects_started_spring_2022_count': count_projects, 'total_funding_usd': total_funding, 'projects': sorted(spring2022_projects)}
print('__RESULT__:')
print(json.dumps(out))"""

env_args = {'var_call_Zjzr6BMRozQbZ5KvFdDjRRjp': 'file_storage/call_Zjzr6BMRozQbZ5KvFdDjRRjp.json', 'var_call_f8u0g3dkEM1CDgRlQB0OcIdZ': 'file_storage/call_f8u0g3dkEM1CDgRlQB0OcIdZ.json'}

exec(code, env_args)
