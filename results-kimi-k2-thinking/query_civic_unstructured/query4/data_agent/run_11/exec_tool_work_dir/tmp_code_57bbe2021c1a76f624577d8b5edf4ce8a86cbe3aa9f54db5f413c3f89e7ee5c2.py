code = """import json

# Load all civic documents
civic_docs_file = locals()['var_functions.query_db:32']
with open(civic_docs_file, 'r') as f:
    civic_docs = json.load(f)

# Load all funding data
funding_file = locals()['var_functions.query_db:36']
with open(funding_file, 'r') as f:
    funding_data = json.load(f)

print(f"Loaded {len(civic_docs)} documents and {len(funding_data)} funding records")

# Create a lookup dictionary for funding by project name
funding_lookup = {}
for fund in funding_data:
    project_name = fund['Project_Name']
    amount = int(fund['Amount'])
    funding_lookup[project_name] = {
        'amount': amount,
        'source': fund['Funding_Source'],
        'id': fund['Funding_ID']
    }

# Define Spring 2022 date patterns
date_patterns = [
    '2022-Spring',
    'Spring 2022',
    '2022-March',
    '2022-April', 
    '2022-May',
    'March 2022',
    'April 2022',
    'May 2022'
]

# Initialize results
spring_2022_projects = set()
funded_projects = []
total_amount = 0

# Process each document to find Spring 2022 projects
for doc in civic_docs:
    text = doc.get('text', '')
    lines = text.split('\n')
    
    for i, line in enumerate(lines):
        line_clean = line.strip()
        if not line_clean:
            continue
            
        # Skip headers and metadata
        if any(skip in line_clean for skip in ['Prepared by:', 'Approved by:', 'Meeting date:', 'Page ', 'Agenda Item']):
            continue
            
        # Look for Spring 2022 patterns in context
        context_start = max(0, i-5)
        context_end = min(len(lines), i+10)
        context = ' '.join(lines[context_start:context_end])
        
        # Check if this is a project line (starts uppercase, reasonable length)
        if line_clean and line_clean[0].isupper() and len(line_clean) > 8:
            # Check if context contains Spring 2022 indicators
            if any(pattern in context for pattern in date_patterns):
                if line_clean.endswith(('.', ':', ';')):
                    continue
                    
                spring_2022_projects.add(line_clean)
                
                # Check for matching funding
                if line_clean in funding_lookup:
                    fund_info = funding_lookup[line_clean]
                    funded_projects.append({
                        'project_name': line_clean,
                        'funding_id': fund_info['id'],
                        'amount': fund_info['amount'],
                        'source': fund_info['source']
                    })
                    total_amount += fund_info['amount']

# Also check for projects that might not be detected above but are in funding data
for fund in funding_data:
    project_name = fund['Project_Name']
    # Check if project name contains 2022
    if '2022' in project_name and any(month in project_name for month in ['March', 'April', 'May', 'Spring']):
        spring_2022_projects.add(project_name)
        
        # Add to funded projects if not already there
        found = any(fp['project_name'] == project_name for fp in funded_projects)
        if not found:
            amount = int(fund['Amount'])
            funded_projects.append({
                'project_name': project_name,
                'funding_id': fund['Funding_ID'],
                'amount': amount,
                'source': fund['Funding_Source']
            })
            total_amount += amount

print(f"Found {len(spring_2022_projects)} unique Spring 2022 projects")
print(f"Total funding: ${total_amount:,}")
print(f"Number of funded projects: {len(funded_projects)}")

result = {
    'number_of_projects': len(spring_2022_projects),
    'total_funding': total_amount,
    'project_names': sorted(list(spring_2022_projects)),
    'funded_projects': funded_projects
}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:2': [{'Funding_ID': '1', 'Project_Name': '2021 Annual Street Maintenance', 'Funding_Source': 'Public-Private Partnership (PPP)', 'Amount': '24000'}, {'Funding_ID': '2', 'Project_Name': '2022 Annual Street Maintenance', 'Funding_Source': 'Government Grant', 'Amount': '45000'}, {'Funding_ID': '3', 'Project_Name': '2022 Morning View Resurfacing & Storm Drain Improvements', 'Funding_Source': 'State Development Grant', 'Amount': '38000'}, {'Funding_ID': '4', 'Project_Name': 'Annual Street Maintenance', 'Funding_Source': 'Corporate Sponsorship', 'Amount': '23000'}, {'Funding_ID': '5', 'Project_Name': 'Birdview Avenue Improvements', 'Funding_Source': 'National Foundation Fund', 'Amount': '79000'}, {'Funding_ID': '6', 'Project_Name': 'Birdview Avenue Improvements (CalOES Project)', 'Funding_Source': 'International Aid', 'Amount': '85000'}, {'Funding_ID': '7', 'Project_Name': 'Birdview Avenue Improvements (FEMA/CalOES Project)', 'Funding_Source': 'Research Institution Funding', 'Amount': '14000'}, {'Funding_ID': '8', 'Project_Name': 'Bluffs Park Shade Structure', 'Funding_Source': 'Government Grant', 'Amount': '21000'}, {'Funding_ID': '9', 'Project_Name': 'Bluffs Park Workout Station', 'Funding_Source': 'University Research Fund', 'Amount': '39000'}, {'Funding_ID': '10', 'Project_Name': 'Broad Beach Road Water Quality Infrastructure Repairs', 'Funding_Source': 'International Organization Grant', 'Amount': '87000'}], 'var_functions.execute_python:18': {'documents_with_spring_2022': 5, 'sample_filenames': ['malibucity_agenda_03222023-2060.txt', 'malibucity_agenda__01262022-1835.txt', 'malibucity_agenda__01272021-1626.txt', 'malibucity_agenda__03022021-1648.txt', 'malibucity_agenda__03232022-1869.txt']}, 'var_functions.query_db:22': 'file_storage/functions.query_db:22.json', 'var_functions.query_db:24': 'file_storage/functions.query_db:24.json', 'var_functions.query_db:28': 'file_storage/functions.query_db:28.json', 'var_functions.query_db:30': 'file_storage/functions.query_db:30.json', 'var_functions.query_db:32': 'file_storage/functions.query_db:32.json', 'var_functions.query_db:36': 'file_storage/functions.query_db:36.json'}

exec(code, env_args)
