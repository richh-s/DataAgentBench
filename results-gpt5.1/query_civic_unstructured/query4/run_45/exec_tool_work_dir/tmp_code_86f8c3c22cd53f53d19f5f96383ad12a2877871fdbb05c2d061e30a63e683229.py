code = """import re, json, pandas as pd

# Load civic docs full data from file
with open(var_call_gF5Pxs8mRXaW6GSwBRKYdYKv, 'r') as f:
    civic_docs = json.load(f)

funding = pd.DataFrame(var_call_C7YFs3RQhPXA5Fqk3d0YPKSC)

# Normalize Amount to int
funding['Amount'] = funding['Amount'].astype(int)

# Very simple heuristic: assume each line that looks like a project name is a project,
# and try to find a start date pattern near it like 'Begin Construction: Spring 2022' or 'Start: 2022-Spring'.

project_starts = []
for doc in civic_docs:
    text = doc.get('text', '')
    # Split into lines
    lines = text.split('\n')
    for i, line in enumerate(lines):
        name = line.strip()
        if not name:
            continue
        # Heuristic: consider a line a project if it contains keywords like 'Project', 'Improvements', 'Repairs', 'Park', 'Road', 'Facility', 'Canyon', 'Drain', 'Bridge', 'Playground', 'Water', 'Median', 'Crosswalk', 'Biofilter', 'Warning', 'Signals', 'Study'
        if not re.search(r"Project|Improvements|Repairs|Park|Road|Facility|Canyon|Drain|Bridge|Playground|Water|Median|Crosswalk|Biofilter|Warning|Signals|Study", name):
            continue
        # Look ahead a few lines for a begin/start date mentioning Spring 2022
        window = '\n'.join(lines[i:i+15])
        # Patterns that indicate a start
        m = re.search(r"(Begin Construction|Start|Project Schedule|Estimated Schedule)[^\n]*Spring 2022", window, re.IGNORECASE)
        if m:
            project_starts.append(name)

# Deduplicate project names
project_starts = sorted(set(project_starts))

# Now match these to Funding.Project_Name using simple case-insensitive equality
projects_df = pd.DataFrame({'Project_Name': project_starts})

# Case-insensitive merge
funding['Project_Name_lower'] = funding['Project_Name'].str.lower()
projects_df['Project_Name_lower'] = projects_df['Project_Name'].str.lower()

merged = projects_df.merge(funding, on='Project_Name_lower', how='left')

# Filter to those that have funding matches
funded = merged[~merged['Funding_ID'].isna()]

num_projects = int(funded['Project_Name_lower'].nunique())

total_funding = int(funded['Amount'].sum()) if num_projects > 0 else 0

result = {'num_projects_started_spring_2022': num_projects, 'total_funding_spring_2022': total_funding}

out = json.dumps(result)
print("__RESULT__:")
print(out)"""

env_args = {'var_call_gF5Pxs8mRXaW6GSwBRKYdYKv': 'file_storage/call_gF5Pxs8mRXaW6GSwBRKYdYKv.json', 'var_call_C7YFs3RQhPXA5Fqk3d0YPKSC': 'file_storage/call_C7YFs3RQhPXA5Fqk3d0YPKSC.json'}

exec(code, env_args)
