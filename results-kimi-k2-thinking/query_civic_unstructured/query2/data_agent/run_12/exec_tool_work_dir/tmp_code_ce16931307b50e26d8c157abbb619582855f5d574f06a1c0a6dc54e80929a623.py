code = """import json, pandas as pd, re

with open('/home/user/funding_data.json', 'r') as f:
    funding_data = json.load(f)

with open('/home/user/civic_docs_data.json', 'r') as f:
    civic_docs_data = json.load(f)

# Create funding dataframe
df_funding = pd.DataFrame(funding_data)
print('Loaded', len(funding_data), 'funding records')

# Find park projects completed in 2022
park_projects = []
for doc in civic_docs_data:
    text = doc['text']
    if 'park' in text.lower():
        lines = text.split('\n')
        for i in range(len(lines)):
            line = lines[i].strip()
            if not line or 'Updates:' in line:
                continue
            # Check if line contains park-related content
            if 'park' in line.lower() and len(line) < 100:
                # Check surrounding context for completion and 2022
                context = ' '.join(lines[max(0,i-2):i+8]).lower()
                if '2022' in context and ('completed' in context or 'construction was completed' in context):
                    park_projects.append(line)
                    print('Found:', line)

print('Park projects:', len(park_projects))

# Clean names for matching
def clean(name):
    if not isinstance(name, str):
        return ''
    name = re.sub(r'(?i)\s+Project\s*$', '', name)
    name = re.sub(r'(?i)\s*-\s*Design\s*$', '', name)
    name = re.sub(r'(?i)\s*-\s*Construction\s*$', '', name)
    return name.strip().lower()

df_funding['clean'] = df_funding['Project_Name'].apply(clean)
park_clean = [clean(p) for p in park_projects]

# Calculate total funding
total = 0
matched = []

for i, park in enumerate(park_clean):
    if not park:
        continue
    # Find matches
    for _, row in df_funding.iterrows():
        fund = row['clean']
        if fund and (park in fund or fund in park):
            amount = int(row['Amount'])
            total += amount
            matched.append({'park': park_projects[i], 'funding': row['Project_Name'], 'amount': amount})
            print('Match:', park_projects[i], '->', row['Project_Name'], '=', amount)

result = {'total_funding': total, 'matches': len(matched)}
print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json'}

exec(code, env_args)
