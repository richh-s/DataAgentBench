code = """import re, json, pandas as pd

# Load funding > 50k
funding_records = var_call_PLevRjtKtnuu2GdFFtJnDWrB
funding_df = pd.DataFrame(funding_records)

# Normalize project names for joining
funding_df['name_norm'] = funding_df['Project_Name'].str.lower().str.replace(r'\s+', ' ', regex=True).str.strip()

# From civic docs text, extract project blocks and infer status and type.
# For this synthetic dataset, we will approximate by:
# - Any project mentioned under a heading containing 'Capital Improvement Projects (Design)' is type 'capital', status 'design'.
# - Project names are lines that are not empty and not headings and are in Title Case-ish.

texts = [doc['text'] for doc in var_call_GzTtGNJ9RV0qW89HRRW4YU8a]

projects = []
for text in texts:
    lines = [l.strip() for l in text.split('\n')]
    status = None
    current_section = None
    for i, line in enumerate(lines):
        if 'Capital Improvement Projects (Design)' in line:
            current_section = 'capital_design'
            continue
        if 'Capital Improvement Projects (Construction)' in line or 'Capital Improvement Projects (Not Started)' in line:
            current_section = None
        # Collect project lines while in capital_design section
        if current_section == 'capital_design':
            if not line or line.startswith('(') or ':' in line:
                continue
            # Heuristic: project name lines often have multiple words and at least one lowercase
            if len(line.split()) >= 2 and any(c.islower() for c in line):
                name = re.sub(r'\s+', ' ', line).strip()
                projects.append({'Project_Name': name, 'type': 'capital', 'status': 'design'})

projects_df = pd.DataFrame(projects).drop_duplicates()
projects_df['name_norm'] = projects_df['Project_Name'].str.lower().str.replace(r'\s+', ' ', regex=True).str.strip()

# Join funding with projects on normalized name
merged = pd.merge(funding_df, projects_df, on='name_norm', how='inner')

# Filter to capital type and design status, amount > 50000 (already filtered)
merged_capital_design = merged[(merged['type'] == 'capital') & (merged['status'] == 'design')]

count_projects = int(merged_capital_design['Project_Name_x'].nunique())

result = json.dumps({'capital_design_projects_over_50000_count': count_projects})

print('__RESULT__:')
print(result)"""

env_args = {'var_call_PLevRjtKtnuu2GdFFtJnDWrB': 'file_storage/call_PLevRjtKtnuu2GdFFtJnDWrB.json', 'var_call_GzTtGNJ9RV0qW89HRRW4YU8a': 'file_storage/call_GzTtGNJ9RV0qW89HRRW4YU8a.json'}

exec(code, env_args)
