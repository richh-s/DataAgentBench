code = """import json
import re

# Load funding data
with open('file_storage/functions.query_db:18.json', 'r') as f:
    funding_data = json.load(f)

# Load civic documents data
with open('file_storage/functions.query_db:14.json', 'r') as f:
    civic_docs = json.load(f)

# Identify disaster-related projects from civic documents
# Look for projects with FEMA, CalOES, CalJPIA in the name or context
disaster_project_names = set()

for doc in civic_docs:
    text = doc.get('text', '')
    
    # Find projects with explicit FEMA/CalOES/CalJPIA markers
    # Pattern: Project Name (FEMA Project) or similar
    explicit_matches = re.findall(r'([^\n]+\((?:FEMA|CalOES|CalJPIA)[^\n]*\))', text, re.IGNORECASE)
    for match in explicit_matches:
        if '2022' in text:
            disaster_project_names.add(match.strip())
    
    # Also look for project blocks that mention both disaster keywords and 2022
    lines = text.split('\n')
    for i, line in enumerate(lines):
        line = line.strip()
        # Skip empty lines and headers
        if not line or len(line) < 5:
            continue
        
        # Check if line contains disaster keywords
        has_disaster = any(keyword in line.lower() for keyword in ['fema', 'caloes', 'caljpia', 'disaster', 'emergency'])
        
        if has_disaster:
            # Look for year info in surrounding lines
            context = '\n'.join(lines[max(0, i-5):min(len(lines), i+10)])
            if '2022' in context:
                # Clean up the project name
                if not any(word in line.lower() for word in ['updates', 'schedule', 'discussion', 'subject']):
                    disaster_project_names.add(line)

# Find funding records for these disaster projects
total_funding = 0
matched_funding = []

for funding_item in funding_data:
    funding_name = funding_item['Project_Name']
    amount = int(funding_item['Amount'])
    
    # Check if this funding matches any disaster project
    # 1. Check if funding name contains disaster keywords and 2022
    if any(keyword in funding_name.lower() for keyword in ['fema', 'caloes', 'caljpia']):
        if '2022' in funding_name:
            total_funding += amount
            matched_funding.append(funding_item)
    
    # 2. Check if funding name matches any identified disaster project (without suffix)
    for disaster_name in disaster_project_names:
        # Remove suffixes for comparison
        base_name = re.sub(r'\s*\([^)]*\)$', '', disaster_name)
        if funding_name == base_name or funding_name.startswith(base_name):
            total_funding += amount
            matched_funding.append(funding_item)
            break

# Remove duplicates from matched funding
unique_matched = []
seen_names = set()
for item in matched_funding:
    if item['Project_Name'] not in seen_names:
        unique_matched.append(item)
        seen_names.add(item['Project_Name'])

total_funding = sum(int(item['Amount']) for item in unique_matched)

print('__RESULT__:')
print(json.dumps({
    'disaster_projects_identified': len(disaster_project_names),
    'funding_records_matched': len(unique_matched),
    'total_funding_2022_disaster': total_funding
}))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.execute_python:6': {'count': 0, 'file_exists': False, 'error': 'File not found: /tmp/tmphn4t1u8a.json'}, 'var_functions.query_db:12': [{'Funding_ID': '1', 'Project_Name': '2021 Annual Street Maintenance', 'Funding_Source': 'Public-Private Partnership (PPP)', 'Amount': '24000'}, {'Funding_ID': '2', 'Project_Name': '2022 Annual Street Maintenance', 'Funding_Source': 'Government Grant', 'Amount': '45000'}, {'Funding_ID': '3', 'Project_Name': '2022 Morning View Resurfacing & Storm Drain Improvements', 'Funding_Source': 'State Development Grant', 'Amount': '38000'}, {'Funding_ID': '4', 'Project_Name': 'Annual Street Maintenance', 'Funding_Source': 'Corporate Sponsorship', 'Amount': '23000'}, {'Funding_ID': '5', 'Project_Name': 'Birdview Avenue Improvements', 'Funding_Source': 'National Foundation Fund', 'Amount': '79000'}], 'var_functions.query_db:14': 'file_storage/functions.query_db:14.json', 'var_functions.query_db:16': 'file_storage/functions.query_db:16.json', 'var_functions.query_db:18': 'file_storage/functions.query_db:18.json', 'var_functions.execute_python:22': {'funding_type': 'str', 'civic_docs_type': 'str', 'funding_preview': 'file_storage/functions.query_db:18.json', 'civic_docs_preview': 'file_storage/functions.query_db:14.json'}, 'var_functions.execute_python:24': 'file_storage/functions.execute_python:24.json'}

exec(code, env_args)
