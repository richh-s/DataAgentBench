code = """import json
import pandas as pd
import re

funding_path = locals()['var_function-call-5156412947149876604']
docs_path = locals()['var_function-call-15531126459955153771']

with open(funding_path, 'r') as f:
    funding_data = json.load(f)
with open(docs_path, 'r') as f:
    docs_data = json.load(f)

df_fund = pd.DataFrame(funding_data)
# Clean Amount
df_fund['Amount'] = df_fund['Amount'].astype(str).str.replace('[$,]', '', regex=True)
df_fund['Amount'] = pd.to_numeric(df_fund['Amount'], errors='coerce')
funded_high = set(df_fund[df_fund['Amount'] > 50000]['Project_Name'].str.strip())

project_records = []

for doc in docs_data:
    filename = doc.get('filename', '')
    text = doc.get('text', '')
    
    # Date extraction
    date_match = re.search(r'(\d{8})', filename)
    if date_match:
        date_str = date_match.group(1)
        date_sort = date_str[4:] + date_str[:4]
    else:
        date_sort = '00000000'

    # Split lines
    lines = text.split('\n')
    
    current_section = None
    
    for i, line in enumerate(lines):
        line = line.strip()
        if not line:
            continue
            
        if 'Capital Improvement Projects (Design)' in line:
            current_section = 'CAP_DESIGN'
            continue
        elif 'Capital Improvement Projects (Construction)' in line:
            current_section = 'CAP_CONST'
            continue
        elif 'Capital Improvement Projects (Not Started)' in line:
            current_section = 'CAP_NOT'
            continue
        elif 'Disaster Recovery Projects' in line:
            current_section = 'DISASTER'
            continue
        elif 'Agenda Item' in line or ('Page' in line and 'of' in line):
            continue
        
        if current_section:
            if line.startswith('(cid:') or line.startswith('Updates:') or \
               line.startswith('Project Description:') or line.startswith('Approved by:') or \
               line.startswith('Prepared by:') or line.startswith('To:') or \
               line.startswith('Subject:') or line.startswith('Recommendation:'):
                continue
                
            is_project = False
            # Check next lines
            limit = min(i+10, len(lines))
            for j in range(i+1, limit):
                next_l = lines[j].strip()
                if not next_l:
                    continue
                if next_l.startswith('(cid:190)'):
                    is_project = True
                break
            
            if is_project:
                p_name = line.strip()
                p_type = 'Capital'
                p_status = 'Unknown'
                if current_section == 'CAP_DESIGN':
                    p_status = 'design'
                elif current_section == 'CAP_CONST':
                    p_status = 'construction'
                elif current_section == 'CAP_NOT':
                    p_status = 'not_started'
                elif current_section == 'DISASTER':
                    p_type = 'Disaster'
                    
                project_records.append({
                    'name': p_name,
                    'date': date_sort,
                    'type': p_type,
                    'status': p_status
                })

df_recs = pd.DataFrame(project_records)
if not df_recs.empty:
    df_recs = df_recs.sort_values('date', ascending=False)
    df_latest = df_recs.drop_duplicates(subset='name', keep='first')
    
    matches = []
    for _, row in df_latest.iterrows():
        if row['type'] == 'Capital' and row['status'] == 'design':
            if row['name'] in funded_high:
                matches.append(row['name'])
    
    result = len(matches)
else:
    result = 0
    matches = []

print('__RESULT__:')
print(json.dumps({'count': result, 'matches': matches}))"""

env_args = {'var_function-call-5156412947149876604': 'file_storage/function-call-5156412947149876604.json', 'var_function-call-5156412947149876803': 'file_storage/function-call-5156412947149876803.json', 'var_function-call-15531126459955153771': 'file_storage/function-call-15531126459955153771.json'}

exec(code, env_args)
