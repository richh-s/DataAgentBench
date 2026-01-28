code = """import json
import re

# Load the full funding data from the file
funding_file = locals()['var_functions.query_db:2']
with open(funding_file, 'r') as f:
    funding_data = json.load(f)

# Load the full civic documents from the file
civic_file = locals()['var_functions.query_db:4']
with open(civic_file, 'r') as f:
    civic_docs = json.load(f)

# Debug: Print sample sizes
print(f'Number of funding records: {len(funding_data)}')
print(f'Number of civic documents: {len(civic_docs)}')

# Look for FEMA/emergency related projects in funding data
fema_projects = []
fema_related_names = []

for item in funding_data:
    project_name = item['Project_Name']
    upper_name = project_name.upper()
    
    # Check if project name contains FEMA or EMERGENCY
    if 'FEMA' in upper_name or 'EMERGENCY' in upper_name:
        fema_projects.append({
            'Project_Name': project_name,
            'Funding_Source': item['Funding_Source'],
            'Amount': int(item['Amount']),
            'status': 'Unknown'
        })
        fema_related_names.append(project_name.split('(')[0].strip().upper())

print(f'Found {len(fema_projects)} projects with FEMA/EMERGENCY in name')

# Now search documents to find status information
# We'll look for pattern matching in documents
for doc in civic_docs:
    text = doc.get('text', '')
    if not text:
        continue
    
    # Find sections with different statuses
    current_status = None
    lines = text.split('\n')
    
    for line in lines:
        line_upper = line.upper()
        
        # Detect status sections
        if '(DESIGN)' in line_upper and 'PROJECT' in line_upper:
            current_status = 'design'
        elif '(CONSTRUCTION)' in line_upper and 'PROJECT' in line_upper:
            current_status = 'construction'
        elif '(NOT STARTED)' in line_upper and 'PROJECT' in line_upper:
            current_status = 'not started'
        
        # Check if any of our FEMA project base names appear in this line
        for proj in fema_projects:
            base_name = proj['Project_Name'].split('(')[0].strip().upper()
            if len(base_name) > 8 and base_name in line_upper:
                if current_status:
                    proj['status'] = current_status
                    print(f"Found status for {proj['Project_Name']}: {current_status}")

# Also look for emergency-related terms in document content that match non-FEMA-named projects
emergency_keywords = ['EMERGENCY', 'FEMA', 'WARNING SIREN', 'WARNING SIGN', 'DISASTER']
additional_projects = []

for doc in civic_docs:
    text = doc.get('text', '')
    text_upper = text.upper()
    
    # Check if document contains emergency keywords
    contains_emergency = any(keyword in text_upper for keyword in emergency_keywords)
    
    if contains_emergency:
        # Look for project names from funding data in this document
        for item in funding_data:
            project_name = item['Project_Name']
            # Skip if already in our list
            if project_name in [p['Project_Name'] for p in fema_projects]:
                continue
            
            base_name = project_name.split('(')[0].strip().upper()
            if len(base_name) > 8 and base_name in text_upper:
                # Found a project in an emergency-related document
                additional_projects.append({
                    'Project_Name': project_name,
                    'Funding_Source': item['Funding_Source'],
                    'Amount': int(item['Amount']),
                    'status': 'Unknown'
                })
                print(f"Found additional emergency-related project: {project_name}")

# Combine all projects
all_projects = fema_projects + additional_projects

# Remove duplicates
unique_dict = {}
for proj in all_projects:
    unique_dict[proj['Project_Name']] = proj

final_result = list(unique_dict.values())

# Create JSON output
output = json.dumps(final_result, indent=2)
print('__RESULT__:')
print(output)"""

env_args = {'var_functions.query_db:0': [{'Funding_ID': '1', 'Project_Name': '2021 Annual Street Maintenance', 'Funding_Source': 'Public-Private Partnership (PPP)', 'Amount': '24000'}, {'Funding_ID': '2', 'Project_Name': '2022 Annual Street Maintenance', 'Funding_Source': 'Government Grant', 'Amount': '45000'}, {'Funding_ID': '3', 'Project_Name': '2022 Morning View Resurfacing & Storm Drain Improvements', 'Funding_Source': 'State Development Grant', 'Amount': '38000'}, {'Funding_ID': '4', 'Project_Name': 'Annual Street Maintenance', 'Funding_Source': 'Corporate Sponsorship', 'Amount': '23000'}, {'Funding_ID': '5', 'Project_Name': 'Birdview Avenue Improvements', 'Funding_Source': 'National Foundation Fund', 'Amount': '79000'}, {'Funding_ID': '6', 'Project_Name': 'Birdview Avenue Improvements (CalOES Project)', 'Funding_Source': 'International Aid', 'Amount': '85000'}, {'Funding_ID': '7', 'Project_Name': 'Birdview Avenue Improvements (FEMA/CalOES Project)', 'Funding_Source': 'Research Institution Funding', 'Amount': '14000'}, {'Funding_ID': '8', 'Project_Name': 'Bluffs Park Shade Structure', 'Funding_Source': 'Government Grant', 'Amount': '21000'}, {'Funding_ID': '9', 'Project_Name': 'Bluffs Park Workout Station', 'Funding_Source': 'University Research Fund', 'Amount': '39000'}, {'Funding_ID': '10', 'Project_Name': 'Broad Beach Road Water Quality Infrastructure Repairs', 'Funding_Source': 'International Organization Grant', 'Amount': '87000'}], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:4': 'file_storage/functions.query_db:4.json'}

exec(code, env_args)
