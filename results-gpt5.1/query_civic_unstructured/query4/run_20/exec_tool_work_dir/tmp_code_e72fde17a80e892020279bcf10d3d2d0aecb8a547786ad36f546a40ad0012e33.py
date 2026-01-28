code = """import re, json, pandas as pd
from datetime import datetime

# Load full civic docs
with open(var_call_WaTQEHqvDqSfUHtWonBKM6yQ, 'r') as f:
    civic_docs = json.load(f)

funding = pd.DataFrame(json.load(open(var_call_X3JRAqdRs7QtjnOdcomLj6Ji, 'r')))

texts = ' '.join(doc['text'] for doc in civic_docs)

project_blocks = re.split(r'\n\n', texts)

projects = []
current_name = None
for block in project_blocks:
    m = re.match(r'([A-Z0-9].+?Project|[0-9]{4}.+|[A-Z][A-Za-z].+)', block.strip())
    if not m:
        continue
    header = m.group(1).strip()
    name_line = header.split('\n')[0].strip()
    if len(name_line.split()) < 2:
        continue
    if any(kw in name_line for kw in ['Agenda Report','Capital Improvement Projects','Disaster Recovery Projects','Project Description','Project Updates']):
        continue
    current_name = name_line
    lower_block = block.lower()
    st = None
    for kw in ['begin construction','start construction','construction start','project start']:
        m2 = re.search(kw + r'.*?(spring|summer|fall|winter)?\s*(20[0-9]{2})', lower_block)
        if m2:
            season = m2.group(1).title() if m2.group(1) else None
            year = m2.group(2)
            st = f"{year}-{season}" if season else year
            break
    if not st:
        m3 = re.search(r'(spring|summer|fall|winter)\s*(20[0-9]{2})', lower_block)
        if m3:
            season = m3.group(1).title()
            year = m3.group(2)
            st = f"{year}-{season}"
    projects.append({'Project_Name': current_name, 'st': st})

proj_df = pd.DataFrame(projects).dropna(subset=['st']).drop_duplicates('Project_Name')

spring22 = proj_df[proj_df['st'].str.contains('2022-Spring', case=False, na=False)]

merged = spring22.merge(funding, on='Project_Name', how='left')

count_projects = spring22['Project_Name'].nunique()

total_funding = pd.to_numeric(merged['Amount'], errors='coerce').sum()

result = {'projects_started_spring_2022': int(count_projects), 'total_funding': int(total_funding)}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_call_WaTQEHqvDqSfUHtWonBKM6yQ': 'file_storage/call_WaTQEHqvDqSfUHtWonBKM6yQ.json', 'var_call_X3JRAqdRs7QtjnOdcomLj6Ji': 'file_storage/call_X3JRAqdRs7QtjnOdcomLj6Ji.json'}

exec(code, env_args)
