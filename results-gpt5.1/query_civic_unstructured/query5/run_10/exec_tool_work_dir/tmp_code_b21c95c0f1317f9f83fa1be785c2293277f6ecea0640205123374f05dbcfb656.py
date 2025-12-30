code = """import re, json, pandas as pd

# Load full civic docs
path_civic = var_call_U7kOMfpDIhawztaDfw2UtvCq
with open(path_civic, 'r') as f:
    civic_docs = json.load(f)

# Load funding table
path_funding = var_call_432j1WT3jZgqIFOaNmGsA3A5
with open(path_funding, 'r') as f:
    funding = json.load(f)

texts = ' '.join(d.get('text','') for d in civic_docs)

# Rough heuristic: disaster projects often have FEMA/CalOES in name; extract lines with 'Project' or capitalized phrases
projects = []
for line in texts.split('\n'):
    if 'FEMA' in line or 'CalOES' in line or 'Disaster' in line or 'disaster' in line:
        projects.append(line.strip())

# Also, find project names mentioned in funding that are likely disaster projects (suffixes)
fund_df = pd.DataFrame(funding)
fund_df['is_disaster_name'] = fund_df['Project_Name'].str.contains('\(FEMA', case=False, regex=False) | fund_df['Project_Name'].str.contains('CalOES', case=False, regex=False) | fund_df['Project_Name'].str.contains('CalJPIA', case=False, regex=False)

# Assume all such are disaster type
# Now need those that started in 2022; search in civic text for occurrences of project name near a 2022 date

start_2022_projects = set()

for pname in fund_df.loc[fund_df['is_disaster_name'], 'Project_Name']:
    if not isinstance(pname, str):
        continue
    # escape for regex
    pattern = re.escape(pname[:40])  # partial to allow small mismatches
    for m in re.finditer(pattern, texts):
        window = texts[max(0, m.start()-100): m.end()+100]
        if '2022' in window:
            start_2022_projects.add(pname)
            break

# Filter funding to these projects and sum Amount
fund_df['Amount'] = pd.to_numeric(fund_df['Amount'])
mask = fund_df['Project_Name'].isin(start_2022_projects)

 total_funding = float(fund_df.loc[mask, 'Amount'].sum())

result = {"total_funding_2022_disaster_projects": total_funding, "projects": sorted(list(start_2022_projects))}

print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_U7kOMfpDIhawztaDfw2UtvCq': 'file_storage/call_U7kOMfpDIhawztaDfw2UtvCq.json', 'var_call_432j1WT3jZgqIFOaNmGsA3A5': 'file_storage/call_432j1WT3jZgqIFOaNmGsA3A5.json'}

exec(code, env_args)
