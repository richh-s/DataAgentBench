code = """import json
import re

# Load civic documents from file path
civic_docs_file = locals()['var_functions.query_db:32']
if isinstance(civic_docs_file, str) and civic_docs_file.endswith('.json'):
    with open(civic_docs_file, 'r') as f:
        civic_docs = json.load(f)
else:
    civic_docs = civic_docs_file

# Load funding data from file path  
funding_file = locals()['var_functions.query_db:33']
if isinstance(funding_file, str) and funding_file.endswith('.json'):
    with open(funding_file, 'r') as f:
        funding_data = json.load(f)
else:
    funding_data = funding_file

spring_2022_projects = []

# Extract Spring 2022 projects from civic documents
for doc in civic_docs:
    text = doc.get('text', '')
    lines = text.split('\n')
    
    current_project = None
    i = 0
    
    while i < len(lines):
        line = lines[i].strip()
        
        # Skip empty lines and headers
        if not line or line.startswith('(') or line.startswith('cid:') or \
           line.startswith('Page') or line.startswith('Agenda') or \
           'RECOMMENDED' in line or 'DISCUSSION:' in line or \
           'To:' in line or 'Prepared by:' in line or 'Approved by:' in line:
            i += 1
            continue
        
        # Look for project-like names (lines with capitalized words, no common headers)
        if len(line) > 5 and len(line) < 200 and line[0].isupper():
            words = line.split()
            capitalized = sum(1 for w in words if w and w[0].isupper())
            
            if capitalized >= 2 and not ('Agenda' in line or 'Page' in line):
                # Look ahead to find schedule info mentioning Spring 2022
                for j in range(i+1, min(i+20, len(lines))):
                    next_line = lines[j].strip()
                    
                    if '2022' in next_line:
                        if any(season in next_line for season in ['Spring', 'spring', 'March', 'April', 'May']):
                            # Found Spring 2022 project
                            project_name = line.strip()
                            spring_2022_projects.append({
                                'project_name': project_name,
                                'schedule': next_line,
                                'doc_id': doc.get('_id')
                            })
                            break
                        # Skip to next iteration if 2022 found but not spring
                    # Stop looking if we hit a new section
                    if next_line.startswith('Capital Improvement') or \
                       next_line.startswith('RECOMMENDED') or \
                       (next_line == '' and j > i+5):
                        break
        
        i += 1

# If no projects found, try regex patterns
if not spring_2022_projects:
    for doc in civic_docs:
        text = doc.get('text', '')
        
        # Find patterns where project name appears before Spring 2022
        pattern = r'([A-Z][a-zA-Z\s\-&]+?(?:\s*\([^\)]*\))?)\s*\n[^\n]{0,100}?(?:Spring|spring|March|April|May)\s*2022'
        
        matches = re.finditer(pattern, text, re.IGNORECASE | re.MULTILINE)
        for match in matches:
            project_name = match.group(1).strip()
            if project_name and len(project_name) < 200:
                spring_2022_projects.append({
                    'project_name': project_name,
                    'doc_id': doc.get('_id')
                })

# Deduplicate projects
unique_projects = {}
for proj in spring_2022_projects:
    name = proj['project_name']
    unique_projects[name] = proj

projects_list = list(unique_projects.values())

# Create lookup for funding - extract base project name (without FEMA/CalOES suffixes)
funding_by_project = {}
for fund in funding_data:
    proj_name = fund.get('Project_Name', '')
    amount = int(fund.get('Amount', 0))
    
    # Store multiple variations for matching
    funding_by_project[proj_name] = amount
    
    # Also store base name without suffixes
    base_name = re.sub(r'\s*\(FEMA[^\)]*\)', '', proj_name)
    base_name = re.sub(r'\s*\(CalOES[^\)]*\)', '', base_name)
    base_name = re.sub(r'\s*\(CalJPIA[^\)]*\)', '', base_name)
    base_name = base_name.strip()
    
    if base_name != proj_name:
        funding_by_project[base_name] = funding_by_project.get(base_name, 0) + amount

# Find funding for Spring 2022 projects
spring_2022_with_funding = []
total_funding = 0

for proj in projects_list:
    proj_name = proj['project_name']
    funding_amount = 0
    
    # Try exact match
    if proj_name in funding_by_project:
        funding_amount = funding_by_project[proj_name]
    else:
        # Try fuzzy matching with common pattern variations
        for fund_name, amount in funding_by_project.items():
            if proj_name in fund_name or fund_name in proj_name:
                funding_amount = amount
                break
    
    if funding_amount > 0:
        proj['funding_amount'] = funding_amount
        spring_2022_with_funding.append(proj)
        total_funding += funding_amount

result = {
    'spring_2022_projects': spring_2022_with_funding,
    'project_count': len(spring_2022_with_funding),
    'total_funding': total_funding
}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': [], 'var_functions.query_db:4': 'file_storage/functions.query_db:4.json', 'var_functions.query_db:5': [{'Funding_ID': '1', 'Project_Name': '2021 Annual Street Maintenance', 'Funding_Source': 'Public-Private Partnership (PPP)', 'Amount': '24000'}, {'Funding_ID': '2', 'Project_Name': '2022 Annual Street Maintenance', 'Funding_Source': 'Government Grant', 'Amount': '45000'}, {'Funding_ID': '3', 'Project_Name': '2022 Morning View Resurfacing & Storm Drain Improvements', 'Funding_Source': 'State Development Grant', 'Amount': '38000'}, {'Funding_ID': '4', 'Project_Name': 'Annual Street Maintenance', 'Funding_Source': 'Corporate Sponsorship', 'Amount': '23000'}, {'Funding_ID': '5', 'Project_Name': 'Birdview Avenue Improvements', 'Funding_Source': 'National Foundation Fund', 'Amount': '79000'}], 'var_functions.execute_python:8': {'civic_docs_count': 5, 'funding_records_count': 5, 'funding_sample': [{'Funding_ID': '1', 'Project_Name': '2021 Annual Street Maintenance', 'Funding_Source': 'Public-Private Partnership (PPP)', 'Amount': '24000'}, {'Funding_ID': '2', 'Project_Name': '2022 Annual Street Maintenance', 'Funding_Source': 'Government Grant', 'Amount': '45000'}, {'Funding_ID': '3', 'Project_Name': '2022 Morning View Resurfacing & Storm Drain Improvements', 'Funding_Source': 'State Development Grant', 'Amount': '38000'}]}, 'var_functions.query_db:10': 'file_storage/functions.query_db:10.json', 'var_functions.query_db:11': 'file_storage/functions.query_db:11.json', 'var_functions.query_db:20': 'file_storage/functions.query_db:20.json', 'var_functions.query_db:21': [{'total_records': '500'}], 'var_functions.query_db:24': 'file_storage/functions.query_db:24.json', 'var_functions.query_db:28': 'file_storage/functions.query_db:28.json', 'var_functions.query_db:32': 'file_storage/functions.query_db:32.json', 'var_functions.query_db:33': 'file_storage/functions.query_db:33.json'}

exec(code, env_args)
