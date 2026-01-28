code = """import json
import pandas as pd
import re

funding_path = '/home/user/funding_data.json'
civic_path = '/home/user/civic_docs_data.json'

with open(funding_path, 'r') as f:
    funding_data = json.load(f)

with open(civic_path, 'r') as f:
    civic_docs_data = json.load(f)

df_funding = pd.DataFrame(funding_data)

park_projects_2022 = []
for doc in civic_docs_data:
    lines = doc['text'].split('\n')
    for i in range(len(lines)):
        line = lines[i].strip()
        if not line or len(line) > 80 or line.startswith('(') or line.startswith('•'):
            continue
        if 'park' in line.lower() and 'Updates:' not in line:
            next_text = ' '.join(lines[i:i+8]).lower()
            if '2022' in next_text and 'completed' in next_text:
                park_projects_2022.append(line)

def clean_name(name):
    if not name:
        return ''
    name = re.sub(r'\s+Project\s*$', '', name, flags=re.IGNORECASE)
    name = re.sub(r'\s*-\s*Design\s*$', '', name, flags=re.IGNORECASE)
    name = re.sub(r'\s*-\s*Construction\s*$', '', name, flags=re.IGNORECASE)
    return name.strip().lower()

df_funding['clean_name'] = df_funding['Project_Name'].apply(clean_name)
clean_park_names = [clean_name(p) for p in park_projects_2022]

total_funding = 0
matched = []

for i, park_name in enumerate(clean_park_names):
    if not park_name:
        continue
    matches = df_funding[df_funding['clean_name'].str.contains(park_name, na=False, case=False) | 
                        df_funding['Project_Name'].str.contains(park_name, na=False, case=False)]
    for _, row in matches.iterrows():
        amount = int(row['Amount'])
        total_funding += amount
        matched.append({
            'park': park_projects_2022[i],
            'funding': row['Project_Name'],
            'amount': amount
        })

for i, park_name in enumerate(clean_park_names):
    if not park_name:
        continue
    for _, row in df_funding.iterrows():
        fund_name = row['clean_name']
        if fund_name and (park_name in fund_name or fund_name in park_name):
            amount = int(row['Amount'])
            is_duplicate = any(m['park'] == park_projects_2022[i] and m['funding'] == row['Project_Name'] for m in matched)
            if not is_duplicate:
                total_funding += amount
                matched.append({
                    'park': park_projects_2022[i],
                    'funding': row['Project_Name'],
                    'amount': amount
                })

result = {
    'total_funding': total_funding,
    'matched_projects': matched,
    'park_projects_found': len(park_projects_2022)
}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json'}

exec(code, env_args)
