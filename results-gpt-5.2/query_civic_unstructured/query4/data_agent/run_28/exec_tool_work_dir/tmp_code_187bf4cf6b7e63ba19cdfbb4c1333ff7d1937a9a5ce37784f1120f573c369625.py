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
fund_names = set(fund_df['Project_Name'].dropna().astype(str).tolist())

begin_pat = re.compile(r"Begin Construction:\s*Spring\s*2022", re.IGNORECASE)

exclude_prefixes = (
    'capital improvement projects', 'disaster recovery projects', 'project schedule', 'updates',
    'discussion', 'recommended action', 'page ', 'agenda item', 'subject', 'to:', 'prepared by',
    'approved by', 'date prepared', 'meeting date'
)

# Accept only lines that exactly match a funding project name

def extract_projects_from_text(text):
    projects = set()
    for m in begin_pat.finditer(text):
        start = max(0, m.start() - 1200)
        window = text[start:m.start()]
        lines = [ln.strip() for ln in window.splitlines() if ln.strip()]
        for ln in reversed(lines):
            low = ln.lower()
            if any(low.startswith(p) for p in exclude_prefixes):
                continue
            if re.search(r"\b(beginning in spring 2022|spring of 2022|woolsey fire)\b", low):
                continue
            if re.search(r"(complete design|advertise|final design|complete construction|notice of completion|bids are due|bid documents|council meeting|public bidding)", low):
                continue
            if ln in fund_names:
                projects.add(ln)
                break
    return projects

spring2022_projects = set()
for doc in civic_docs:
    txt = doc.get('text','') or ''
    if 'Spring 2022' not in txt and 'spring 2022' not in txt:
        continue
    spring2022_projects |= extract_projects_from_text(txt)

proj_df = pd.DataFrame({'Project_Name': sorted(spring2022_projects)})
merged = proj_df.merge(fund_df, on='Project_Name', how='left') if not proj_df.empty else pd.DataFrame(columns=['Project_Name','total_amount'])
if not merged.empty:
    merged['total_amount'] = merged['total_amount'].fillna(0).astype(int)
count_projects = int(len(proj_df))
total_funding = int(merged['total_amount'].sum())

out = {
    'projects_started_spring_2022_count': count_projects,
    'total_funding_usd': total_funding,
    'projects': sorted(spring2022_projects)
}
print('__RESULT__:')
print(json.dumps(out))"""

env_args = {'var_call_Zjzr6BMRozQbZ5KvFdDjRRjp': 'file_storage/call_Zjzr6BMRozQbZ5KvFdDjRRjp.json', 'var_call_f8u0g3dkEM1CDgRlQB0OcIdZ': 'file_storage/call_f8u0g3dkEM1CDgRlQB0OcIdZ.json', 'var_call_wwRNMX8Q114amMFBYNpUQ4ol': {'projects_started_spring_2022_count': 14, 'total_funding_usd': 87000, 'projects': ['Fire.', 'Trancas Canyon Park Planting and Irrigation Repairs (CalJPIA/FEMA Project)', 'Trancas Canyon Park Slope Stabilization Project (CalJPIA Project)', 'beginning in Spring 2022.', 'damaged by the Woolsey Fire.', 'facilities and roadway embankments that were damaged by the Woolsey Fire.', 'is finalizing the bid documents.', 'is working on the project plans to prepare for public bidding.', 'manufacturers for filters that will work in the proposed project area. It is', 'scheduled for the April 11, 2022 Council meeting.', 'sending this project out to bid during the Spring of 2022.', 'shade structures at Malibu Bluffs Park.', 'that was damaged by the Woolsey Fire.', 'timber with non-combustible materials.']}}

exec(code, env_args)
