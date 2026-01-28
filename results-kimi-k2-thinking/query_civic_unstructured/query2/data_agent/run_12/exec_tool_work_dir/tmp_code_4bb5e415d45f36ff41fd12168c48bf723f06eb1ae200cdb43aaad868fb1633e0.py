code = """import json
import pandas as pd
import re

# Load funding data
funding_path = '/home/user/funding_data.json'
civic_path = '/home/user/civic_docs_data.json'

with open(funding_path, 'r') as f:
    funding_data = json.load(f)

with open(civic_path, 'r') as f:
    civic_docs_data = json.load(f)

# Create funding dataframe
df_funding = pd.DataFrame(funding_data)
print('Total funding records:', len(df_funding))

# Extract park projects completed in 2022 from civic docs
park_projects_2022 = []

for doc in civic_docs_data:
    text = doc['text']
    
    # Look for park projects that were completed in 2022
    # Pattern: Project name, then later "completed" and "2022"
    lines = text.split('\n')
    
    for i in range(len(lines)):
        line = lines[i].strip()
        if not line or len(line) > 80:
            continue
            
        # Check if this might be a project name (not too long, not a bullet)
        if not line.startswith('(') and not line.startswith('-') and not line.startswith('.'):
            # Check if it mentions park
            if 'park' in line.lower():
                # Look ahead for completion status and date
                next_text = '\n'.join(lines[i:i+8]).lower()
                if 'completed' in next_text and '2022' in next_text:
                    park_projects_2022.append({
                        'name': line,
                        'status': 'completed',
                        'year': '2022'
                    })
                    print('Found park project:', line)

print('Total park projects found:', len(park_projects_2022))

# Clean names for matching
def clean_name(name):
    name = re.sub(r'\s+Project\s*$', '', name, flags=re.IGNORECASE)
    name = re.sub(r'\s*-\s*Design$', '', name, flags=re.IGNORECASE)
    name = re.sub(r'\s*-\s*Construction$', '', name, flags=re.IGNORECASE)
    return name.strip().lower()

# Clean funding names
df_funding['clean_name'] = df_funding['Project_Name'].apply(clean_name)

# Find matches and calculate funding
matched = []
total = 0

for proj in park_projects_2022:
    proj_clean = clean_name(proj['name'])
    
    # Look for matches in funding data
    for _, fund in df_funding.iterrows():
        fund_clean = fund['clean_name']
        
        # Check if one contains the other
        if proj_clean in fund_clean or fund_clean in proj_clean:
            amount = int(fund['Amount'])
            total += amount
            matched.append({
                'project': proj['name'],
                'funding': fund['Project_Name'],
                'amount': amount
            })
            print(f'Match: {proj[\"name\"]} -> {fund[\"Project_Name\"]} = ${amount}')

print('\nTotal matched projects:', len(matched))
print('Total funding:', total)

result = {'total_funding': total, 'projects': matched}
print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json'}

exec(code, env_args)
