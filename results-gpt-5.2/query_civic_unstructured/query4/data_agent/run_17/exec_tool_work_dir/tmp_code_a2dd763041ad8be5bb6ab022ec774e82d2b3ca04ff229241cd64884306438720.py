code = """import json, re
import pandas as pd

# load civic docs
path_docs = var_call_5FRoyKoaGE92xUhwFnjuJHFV
with open(path_docs, 'r', encoding='utf-8') as f:
    docs = json.load(f)

# load funding sums
path_fund = var_call_B8i9KzeWghvmclogSXmtIm7J
with open(path_fund, 'r', encoding='utf-8') as f:
    fund = json.load(f)

fund_df = pd.DataFrame(fund)
if not fund_df.empty:
    fund_df['total_amount'] = pd.to_numeric(fund_df['total_amount'], errors='coerce').fillna(0).astype(int)

# Extract project blocks and their schedules from text
spring_2022_projects = set()

# Pattern for schedule lines e.g., Begin Construction: Spring 2022, Advertise: Spring 2022, Start: Spring 2022
sched_re = re.compile(r'(?im)^\s*(?:Project\s+Schedule|Estimated\s+Schedule|Schedule)\b.*?$')
start_line_re = re.compile(r'(?im)^\s*(?:Begin\s+Construction|Start(?:\s+Construction)?|Begin\s+Work|Construction\s+Start|Advertise|Bid\s+and\s+Award|Issue\s+RFP|Issue\s+RFQ|Notice\s+to\s+Proceed)\s*:\s*([^\n\r]+)')

# Heuristic for project name: a standalone line with Title Case words, not bullet, not section header
name_re = re.compile(r'(?m)^(?!\s*(?:\(cid:|Page\s+\d+\s+of\s+\d+|Agenda\s+Item|Capital\s+Improvement\s+Projects|Disaster\s+Recovery\s+Projects|RECOMMENDED\s+ACTION|DISCUSSION|To:|Prepared\s+by:|Approved\s+by:|Date\s+prepared:|Meeting\s+date:|Subject:|Updates:|Project\s+Description:))\s*([A-Z][^\n]{2,120})\s*$')

for d in docs:
    text = d.get('text','')
    # Split into lines for scanning
    lines = text.splitlines()
    # Build indices of candidate project names and look ahead for schedule info within next 40 lines
    for i, line in enumerate(lines):
        m = name_re.match(line)
        if not m:
            continue
        pname = m.group(1).strip()
        # exclude lines that end with ':' and common non-projects
        if pname.endswith(':'):
            continue
        if len(pname) < 4:
            continue
        if pname.lower() in {'discussion','recommended action'}:
            continue
        # lookahead chunk
        chunk = "\n".join(lines[i:i+60])
        # any start-related line containing Spring 2022?
        found = False
        for sm in start_line_re.finditer(chunk):
            val = sm.group(1)
            if re.search(r'(?i)\bSpring\s+2022\b', val):
                found = True
                break
        # also accept direct 'Spring 2022' near 'Begin' words in same chunk
        if not found and re.search(r'(?i)Begin\s+Construction\s*:\s*Spring\s+2022', chunk):
            found = True
        if found:
            spring_2022_projects.add(pname)

# Join to funding and compute totals
spring_list = sorted(spring_2022_projects)
if spring_list:
    joined = fund_df[fund_df['Project_Name'].isin(spring_list)]
    total_funding = int(joined['total_amount'].sum())
else:
    total_funding = 0

result = {
    'projects_started_spring_2022_count': int(len(spring_list)),
    'total_funding_usd': total_funding,
    'projects_found': spring_list
}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_call_5FRoyKoaGE92xUhwFnjuJHFV': 'file_storage/call_5FRoyKoaGE92xUhwFnjuJHFV.json', 'var_call_B8i9KzeWghvmclogSXmtIm7J': 'file_storage/call_B8i9KzeWghvmclogSXmtIm7J.json'}

exec(code, env_args)
