code = """import json
import pandas as pd
import re

civic_path = var_call_i2pMnNzEtdd5lYvmGV3JORo0
funding_path = var_call_E0J4qSiBHu2E6MF8mzAh9B6l

with open(civic_path, 'r', encoding='utf-8') as f:
    civic_docs = json.load(f)
with open(funding_path, 'r', encoding='utf-8') as f:
    funding_records = json.load(f)

funding_df = pd.DataFrame(funding_records)
funding_df['Amount'] = funding_df['Amount'].astype(int)
funding_df['pn_norm'] = funding_df['Project_Name'].str.lower().str.replace('\n',' ').str.strip()

found_projects = []

spring_months = ['march', 'april', 'may']

for doc in civic_docs:
    text = doc.get('text','')
    lines = text.splitlines()
    for i, line in enumerate(lines):
        l = line.lower()
        if 'begin construction' in l:
            # Check if this line references 2022 spring months or 'spring' with 2022 nearby
            context = ' '.join(lines[max(0,i-2):i+3]).lower()
            if '2022' in context or any(m in context for m in spring_months) or 'spring' in context:
                # find project title above
                title = None
                for j in range(i-1, max(-1, i-15), -1):
                    cand = lines[j].strip()
                    cand_l = cand.lower()
                    if not cand:
                        continue
                    if cand_l.startswith('(cid') or cand_l.startswith('updates') or cand_l.startswith('project schedule') or cand_l.startswith('project description') or cand_l.startswith('page') or cand_l.startswith('agenda') or cand_l.startswith('item') or cand_l.startswith('subject') or cand_l.startswith('recommended') or cand_l.startswith('discussion'):
                        continue
                    # if it looks like a short metadata like 'Project Updates:' skip
                    if len(cand) < 4:
                        continue
                    # Accept candidate as title
                    title = cand
                    break
                if title:
                    # clean
                    title = title.strip(' \t:\u2013\u2014')
                    found_projects.append(title)

# dedup preserving order
seen = set()
projects = []
for p in found_projects:
    key = p.lower()
    if key not in seen:
        seen.add(key)
        projects.append(p)

# Now try to match to funding
project_matches = []
for p in projects:
    p_norm = p.lower().strip()
    # remove common leading bullets like numbers
    p_norm = re.sub(r'^\d+\.\s*','',p_norm)
    # attempts
    matches = funding_df[funding_df['pn_norm'] == p_norm]
    if matches.empty:
        # remove trailing parenthetical descriptors from funding names and project name
        p_base = re.sub(r"\s*\(.*\)$", "", p_norm).strip()
        matches = funding_df[funding_df['pn_norm'].str.replace(r"\s*\(.*\)$", "", regex=True).str.strip() == p_base]
    if matches.empty:
        matches = funding_df[funding_df['pn_norm'].str.contains(re.escape(p_norm))]
    if matches.empty:
        matches = funding_df[funding_df['pn_norm'].str.contains(re.escape(p_base))]
    total = int(matches['Amount'].sum()) if not matches.empty else 0
    project_matches.append({'project_name': p, 'matched_rows': int(matches.shape[0]), 'funding': int(total)})

num_projects = len(project_matches)
total_funding = sum([m['funding'] for m in project_matches])

result = {'num_projects': num_projects, 'total_funding': total_funding, 'projects': project_matches}

import json as _json
print('__RESULT__:')
print(_json.dumps(result))"""

env_args = {'var_call_i2pMnNzEtdd5lYvmGV3JORo0': 'file_storage/call_i2pMnNzEtdd5lYvmGV3JORo0.json', 'var_call_E0J4qSiBHu2E6MF8mzAh9B6l': 'file_storage/call_E0J4qSiBHu2E6MF8mzAh9B6l.json', 'var_call_Zh3YHdg04leUxuZJ8Q6l7HfJ': {'num_projects': 8, 'total_funding': 0, 'projects': [{'project_name': '(cid:131) Complete Design: March 2022', 'funding': 0, 'matched_rows': 0}, {'project_name': '(cid:131) Advertise: Spring/Summer 2022', 'funding': 0, 'matched_rows': 0}, {'project_name': '(cid:131) Complete Design: Spring 2022', 'funding': 0, 'matched_rows': 0}, {'project_name': '(cid:131) Complete Design: February 2022', 'funding': 0, 'matched_rows': 0}, {'project_name': '(cid:131) Complete Design: Winter 2021', 'funding': 0, 'matched_rows': 0}, {'project_name': '(cid:131) Advertise: Spring 2022', 'funding': 0, 'matched_rows': 0}, {'project_name': '(cid:131) Complete Design: Winter 2021/2022', 'funding': 0, 'matched_rows': 0}, {'project_name': '(cid:131) Complete Design: January 2022', 'funding': 0, 'matched_rows': 0}]}}

exec(code, env_args)
