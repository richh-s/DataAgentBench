code = """import json, pandas as pd, re

# Load data files
with open('/home/user/funding_data.json', 'r') as f:
    funding_data = json.load(f)

with open('/home/user/civic_docs_data.json', 'r') as f:
    civic_docs_data = json.load(f)

# Create funding dataframe
df_funding = pd.DataFrame(funding_data)
print('Funding records loaded:', len(df_funding))

# Find park projects completed in 2022
park_projects_2022 = []
for doc in civic_docs_data:
    text = doc['text']
    # Look for park projects completed in 2022 using text patterns
    if 'park' in text.lower() and 'completed' in text.lower() and '2022' in text:
        lines = text.split('\n')
        for i in range(len(lines)):
            line = lines[i].strip()
            if line and 'park' in line.lower() and len(line) < 100:
                # Check context for completion date
                context = ' '.join(lines[i:i+8]).lower()
                if 'completed' in context and '2022' in context:
                    park_projects_2022.append(line)
                    print('Found project:', line)

print('Park projects completed in 2022:', len(park_projects_2022))

# Clean names for matching
def clean_name(name):
    name = re.sub(r'\s+Project\s*$', '', name, flags=re.IGNORECASE)
    name = re.sub(r'\s*-\s*Design\s*$', '', name, flags=re.IGNORECASE)
    name = re.sub(r'\s*-\s*Construction\s*$', '', name, flags=re.IGNORECASE)
    return name.strip().lower()

df_funding['clean_name'] = df_funding['Project_Name'].apply(clean_name)
clean_park_names = [clean_name(p) for p in park_projects_2022]

# Match projects and sum funding
total_funding = 0
matched = []

for i, park_name in enumerate(clean_park_names):
    # Direct matches
    matches = df_funding[df_funding['clean_name'].str.contains(park_name, na=False) | 
                        df_funding['Project_Name'].str.contains(park_name, na=False)]
    for _, row in matches.iterrows():
        amount = int(row['Amount'])
        total_funding += amount
        matched.append({'park': park_projects_2022[i], 'funding': row['Project_Name'], 'amount': amount})
        print('Match:', park_projects_2022[i], '->', row['Project_Name'], '=', amount)

# Cross-check for any missed matches
for i, park_name in enumerate(clean_park_names):
    for _, row in df_funding.iterrows():
        fund_name = row['clean_name']
        if park_name in fund_name or fund_name in park_name:
            amount = int(row['Amount'])
            # Avoid duplicates
            if not any(m['park'] == park_projects_2022[i] and m['funding'] == row['Project_Name'] for m in matched):
                total_funding += amount
                matched.append({'park': park_projects_2022[i], 'funding': row['Project_Name'], 'amount': amount})
                print('Additional match:', park_projects_2022[i], '->', row['Project_Name'], '=', amount)

print('Total funding:', total_funding)
result = {'total_funding': total_funding, 'matched': matched}
print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json'}

exec(code, env_args)
