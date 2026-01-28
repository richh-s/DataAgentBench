code = """import json
import pandas as pd

civic_path = var_call_i2pMnNzEtdd5lYvmGV3JORo0
funding_path = var_call_E0J4qSiBHu2E6MF8mzAh9B6l

with open(civic_path, 'r', encoding='utf-8') as f:
    civic_docs = json.load(f)
with open(funding_path, 'r', encoding='utf-8') as f:
    funding_records = json.load(f)

funding_df = pd.DataFrame(funding_records)
funding_df['Amount'] = funding_df['Amount'].astype(int)
funding_df['pn_lower'] = funding_df['Project_Name'].str.lower()

found = []
for doc in civic_docs:
    text = doc.get('text','')
    lower = text.lower()
    start = 0
    while True:
        idx = lower.find('begin construction', start)
        if idx == -1:
            break
        window = lower[max(0, idx-200): idx+200]
        # Check for spring 2022 context
        if ('spring' in window and '2022' in window) or (('2022' in window) and any(m in window for m in ['march','april','may'])):
            # find title by scanning lines before this position
            preceding = text[:idx]
            lines = preceding.splitlines()
            title = None
            for line in reversed(lines):
                s = line.strip()
                if not s:
                    continue
                low = s.lower()
                if low.startswith('(cid') or low.startswith('updates') or low.startswith('project schedule') or low.startswith('project description') or low.startswith('page') or low.startswith('agenda') or low.startswith('item') or low.startswith('subject') or low.startswith('recommended') or low.startswith('discussion'):
                    continue
                if len(s) < 4:
                    continue
                title = s
                break
            if title:
                found.append(title)
        start = idx + 1

# deduplicate
seen = set()
projects = []
for p in found:
    key = p.lower()
    if key not in seen:
        seen.add(key)
        projects.append(p)

# match to funding
project_matches = []
for p in projects:
    p_base = p.lower().split('(')[0].strip()
    # exact
    matches = funding_df[funding_df['pn_lower'] == p.lower()]
    if matches.empty:
        matches = funding_df[funding_df['pn_lower'].str.contains(p_base)]
    total = int(matches['Amount'].sum()) if not matches.empty else 0
    project_matches.append({'project_name': p, 'matched_rows': int(matches.shape[0]) if not matches.empty else 0, 'funding': int(total)})

num_projects = len(project_matches)
total_funding = sum(m['funding'] for m in project_matches)

result = {'num_projects': num_projects, 'total_funding': total_funding, 'projects': project_matches}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_call_i2pMnNzEtdd5lYvmGV3JORo0': 'file_storage/call_i2pMnNzEtdd5lYvmGV3JORo0.json', 'var_call_E0J4qSiBHu2E6MF8mzAh9B6l': 'file_storage/call_E0J4qSiBHu2E6MF8mzAh9B6l.json', 'var_call_Zh3YHdg04leUxuZJ8Q6l7HfJ': {'num_projects': 8, 'total_funding': 0, 'projects': [{'project_name': '(cid:131) Complete Design: March 2022', 'funding': 0, 'matched_rows': 0}, {'project_name': '(cid:131) Advertise: Spring/Summer 2022', 'funding': 0, 'matched_rows': 0}, {'project_name': '(cid:131) Complete Design: Spring 2022', 'funding': 0, 'matched_rows': 0}, {'project_name': '(cid:131) Complete Design: February 2022', 'funding': 0, 'matched_rows': 0}, {'project_name': '(cid:131) Complete Design: Winter 2021', 'funding': 0, 'matched_rows': 0}, {'project_name': '(cid:131) Advertise: Spring 2022', 'funding': 0, 'matched_rows': 0}, {'project_name': '(cid:131) Complete Design: Winter 2021/2022', 'funding': 0, 'matched_rows': 0}, {'project_name': '(cid:131) Complete Design: January 2022', 'funding': 0, 'matched_rows': 0}]}}

exec(code, env_args)
