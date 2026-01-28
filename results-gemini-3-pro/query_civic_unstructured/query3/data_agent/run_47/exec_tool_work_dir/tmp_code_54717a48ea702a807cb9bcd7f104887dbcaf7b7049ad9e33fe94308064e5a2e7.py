code = """import json
import pandas as pd

civic_key = 'var_function-call-620945809164347431'
funding_key = 'var_function-call-620945809164347688'

with open(locals()[civic_key], 'r') as f:
    civic_docs = json.load(f)

with open(locals()[funding_key], 'r') as f:
    funding_records = json.load(f)

df_funding = pd.DataFrame(funding_records)
df_funding['Project_Name'] = df_funding['Project_Name'].str.strip()

projects = []
# Keywords to lower case
keywords = ['park', 'road', 'fema', 'fire', 'emergency', 'drainage', 'storm drain', 'highway', 'bridge', 'playground', 'water treatment', 'guardrail']

for doc in civic_docs:
    text = doc.get('text', '')
    lines = text.split('\n')
    current_type = None
    current_status = None
    
    i = 0
    while i < len(lines):
        line = lines[i].strip()
        
        # Headers
        if 'Capital Improvement Projects' in line:
            current_type = 'capital'
            if '(Design)' in line:
                current_status = 'design'
            elif '(Construction)' in line:
                current_status = 'construction'
            elif '(Not Started)' in line:
                current_status = 'not started'
        elif 'Disaster Recovery Projects' in line:
            current_type = 'disaster'
            if '(Design)' in line:
                current_status = 'design'
            elif '(Construction)' in line:
                current_status = 'construction'
            elif '(Not Started)' in line:
                current_status = 'not started'
        
        is_project = False
        if i + 1 < len(lines):
            next_line = lines[i+1].strip()
            if 'Updates:' in next_line or 'Project Description:' in next_line:
                if line and 'Projects' not in line and 'Page' not in line and 'Item' not in line:
                    is_project = True
        
        if is_project:
            p_name = line
            p_status = current_status
            
            block_lines = []
            j = i + 1
            while j < len(lines):
                subline = lines[j].strip()
                if 'Capital Improvement Projects' in subline or 'Disaster Recovery Projects' in subline:
                    break
                if j + 1 < len(lines):
                    next_sub = lines[j+1].strip()
                    if ('Updates:' in next_sub or 'Project Description:' in next_sub) and subline and 'Projects' not in subline and 'Page' not in subline:
                        break
                block_lines.append(subline)
                j += 1
            
            block_text = ' '.join(block_lines).lower()
            
            # Topics
            found = []
            for k in keywords:
                if k in block_text or k in p_name.lower():
                    found.append(k)
            # Add FEMA if explicit
            if 'fema' in p_name.lower():
                found.append('fema')
            
            p_topic = ', '.join(sorted(list(set(found))))
            
            # Status check
            if p_status == 'construction':
                if 'construction was completed' in block_text or 'notice of completion' in block_text:
                    p_status = 'completed'
            
            projects.append({
                'Project_Name': p_name,
                'topic': p_topic,
                'status': p_status
            })
            i = j - 1
        i += 1

df_projects = pd.DataFrame(projects)
merged = pd.merge(df_funding, df_projects, on='Project_Name', how='inner')

results = []
for idx, row in merged.iterrows():
    t = str(row['topic']).lower()
    n = str(row['Project_Name']).lower()
    if 'emergency' in t or 'fema' in t or 'emergency' in n or 'fema' in n:
        results.append({
            'Project_Name': row['Project_Name'],
            'Funding_Source': row['Funding_Source'],
            'Amount': row['Amount'],
            'status': row['status']
        })

print('__RESULT__:')
print(json.dumps(results))"""

env_args = {'var_function-call-12743158555268498599': 'file_storage/function-call-12743158555268498599.json', 'var_function-call-12743158555268500242': [{'Funding_ID': '1', 'Project_Name': '2021 Annual Street Maintenance', 'Funding_Source': 'Public-Private Partnership (PPP)', 'Amount': '24000'}, {'Funding_ID': '2', 'Project_Name': '2022 Annual Street Maintenance', 'Funding_Source': 'Government Grant', 'Amount': '45000'}, {'Funding_ID': '3', 'Project_Name': '2022 Morning View Resurfacing & Storm Drain Improvements', 'Funding_Source': 'State Development Grant', 'Amount': '38000'}, {'Funding_ID': '4', 'Project_Name': 'Annual Street Maintenance', 'Funding_Source': 'Corporate Sponsorship', 'Amount': '23000'}, {'Funding_ID': '5', 'Project_Name': 'Birdview Avenue Improvements', 'Funding_Source': 'National Foundation Fund', 'Amount': '79000'}], 'var_function-call-620945809164347431': 'file_storage/function-call-620945809164347431.json', 'var_function-call-620945809164347688': 'file_storage/function-call-620945809164347688.json'}

exec(code, env_args)
