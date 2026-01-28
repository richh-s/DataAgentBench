code = """import json
import pandas as pd
import re

# Load funding data
funding_file = locals()['var_functions.query_db:0']
with open(funding_file, 'r') as f:
    funding_data = json.load(f)

# Load civic documents data  
civic_file = locals()['var_functions.query_db:2']
with open(civic_file, 'r') as f:
    civic_docs = json.load(f)

# Extract project information from civic documents
projects = []

for doc in civic_docs:
    text = doc.get('text', '')
    
    # Find potential project names and their details
    lines = text.split('\n')
    
    for i in range(len(lines)):
        line = lines[i].strip()
        if not line:
            continue
            
        # Check if this looks like a project name
        if len(line) < 150 and (line.istitle() or 'Project' in line):
            # Look ahead for project details
            project_info = {'Project_Name': line}
            details = []
            
            for j in range(i+1, min(i+10, len(lines))):
                next_line = lines[j].strip()
                if not next_line or (len(next_line) < 150 and next_line.istitle()):
                    break
                details.append(next_line)
            
            detail_text = ' '.join(details).lower()
            
            # Get status
            if 'design' in detail_text:
                project_info['status'] = 'design'
            elif 'construction' in detail_text:
                project_info['status'] = 'construction'
            elif 'completed' in detail_text:
                project_info['status'] = 'completed'
            elif 'not started' in detail_text:
                project_info['status'] = 'not started'
            
            # Check for FEMA/Emergency
            check_text = line.lower() + ' ' + detail_text
            has_fema = 'fema' in check_text
            has_emergency = 'emergency' in check_text or 'warning' in check_text
            
            if has_fema or has_emergency:
                topics = []
                if has_fema:
                    topics.append('FEMA')
                if has_emergency:
                    topics.append('emergency')
                project_info['topic'] = ','.join(topics)
                projects.append(project_info)

# Create DataFrames
df_funding = pd.DataFrame(funding_data)
df_projects = pd.DataFrame(projects)

# Filter for emergency/FEMA projects
emergency_projects = df_projects[df_projects['topic'].str.contains('FEMA|emergency', case=False, na=False)]
project_names = emergency_projects['Project_Name'].unique()

results = []

# Match funding with project info
for proj_name in project_names:
    # Find funding records
    for _, fund in df_funding.iterrows():
        if proj_name.lower() in fund['Project_Name'].lower() or fund['Project_Name'].lower() in proj_name.lower():
            status = 'Unknown'
            matching_proj = emergency_projects[emergency_projects['Project_Name'] == proj_name]
            if not matching_proj.empty and 'status' in matching_proj.columns:
                status = matching_proj['status'].iloc[0]
            
            results.append({
                'Project_Name': fund['Project_Name'],
                'Funding_Source': fund['Funding_Source'],
                'Amount': int(fund['Amount']),
                'Status': status
            })

# Also check funding data directly for FEMA/emergency keywords
fema_keywords = ['fema', 'emergency', 'warning']
for _, fund in df_funding.iterrows():
    if any(keyword in fund['Project_Name'].lower() for keyword in fema_keywords):
        # Check if already added
        already_added = any(r['Project_Name'] == fund['Project_Name'] for r in results)
        if not already_added:
            results.append({
                'Project_Name': fund['Project_Name'],
                'Funding_Source': fund['Funding_Source'],
                'Amount': int(fund['Amount']),
                'Status': 'Unknown'
            })

result_df = pd.DataFrame(results)
result_df = result_df.sort_values('Project_Name')

print('__RESULT__:')
print(json.dumps(result_df.to_dict('records'), indent=2))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json'}

exec(code, env_args)
