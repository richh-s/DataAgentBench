code = """import re, json, pandas as pd, os, textwrap

# Load full civic docs
path_docs = var_call_h2vugZBISAZhlGnLPs5gVeYj
with open(path_docs, 'r') as f:
    docs = json.load(f)
texts = [d['text'] for d in docs]
full_text = '\n'.join(texts)

# Heuristic: consider "Project" lines followed by schedules; extract project name and any 'Begin Construction' or 'Start' lines
projects = {}
lines = full_text.split('\n')
current_project = None
for line in lines:
    stripped = line.strip()
    if not stripped:
        continue
    # project title line heuristic: ends with 'Project' or 'Improvements' or 'Repairs' or 'Facility' or 'Maintenance' etc.
    if re.match(r'.*(Project|Improvements|Repairs|Maintenance|Facility|Study|Playground|Park|Biofilter)', stripped) and not stripped.startswith('('):
        current_project = stripped
        projects.setdefault(current_project, set())
        continue
    if current_project:
        # look for start phrases in 2022 Spring timeframe
        if re.search(r'Begin (Construction|Design):?\s*(Spring 2022|March 2022|April 2022|May 2022|2022-Spring)', stripped, re.IGNORECASE) or \
           re.search(r'Start (Construction|Design):?\s*(Spring 2022|March 2022|April 2022|May 2022|2022-Spring)', stripped, re.IGNORECASE):
            projects[current_project].add('Spring 2022')

spring_projects = [name for name, seasons in projects.items() if 'Spring 2022' in seasons]

# Load funding table
funding = var_call_UvDtXapE7vT6G5nCBlCwTOMB
if isinstance(funding, str) and os.path.isfile(funding):
    with open(funding, 'r') as f:
        funding_records = json.load(f)
else:
    funding_records = funding

df_fund = pd.DataFrame(funding_records)

# Join by exact project name; count and sum funding
matched = df_fund[df_fund['Project_Name'].isin(spring_projects)].copy()
matched['Amount'] = pd.to_numeric(matched['Amount'], errors='coerce').fillna(0)
project_count = int(matched['Project_Name'].nunique())
amount_sum = float(matched['Amount'].sum())

result = {"project_count_spring_2022": project_count, "total_funding_spring_2022": amount_sum, "matched_projects": spring_projects}

out = json.dumps(result)
print("__RESULT__:")
print(out)"""

env_args = {'var_call_h2vugZBISAZhlGnLPs5gVeYj': 'file_storage/call_h2vugZBISAZhlGnLPs5gVeYj.json', 'var_call_UvDtXapE7vT6G5nCBlCwTOMB': 'file_storage/call_UvDtXapE7vT6G5nCBlCwTOMB.json'}

exec(code, env_args)
