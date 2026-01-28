code = """import re, json, pandas as pd

# Load full civic docs
import pathlib, json as jsonlib
path = var_call_ZGWwBakBIQYhbKSh7caDx0aF
with open(path, 'r') as f:
    civic_docs = jsonlib.load(f)

# Simple heuristic: a project line starts at beginning and has a year or capitalized words; disaster if contains FEMA/CalOES or 'Disaster Recovery'
projects = []
for doc in civic_docs:
    text = doc.get('text','')
    for line in text.split('\n'):
        line = line.strip()
        if not line:
            continue
        if any(kw in line for kw in ['Project','Improvements','Repairs','Warning','Canyon','Park','Bridge','Storm','Drain']) and not line.endswith(':'):
            # crude date search in nearby text
            # for simplicity, look for patterns like 'Begin Construction: Fall 2022' or '2022' on same line
            st = None
            if '2022' in line:
                st = '2022'
            # classify type
            lcl = line.lower()
            ptype = 'disaster' if ('fema' in lcl or 'caloes' in lcl or 'woolsey' in lcl or 'disaster' in lcl) else 'capital'
            projects.append({'Project_Name': line, 'type': ptype, 'st': st})

# Now load funding table
path_f = var_call_z90Et5cc3455n0aINWlQsQOl
with open(path_f, 'r') as f:
    funding = jsonlib.load(f)

fund_df = pd.DataFrame(funding)
fund_df['Amount'] = fund_df['Amount'].astype(int)

proj_df = pd.DataFrame(projects)

# Join on project name exact match
merged = fund_df.merge(proj_df, on='Project_Name', how='inner')

# Filter disaster type and start year 2022
mask = (merged['type']=='disaster') & (merged['st'].fillna('').str.contains('2022'))
result_sum = int(merged.loc[mask, 'Amount'].sum())

out = json.dumps(result_sum)
print('__RESULT__:')
print(out)"""

env_args = {'var_call_ZGWwBakBIQYhbKSh7caDx0aF': 'file_storage/call_ZGWwBakBIQYhbKSh7caDx0aF.json', 'var_call_z90Et5cc3455n0aINWlQsQOl': 'file_storage/call_z90Et5cc3455n0aINWlQsQOl.json'}

exec(code, env_args)
