code = """import json
import re

# Load data from files
with open('file_storage/functions.query_db:18.json', 'r') as f:
    funding_data = json.load(f)

with open('file_storage/functions.query_db:14.json', 'r') as f:
    civic_docs = json.load(f)

# Step 1: Identify disaster projects with 2022 start dates from civic documents
disaster_projects_2022 = set()

for doc in civic_docs:
    text = doc.get('text', '')
    
    # Find all mentions of projects with disaster keywords
    disaster_keywords = ['fema', 'caloes', 'caljpia', 'disaster', 'emergency', 'woolsey fire']
    
    for keyword in disaster_keywords:
        if keyword in text.lower():
            # Look for 2022 dates in the text
            if '2022' in text:
                # Find project names near the disaster keyword
                # Usually formatted as "Project Name" followed by schedule info
                lines = text.split('\n')
                for i, line in enumerate(lines):
                    line = line.strip()
                    if keyword in line.lower() and len(line) > 10:
                        # This line or nearby lines might contain the project name
                        # Look ahead and behind for project names
                        for j in range(max(0, i-3), min(len(lines), i+4)):
                            proj_line = lines[j].strip()
                            if (len(proj_line) > 5 and 
                                not proj_line.startswith('(') and 
                                not any(x in proj_line.lower() for x in ['updates:', 'schedule:', 'discussion:'])):
                                # Check if this looks like a project name
                                if any(indicator in proj_line.lower() for indicator in 
                                      ['project', 'improvements', 'repairs', 'replacement', 'renovation', 
                                       'drainage', 'resurfacing', 'bridge', 'culvert', 'guardrail']):
                                    disaster_projects_2022.add(proj_line)
                                    break

# Also find explicit project names with FEMA/CalOES/CalJPIA suffixes
for doc in civic_docs:
    text = doc.get('text', '')
    
    # Pattern to find "Project Name (FEMA Project)" or similar
    matches = re.findall(r'([A-Za-z0-9][^\n]{5,80}\s*\((?:FEMA|CalOES|CalJPIA)[^\n]{0,30}\))', text, re.IGNORECASE)
    
    for match in matches:
        if '2022' in text:  # If the document mentions 2022 anywhere
            project_name = match.strip()
            # Clean up the name
            if len(project_name) > 5 and not project_name.startswith('('):
                disaster_projects_2022.add(project_name)

# Step 2: Find funding records that match these disaster projects
total_funding = 0
matched_projects = []

# For better matching, create a mapping of simplified names
simplified_disaster = {}
for full_name in disaster_projects_2022:
    # Remove parenthetical suffixes
    simple_name = re.sub(r'\s*\([^)]*\)$', '', full_name).strip()
    simplified_disaster[simple_name] = full_name

for funding_item in funding_data:
    funding_name = funding_item['Project_Name']
    amount = int(funding_item['Amount'])
    
    # Direct match
    if funding_name in disaster_projects_2022:
        total_funding += amount
        matched_projects.append(funding_item)
    
    # Match against simplified names
    elif funding_name in simplified_disaster:
        total_funding += amount
        funding_item['Full_Project_Name'] = simplified_disaster[funding_name]
        matched_projects.append(funding_item)
    
    # Check if funding name itself indicates disaster project with 2022
    else:
        has_disaster = any(keyword in funding_name.lower() for keyword in ['fema', 'caloes', 'caljpia'])
        has_2022 = '2022' in funding_name
        
        if has_disaster and has_2022:
            total_funding += amount
            matched_projects.append(funding_item)

# Deduplicate matched projects
unique_matched = []
seen = set()

for item in matched_projects:
    name = item['Project_Name']
    if name not in seen:
        seen.add(name)
        unique_matched.append(item)

# Recalculate total with unique records
total_funding = sum(int(item['Amount']) for item in unique_matched)

print('__RESULT__:')
print(json.dumps({
    'total_funding_2022_disaster_projects': total_funding,
    'number_of_disaster_projects': len(disaster_projects_2022),
    'number_of_matched_funding_records': len(unique_matched)
}))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.execute_python:6': {'count': 0, 'file_exists': False, 'error': 'File not found: /tmp/tmphn4t1u8a.json'}, 'var_functions.query_db:12': [{'Funding_ID': '1', 'Project_Name': '2021 Annual Street Maintenance', 'Funding_Source': 'Public-Private Partnership (PPP)', 'Amount': '24000'}, {'Funding_ID': '2', 'Project_Name': '2022 Annual Street Maintenance', 'Funding_Source': 'Government Grant', 'Amount': '45000'}, {'Funding_ID': '3', 'Project_Name': '2022 Morning View Resurfacing & Storm Drain Improvements', 'Funding_Source': 'State Development Grant', 'Amount': '38000'}, {'Funding_ID': '4', 'Project_Name': 'Annual Street Maintenance', 'Funding_Source': 'Corporate Sponsorship', 'Amount': '23000'}, {'Funding_ID': '5', 'Project_Name': 'Birdview Avenue Improvements', 'Funding_Source': 'National Foundation Fund', 'Amount': '79000'}], 'var_functions.query_db:14': 'file_storage/functions.query_db:14.json', 'var_functions.query_db:16': 'file_storage/functions.query_db:16.json', 'var_functions.query_db:18': 'file_storage/functions.query_db:18.json', 'var_functions.execute_python:22': {'funding_type': 'str', 'civic_docs_type': 'str', 'funding_preview': 'file_storage/functions.query_db:18.json', 'civic_docs_preview': 'file_storage/functions.query_db:14.json'}, 'var_functions.execute_python:24': 'file_storage/functions.execute_python:24.json'}

exec(code, env_args)
