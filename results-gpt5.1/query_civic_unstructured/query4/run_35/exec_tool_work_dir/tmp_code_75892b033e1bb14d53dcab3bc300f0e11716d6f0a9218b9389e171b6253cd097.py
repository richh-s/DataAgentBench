code = """import re, json, pandas as pd, os, textwrap

# Load full civic docs
path_docs = var_call_b3v6pQbcukgatx6zXyMtvRWO
with open(path_docs, 'r') as f:
    civic_docs = json.load(f)

# Load funding table
path_fund = var_call_3LcqDBRsgKnCjjjnZU9cIitw
with open(path_fund, 'r') as f:
    funding = json.load(f)

fund_df = pd.DataFrame(funding)

# Very simple project name extraction: assume project lines are those that end with 'Project' or contain 'Improvements', 'Repairs', 'Resurfacing', etc.
pattern = re.compile(r"^(?P<name>.*?(Project|Improvements|Repairs|Resurfacing|Storm Drain|Road Slope|Roadway/Retaining Wall Improvements|Playground|Park|Biofilter|Water Treatment Facility|Green Streets|Crosswalk Improvements).*?)$", re.IGNORECASE)

projects = []
for doc in civic_docs:
    for line in doc['text'].split('\n'):
        line = line.strip()
        m = pattern.match(line)
        if m:
            name = m.group('name').strip()
            # crude date extraction looking for patterns like '2022-Spring', 'Spring 2022', months with 2022
            # we'll scan nearby context within same doc later if needed
            projects.append({'Project_Name': name})

proj_df = pd.DataFrame(projects).drop_duplicates()

# We'll now try to infer a start time (st) from text patterns containing 2022 and spring months around each project name.
# For simplicity, we will approximate: if the doc contains 'Spring 2022' or '2022-Spring', we treat all projects mentioned as starting in Spring 2022.

spring2022_docs = []
for doc in civic_docs:
    text_lower = doc['text'].lower()
    if 'spring 2022' in text_lower or '2022-spring' in text_lower or 'march 2022' in text_lower or 'april 2022' in text_lower or 'may 2022' in text_lower:
        spring2022_docs.append(doc)

spring_projects = set()
for doc in spring2022_docs:
    for line in doc['text'].split('\n'):
        line = line.strip()
        m = pattern.match(line)
        if m:
            spring_projects.add(m.group('name').strip())

spring_proj_df = pd.DataFrame({'Project_Name': list(spring_projects)})

# Join with funding on exact Project_Name
merged = pd.merge(spring_proj_df, fund_df, on='Project_Name', how='inner')

merged['Amount'] = pd.to_numeric(merged['Amount'])

result = {
    'projects_count': int(merged['Project_Name'].nunique()),
    'total_funding': int(merged['Amount'].sum()),
    'projects': merged[['Project_Name','Amount']].drop_duplicates().to_dict(orient='records')
}

out = json.dumps(result)
print("__RESULT__:")
print(out)"""

env_args = {'var_call_b3v6pQbcukgatx6zXyMtvRWO': 'file_storage/call_b3v6pQbcukgatx6zXyMtvRWO.json', 'var_call_3LcqDBRsgKnCjjjnZU9cIitw': 'file_storage/call_3LcqDBRsgKnCjjjnZU9cIitw.json'}

exec(code, env_args)
