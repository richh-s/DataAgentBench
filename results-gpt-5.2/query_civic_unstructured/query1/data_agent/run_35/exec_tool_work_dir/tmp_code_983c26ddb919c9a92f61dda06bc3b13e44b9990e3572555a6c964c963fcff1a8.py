code = """import json, re
import pandas as pd

# Load civic docs
path_docs = var_call_YKlSJCDsAfiW8J9rSNGBdU74
with open(path_docs, 'r', encoding='utf-8') as f:
    docs = json.load(f)

# Extract project names under 'Capital Improvement Projects (Design)'
project_names = set()
for d in docs:
    text = d.get('text','')
    # locate design section
    m = re.search(r"Capital Improvement Projects\s*\(Design\)(.*?)(Capital Improvement Projects\s*\(|Disaster Recovery Projects\s*\(|$)", text, flags=re.S|re.I)
    if not m:
        continue
    section = m.group(1)
    # Split lines and pick candidate name lines (non-empty, not bullet/update/schedule/page)
    for line in section.splitlines():
        l = line.strip()
        if not l:
            continue
        if re.search(r"^(\(cid:|Page \d+ of|Agenda Item|To:|Prepared by|Approved by|Date prepared|Meeting date|Subject:|RECOMMENDED ACTION|DISCUSSION:|Updates:|Project Schedule|Estimated Schedule|Complete Design|Advertise|Begin Construction|Final Design|Project Description)", l, flags=re.I):
            continue
        # ignore lines that are clearly continuation/bullets
        if l.startswith(('•','-','–','—')):
            continue
        # Heuristic: project name line often has no colon and no period at end
        if ':' in l:
            continue
        # exclude lines with too many words that look like sentences
        if len(l) > 120:
            continue
        # keep
        project_names.add(l)

# Load funding totals > 50000
path_fund = var_call_kPbCoCKs1Tcl0ulNBUmMtQU1
with open(path_fund, 'r', encoding='utf-8') as f:
    fund = json.load(f)
fund_df = pd.DataFrame(fund)
fund_df['total_amount'] = fund_df['total_amount'].astype(int)

# Join by exact match
design_df = pd.DataFrame({'Project_Name': sorted(project_names)})
merged = design_df.merge(fund_df, on='Project_Name', how='inner')
count = int((merged['total_amount'] > 50000).sum())

print('__RESULT__:')
print(json.dumps({'count': count}))"""

env_args = {'var_call_SHMFoiaZc0NBB8bXdURQsgPX': [{'cnt': '276'}], 'var_call_YKlSJCDsAfiW8J9rSNGBdU74': 'file_storage/call_YKlSJCDsAfiW8J9rSNGBdU74.json', 'var_call_kPbCoCKs1Tcl0ulNBUmMtQU1': 'file_storage/call_kPbCoCKs1Tcl0ulNBUmMtQU1.json'}

exec(code, env_args)
