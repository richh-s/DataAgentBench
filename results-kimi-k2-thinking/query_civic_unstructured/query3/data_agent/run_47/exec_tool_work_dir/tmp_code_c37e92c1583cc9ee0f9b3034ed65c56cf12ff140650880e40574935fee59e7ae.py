code = """import json
import re

# Load funding data
funding_file = var_functions.query_db:2
with open(funding_file, 'r') as f:
    funding_data = json.load(f)

# Load civic documents
civic_file = var_functions.query_db:4
with open(civic_file, 'r') as f:
    civic_docs = json.load(f)

# Create a dictionary of funding data by project name for easy lookup
funding_dict = {}
for item in funding_data:
    project_name = item['Project_Name']
    funding_dict[project_name] = {
        'Funding_Source': item['Funding_Source'],
        'Amount': int(item['Amount'])
    }

# First, let's identify projects with FEMA or emergency in their names
fema_projects = []
for project_name in funding_dict.keys():
    if 'FEMA' in project_name.upper() or 'EMERGENCY' in project_name.upper():
        fema_projects.append({
            'Project_Name': project_name,
            'Funding_Source': funding_dict[project_name]['Funding_Source'],
            'Amount': funding_dict[project_name]['Amount'],
            'status': 'Unknown'  # We'll try to find the status from documents
        })

# Search for these projects in the civic documents to extract status
project_statuses = {}
for doc in civic_docs:
    text = doc.get('text', '')
    
    # Look for status indicators in the text
    # Check for different sections that indicate status
    design_section = False
    construction_section = False
    not_started_section = False
    
    lines = text.split('\n')
    for line in lines:
        line_upper = line.upper()
        
        # Detect status sections
        if 'CAPITAL IMPROVEMENT PROJECTS (DESIGN)' in line_upper:
            design_section = True
            construction_section = False
            not_started_section = False
        elif 'CAPITAL IMPROVEMENT PROJECTS (CONSTRUCTION)' in line_upper:
            design_section = False
            construction_section = True
            not_started_section = False
        elif 'CAPITAL IMPROVEMENT PROJECTS (NOT STARTED)' in line_upper:
            design_section = False
            construction_section = False
            not_started_section = True
        
        # Look for project names and update their status
        for project in fema_projects:
            proj_name = project['Project_Name']
            # Check if project name appears in line (handle variations)
            if proj_name.split('(')[0].strip() in line:
                if design_section:
                    project['status'] = 'design'
                elif construction_section:
                    project['status'] = 'construction'
                elif not_started_section:
                    project['status'] = 'not started'

# Now search for emergency-related projects (not just in name, but in content)
emergency_keywords = ['EMERGENCY', 'FEMA', 'WARNING', 'SIREN', 'DISASTER']

# Look for projects that might be emergency-related based on content
for doc in civic_docs:
    text = doc.get('text', '').upper()
    
    # Find sections with emergency/FEMA keywords
    for keyword in emergency_keywords:
        if keyword in text:
            # Extract lines around the keyword to find project names
            lines = doc.get('text', '').split('\n')
            for i, line in enumerate(lines):
                line_upper = line.upper()
                if keyword in line_upper and len(line.strip()) > 0:
                    # Look for project names in this line or nearby lines
                    # Check if this line contains a project name from funding
                    for project_name in funding_dict.keys():
                        base_name = project_name.split('(')[0].strip()
                        if base_name.upper() in line_upper and len(base_name) > 5:
                            # Found a potential match
                            if project_name not in [p['Project_Name'] for p in fema_projects]:
                                fema_projects.append({
                                    'Project_Name': project_name,
                                    'Funding_Source': funding_dict[project_name]['Funding_Source'],
                                    'Amount': funding_dict[project_name]['Amount'],
                                    'status': 'Unknown'
                                })

# Remove duplicates and finalize
unique_projects = {}
for proj in fema_projects:
    unique_projects[proj['Project_Name']] = proj

result = list(unique_projects.values())

# Format output nicely
print('__RESULT__:')
print(json.dumps(result, indent=2))"""

env_args = {'var_functions.query_db:0': [{'Funding_ID': '1', 'Project_Name': '2021 Annual Street Maintenance', 'Funding_Source': 'Public-Private Partnership (PPP)', 'Amount': '24000'}, {'Funding_ID': '2', 'Project_Name': '2022 Annual Street Maintenance', 'Funding_Source': 'Government Grant', 'Amount': '45000'}, {'Funding_ID': '3', 'Project_Name': '2022 Morning View Resurfacing & Storm Drain Improvements', 'Funding_Source': 'State Development Grant', 'Amount': '38000'}, {'Funding_ID': '4', 'Project_Name': 'Annual Street Maintenance', 'Funding_Source': 'Corporate Sponsorship', 'Amount': '23000'}, {'Funding_ID': '5', 'Project_Name': 'Birdview Avenue Improvements', 'Funding_Source': 'National Foundation Fund', 'Amount': '79000'}, {'Funding_ID': '6', 'Project_Name': 'Birdview Avenue Improvements (CalOES Project)', 'Funding_Source': 'International Aid', 'Amount': '85000'}, {'Funding_ID': '7', 'Project_Name': 'Birdview Avenue Improvements (FEMA/CalOES Project)', 'Funding_Source': 'Research Institution Funding', 'Amount': '14000'}, {'Funding_ID': '8', 'Project_Name': 'Bluffs Park Shade Structure', 'Funding_Source': 'Government Grant', 'Amount': '21000'}, {'Funding_ID': '9', 'Project_Name': 'Bluffs Park Workout Station', 'Funding_Source': 'University Research Fund', 'Amount': '39000'}, {'Funding_ID': '10', 'Project_Name': 'Broad Beach Road Water Quality Infrastructure Repairs', 'Funding_Source': 'International Organization Grant', 'Amount': '87000'}], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:4': 'file_storage/functions.query_db:4.json'}

exec(code, env_args)
