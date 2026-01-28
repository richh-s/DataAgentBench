code = """import json
import re

# Load funding data
funding_file = var_functions.query_db:4
if isinstance(funding_file, str) and funding_file.endswith('.json'):
    with open(funding_file, 'r') as f:
        funding_data = json.load(f)
else:
    funding_data = var_functions.query_db:4

# Load civic documents
civic_file = var_functions.query_db:11
if isinstance(civic_file, str) and civic_file.endswith('.json'):
    with open(civic_file, 'r') as f:
        civic_docs = json.load(f)
else:
    civic_docs = var_functions.query_db:11

print(f"Funding records loaded: {len(funding_data)}")
print(f"Civic documents loaded: {len(civic_docs)}")

# Create a set of project names from funding data for fast lookup
funding_projects = {record['Project_Name'] for record in funding_data}

# Debug: Show some funding project names
print(f"Sample funding projects: {list(funding_projects)[:10]}")

# Extract project information from civic documents
extracted_projects = []

for doc in civic_docs:
    text = doc.get('text', '')
    
    # Look for project patterns in the text
    # Common patterns:
    # - Project names are often at the start of lines or after bullet points
    # - Status information follows (Design, Construction, Not Started)
    # - Type is often indicated (Capital Improvement Projects, Disaster Recovery Projects)
    
    # Split text into lines for easier processing
    lines = text.split('\n')
    
    current_section = None
    current_type = None
    
    for line in lines:
        line = line.strip()
        
        # Identify sections and types
        if 'Capital Improvement Projects' in line and 'Design' in line:
            current_section = 'Design'
            current_type = 'capital'
        elif 'Capital Improvement Projects' in line and 'Construction' in line:
            current_section = 'Construction'
            current_type = 'capital'
        elif 'Capital Improvement Projects' in line and 'Not Started' in line:
            current_section = 'Not Started'
            current_type = 'capital'
        elif 'Disaster Recovery Projects' in line:
            current_type = 'disaster'
        
        # Look for project names - they typically appear as separate lines
        # or after bullet points
        if current_section == 'Design' and current_type == 'capital' and line:
            # Skip section headers and empty lines
            if (line.startswith('Capital Improvement Projects') or 
                line.startswith('DISCUSSION:') or
                line.startswith('RECOMMENDED ACTION:') or
                line.startswith('Page') or
                line.startswith('Agenda Item') or
                len(line) < 5):
                continue
                
            # Look for project name patterns
            # Often project names are followed by status indicators or descriptions
            if (line[0].isupper() or line.startswith('â€¢') or line.startswith('â€‘')):
                # Clean up the project name
                project_name = line.strip('â€¢â€‘- ').strip()
                
                # Skip common non-project lines
                skip_patterns = [
                    'Updates:', 'Project Schedule:', 'Complete Design:', 
                    'Advertise:', 'Begin Construction:', 'To:', 'Prepared by:',
                    'Approved by:', 'Date prepared:', 'Meeting date:', 'Subject:',
                    'RECOMMENDED ACTION:', 'DISCUSSION:', 'Page', 'Agenda Item'
                ]
                
                if any(pattern in project_name for pattern in skip_patterns):
                    continue
                
                # Skip lines that seem like descriptions rather than names
                if len(project_name) > 150 or project_name.endswith(':'):
                    continue
                
                # Look for status indicators in the text around this line
                status = 'design'  # Default for this section
                
                # Check if this project has funding
                if project_name in funding_projects:
                    extracted_projects.append({
                        'Project_Name': project_name,
                        'status': status,
                        'type': current_type
                    })

print(f"Extracted projects with design status: {len(extracted_projects)}")

# Now match with funding data and filter for amount > 50000
matched_projects = []

for project in extracted_projects:
    # Find matching funding records
    for funding_record in funding_data:
        if funding_record['Project_Name'] == project['Project_Name']:
            amount = int(funding_record['Amount'])
            if amount > 50000:
                matched_projects.append({
                    'Project_Name': project['Project_Name'],
                    'Amount': amount,
                    'Funding_Source': funding_record['Funding_Source']
                })

print(f"Capital projects with design status and funding > $50,000: {len(matched_projects)}")

# Print the matches for verification
for proj in matched_projects[:10]:
    print(f"  - {proj['Project_Name']}: ${proj['Amount']}")

# Save the result
result = {
    'count': len(matched_projects),
    'projects': matched_projects
}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.query_db:0': [{'Funding_ID': '5', 'Project_Name': 'Birdview Avenue Improvements', 'Funding_Source': 'National Foundation Fund', 'Amount': '79000'}, {'Funding_ID': '6', 'Project_Name': 'Birdview Avenue Improvements (CalOES Project)', 'Funding_Source': 'International Aid', 'Amount': '85000'}, {'Funding_ID': '10', 'Project_Name': 'Broad Beach Road Water Quality Infrastructure Repairs', 'Funding_Source': 'International Organization Grant', 'Amount': '87000'}, {'Funding_ID': '11', 'Project_Name': 'Broad Beach Road Water Quality Infrastructure Repairs (CalJPIA Project)', 'Funding_Source': 'Government Grant', 'Amount': '81000'}, {'Funding_ID': '12', 'Project_Name': 'Broad Beach Road Water Quality Repair', 'Funding_Source': 'University Research Fund', 'Amount': '93000'}, {'Funding_ID': '13', 'Project_Name': 'City Hall Roof Replacement', 'Funding_Source': 'Educational Sponsorship', 'Amount': '79000'}, {'Funding_ID': '15', 'Project_Name': 'City Traffic Signals Backup Power', 'Funding_Source': 'Social Impact Investment', 'Amount': '85000'}, {'Funding_ID': '18', 'Project_Name': 'Civic Center Stormwater Diversion Structure', 'Funding_Source': 'Educational Sponsorship', 'Amount': '64000'}, {'Funding_ID': '21', 'Project_Name': 'Clover Heights Storm Drain', 'Funding_Source': 'Infrastructure Bond', 'Amount': '53000'}, {'Funding_ID': '24', 'Project_Name': 'Corral Canyon Culvert Repairs', 'Funding_Source': 'Federal Assistance', 'Amount': '54000'}], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:4': 'file_storage/functions.query_db:4.json', 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.query_db:11': 'file_storage/functions.query_db:11.json'}

exec(code, env_args)
