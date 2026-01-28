code = """import json
import re

# Load the full funding data from the file
funding_file_key = 'var_functions.query_db:2'
funding_file = locals()['var_functions.query_db:2']
with open(funding_file, 'r') as f:
    funding_data = json.load(f)

# Load the full civic documents from the file
civic_file = locals()['var_functions.query_db:4']
with open(civic_file, 'r') as f:
    civic_docs = json.load(f)

print(f'Number of funding records: {len(funding_data)}')
print(f'Number of civic documents: {len(civic_docs)}')

# Find projects with FEMA or EMERGENCY in their names from funding data
fema_projects = []
emergency_keywords = ['FEMA', 'EMERGENCY', 'WARNING SIREN', 'WARNING SIGN']

for item in funding_data:
    project_name = item['Project_Name']
    upper_name = project_name.upper()
    
    # Check for FEMA/EMERGENCY in name
    if any(keyword in upper_name for keyword in emergency_keywords):
        fema_projects.append({
            'Project_Name': project_name,
            'Funding_Source': item['Funding_Source'],
            'Amount': int(item['Amount']),
            'status': 'Unknown'
        })

print(f'Initial FEMA/EMERGENCY projects found: {len(fema_projects)}')

# Search through documents to find status information
for doc in civic_docs:
    text = doc.get('text', '')
    if not text:
        continue
    
    lines = text.split('\n')
    current_section = None
    
    for line in lines:
        line_upper = line.strip().upper()
        
        # Identify current section based on status
        if 'CAPITAL IMPROVEMENT PROJECTS' in line_upper or 'DISASTER RECOVERY PROJECTS' in line_upper:
            if '(DESIGN)' in line_upper:
                current_section = 'design'
            elif '(CONSTRUCTION)' in line_upper:
                current_section = 'construction'
            elif '(NOT STARTED)' in line_upper:
                current_section = 'not started'
        
        # Update status for matching projects
        if current_section:
            for proj in fema_projects:
                base_name = proj['Project_Name'].split('(')[0].strip().upper()
                if len(base_name) > 5 and base_name in line_upper:
                    proj['status'] = current_section

# Also find projects that aren't named with FEMA but are emergency-related based on document content
additional_projects = []
warning_projects = []

for doc in civic_docs:
    text = doc.get('text', '')
    text_upper = text.upper()
    
    # Look for warning siren/sign projects specifically
    if 'WARNING SIREN' in text_upper or 'WARNING SIGN' in text_upper:
        # Extract context around warning mentions
        lines = text.split('\n')
        for line in lines:
            if 'WARNING' in line.upper():
                # Look for project names from funding in this line
                for item in funding_data:
                    project_name = item['Project_Name']
                    if project_name in [p['Project_Name'] for p in fema_projects]:
                        continue
                    
                    base_name = project_name.split('(')[0].strip()
                    if base_name.upper() in line.upper() and len(base_name) > 5:
                        warning_projects.append({
                            'Project_Name': project_name,
                            'Funding_Source': item['Funding_Source'],
                            'Amount': int(item['Amount']),
                            'status': 'Unknown'
                        })

# Combine and deduplicate
all_projects = fema_projects + warning_projects
unique_projects = {}
for proj in all_projects:
    unique_projects[proj['Project_Name']] = proj

final_list = list(unique_projects.values())
print(f'Total unique emergency/FEMA projects: {len(final_list)}')

# Format output
result_json = json.dumps(final_list, indent=2)
print('__RESULT__:')
print(result_json)"""

env_args = {'var_functions.query_db:0': [{'Funding_ID': '1', 'Project_Name': '2021 Annual Street Maintenance', 'Funding_Source': 'Public-Private Partnership (PPP)', 'Amount': '24000'}, {'Funding_ID': '2', 'Project_Name': '2022 Annual Street Maintenance', 'Funding_Source': 'Government Grant', 'Amount': '45000'}, {'Funding_ID': '3', 'Project_Name': '2022 Morning View Resurfacing & Storm Drain Improvements', 'Funding_Source': 'State Development Grant', 'Amount': '38000'}, {'Funding_ID': '4', 'Project_Name': 'Annual Street Maintenance', 'Funding_Source': 'Corporate Sponsorship', 'Amount': '23000'}, {'Funding_ID': '5', 'Project_Name': 'Birdview Avenue Improvements', 'Funding_Source': 'National Foundation Fund', 'Amount': '79000'}, {'Funding_ID': '6', 'Project_Name': 'Birdview Avenue Improvements (CalOES Project)', 'Funding_Source': 'International Aid', 'Amount': '85000'}, {'Funding_ID': '7', 'Project_Name': 'Birdview Avenue Improvements (FEMA/CalOES Project)', 'Funding_Source': 'Research Institution Funding', 'Amount': '14000'}, {'Funding_ID': '8', 'Project_Name': 'Bluffs Park Shade Structure', 'Funding_Source': 'Government Grant', 'Amount': '21000'}, {'Funding_ID': '9', 'Project_Name': 'Bluffs Park Workout Station', 'Funding_Source': 'University Research Fund', 'Amount': '39000'}, {'Funding_ID': '10', 'Project_Name': 'Broad Beach Road Water Quality Infrastructure Repairs', 'Funding_Source': 'International Organization Grant', 'Amount': '87000'}], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:4': 'file_storage/functions.query_db:4.json'}

exec(code, env_args)
