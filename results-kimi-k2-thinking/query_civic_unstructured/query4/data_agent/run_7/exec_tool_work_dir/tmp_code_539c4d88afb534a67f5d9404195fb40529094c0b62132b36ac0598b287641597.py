code = """import json
import re

# Get file paths
civic_docs_path = var_functions.query_db_10
funding_path = var_functions.query_db_11

# Read data
civic_docs = json.load(open(civic_docs_path))
funding = json.load(open(funding_path))

# Create funding map
funding_map = {}
for record in funding:
    project_name = record['Project_Name']
    amount = int(record['Amount'])
    funding_map[project_name] = amount

print(f"Loaded {len(civic_docs)} documents and {len(funding)} funding records")

# Extract Spring 2022 projects
spring_projects = []

for doc in civic_docs:
    text = doc.get('text', '')
    lines = text.split('\n')
    current_project = None
    
    for i, line in enumerate(lines):
        line = line.strip()
        
        # Skip empty lines and bullet points
        if len(line) < 5 or line[0] in ['(', '•', '-', '■', '□']:
            continue
        
        # Try to identify project names (title case, reasonable length, not metadata)
        if line[0].isalpha() and line[0].isupper() and ':' not in line and len(line.split()) <= 20:
            current_project = line
            continue
        
        # Check if this line or next few lines mention Spring 2022
        if current_project:
            # Check this line and next 2 lines
            check_range = lines[i:min(i+3, len(lines))]
            combined = ' '.join(check_range).lower()
            
            if '2022' in combined and ('spring' in combined or 'march' in combined or 'april' in combined or 'may' in combined):
                if current_project not in spring_projects:
                    spring_projects.append(current_project)
                current_project = None

# Remove duplicates
spring_projects = list(dict.fromkeys(spring_projects))
print(f"Found {len(spring_projects)} potential Spring 2022 projects")

# Match with funding
matched_projects = []
total_funding = 0

for proj in spring_projects:
    # Direct match
    if proj in funding_map:
        total_funding += funding_map[proj]
        matched_projects.append({'name': proj, 'funding': funding_map[proj]})
    else:
        # Try fuzzy matching by base name (without parentheses)
        base_name = proj.split('(')[0].strip().lower()
        
        for fund_name, amount in funding_map.items():
            fund_base = fund_name.split('(')[0].strip().lower()
            
            # Check for substantial overlap
            if base_name in fund_base or fund_base in base_name:
                total_funding += amount
                matched_projects.append({'name': fund_name, 'funding': amount})
                break

result = {
    'project_count': len(matched_projects),
    'total_funding': total_funding,
    'projects': matched_projects
}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.list_db:1': ['Funding'], 'var_functions.query_db:4': 'file_storage/functions.query_db:4.json', 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.query_db:8': [{'Funding_ID': '1', 'Project_Name': '2021 Annual Street Maintenance', 'Funding_Source': 'Public-Private Partnership (PPP)', 'Amount': '24000'}, {'Funding_ID': '2', 'Project_Name': '2022 Annual Street Maintenance', 'Funding_Source': 'Government Grant', 'Amount': '45000'}, {'Funding_ID': '3', 'Project_Name': '2022 Morning View Resurfacing & Storm Drain Improvements', 'Funding_Source': 'State Development Grant', 'Amount': '38000'}, {'Funding_ID': '4', 'Project_Name': 'Annual Street Maintenance', 'Funding_Source': 'Corporate Sponsorship', 'Amount': '23000'}, {'Funding_ID': '5', 'Project_Name': 'Birdview Avenue Improvements', 'Funding_Source': 'National Foundation Fund', 'Amount': '79000'}, {'Funding_ID': '6', 'Project_Name': 'Birdview Avenue Improvements (CalOES Project)', 'Funding_Source': 'International Aid', 'Amount': '85000'}, {'Funding_ID': '7', 'Project_Name': 'Birdview Avenue Improvements (FEMA/CalOES Project)', 'Funding_Source': 'Research Institution Funding', 'Amount': '14000'}, {'Funding_ID': '8', 'Project_Name': 'Bluffs Park Shade Structure', 'Funding_Source': 'Government Grant', 'Amount': '21000'}, {'Funding_ID': '9', 'Project_Name': 'Bluffs Park Workout Station', 'Funding_Source': 'University Research Fund', 'Amount': '39000'}, {'Funding_ID': '10', 'Project_Name': 'Broad Beach Road Water Quality Infrastructure Repairs', 'Funding_Source': 'International Organization Grant', 'Amount': '87000'}], 'var_functions.query_db:10': 'file_storage/functions.query_db:10.json', 'var_functions.query_db:11': 'file_storage/functions.query_db:11.json'}

exec(code, env_args)
