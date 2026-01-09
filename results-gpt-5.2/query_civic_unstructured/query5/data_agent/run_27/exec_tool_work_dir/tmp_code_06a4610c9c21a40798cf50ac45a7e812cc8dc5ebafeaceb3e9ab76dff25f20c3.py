code = """import json, re
import pandas as pd

fp = var_call_sEZ4zSgyrgwEXKFGtH9vxTm5
with open(fp, 'r', encoding='utf-8') as f:
    funding = json.load(f)
fund_df = pd.DataFrame(funding)
if not fund_df.empty:
    fund_df['total_amount'] = pd.to_numeric(fund_df['total_amount'], errors='coerce').fillna(0).astype(int)

dp = var_call_i22P9BMqB3rVlJUYjhpUzn8Y
with open(dp, 'r', encoding='utf-8') as f:
    docs = json.load(f)

def extract_disaster_2022_projects(text):
    pat = re.compile(r"Disaster Recovery Projects\b(.*?)(?:\n\s*(?:Capital Improvement Projects|Public Safety|Parks|Page\s+\d+\s+of\s+\d+|$))", re.IGNORECASE|re.DOTALL)
    m = pat.search(text)
    if not m:
        return []
    section = m.group(1)

    candidates = []
    for line in section.splitlines():
        ln = line.strip()
        if not ln:
            continue
        if re.search(r"^(?:\(cid:|\*|\-|\u2022)", ln):
            continue
        if re.search(r"^(?:Updates|Project Schedule|Estimated Schedule|Project Description|RECOMMENDED ACTION|DISCUSSION|To:|Prepared by:|Approved by:|Date prepared:|Meeting date:|Subject:)", ln, flags=re.IGNORECASE):
            continue
        if re.search(r"\b(?:Complete|Begin|Advertise|Final Design|Preliminary design)\b\s*:\s*", ln, flags=re.IGNORECASE):
            continue
        if len(ln) > 120:
            continue
        if not re.search(r"[A-Za-z]", ln):
            continue
        candidates.append(ln)

    titles = []
    seen = set()
    for c in candidates:
        cl = c.lower()
        if cl not in seen:
            seen.add(cl)
            titles.append(c)

    projects = []
    lower_section = section.lower()
    for t in titles:
        idx = lower_section.find(t.lower())
        if idx == -1:
            continue
        window = section[idx: idx+800]
        if re.search(r"\b(?:begin|start)\s+(?:construction|design)?\s*:\s*[^\n]*2022", window, flags=re.IGNORECASE):
            projects.append(t)
        elif re.search(r"\bproject schedule\b.*?\b(?:begin|start)\b[^\n]*2022", window, flags=re.IGNORECASE|re.DOTALL):
            projects.append(t)
        elif re.search(r"\bbegin\b[^\n]*\n[^\n]*2022", window, flags=re.IGNORECASE):
            projects.append(t)
    return projects

all_projects = set()
for d in docs:
    text = d.get('text','') or ''
    for p in extract_disaster_2022_projects(text):
        all_projects.add(p)

proj_df = pd.DataFrame({'Project_Name': sorted(all_projects)})
merged = proj_df.merge(fund_df, on='Project_Name', how='left') if not proj_df.empty else pd.DataFrame(columns=['Project_Name','total_amount'])
if not merged.empty:
    merged['total_amount'] = merged['total_amount'].fillna(0).astype(int)

total = int(merged['total_amount'].sum())

print('__RESULT__:')
print(json.dumps({'total_funding_disaster_projects_started_2022': total, 'matched_projects_count': int((merged['total_amount']>0).sum()) if not merged.empty else 0, 'projects_found_count': int(len(all_projects))}))"""

env_args = {'var_call_sEZ4zSgyrgwEXKFGtH9vxTm5': 'file_storage/call_sEZ4zSgyrgwEXKFGtH9vxTm5.json', 'var_call_i22P9BMqB3rVlJUYjhpUzn8Y': 'file_storage/call_i22P9BMqB3rVlJUYjhpUzn8Y.json'}

exec(code, env_args)
