code = """import json
import re
from collections import defaultdict

# Read the full funding data
funding_file_path = locals()['var_functions.query_db:5']
with open(funding_file_path, 'r') as f:
    funding_data = json.load(f)

# Read the MongoDB documents
mongo_docs = locals()['var_functions.query_db:6']

# Extract project information from MongoDB documents
project_info = defaultdict(dict)

for doc in mongo_docs:
    text = doc.get('text', '')
    filename = doc.get('filename', '')
    
    # Look for project patterns in the text
    lines = text.split('\n')
    
    for i, line in enumerate(lines):
        line = line.strip()
        
        # Skip headers and metadata
        if (len(line) > 10 and 
            not line.startswith('Agenda Item') and
            not line.startswith('Page') and
            not line.startswith('To:') and
            not line.startswith('Prepared by') and
            not line.startswith('Approved by') and
            not line.startswith('DISCUSSION') and
            not line.startswith('RECOMMENDED')):
            
            # Check if line contains project keywords
            if any(keyword in line.lower() for keyword in ['project', 'improvements', 'repairs', 'replacement']):
                # Extract potential project name
                if 'Updates:' not in line and 'Project Schedule:' not in line and 'Project Description:' not in line:
                    # Clean the line
                    clean_line = re.sub(r'^[^a-zA-Z]*', '', line)
                    clean_line = re.sub(r'[^a-zA-Z0-9\s\-\(\)]*$', '', clean_line)
                    
                    if clean_line and len(clean_line) > 10:
                        # Determine if this is an emergency/FEMA project
                        is_emergency = 'emergency' in clean_line.lower() or 'FEMA' in clean_line
                        
                        if is_emergency:
                            project_info[clean_line] = {
                                'status': None,
                                'type': 'disaster',
                                'topic': 'emergency,FEMA',
                                'source_file': filename
                            }

# Create a mapping of project names from funding data
fema_projects = []
for fund in funding_data:
    proj_name = fund['Project_Name']
    if 'FEMA' in proj_name or 'emergency' in proj_name.lower():
        fema_projects.append({
            'Project_Name': proj_name,
            'Funding_Source': fund['Funding_Source'],
            'Amount': int(fund['Amount']),
            'Status': None
        })

print("__RESULT__:")
print(json.dumps(fema_projects[:20]))  # Return first 20 matches"""

env_args = {'var_functions.list_db:0': ['Funding'], 'var_functions.query_db:2': [{'Funding_ID': '1', 'Project_Name': '2021 Annual Street Maintenance', 'Funding_Source': 'Public-Private Partnership (PPP)', 'Amount': '24000'}, {'Funding_ID': '2', 'Project_Name': '2022 Annual Street Maintenance', 'Funding_Source': 'Government Grant', 'Amount': '45000'}, {'Funding_ID': '3', 'Project_Name': '2022 Morning View Resurfacing & Storm Drain Improvements', 'Funding_Source': 'State Development Grant', 'Amount': '38000'}, {'Funding_ID': '4', 'Project_Name': 'Annual Street Maintenance', 'Funding_Source': 'Corporate Sponsorship', 'Amount': '23000'}, {'Funding_ID': '5', 'Project_Name': 'Birdview Avenue Improvements', 'Funding_Source': 'National Foundation Fund', 'Amount': '79000'}, {'Funding_ID': '6', 'Project_Name': 'Birdview Avenue Improvements (CalOES Project)', 'Funding_Source': 'International Aid', 'Amount': '85000'}, {'Funding_ID': '7', 'Project_Name': 'Birdview Avenue Improvements (FEMA/CalOES Project)', 'Funding_Source': 'Research Institution Funding', 'Amount': '14000'}, {'Funding_ID': '8', 'Project_Name': 'Bluffs Park Shade Structure', 'Funding_Source': 'Government Grant', 'Amount': '21000'}, {'Funding_ID': '9', 'Project_Name': 'Bluffs Park Workout Station', 'Funding_Source': 'University Research Fund', 'Amount': '39000'}, {'Funding_ID': '10', 'Project_Name': 'Broad Beach Road Water Quality Infrastructure Repairs', 'Funding_Source': 'International Organization Grant', 'Amount': '87000'}], 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.execute_python:11': {'funding_count': 500, 'mongo_docs_count': 38}}

exec(code, env_args)
