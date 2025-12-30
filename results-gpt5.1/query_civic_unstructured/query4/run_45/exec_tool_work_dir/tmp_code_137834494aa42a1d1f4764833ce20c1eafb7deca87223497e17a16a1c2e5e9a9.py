code = """import re, json, pandas as pd

with open(var_call_gF5Pxs8mRXaW6GSwBRKYdYKv, 'r') as f:
    civic_docs = json.load(f)

funding = pd.DataFrame(var_call_C7YFs3RQhPXA5Fqk3d0YPKSC)
funding['Amount'] = funding['Amount'].astype(int)

project_starts = []
for doc in civic_docs:
    text = doc.get('text', '')
    lines = text.split('\n')
    for i, line in enumerate(lines):
        name = line.strip()
        if not name:
            continue
        if not re.search(r'Project|Improvements|Repairs|Park|Road|Facility|Canyon|Drain|Bridge|Playground|Water|Median|Crosswalk|Biofilter|Warning|Signals|Study', name):
            continue
        window = '\n'.join(lines[i:i+15])
        if re.search(r'(Begin Construction|Start|Project Schedule|Estimated Schedule)[^\n]*Spring 2022', window, re.IGNORECASE):
            project_starts.append(name)

project_starts = sorted(set(project_starts))

projects_df = pd.DataFrame({'Project_Name': project_starts})
funding['Project_Name_lower'] = funding['Project_Name'].str.lower()
projects_df['Project_Name_lower'] = projects_df['Project_Name'].str.lower()

merged = projects_df.merge(funding, on='Project_Name_lower', how='left')
funded = merged[~merged['Funding_ID'].isna()]

num_projects = int(funded['Project_Name_lower'].nunique())

total_funding = int(funded['Amount'].sum()) if num_projects > 0 else 0

result = {'num_projects_started_spring_2022': num_projects, 'total_funding_spring_2022': total_funding}

out = json.dumps(result)
print("__RESULT__:")
print(out)"""

env_args = {'var_call_gF5Pxs8mRXaW6GSwBRKYdYKv': 'file_storage/call_gF5Pxs8mRXaW6GSwBRKYdYKv.json', 'var_call_C7YFs3RQhPXA5Fqk3d0YPKSC': 'file_storage/call_C7YFs3RQhPXA5Fqk3d0YPKSC.json'}

exec(code, env_args)
