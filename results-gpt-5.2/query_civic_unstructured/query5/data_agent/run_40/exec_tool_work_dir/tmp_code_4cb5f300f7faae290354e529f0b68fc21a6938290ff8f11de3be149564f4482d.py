code = """import json, re, pandas as pd

funding_path = var_call_BvPotNFTJ1r3WJTnMNxvhIZp
with open(funding_path, 'r') as f:
    funding_records = json.load(f)
fund_df = pd.DataFrame(funding_records)
if not fund_df.empty:
    fund_df['total_amount'] = pd.to_numeric(fund_df['total_amount'], errors='coerce').fillna(0).astype(int)

civic_path = var_call_fFSZkBXb2EEnVFMFdFbLhICH
with open(civic_path, 'r') as f:
    civic_records = json.load(f)

# Simple robust approach:
# 1) Find candidate project names in documents that are disaster-related by name markers.
# 2) For each candidate occurrence, look nearby for schedule lines containing 2022 and 'Begin'.

disaster_mark = re.compile(r"\b(FEMA|CalOES|CalJPIA)\b", re.IGNORECASE)
begin_2022 = re.compile(r"Begin\s+(Construction|Design)\s*:\s*.*2022", re.IGNORECASE)

projects=set()
for rec in civic_records:
    text = rec.get('text','') or ''
    lines = [ln.strip() for ln in text.splitlines()]
    for i, ln in enumerate(lines):
        if not ln:
            continue
        if disaster_mark.search(ln):
            window = "\n".join(lines[i:i+40])
            if begin_2022.search(window):
                # take the line as project name, normalize extra whitespace
                projects.add(re.sub(r"\s+", " ", ln))

# Join to funding totals on exact Project_Name
proj_df = pd.DataFrame({'Project_Name': sorted(projects)})
if proj_df.empty:
    out={'total_funding':0,'matched_projects':[],'identified_projects':[]}
else:
    merged = proj_df.merge(fund_df[['Project_Name','total_amount']], on='Project_Name', how='left')
    merged['total_amount']=merged['total_amount'].fillna(0).astype(int)
    total_funding=int(merged['total_amount'].sum())
    out={'total_funding': total_funding,
         'matched_projects': merged[merged.total_amount>0].to_dict(orient='records'),
         'identified_projects': merged['Project_Name'].tolist()}

print('__RESULT__:')
print(json.dumps(out))"""

env_args = {'var_call_BvPotNFTJ1r3WJTnMNxvhIZp': 'file_storage/call_BvPotNFTJ1r3WJTnMNxvhIZp.json', 'var_call_fFSZkBXb2EEnVFMFdFbLhICH': 'file_storage/call_fFSZkBXb2EEnVFMFdFbLhICH.json', 'var_call_beBgSXI1cPOhnVj0KrZFNscR': ['Funding']}

exec(code, env_args)
