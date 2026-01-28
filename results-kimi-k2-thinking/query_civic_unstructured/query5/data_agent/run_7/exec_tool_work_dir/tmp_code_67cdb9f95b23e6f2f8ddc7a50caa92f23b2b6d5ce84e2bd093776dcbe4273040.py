code = """import json
import re

# Load the data
civic_docs_path = locals()['var_functions.query_db:8']
funding_path = locals()['var_functions.query_db:0']

with open(civic_docs_path, 'r') as f:
    civic_docs = json.load(f)

with open(funding_path, 'r') as f:
    funding_data = json.load(f)

# Convert funding amounts to integers
for record in funding_data:
    record['Amount'] = int(record['Amount'])

def is_disaster_project(project_name, text_context):
    # Check for FEMA/CalJPIA/CalOES project markers in name
    if '(FEMA Project)' in project_name or '(CalJPIA Project)' in project_name or '(CalOES Project)' in project_name:
        return True
    
    # Check for disaster-related keywords in project name
    disaster_keywords = ['FEMA', 'fire', 'emergency', 'recovery', 'disaster', 'CalOES', 'CalJPIA']
    name_lower = project_name.lower()
    for keyword in disaster_keywords:
        if keyword.lower() in name_lower:
            return True
    
    return False

def project_started_in_2022(project_name, text_context):
    # Look for project lines starting with 2022
    if project_name.startswith('2022 '):
        return True
    
    # Look for 2022 mentions near the project in text
    if '2022' in text_context and any(word in text_context.lower() for word in ['disaster', 'fema']):
        return True
    
    return False

# Extract disaster projects with 2022 start
extracted_projects = []

for doc in civic_docs:
    text = doc.get('text', '')
    lines = text.split('\n')
    
    current_project = None
    
    for line in lines:
        line = line.strip()
        # Skip empty lines and markers
        if not line or line.startswith('(') or line.startswith('Page'):
            continue
        
        # Look for project names (typically bolded/uppercase or start with year)
        if len(line) > 10 and not line.startswith('cid:') and not line.lower().startswith('and '):
            
            has_noun = any(word in line.lower() for word in ['road', 'avenue', 'street', 'drain', 'park', 'bridge', 'culvert', 'siren', 'warning', 'slope', 'repair'])
            has_action = any(word in line.lower() for word in ['repair', 'improvement', 'replacement', 'project', 'maintenance', 'construction'])
            
            if has_noun or has_action:
                current_project = line.strip()
                
                # Check if it's a disaster project
                if is_disaster_project(current_project, text):
                    # Check if started in 2022
                    if project_started_in_2022(current_project, text):
                        extracted_projects.append({
                            'Project_Name': current_project,
                            'type': 'disaster',
                            'st': '2022'
                        })

# Identify disaster projects from funding data
disaster_project_names = []
for record in funding_data:
    name = record['Project_Name']
    if is_disaster_project(name, '') and not name.startswith('Discussion'):
        disaster_project_names.append(name)

# Calculate total funding for disaster projects
total_disaster_funding = 0
disaster_funding_records = []

for fund_record in funding_data:
    if is_disaster_project(fund_record['Project_Name'], ''):
        total_disaster_funding += fund_record['Amount']
        disaster_funding_records.append(fund_record)

print('__RESULT__:')
print(json.dumps({
    'disaster_projects_found': len(disaster_project_names),
    'total_disaster_funding': total_disaster_funding,
    'sample_disaster_projects': disaster_project_names[:10],
    'sample_funding_records': disaster_funding_records[:10]
}))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.execute_python:6': {'funding_records_count': 500, 'funding_sample': [{'Funding_ID': '1', 'Project_Name': '2021 Annual Street Maintenance', 'Funding_Source': 'Public-Private Partnership (PPP)', 'Amount': '24000'}, {'Funding_ID': '2', 'Project_Name': '2022 Annual Street Maintenance', 'Funding_Source': 'Government Grant', 'Amount': '45000'}, {'Funding_ID': '3', 'Project_Name': '2022 Morning View Resurfacing & Storm Drain Improvements', 'Funding_Source': 'State Development Grant', 'Amount': '38000'}, {'Funding_ID': '4', 'Project_Name': 'Annual Street Maintenance', 'Funding_Source': 'Corporate Sponsorship', 'Amount': '23000'}, {'Funding_ID': '5', 'Project_Name': 'Birdview Avenue Improvements', 'Funding_Source': 'National Foundation Fund', 'Amount': '79000'}]}, 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json', 'var_functions.execute_python:10': {'civic_docs_count': 5, 'funding_records_count': 500}}

exec(code, env_args)
