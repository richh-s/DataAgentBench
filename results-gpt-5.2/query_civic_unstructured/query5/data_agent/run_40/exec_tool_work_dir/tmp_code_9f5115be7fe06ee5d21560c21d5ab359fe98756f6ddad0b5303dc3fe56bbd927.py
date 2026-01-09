code = """import json, re, pandas as pd

# load funding totals per project
funding_path = var_call_BvPotNFTJ1r3WJTnMNxvhIZp
with open(funding_path, 'r') as f:
    funding_records = json.load(f)
fund_df = pd.DataFrame(funding_records)
if fund_df.empty:
    total = 0
else:
    fund_df['total_amount'] = pd.to_numeric(fund_df['total_amount'], errors='coerce').fillna(0).astype(int)

# load civic docs
civic_path = var_call_fFSZkBXb2EEnVFMFdFbLhICH
with open(civic_path, 'r') as f:
    civic_records = json.load(f)

# extract disaster projects with start year 2022
# We'll parse sections under 'Disaster Recovery Projects' and look for 'Project Schedule'/'Estimated Schedule' and fields like 'Begin Construction:'
# If any of those schedule lines contain '2022', consider started in 2022.

def find_disaster_started_2022(text):
    results = []
    # locate disaster recovery section(s)
    for m in re.finditer(r"Disaster Recovery Projects.*?(?=\n\s*(Capital Improvement Projects|Page \d+ of \d+|$))", text, flags=re.IGNORECASE|re.DOTALL):
        sec = m.group(0)
        # project name lines: heuristic - non-empty line not starting with bullets/labels and with titlecase words, followed by blank line or updates
        lines = [ln.strip() for ln in sec.splitlines()]
        # build blocks by project name when line has no colon and not label and next non-empty line starts with something like '(cid' or 'Updates' or 'Project'
        i=0
        while i < len(lines):
            ln = lines[i]
            if not ln or ':' in ln or ln.lower() in {'updates','project schedule','estimated schedule','project updates','project description'}:
                i+=1
                continue
            if ln.lower().startswith(('page ', 'agenda item')):
                i+=1
                continue
            if ln.lower().startswith(('recommended action', 'discussion')):
                i+=1
                continue
            # candidate project name if contains letters and length
            if re.search(r'[A-Za-z]', ln) and len(ln) >= 6:
                # gather block until next candidate name or end
                j=i+1
                block_lines=[]
                while j < len(lines):
                    ln2=lines[j]
                    if ln2 and ':' not in ln2 and re.search(r'[A-Za-z]', ln2) and len(ln2)>=6 and not ln2.lower().startswith(('page ', 'agenda item')) and ln2.lower() not in {'updates','project schedule','estimated schedule','project updates','project description'} and not ln2.lower().startswith('('):
                        # treat as next project name if preceded by blank line or label
                        break
                    block_lines.append(ln2)
                    j+=1
                block = '\n'.join(block_lines)
                # start indicators
                if re.search(r"Begin (Construction|Design)\s*:\s*.*2022", block, flags=re.IGNORECASE) or re.search(r"Advertise\s*:\s*.*2022", block, flags=re.IGNORECASE):
                    results.append(ln)
                i=j
            else:
                i+=1
    return results

projects=set()
for rec in civic_records:
    text = rec.get('text','') or ''
    for p in find_disaster_started_2022(text):
        projects.add(p)

# some disaster projects might appear in capital section but are FEMA/CalOES indicated; however question asks disaster-related projects.
# include those with explicit FEMA/CalOES/CalJPIA in name that started 2022 anywhere in doc.

def find_any_project_started_2022_with_disaster_name(text):
    res=set()
    # find all occurrences of lines that look like project names with disaster markers
    lines=[ln.strip() for ln in text.splitlines()]
    for idx, ln in enumerate(lines):
        if re.search(r"\((FEMA|CalOES|CalJPIA).*?Project\)", ln, flags=re.IGNORECASE) or re.search(r"\bFEMA\b", ln):
            # look ahead for schedule lines within next 25 lines
            window='\n'.join(lines[idx:idx+35])
            if re.search(r"Begin (Construction|Design)\s*:\s*.*2022", window, flags=re.IGNORECASE) or re.search(r"Advertise\s*:\s*.*2022", window, flags=re.IGNORECASE):
                # project name likely before schedule lines; use ln as name
                res.add(ln)
    return res

for rec in civic_records:
    text=rec.get('text','') or ''
    projects |= find_any_project_started_2022_with_disaster_name(text)

# join to funding totals
proj_list=sorted(projects)
proj_df=pd.DataFrame({'Project_Name':proj_list})
merged=proj_df.merge(fund_df[['Project_Name','total_amount']], on='Project_Name', how='left')
merged['total_amount']=merged['total_amount'].fillna(0).astype(int)

total_funding=int(merged['total_amount'].sum())

out={'total_funding': total_funding, 'matched_projects': merged[merged.total_amount>0].to_dict(orient='records'), 'identified_projects': proj_list}
print('__RESULT__:')
print(json.dumps(out))"""

env_args = {'var_call_BvPotNFTJ1r3WJTnMNxvhIZp': 'file_storage/call_BvPotNFTJ1r3WJTnMNxvhIZp.json', 'var_call_fFSZkBXb2EEnVFMFdFbLhICH': 'file_storage/call_fFSZkBXb2EEnVFMFdFbLhICH.json', 'var_call_beBgSXI1cPOhnVj0KrZFNscR': ['Funding']}

exec(code, env_args)
