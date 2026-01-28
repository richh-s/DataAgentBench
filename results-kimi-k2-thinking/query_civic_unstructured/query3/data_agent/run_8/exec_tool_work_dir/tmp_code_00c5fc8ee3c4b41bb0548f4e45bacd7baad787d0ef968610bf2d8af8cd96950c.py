code = """import json
import re

# Read the data again
with open('file_storage/functions.query_db:5.json', 'r') as f:
    funding_data = json.load(f)

with open('file_storage/functions.query_db:8.json', 'r') as f:
    civic_docs = json.load(f)

# Find all FEMA/emergency related projects in funding
fema_funding = {}
for row in funding_data:
    project_name = row.get('Project_Name', '')
    lower_name = project_name.lower()
    if 'fema' in lower_name or 'emergency' in lower_name or 'warning' in lower_name or 'caloes' in lower_name:
        fema_funding[project_name] = row

# Process civic documents to extract project information
project_dict = {}

for doc in civic_docs:
    text = doc.get('text', '')
    lines = text.split('\n')
    
    current_project = None
    
    for line in lines:
        # Look for project names (typically title case lines)
        line = line.strip()
        if not line:
            continue
            
        # Skip common headers
        if any(header in line for header in ['Page', 'Agenda Item', 'Public Works', 'Commission', 'Meeting']):
            continue
            
        # Look for status indicators
        status_match = None
        if 'Updates:' in line or 'Project Schedule:' in line:
            # Check previous line for project name
            if current_project:
                # Determine status based on keywords
                if 'Construction was completed' in line:
                    status = 'completed'
                elif 'Complete Design:' in line or 'Staff is working' in line:
                    status = 'design'
                elif 'Project is in the preliminary' in line or 'not started' in line.lower() in line:
                    status = 'not started'
                elif 'currently under construction' in line.lower() in line:
                    status = 'construction'
                else:
                    status = None
                    
                if status and current_project not in project_dict:
                    project_dict[current_project] = {'status': status, 'topic': 'emergency, FEMA', 'type': 'disaster'}
        
        # Look for project names
        elif line and line[0].isupper() and len(line) > 10 and not line.startswith('('):
            # Check if this is a funding project we care about
            for funding_project in fema_funding.keys():
                if funding_project.lower() in line.lower() or line.lower() in funding_project.lower():
                    current_project = funding_project
                    break
            else:
                current_project = line

# Create final results by matching with funding
target_projects = [
    'Outdoor Warning Sirens',
    'Outdoor Warning Signs',
    'Clover Heights Storm Drain',
    'Guardrail Replacement Citywide',
    'Latigo Canyon Road Culvert Repairs',
    'Latigo Canyon Road Roadway/Retaining Wall Improvements',
    'Birdview Avenue Improvements',
    'Corral Canyon Culvert Repairs',
    'Corral Canyon Road Bridge Repairs',
    'Encinal Canyon Road Drainage Improvements'
]

results = []
for project_name in target_projects:
    # Find matching funding records
    for funding_row in funding_data:
        if project_name in funding_row['Project_Name']:
            # Find status from civic docs
            status = project_dict.get(funding_row['Project_Name'], {}).get('status', 'unknown')
            if status == 'unknown':
                # Try to find partial match
                for proj_key in project_dict.keys():
                    if project_name.lower() in proj_key.lower():
                        status = project_dict[proj_key]['status']
                        break
            
            results.append({
                'Project_Name': funding_row['Project_Name'],
                'Funding_Source': funding_row['Funding_Source'],
                'Amount': float(funding_row['Amount']),
                'Status': status
            })

# Return results
print('__RESULT__:')
print(json.dumps(results))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.list_db:2': ['Funding'], 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json', 'var_functions.execute_python:12': {'funding_storage_key': 'var_functions.query_db:5', 'civic_docs_storage_key': 'var_functions.query_db:8'}, 'var_functions.execute_python:20': ['var_functions.list_db:0', 'var_functions.list_db:2', 'var_functions.query_db:5', 'var_functions.query_db:6', 'var_functions.query_db:8', 'var_functions.execute_python:12', '__builtins__', 'json', 're'], 'var_functions.execute_python:26': ['var_functions.list_db:0', 'var_functions.list_db:2', 'var_functions.query_db:5', 'var_functions.query_db:6', 'var_functions.query_db:8', 'var_functions.execute_python:12', 'var_functions.execute_python:20'], 'var_functions.execute_python:30': {'funding_path': 'file_storage/functions.query_db:5.json', 'civic_path': 'file_storage/functions.query_db:8.json', 'funding_type': "<class 'list'>", 'civic_type': "<class 'list'>"}, 'var_functions.execute_python:32': {'fema_funding_count': 23, 'civic_docs_count': 5, 'sample_funding': [{'Funding_ID': '7', 'Project_Name': 'Birdview Avenue Improvements (FEMA/CalOES Project)', 'Funding_Source': 'Research Institution Funding', 'Amount': '14000'}, {'Funding_ID': '22', 'Project_Name': 'Clover Heights Storm Drain (FEMA Project)', 'Funding_Source': 'Local NGO Fund', 'Amount': '21000'}, {'Funding_ID': '25', 'Project_Name': 'Corral Canyon Culvert Repairs (FEMA Project)', 'Funding_Source': 'Municipal Fund', 'Amount': '43000'}, {'Funding_ID': '26', 'Project_Name': 'Corral Canyon Culvert Repairs (FEMA/CalOES Project)', 'Funding_Source': 'Taxpayer Contribution', 'Amount': '15000'}, {'Funding_ID': '28', 'Project_Name': 'Corral Canyon Road Bridge Repairs (FEMA Project)', 'Funding_Source': 'Local Business Support', 'Amount': '25000'}, {'Funding_ID': '29', 'Project_Name': 'Corral Canyon Road Bridge Repairs (FEMA/CalOES Project)', 'Funding_Source': 'Cultural Heritage Grant', 'Amount': '58000'}, {'Funding_ID': '35', 'Project_Name': 'Encinal Canyon Road Drainage Improvements (FEMA/CalOES Project)', 'Funding_Source': 'Private Sponsor', 'Amount': '94000'}, {'Funding_ID': '38', 'Project_Name': 'Guardrail Replacement Citywide (FEMA Project)', 'Funding_Source': 'Impact Investment Fund', 'Amount': '22000'}, {'Funding_ID': '39', 'Project_Name': 'Guardrail Replacement Citywide (FEMA/CalOES Project)', 'Funding_Source': 'Development Bank Loan', 'Amount': '45000'}, {'Funding_ID': '43', 'Project_Name': 'Latigo Canyon Road Culvert Repairs (FEMA Project)', 'Funding_Source': 'Federal Assistance', 'Amount': '36000'}, {'Funding_ID': '44', 'Project_Name': 'Latigo Canyon Road Culvert Repairs (FEMA/CalOES Project)', 'Funding_Source': 'National Foundation Fund', 'Amount': '44000'}, {'Funding_ID': '47', 'Project_Name': 'Latigo Canyon Road Roadway/Retaining Wall Improvements (FEMA Project)', 'Funding_Source': 'Municipal Fund', 'Amount': '91000'}, {'Funding_ID': '48', 'Project_Name': 'Latigo Canyon Road Roadway/Retaining Wall Improvements (FEMA/CalOES Project)', 'Funding_Source': 'Community Fund', 'Amount': '78000'}, {'Funding_ID': '64', 'Project_Name': 'Outdoor Warning Signs', 'Funding_Source': 'Urban Renewal Fund', 'Amount': '92000'}, {'Funding_ID': '65', 'Project_Name': 'Outdoor Warning Sirens', 'Funding_Source': 'Social Impact Investment', 'Amount': '28000'}]}}

exec(code, env_args)
