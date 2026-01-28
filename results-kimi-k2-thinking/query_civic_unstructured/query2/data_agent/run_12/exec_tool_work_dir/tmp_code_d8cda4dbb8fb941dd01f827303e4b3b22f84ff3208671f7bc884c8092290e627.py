code = """import json, re
import pandas as pd

funding_path = '/home/user/funding_data.json'
civic_path = '/home/user/civic_docs_data.json'

with open(funding_path) as f:
    funding = json.load(f)

with open(civic_path) as f:
    civic = json.load(f)

df_funding = pd.DataFrame(funding)
print('Funding loaded', len(df_funding))

park_projects = []
for doc in civic:
    text = doc.get('text', '')
    lines = text.split('\n')
    for i, line in enumerate(lines):
        line = line.strip()
        if not line:
            continue
        if 'park' in line.lower() and len(line) < 90:
            context = ' '.join(lines[i:i+8]).lower()
            if '2022' in context and 'completed' in context:
                park_projects.append(line)
                print('Project found', line)

def clean_name(n):
    if not n:
        return ''
    n = re.sub(r'(?i)\s+Project\s*$', '', n)
    n = re.sub(r'(?i)\s*-\s*Design\s*$', '', n)
    n = re.sub(r'(?i)\s*-\s*Construction\s*$', '', n)
    return n.strip().lower()

df_funding['clean'] = df_funding['Project_Name'].apply(clean_name)
df_funding['amount_num'] = df_funding['Amount'].astype(int)

total = 0
for park in park_projects:
    park_clean = clean_name(park)
    if not park_clean:
        continue
    for _, row in df_funding.iterrows():
        fund = row['clean']
        if fund and (park_clean in fund or fund in park_clean):
            total += row['amount_num']
            print('Matched', park, '->', row['Project_Name'], '=', row['amount_num'])

print('__RESULT__:')
print(json.dumps({'total_funding': total}))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json'}

exec(code, env_args)
