code = """import json
import re

# Read civic documents data
civic_docs_data = var_functions.query_db:10

# Read funding data  
funding_data = var_functions.query_db:11

print(f"Loaded {len(civic_docs_data)} civic documents and {len(funding_data)} funding records")

# Create funding map
funding_map = {}
for record in funding_data:
    project_name = record['Project_Name']
    amount = int(record['Amount'])
    funding_map[project_name] = amount

spring_2022_projects = []
spring_patterns = [r'2022[-\s]?Spring', r'2022[-\s]?March', r'2022[-\s]?April', r'2022[-\s]?May', r'2022[-\s]?03', r'2022[-\s]?04', r'2022[-\s]?05']

# Process documents
for doc in civic_docs_data:
    text = doc.get('text', '')
    lines = text.split('\n')
    current_project = None
    
    for i, line in enumerate(lines):
        line = line.strip()
        
        if len(line) < 5 or line.startswith(('(', '•', '-', '–', '—', '•', '●', '○', '■')):
            continue
            
        if (line[0].isalpha() and line[0].isupper() and ':' not in line and not any(skip in line.lower() for skip in ['subject:', 'recommended action', 'discussion:', 'update', 'schedule']) and len(line.split()) <= 15):
            current_project = line
            continue
        
        if current_project:
            for pattern in spring_patterns:
                if re.search(pattern, line, re.IGNORECASE):
                    spring_2022_projects.append(current_project)
                    current_project = None
                    break
            
            if current_project and i < len(lines) - 3:
                next_lines = ' '.join(lines[i:i+3])
                for pattern in spring_patterns:
                    if re.search(pattern, next_lines, re.IGNORECASE):
                        spring_2022_projects.append(current_project)
                        current_project = None
                        break

# Remove duplicates
spring_2022_projects = list(dict.fromkeys(spring_2022_projects))
print(f"Found {len(spring_2022_projects)} Spring 2022 projects")

# Match with funding
total_funding = 0
matched_projects = []

for proj_name in spring_2022_projects:
    if proj_name in funding_map:
        funding = funding_map[proj_name]
        total_funding += funding
        matched_projects.append({'name': proj_name, 'funding': funding})
    else:
        base_name = proj_name.split('(')[0].strip()
        for fund_name, fund_amount in funding_map.items():
            fund_base = fund_name.split('(')[0].strip()
            if base_name in fund_name or fund_base in proj_name or base_name.lower() == fund_base.lower():
                total_funding += fund_amount
                matched_projects.append({'name': fund_name, 'funding': fund_amount})
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
