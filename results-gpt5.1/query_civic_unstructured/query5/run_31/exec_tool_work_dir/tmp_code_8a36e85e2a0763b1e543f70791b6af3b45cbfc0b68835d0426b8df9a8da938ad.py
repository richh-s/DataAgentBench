code = """import re, json, pandas as pd, os, textwrap

# Load full civic docs
path_docs = var_call_LaAkSdAirhBApfNfR7zb5WQr
with open(path_docs, 'r') as f:
    docs = json.load(f)

# Make a simple heuristic extractor for project blocks with dates
projects = []
for doc in docs:
    text = doc.get('text','')
    # Split on double newlines as rough paragraphs
    blocks = re.split(r"\n\s*\n", text)
    for block in blocks:
        if '2022' not in block:
            continue
        # project name: first line up to 'Project' or full first line
        lines = [l.strip() for l in block.split('\n') if l.strip()]
        if not lines:
            continue
        first = lines[0]
        # skip headers
        if len(first.split())<2 or first.lower().startswith(('agenda','page ','public works commission','capital improvement projects','discussion')):
            continue
        proj_name = first
        # type: disaster if FEMA/CalOES etc in block
        ptype = 'disaster' if re.search(r'FEMA|CalOES|CalJPIA|Woolsey', block, re.I) else 'capital'
        # status heuristics
        status = None
        if re.search(r'completed', block, re.I):
            status = 'completed'
        elif re.search(r'not started', block, re.I):
            status = 'not started'
        elif re.search(r'design', block, re.I):
            status = 'design'
        # start/end date: search patterns like 'Begin Construction: ...' with 2022 or any 2022- token
        st = None
        for line in lines:
            if 'Begin Construction' in line or 'Start' in line:
                if '2022' in line:
                    st = line
                    break
        if not st:
            # generic year in block
            m = re.search(r'(2022[-A-Za-z]*)', block)
            if m:
                st = m.group(1)
        if not st:
            continue
        projects.append({'Project_Name': proj_name, 'type': ptype, 'status': status, 'st': st})

# Load Funding table
path_fund = var_call_dnaHXVgz0BvXKZhU3VnKga0s
with open(path_fund, 'r') as f:
    funding = json.load(f)

fund_df = pd.DataFrame(funding)
fund_df['Amount'] = fund_df['Amount'].astype(int)

proj_df = pd.DataFrame(projects)

# Fuzzy match by exact name containment both ways
merged_rows = []
for _, prow in proj_df.iterrows():
    pname = prow['Project_Name']
    for _, frow in fund_df.iterrows():
        fname = frow['Project_Name']
        if pname in fname or fname in pname:
            merged = {**prow.to_dict(), **{k: frow[k] for k in frow.index}}
            merged_rows.append(merged)

merged_df = pd.DataFrame(merged_rows)
if not merged_df.empty:
    # Filter disaster type and st contains 2022
    mask = (merged_df['type']=='disaster') & merged_df['st'].astype(str).str.contains('2022')
    total = int(merged_df.loc[mask, 'Amount'].sum())
else:
    total = 0

result = {'total_disaster_funding_2022_start_projects': total}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_call_LaAkSdAirhBApfNfR7zb5WQr': 'file_storage/call_LaAkSdAirhBApfNfR7zb5WQr.json', 'var_call_dnaHXVgz0BvXKZhU3VnKga0s': 'file_storage/call_dnaHXVgz0BvXKZhU3VnKga0s.json'}

exec(code, env_args)
