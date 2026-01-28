code = """import re, json, pandas as pd, os, textwrap

# Load full civic docs
path = var_call_HwolQVNE4qqtYYrFDmddDXvs
with open(path, 'r') as f:
    civic_docs = json.load(f)

# Load funding table
path2 = var_call_yqzspAdO4D1uar8cSCOkjqk8
with open(path2, 'r') as f:
    funding = json.load(f)

# Very simple heuristic extraction: we'll look for patterns like 'ProjectName ... Start: 2022-Spring' or 'Begin Construction: Spring 2022'
# For this synthetic dataset, assume that if a line contains '2022-Spring' or 'Spring 2022' it's a start date for the nearest preceding project title line.

projects = []
for doc in civic_docs:
    text = doc.get('text','')
    lines = text.split('\n')
    current_project = None
    for line in lines:
        stripped = line.strip()
        # Heuristic: project title lines are those that are not empty and not too short and in title case-like or contain keywords like 'Project'
        if stripped and ("Project" in stripped or "Improvements" in stripped or "Repairs" in stripped or "Park" in stripped or "Road" in stripped or "Canyon" in stripped):
            current_project = stripped
        if "Spring 2022" in stripped or "2022-Spring" in stripped:
            if current_project:
                projects.append({"Project_Name": current_project, "st": "Spring 2022"})

# Normalize project names for joining with Funding table: we'll try exact match only for this exercise
proj_df = pd.DataFrame(projects).drop_duplicates(subset=['Project_Name'])
fund_df = pd.DataFrame(funding)

# Coerce amount to int
fund_df['Amount'] = fund_df['Amount'].astype(int)

merged = proj_df.merge(fund_df, how='inner', on='Project_Name')

count_projects = int(merged['Project_Name'].nunique())
Total_funding = int(merged['Amount'].sum())

result = {"projects_started_spring_2022": count_projects, "total_funding": Total_funding}

print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_HwolQVNE4qqtYYrFDmddDXvs': 'file_storage/call_HwolQVNE4qqtYYrFDmddDXvs.json', 'var_call_yqzspAdO4D1uar8cSCOkjqk8': 'file_storage/call_yqzspAdO4D1uar8cSCOkjqk8.json', 'var_call_whbnrleLFJRhOWP9EAsG6aZa': ['civic_docs'], 'var_call_zNklrVo5UdoO20nsiSFeUTG5': ['Funding']}

exec(code, env_args)
