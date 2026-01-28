code = """import json
import pandas as pd

# Data paths
docs_path = locals()['var_function-call-14510963906005286500']
funds_path = locals()['var_function-call-14510963906005285081']

# Load
with open(docs_path, 'r') as f:
    docs = json.load(f)

with open(funds_path, 'r') as f:
    funds = json.load(f)

df = pd.DataFrame(funds)
df['Amount'] = pd.to_numeric(df['Amount'])

# Known names
known = set(df['Project_Name'].str.strip())

found_projects = []

for d in docs:
    lines = d['text'].split('\n')
    curr = None
    buf = []
    
    for line in lines:
        s = line.strip()
        if s in known:
            # Check previous
            if curr:
                txt = ' '.join(buf).lower()
                # Check park
                is_park = 'park' in curr.lower() or 'park' in txt
                # Check completed 2022
                is_comp = False
                if 'completed' in txt and '2022' in txt:
                    if 'was completed' in txt or 'construction was completed' in txt or 'completed,' in txt:
                        is_comp = True
                
                if is_park and is_comp:
                    found_projects.append(curr)
            
            curr = s
            buf = []
        else:
            if curr:
                buf.append(s)
                
    # Check last
    if curr:
        txt = ' '.join(buf).lower()
        is_park = 'park' in curr.lower() or 'park' in txt
        is_comp = False
        if 'completed' in txt and '2022' in txt:
             if 'was completed' in txt or 'completed,' in txt:
                 is_comp = True
        
        if is_park and is_comp:
            found_projects.append(curr)

unique = list(set(found_projects))
total = df[df['Project_Name'].isin(unique)]['Amount'].sum()

print('__RESULT__:')
print(json.dumps({'projects': unique, 'total': float(total)}))"""

env_args = {'var_function-call-7656597533557058168': 'file_storage/function-call-7656597533557058168.json', 'var_function-call-7656597533557058431': [{'Funding_ID': '1', 'Project_Name': '2021 Annual Street Maintenance', 'Funding_Source': 'Public-Private Partnership (PPP)', 'Amount': '24000'}, {'Funding_ID': '2', 'Project_Name': '2022 Annual Street Maintenance', 'Funding_Source': 'Government Grant', 'Amount': '45000'}, {'Funding_ID': '3', 'Project_Name': '2022 Morning View Resurfacing & Storm Drain Improvements', 'Funding_Source': 'State Development Grant', 'Amount': '38000'}, {'Funding_ID': '4', 'Project_Name': 'Annual Street Maintenance', 'Funding_Source': 'Corporate Sponsorship', 'Amount': '23000'}, {'Funding_ID': '5', 'Project_Name': 'Birdview Avenue Improvements', 'Funding_Source': 'National Foundation Fund', 'Amount': '79000'}], 'var_function-call-14510963906005286500': 'file_storage/function-call-14510963906005286500.json', 'var_function-call-14510963906005285081': 'file_storage/function-call-14510963906005285081.json'}

exec(code, env_args)
