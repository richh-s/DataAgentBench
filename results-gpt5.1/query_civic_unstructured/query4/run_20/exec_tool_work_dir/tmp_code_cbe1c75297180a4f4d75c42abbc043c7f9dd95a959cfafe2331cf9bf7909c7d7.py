code = """import re, json, pandas as pd

with open(var_call_WaTQEHqvDqSfUHtWonBKM6yQ, 'r') as f:
    civic_docs = json.load(f)

with open(var_call_X3JRAqdRs7QtjnOdcomLj6Ji, 'r') as f:
    funding_records = json.load(f)

funding = pd.DataFrame(funding_records)

texts = ' '.join(doc['text'] for doc in civic_docs)

project_blocks = re.split('\n\n', texts)

projects = []
for block in project_blocks:
    block_strip = block.strip()
    if not block_strip:
        continue
    m = re.match('([A-Z0-9].+?Project|[0-9]{4}.+|[A-Z][A-Za-z].+)', block_strip)
    if not m:
        continue
    header = m.group(1).strip()
    name_line = header.split('\n')[0].strip()
    if len(name_line.split()) < 2:
        continue
    skip_terms = ['Agenda Report','Capital Improvement Projects','Disaster Recovery Projects','Project Description','Project Updates']
    skip = False
    for kw in skip_terms:
        if kw in name_line:
            skip = True
            break
    if skip:
        continue
    project_name = name_line
    lower_block = block_strip.lower()
    st = None
    kws = ['begin construction','start construction','construction start','project start']
    for kw in kws:
        pattern = kw + '.*?(spring|summer|fall|winter)?\s*(20[0-9]{2})'
        m2 = re.search(pattern, lower_block)
        if m2:
            season = m2.group(1).title() if m2.group(1) else None
            year = m2.group(2)
            st = year + '-' + season if season else year
            break
    if not st:
        m3 = re.search('(spring|summer|fall|winter)\s*(20[0-9]{2})', lower_block)
        if m3:
            season = m3.group(1).title()
            year = m3.group(2)
            st = year + '-' + season
    projects.append({'Project_Name': project_name, 'st': st})

proj_df = pd.DataFrame(projects)
proj_df = proj_df.dropna(subset=['st']).drop_duplicates('Project_Name')

spring22 = proj_df[proj_df['st'].str.contains('2022-Spring', case=False, na=False)]

merged = spring22.merge(funding, on='Project_Name', how='left')

count_projects = spring22['Project_Name'].nunique()

total_funding = pd.to_numeric(merged['Amount'], errors='coerce').sum()

result = {'projects_started_spring_2022': int(count_projects), 'total_funding': int(total_funding)}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_call_WaTQEHqvDqSfUHtWonBKM6yQ': 'file_storage/call_WaTQEHqvDqSfUHtWonBKM6yQ.json', 'var_call_X3JRAqdRs7QtjnOdcomLj6Ji': 'file_storage/call_X3JRAqdRs7QtjnOdcomLj6Ji.json'}

exec(code, env_args)
