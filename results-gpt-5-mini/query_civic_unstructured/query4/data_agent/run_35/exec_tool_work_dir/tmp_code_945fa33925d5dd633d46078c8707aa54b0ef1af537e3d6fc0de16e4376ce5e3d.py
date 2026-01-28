code = """import json
import re
import pandas as pd

civic_path = var_call_i2pMnNzEtdd5lYvmGV3JORo0
funding_path = var_call_E0J4qSiBHu2E6MF8mzAh9B6l

with open(civic_path, 'r', encoding='utf-8') as f:
    civic_docs = json.load(f)
with open(funding_path, 'r', encoding='utf-8') as f:
    funding_records = json.load(f)

funding_df = pd.DataFrame(funding_records)
funding_df['Amount'] = funding_df['Amount'].astype(int)
funding_df['pn_norm'] = funding_df['Project_Name'].str.lower().str.replace('\n',' ').str.strip()

spring_months = ['march', 'april', 'may']

found_titles = []

for doc in civic_docs:
    text = doc.get('text','')
    lines = [ln.rstrip() for ln in text.splitlines()]
    n = len(lines)
    # find candidate title lines
    for i, line in enumerate(lines):
        if not line or len(line) < 15:
            continue
        low = line.lower()
        if low.startswith('(cid') or low.startswith('page') or low.startswith('agenda') or low.startswith('item'):
            continue
        # count capitalized words
        caps = re.findall(r"\b[A-Z][a-z]+", line)
        if len(caps) >= 2:
            # check following lines for begin construction with spring 2022
            window = ' '.join(lines[i+1:i+12]).lower()
            if 'begin construction' in window and (('2022' in window) or any(m in window for m in spring_months) or 'spring' in window):
                title = line.strip()
                found_titles.append(title)
            else:
                # sometimes schedule appears above title, check after some markers
                # also check within nearby lines for 'advertise: spring 2022' or 'complete design: spring 2022' with Begin Construction maybe elsewhere
                sched_window = ' '.join(lines[max(0,i-12):i+12]).lower()
                if 'begin construction' in sched_window and (('2022' in sched_window) or any(m in sched_window for m in spring_months) or 'spring' in sched_window):
                    title = line.strip()
                    found_titles.append(title)

# deduplicate preserving order
seen = set()
projects = []
for t in found_titles:
    k = t.lower()
    if k not in seen:
        seen.add(k)
        projects.append(t)

# match to funding
project_matches = []
for p in projects:
    p_norm = p.lower().strip()
    # try exact match
    matches = funding_df[funding_df['pn_norm'] == p_norm]
    # try removing parenthetical parts from funding names and project name
    p_base = re.sub(r"\s*\(.*\)$", "", p_norm).strip()
    if matches.empty:
        fnorm = funding_df['pn_norm'].str.replace(r"\s*\(.*\)$", "", regex=True).str.strip()
        matches = funding_df[fnorm == p_base]
    # try contains both ways
    if matches.empty:
        matches = funding_df[funding_df['pn_norm'].str.contains(re.escape(p_base))]
    if matches.empty:
        matches = funding_df[funding_df['pn_norm'].str.contains(re.escape(p_norm))]
    # as fallback, try if project name contains a funding name
    if matches.empty:
        for idx, row in funding_df.iterrows():
            if row['pn_norm'] in p_norm:
                matches = pd.DataFrame([row]) if matches.empty else matches.append(row)
    total = int(matches['Amount'].sum()) if not matches.empty else 0
    project_matches.append({'project_name': p, 'matched_rows': int(matches.shape[0]) if hasattr(matches, 'shape') else 0, 'funding': int(total)})

num_projects = len(project_matches)
total_funding = sum([m['funding'] for m in project_matches])

result = {'num_projects': num_projects, 'total_funding': total_funding, 'projects': project_matches}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_call_i2pMnNzEtdd5lYvmGV3JORo0': 'file_storage/call_i2pMnNzEtdd5lYvmGV3JORo0.json', 'var_call_E0J4qSiBHu2E6MF8mzAh9B6l': 'file_storage/call_E0J4qSiBHu2E6MF8mzAh9B6l.json', 'var_call_Zh3YHdg04leUxuZJ8Q6l7HfJ': {'num_projects': 8, 'total_funding': 0, 'projects': [{'project_name': '(cid:131) Complete Design: March 2022', 'funding': 0, 'matched_rows': 0}, {'project_name': '(cid:131) Advertise: Spring/Summer 2022', 'funding': 0, 'matched_rows': 0}, {'project_name': '(cid:131) Complete Design: Spring 2022', 'funding': 0, 'matched_rows': 0}, {'project_name': '(cid:131) Complete Design: February 2022', 'funding': 0, 'matched_rows': 0}, {'project_name': '(cid:131) Complete Design: Winter 2021', 'funding': 0, 'matched_rows': 0}, {'project_name': '(cid:131) Advertise: Spring 2022', 'funding': 0, 'matched_rows': 0}, {'project_name': '(cid:131) Complete Design: Winter 2021/2022', 'funding': 0, 'matched_rows': 0}, {'project_name': '(cid:131) Complete Design: January 2022', 'funding': 0, 'matched_rows': 0}]}}

exec(code, env_args)
