code = """import json
import re

# Load funding data
funding_path = locals()['var_functions.query_db:6']
if isinstance(funding_path, str) and funding_path.endswith('.json'):
    with open(funding_path, 'r') as f:
        funding_data = json.load(f)
else:
    funding_data = locals()['var_functions.query_db:6']

# Load civic docs data
civic_docs_path = locals()['var_functions.query_db:8']
if isinstance(civic_docs_path, str) and civic_docs_path.endswith('.json'):
    with open(civic_docs_path, 'r') as f:
        civic_docs = json.load(f)
else:
    civic_docs = locals()['var_functions.query_db:8']

print(f"Funding records: {len(funding_data)}")
print(f"Civic documents: {len(civic_docs)}")

# Create a project info dictionary to store extracted data
project_info = {}

# Process each civic document
for doc in civic_docs:
    text = doc.get('text', '')
    filename = doc.get('filename', '')
    
    # Look for project sections
    # Pattern: project name followed by details
    lines = text.split('\n')
    current_project = None
    
    for i, line in enumerate(lines):
        line = line.strip()
        
        # Look for project names (typically on their own line, title case)
        # Skip empty lines, bullet points, and common headers
        if (line and 
            not line.startswith('(') and 
            not line.startswith('•') and 
            not line.startswith('·') and 
            not line.startswith('Page') and
            not line.startswith('Agenda') and
            len(line) > 10 and
            (line.istitle() or '(FEMA' in line or '(Cal' in line)):
            
            # Check if this looks like a project name
            project_indicators = ['Project', 'Improvements', 'Repairs', 'Structure', 'System', 
                                'Plan', 'Facility', 'Study', 'Drainage', 'Road', 'Bridge', 
                                'Roadway', 'Wall', 'Park', 'Signs', 'Sirens']
            
            if any(indicator in line for indicator in project_indicators) or '(FEMA' in line:
                current_project = line
                project_info[current_project] = {
                    'type': None,
                    'status': None,
                    'st': None,
                    'et': None,
                    'topic': []
                }
        
        # Look for schedule/updates after project name
        if current_project and i < len(lines) - 1:
            next_lines = '\n'.join(lines[i:i+5])
            
            # Look for start/completion dates
            if 'Begin' in next_lines or 'Complete' in next_lines or 'Schedule' in next_lines:
                # Extract dates mentioned
                date_patterns = [
                    r'(\d{4}[-\s]\w+)',
                    r'(\d{4})'
                ]
                
                for pattern in date_patterns:
                    dates = re.findall(pattern, next_lines)
                    if dates:
                        for date in dates:
                            if '2022' in date and not project_info[current_project]['st']:
                                project_info[current_project]['st'] = date
                            elif '2023' in date and not project_info[current_project]['st']:
                                project_info[current_project]['st'] = date

# Display extracted projects for debugging
disaster_projects = []
for name, info in project_info.items():
    # Check if it's a disaster project
    is_disaster = '(FEMA' in name or 'FEMA' in name or 'CalOES' in name or 'CalJPIA' in name
    
    if is_disaster:
        info['type'] = 'disaster'
        if info['st'] and '2022' in info['st']:
            disaster_projects.append(name)

print(f"\nFound {len(project_info)} potential projects")
print(f"Found {len(disaster_projects)} disaster projects that started in 2022")

for proj in disaster_projects[:10]:
    print(f"  - {proj}: {project_info[proj]['st']}")

# Create a mapping of project names to amounts from funding data
funding_map = {}
for record in funding_data:
    project_name = record.get('Project_Name', '')
    amount = int(record.get('Amount', 0))
    funding_map[project_name] = amount

print(f"\nFunding map has {len(funding_map)} entries")

# Match disaster projects with funding
total_funding = 0
matched_projects = []

for project_name in disaster_projects:
    # Exact match
    if project_name in funding_map:
        amount = funding_map[project_name]
        total_funding += amount
        matched_projects.append((project_name, amount))
    else:
        # Try partial matching
        for fund_name, amount in funding_map.items():
            # Check if one name contains the other
            if (project_name in fund_name or fund_name in project_name) and abs(len(project_name) - len(fund_name)) < 20:
                total_funding += amount
                matched_projects.append((project_name, amount, fund_name))
                break

print(f"\nMatched {len(matched_projects)} projects with funding")
print(f"Total funding: ${total_funding:,}")

for proj in matched_projects:
    if len(proj) == 2:
        print(f"  - {proj[0]}: ${proj[1]:,}")
    else:
        print(f"  - {proj[0]} -> {proj[2]}: ${proj[1]:,}")"""

env_args = {'var_functions.list_db:0': ['Funding'], 'var_functions.query_db:2': [{'Funding_ID': '1', 'Project_Name': '2021 Annual Street Maintenance', 'Funding_Source': 'Public-Private Partnership (PPP)', 'Amount': '24000'}, {'Funding_ID': '2', 'Project_Name': '2022 Annual Street Maintenance', 'Funding_Source': 'Government Grant', 'Amount': '45000'}, {'Funding_ID': '3', 'Project_Name': '2022 Morning View Resurfacing & Storm Drain Improvements', 'Funding_Source': 'State Development Grant', 'Amount': '38000'}, {'Funding_ID': '4', 'Project_Name': 'Annual Street Maintenance', 'Funding_Source': 'Corporate Sponsorship', 'Amount': '23000'}, {'Funding_ID': '5', 'Project_Name': 'Birdview Avenue Improvements', 'Funding_Source': 'National Foundation Fund', 'Amount': '79000'}], 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json'}

exec(code, env_args)
