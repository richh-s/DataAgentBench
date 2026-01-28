code = """import json
import pandas as pd
import re

print('Loading data files')
with open('/home/user/funding_data.json', 'r') as f:
    funding_data = json.load(f)

with open('/home/user/civic_docs_data.json', 'r') as f:
    civic_docs_data = json.load(f)

df_funding = pd.DataFrame(funding_data)
print('Funding records loaded', len(df_funding))

park_projects_2022 = []
for doc in civic_docs_data:
    lines = doc['text'].split('\n')
    for i in range(len(lines)):
        line = lines[i].strip()
        if not line or len(line) > 80 or line.startswith('(') or line.startswith('•'):
            continue
        if 'park' in line.lower():
            next_text = ' '.join(lines[i:i+8]).lower()
            if '2022' in next_text and 'completed' in next_text:
                park_projects_2022.append(line)
                print('Found:', line)

print('Park projects found:', len(park_projects_2022))

def clean_name(name):
    name = re.sub(r'\s+Project\s*$', '', name, flags=re.IGNORECASE)
    name = re.sub(r'\s*-\s*Design\s*$', '', name, flags=re.IGNORECASE)
    name = re.sub(r'\s*-\s*Construction\s*$', '', name, flags=re.IGNORECASE)
    return name.strip().lower()

df_funding['clean_name'] = df_funding['Project_Name'].apply(clean_name)
clean_park_projects = [clean_name(p) for p in park_projects_2022]

total_funding = 0
matched_projects = []

for i, park_name in enumerate(clean_park_projects):
    matches = df_funding[df_funding['clean_name'].str.contains(park_name, na=False) | 
                        df_funding['Project_Name'].str.contains(park_name, na=False)]
    for _, match_row in matches.iterrows():
        amount = int(match_row['Amount'])
        total_funding += amount
        matched_projects.append({
            'park_project': park_projects_2022[i],
            'funding_record': match_row['Project_Name'],
            'amount': amount
        })
        print('Match found:', park_projects_2022[i], '->', match_row['Project_Name'], '=', amount)

for i, park_name in enumerate(clean_park_projects):
    for _, fund_row in df_funding.iterrows():
        fund_name = fund_row['clean_name']
        if park_name in fund_name or fund_name in park_name:
            amount = int(fund_row['Amount'])
            already = any(m['park_project'] == park_projects_2022[i] and m['funding_record'] == fund_row['Project_Name'] for m in matched_projects)
            if not already:
                total_funding += amount
                matched_projects.append({
                    'park_project': park_projects_2022[i],
                    'funding_record': fund_row['Project_Name'],
                    'amount': amount
                })
                print('Additional match:', park_projects_2022[i], '->', fund_row['Project_Name'], '=', amount)

print('Total funding:', total_funding)
result = {'total_funding': total_funding, 'matched_projects': matched_projects}
print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json'}

exec(code, env_args)
