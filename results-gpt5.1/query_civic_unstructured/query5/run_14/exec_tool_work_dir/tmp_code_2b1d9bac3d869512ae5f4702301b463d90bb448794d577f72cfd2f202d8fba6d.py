code = """import re, json, pandas as pd

# Load full civic docs from file
with open(var_call_regjihqD0YcOz2LaOk1w5e8Z, 'r') as f:
    civic_docs = json.load(f)

texts = ' '.join(doc['text'] for doc in civic_docs)

# Get funding table from storage variable (it's a filepath string)
with open(var_call_sNebHVFA58PyIoie8pT1LswA, 'r') as f:
    funding_records = json.load(f)

fund_df = pd.DataFrame(funding_records)
fund_df['Amount'] = pd.to_numeric(fund_df['Amount'])

# Disaster-type projects: those that have FEMA/CalOES/CalJPIA in the project name
disaster_mask = fund_df['Project_Name'].str.contains('FEMA|CalOES|CalJPIA', case=False, regex=True)

disaster_funding = fund_df[disaster_mask].copy()

# Identify project names in civic docs that are disaster projects and have 2022 in a nearby date string.
# Heuristic: search for lines containing FEMA/CalOES/CalJPIA and also '2022'
projects_2022 = set()
for line in texts.split('\n'):
    line_stripped = line.strip()
    if not line_stripped:
        continue
    if ('2022' in line_stripped) and (('FEMA' in line_stripped) or ('CalOES' in line_stripped) or ('CalJPIA' in line_stripped)):
        projects_2022.add(line_stripped)

# Map these noisy lines to funding project names by substring matching
proj_names_2022 = set()
for noisy in projects_2022:
    for name in disaster_funding['Project_Name']:
        if name in noisy or noisy in name:
            proj_names_2022.add(name)

# Additionally, include any disaster projects whose own name includes '2022'
for name in disaster_funding['Project_Name']:
    if '2022' in name:
        proj_names_2022.add(name)

fund_2022_disaster = disaster_funding[disaster_funding['Project_Name'].isin(sorted(proj_names_2022))]

total_2022_disaster = float(fund_2022_disaster['Amount'].sum())

result = {
    'total_2022_disaster_funding': total_2022_disaster,
    'matched_project_names': sorted(proj_names_2022)
}

out = json.dumps(result)
print('__RESULT__:')
print(out)"""

env_args = {'var_call_regjihqD0YcOz2LaOk1w5e8Z': 'file_storage/call_regjihqD0YcOz2LaOk1w5e8Z.json', 'var_call_sNebHVFA58PyIoie8pT1LswA': 'file_storage/call_sNebHVFA58PyIoie8pT1LswA.json'}

exec(code, env_args)
