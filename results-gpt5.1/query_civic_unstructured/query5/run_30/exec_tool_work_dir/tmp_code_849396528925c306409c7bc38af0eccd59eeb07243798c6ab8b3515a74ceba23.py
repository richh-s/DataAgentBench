code = """import re, json, pandas as pd

# Load full civic docs
path_docs = var_call_njyvB1lS7IEI8ay3XFxkeD0D
with open(path_docs, 'r') as f:
    civic_docs = json.load(f)

# Load funding table
path_fund = var_call_uuKyY6h340c6oId7AtasSSnf
with open(path_fund, 'r') as f:
    funding = json.load(f)

# Identify disaster-related project names from text with year 2022 in start date
project_names_2022_disaster = set()

for doc in civic_docs:
    text = doc.get('text','')
    # crude heuristic: lines containing '(FEMA' or '(CalOES' or '(CalJPIA' or 'Disaster Recovery' are disaster-related
    for line in text.split('\n'):
        if any(k in line for k in ['FEMA', 'CalOES', 'CalJPIA', 'Disaster Recovery']):
            # look for a year-like start marker with 2022
            if '2022' in line:
                # extract capitalized phrase before first '(' as project name
                m = re.match(r'\s*(.+?)(?:\s*\(|$)', line.strip())
                if m:
                    name = m.group(1).strip()
                    if len(name) > 3:
                        project_names_2022_disaster.add(name)

# Additionally, some project lines may list like '2022 Morning View Resurfacing & Storm Drain Improvements' as design list
for doc in civic_docs:
    text = doc.get('text','')
    for line in text.split('\n'):
        if '2022' in line and any(w in line for w in ['Fire','Disaster','FEMA','CalOES','CalJPIA']):
            s = line.strip()
            if len(s)>3:
                project_names_2022_disaster.add(s)

# Build funding DataFrame
fund_df = pd.DataFrame(funding)
fund_df['Amount'] = fund_df['Amount'].astype(int)

# Disaster-related projects in funding are heuristically those whose Project_Name contains 'FEMA', 'CalOES', 'CalJPIA', 'Fire', or 'Disaster'
mask_disaster = fund_df['Project_Name'].str.contains('FEMA|CalOES|CalJPIA|Fire|Disaster', case=False, regex=True)

# For 2022 start, approximate by joining on project names we found (if there are overlaps)
if project_names_2022_disaster:
    mask_2022_name = fund_df['Project_Name'].isin(project_names_2022_disaster)
    final_mask = mask_disaster & mask_2022_name
else:
    # if we couldn't parse any, fallback: assume all disaster-type (FEMA/CalOES etc.) started in or before 2022 and user wants total for 2022 starts only -> cannot determine.
    total = None
    result = {"total_funding_2022_disaster_projects": total, "note": "Could not reliably determine which disaster projects started in 2022 from the available text."}
    print("__RESULT__:")
    print(json.dumps(result))
    raise SystemExit

total = int(fund_df.loc[final_mask, 'Amount'].sum())

result = {"total_funding_2022_disaster_projects": total, "matched_projects": sorted(fund_df.loc[final_mask, 'Project_Name'].unique().tolist())}

print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_njyvB1lS7IEI8ay3XFxkeD0D': 'file_storage/call_njyvB1lS7IEI8ay3XFxkeD0D.json', 'var_call_uuKyY6h340c6oId7AtasSSnf': 'file_storage/call_uuKyY6h340c6oId7AtasSSnf.json'}

exec(code, env_args)
