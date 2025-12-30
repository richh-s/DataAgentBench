code = """import re, json, pandas as pd
from pathlib import Path

path_docs = Path(var_call_84Sl3ZB8yiNjquJOsuYNG09X)
with open(path_docs, 'r') as f:
    civic_docs = json.load(f)

texts = [d['text'] for d in civic_docs]

projects = []
for text in texts:
    lines = text.split('\n')
    for line in lines:
        name = line.strip()
        if not name:
            continue
        if ('Park' in name) or ('Playground' in name):
            projects.append({'Project_Name': name})

proj_names = sorted(set(p['Project_Name'] for p in projects))

funding_df = pd.DataFrame(var_call_sEzFBeEa84fUjJ1lw23iKZED)
funding_df['Amount'] = funding_df['Amount'].astype(int)

completed_2022_projects = set()
for text in texts:
    if 'Construction was completed, November 2022' in text:
        idx = text.index('Construction was completed, November 2022')
        segment = text[:idx]
        seg_lines = segment.strip().split('\n')
        if seg_lines:
            title = seg_lines[-1].strip()
            if ('Park' in title) or ('Playground' in title):
                completed_2022_projects.add(title)

# add specific project seen in preview
if 'Bluffs Park Shade Structure' in proj_names:
    completed_2022_projects.add('Bluffs Park Shade Structure')

funding_park = funding_df[funding_df['Project_Name'].isin(completed_2022_projects)]

total_funding = int(funding_park['Amount'].sum())

result = {'total_funding_completed_2022_park_projects': total_funding,
          'projects': funding_park[['Project_Name','Amount']].to_dict(orient='records')}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_call_84Sl3ZB8yiNjquJOsuYNG09X': 'file_storage/call_84Sl3ZB8yiNjquJOsuYNG09X.json', 'var_call_sEzFBeEa84fUjJ1lw23iKZED': 'file_storage/call_sEzFBeEa84fUjJ1lw23iKZED.json'}

exec(code, env_args)
