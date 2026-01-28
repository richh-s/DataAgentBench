code = """import json
import pandas as pd
import re

# Load funding data from the file path stored in the variable
funding_file = locals()['var_functions.query_db:0']
with open(funding_file, 'r') as f:
    funding_data = json.load(f)

# Load civic documents data from the file path stored in the variable
civic_file = locals()['var_functions.query_db:2']
with open(civic_file, 'r') as f:
    civic_docs = json.load(f)

# Parse civic documents to extract project information more systematically
projects = []

for doc in civic_docs:
    text = doc.get('text', '')
    
    # Split into sections to better identify project information
    # Look for patterns like project names followed by details
    chunks = text.split('\n\n')
    
    for chunk in chunks:
        lines = chunk.strip().split('\n')
        if not lines:
            continue
        
        # First line is often the project name
        potential_name = lines[0].strip()
        
        # Check if this looks like a project name
        if (len(potential_name) > 5 and 
            len(potential_name) < 150 and
            any(keyword in potential_name for keyword in ['Project', 'Improvement', 'Repair', 'Replace', 'System', 
                                                         'Facility', 'Structure', 'Plan', 'Program', 'Upgrade',
                                                         'Road', 'Street', 'Park', 'Drain', 'Bridge']) or
            potential_name.istitle()):
            
            project_info = {'Project_Name': potential_name}
            
            # Look for status in the entire chunk
            chunk_text = ' '.join(lines[1:]).lower()
            
            # Determine status
            if 'design' in chunk_text or 'planning' in chunk_text or 'preliminary design' in chunk_text:
                project_info['status'] = 'design'
            elif 'construction' in chunk_text or 'constructed' in chunk_text or 'under construction' in chunk_text:
                project_info['status'] = 'construction'
            elif 'completed' in chunk_text:
                project_info['status'] = 'completed'
            elif 'not started' in chunk_text:
                project_info['status'] = 'not started'
            
            # Check for FEMA/emergency keywords in project name and chunk
            topics = []
            full_text = (potential_name + ' ' + chunk_text).lower()
            
            if 'fema' in full_text:
                topics.append('FEMA')
            if 'emergency' in full_text:
                topics.append('emergency')
            if 'warning' in full_text:
                topics.append('emergency warning')
            if 'fire' in full_text:
                topics.append('fire')
            
            if topics:
                project_info['topic'] = ','.join(topics)
                projects.append(project_info)

# Add projects from funding data that have FEMA or emergency in their names
for fund_item in funding_data:
    proj_name = fund_item['Project_Name']
    if any(keyword.lower() in proj_name.lower() for keyword in ['fema', 'emergency', 'warning']):
        projects.append({
            'Project_Name': proj_name,
            'topic': 'FEMA' if 'fema' in proj_name.lower() else 'emergency'
        })

# Create DataFrame and deduplicate
df_projects = pd.DataFrame(projects)
df_projects = df_projects.drop_duplicates(subset=['Project_Name'])

df_funding = pd.DataFrame(funding_data)

# Filter for projects with emergency or FEMA
emergency_projects = df_projects[df_projects['topic'].str.contains('FEMA|emergency', case=False, na=False)]

# Get all project names that are emergency/FEMA related
emergency_project_names = emergency_projects['Project_Name'].unique()

# Find all funding records for these projects
all_results = []
for proj_name in emergency_project_names:
    # Find matching funding records
    matching_funds = df_funding[df_funding['Project_Name'].str.contains(re.escape(proj_name), case=False, na=False)]
    
    if not matching_funds.empty:
        for _, fund in matching_funds.iterrows():
            # Get status if available
            status_info = emergency_projects[emergency_projects['Project_Name'].str.contains(re.escape(proj_name), case=False, na=False)]
            status = status_info['status'].iloc[0] if not status_info.empty and 'status' in status_info.columns else 'Unknown'
            
            all_results.append({
                'Project_Name': fund['Project_Name'],
                'Funding_Source': fund['Funding_Source'],
                'Amount': int(fund['Amount']),
                'Status': status
            })

# Also get projects that are in funding data with FEMA/emergency keywords but might not be in civic docs
fema_funding = df_funding[df_funding['Project_Name'].str.contains('fema|emergency|warning', case=False, na=False)]

for _, fund in fema_funding.iterrows():
    proj_name = fund['Project_Name']
    
    # Check if we already have this project
    existing = [r for r in all_results if r['Project_Name'] == proj_name]
    
    if not existing:
        # Try to find status information
        status = 'Unknown'
        for doc_proj in projects:
            if proj_name.lower() in doc_proj['Project_Name'].lower() or doc_proj['Project_Name'].lower() in proj_name.lower():
                status = doc_proj.get('status', 'Unknown')
                break
        
        all_results.append({
            'Project_Name': proj_name,
            'Funding_Source': fund['Funding_Source'],
            'Amount': int(fund['Amount']),
            'Status': status
        })

result_df = pd.DataFrame(all_results)

# Sort by project name
result_df = result_df.sort_values('Project_Name')

# Convert to list of dictionaries
output = result_df.to_dict('records')

# Print in required format
print('__RESULT__:')
print(json.dumps(output, indent=2))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json'}

exec(code, env_args)
