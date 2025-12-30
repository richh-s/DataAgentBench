code = """import re, json, pandas as pd

path_docs = var_call_b3v6pQbcukgatx6zXyMtvRWO
with open(path_docs, 'r') as f:
    civic_docs = json.load(f)

path_fund = var_call_3LcqDBRsgKnCjjjnZU9cIitw
with open(path_fund, 'r') as f:
    funding = json.load(f)

fund_df = pd.DataFrame(funding)

pattern = re.compile(r'^(?P<name>.*?(Project|Improvements|Repairs|Resurfacing|Storm Drain|Road Slope|Roadway/Retaining Wall Improvements|Playground|Park|Biofilter|Water Treatment Facility|Green Streets|Crosswalk Improvements).*?)$', re.IGNORECASE)

projects = []
for doc in civic_docs:
    for line in doc['text'].split('\n'):
        line = line.strip()
        m = pattern.match(line)
        if m:
            name = m.group('name').strip()
            projects.append({'Project_Name': name})

proj_df = pd.DataFrame(projects).drop_duplicates()

spring2022_docs = []
for doc in civic_docs:
    text_lower = doc['text'].lower()
    if ('spring 2022' in text_lower) or ('2022-spring' in text_lower) or ('march 2022' in text_lower) or ('april 2022' in text_lower) or ('may 2022' in text_lower):
        spring2022_docs.append(doc)

spring_projects = set()
for doc in spring2022_docs:
    for line in doc['text'].split('\n'):
        line = line.strip()
        m = pattern.match(line)
        if m:
            spring_projects.add(m.group('name').strip())

spring_proj_df = pd.DataFrame({'Project_Name': list(spring_projects)})

merged = pd.merge(spring_proj_df, fund_df, on='Project_Name', how='inner')

merged['Amount'] = pd.to_numeric(merged['Amount'])

result = {
    'projects_count': int(merged['Project_Name'].nunique()),
    'total_funding': int(merged['Amount'].sum())
}

import json as _json
out = _json.dumps(result)
print("__RESULT__:")
print(out)"""

env_args = {'var_call_b3v6pQbcukgatx6zXyMtvRWO': 'file_storage/call_b3v6pQbcukgatx6zXyMtvRWO.json', 'var_call_3LcqDBRsgKnCjjjnZU9cIitw': 'file_storage/call_3LcqDBRsgKnCjjjnZU9cIitw.json'}

exec(code, env_args)
