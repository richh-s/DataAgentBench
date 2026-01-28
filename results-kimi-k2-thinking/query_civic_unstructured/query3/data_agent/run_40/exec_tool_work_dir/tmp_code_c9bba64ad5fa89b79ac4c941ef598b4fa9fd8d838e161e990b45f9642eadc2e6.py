code = """import json
import pandas as pd
import re

# Load funding data
with open(var_functions.query_db:0, 'r') as f:
    funding_data = json.load(f)

# Load civic documents data
with open(var_functions.query_db:2, 'r') as f:
    civic_docs = json.load(f)

# Parse civic documents to extract project information
projects = []

for doc in civic_docs:
    text = doc.get('text', '')
    
    # Split text into lines
    lines = text.split('\n')
    
    current_project = None
    
    for line in lines:
        # Look for project names (typically on their own line and in Title Case)
        line = line.strip()
        if not line:
            continue
            
        # Check if line looks like a project name
        # Project names are often:
        # - Not very long
        # - In title case or have specific keywords
        # - Followed by project details
        if len(line) < 100 and (line.istitle() or 'Project' in line or 'Program' in line):
            # Check if it contains keywords that suggest it's a project
            project_indicators = ['Project', 'Program', 'Improvements', 'Repairs', 'Replacement', 
                                  'Upgrade', 'System', 'Facility', 'Plan', 'Phase', 'Road', 
                                  'Street', 'Park', 'Drain', 'Bridge', 'Walkway', 'Structure']
            
            if any(indicator in line for indicator in project_indicators):
                current_project = line
        
        # Extract other details if we have a current project
        if current_project:
            project_info = {'Project_Name': current_project}
            
            # Look for status information
            if 'Updates:' in line and ('design' in line.lower() or 'construction' in line.lower() or 
                                      'completed' in line.lower() or 'not started' in line.lower()):
                if 'design' in line.lower():
                    project_info['status'] = 'design'
                elif 'construction' in line.lower() or 'constructed' in line.lower():
                    project_info['status'] = 'construction'
                elif 'completed' in line.lower():
                    project_info['status'] = 'completed'
                elif 'not started' in line.lower():
                    project_info['status'] = 'not started'
            
            # Look for project type
            if any(word in line for word in ['Capital Improvement', 'Capital', 'infrastructure', 'park']):
                project_info['type'] = 'capital'
            elif any(word in line for word in ['Disaster', 'FEMA', 'CalOES', 'CalJPIA', 'fire', 'recovery']):
                project_info['type'] = 'disaster'
            
            # Look for FEMA or emergency keywords
            topics = []
            if 'FEMA' in line or 'fema' in line:
                topics.append('FEMA')
            if 'emergency' in line.lower():
                topics.append('emergency')
            if 'fire' in line.lower():
                topics.append('fire')
            if 'warning' in line.lower():
                topics.append('emergency warning')
            
            if topics:
                project_info['topic'] = ','.join(topics)
            
            # Look for dates
            date_patterns = [r'(\d{4})[-\s](Spring|Summer|Fall|Winter)',
                            r'(Spring|Summer|Fall|Winter)[\s](\d{4})',
                            r'(\d{4})[-\s](January|February|March|April|May|June|July|August|September|October|November|December)'
            ]
            
            for pattern in date_patterns:
                matches = re.findall(pattern, line, re.IGNORECASE)
                if matches:
                    for match in matches:
                        if 'st' not in project_info:
                            project_info['st'] = '-'.join(match)
                        else:
                            project_info['et'] = '-'.join(match)
                            break
            
            if project_info.get('status') or project_info.get('topic'):
                projects.append(project_info)

# Create DataFrames
df_funding = pd.DataFrame(funding_data)
df_projects = pd.DataFrame(projects)

# Filter for projects with emergency or FEMA in topics
emergency_fema_projects = df_projects[df_projects['topic'].str.contains('FEMA|emergency', case=False, na=False)]

# Get unique project names
project_names = emergency_fema_projects['Project_Name'].unique()

# Find matching funding records
matching_funding = df_funding[df_funding['Project_Name'].isin(project_names)]

# For projects without direct matches, also look for projects that contain emergency/FEMA in name
emergency_keywords = ['FEMA', 'emergency', 'warning']
all_matching = df_funding[df_funding['Project_Name'].str.contains('|'.join(emergency_keywords), case=False)]

# Combine both approaches
all_emergency_projects = pd.concat([matching_funding, all_matching]).drop_duplicates()

# Try to match project names from funding data back to civic docs
result = []
for _, fund_row in all_emergency_projects.iterrows():
    proj_name = fund_row['Project_Name']
    
    # Find matching project info from civic docs
    proj_info = emergency_fema_projects[emergency_fema_projects['Project_Name'].str.contains(re.escape(proj_name), case=False, na=False)]
    if proj_info.empty:
        # Try reverse - see if civic doc project name contains funding project name
        proj_info = emergency_fema_projects[emergency_fema_projects['Project_Name'].apply(lambda x: proj_name.lower() in x.lower())]
    
    status = proj_info['status'].iloc[0] if not proj_info.empty else 'Unknown'
    
    result.append({
        'Project_Name': proj_name,
        'Funding_Source': fund_row['Funding_Source'],
        'Amount': fund_row['Amount'],
        'Status': status
    })

result_df = pd.DataFrame(result)

# Format output
output = result_df.to_dict('records')

# Print in required format
print('__RESULT__:')
print(json.dumps(output))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json'}

exec(code, env_args)
