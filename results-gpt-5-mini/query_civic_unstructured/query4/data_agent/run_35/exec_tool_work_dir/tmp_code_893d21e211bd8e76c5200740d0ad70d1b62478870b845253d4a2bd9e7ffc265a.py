code = """import json
import pandas as pd
import re

# Load data from storage-provided variables
civic_path = var_call_i2pMnNzEtdd5lYvmGV3JORo0
funding_path = var_call_E0J4qSiBHu2E6MF8mzAh9B6l

with open(civic_path, 'r', encoding='utf-8') as f:
    civic_docs = json.load(f)
with open(funding_path, 'r', encoding='utf-8') as f:
    funding_records = json.load(f)

funding_df = pd.DataFrame(funding_records)
# Normalize Amount to int
funding_df['Amount'] = funding_df['Amount'].astype(int)
funding_df['pn_lower'] = funding_df['Project_Name'].str.lower().str.strip()

projects_started_spring_2022 = []

for doc in civic_docs:
    text = doc.get('text', '')
    lines = text.splitlines()
    for idx, line in enumerate(lines):
        low = line.lower()
        if 'begin construction' in low and 'spring' in low and '2022' in low:
            # scan upward to find project title
            j = idx - 1
            project_name = None
            while j >= 0:
                candidate = lines[j].strip()
                cand_low = candidate.lower()
                # skip empty lines and common section headers/metadata
                if (not candidate
                    or cand_low.startswith('updates')
                    or cand_low.startswith('project schedule')
                    or cand_low.startswith('project description')
                    or cand_low.startswith('capital improvement')
                    or cand_low.startswith('agenda')
                    or cand_low.startswith('page')
                    or cand_low.startswith('item')
                    or cand_low.startswith('subject')
                    or cand_low.startswith('recommended')
                    or cand_low.startswith('discussion')
                    or cand_low.startswith('cid:')
                   ):
                    j -= 1
                    continue
                # if the candidate looks like a short header like 'Project Updates:' skip
                if len(candidate) < 3:
                    j -= 1
                    continue
                # Otherwise take this as project name
                project_name = candidate
                break
            if project_name:
                # clean project name
                project_name = project_name.strip(' \t:\u2019\u2013')
                projects_started_spring_2022.append(project_name)

# deduplicate while preserving order
seen = set()
projects = []
for p in projects_started_spring_2022:
    key = p.lower()
    if key not in seen:
        seen.add(key)
        projects.append(p)

# For each project, find matching funding records
project_funding = []
for p in projects:
    p_low = p.lower().strip()
    # exact match
    matches = funding_df[funding_df['pn_lower'] == p_low]
    # if none, try contains
    if matches.empty:
        matches = funding_df[funding_df['pn_lower'].str.contains(re.escape(p_low))]
    # if still none, try reverse contains (project name contains funding name)
    if matches.empty:
        matches = funding_df[funding_df['pn_lower'].apply(lambda x: p_low in x)]
    total = int(matches['Amount'].sum()) if not matches.empty else 0
    project_funding.append({'project_name': p, 'funding': total, 'matched_rows': matches.shape[0]})

num_projects = len(projects)
total_funding = sum([pf['funding'] for pf in project_funding])

# Prepare result
result = {
    'num_projects': num_projects,
    'total_funding': total_funding,
    'projects': project_funding
}

import json as _json
print('__RESULT__:')
print(_json.dumps(result))"""

env_args = {'var_call_i2pMnNzEtdd5lYvmGV3JORo0': 'file_storage/call_i2pMnNzEtdd5lYvmGV3JORo0.json', 'var_call_E0J4qSiBHu2E6MF8mzAh9B6l': 'file_storage/call_E0J4qSiBHu2E6MF8mzAh9B6l.json'}

exec(code, env_args)
