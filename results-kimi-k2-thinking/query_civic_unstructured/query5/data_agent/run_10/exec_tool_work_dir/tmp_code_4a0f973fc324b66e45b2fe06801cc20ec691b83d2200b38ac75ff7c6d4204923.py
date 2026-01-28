code = """import json
import re

# Load funding data
with open('file_storage/functions.query_db:18.json', 'r') as f:
    funding_data = json.load(f)

# Load civic documents
with open('file_storage/functions.query_db:14.json', 'r') as f:
    civic_docs = json.load(f)

# Identify disaster-related projects with 2022 dates
disaster_projects = []

for doc in civic_docs:
    text = doc.get('text', '')
    
    # Find projects with disaster-related keywords and 2022 dates
    # Look for patterns like "Project Name" followed by schedule info with 2022
    
    # Split into project blocks
    blocks = text.split('\n\n')
    
    for block in blocks:
        block_lower = block.lower()
        
        # Check if this is a disaster-related block
        has_disaster = any(keyword in block_lower for keyword in ['fema', 'caloes', 'caljpia', 'disaster', 'emergency'])
        has_2022 = '2022' in block
        
        if has_disaster and has_2022:
            # Extract project name (first line that's not empty and looks like a title)
            lines = [line.strip() for line in block.split('\n') if line.strip()]
            
            for line in lines:
                if len(line) > 10 and not line.startswith('('):
                    project_name = line
                    # Look for schedule line with 2022
                    if '2022' in block:
                        disaster_projects.append(project_name)
                        break

# Also find explicit FEMA/CalOES projects
for doc in civic_docs:
    text = doc.get('text', '')
    matches = re.findall(r'([^\n]+\(FEMA[^\n]*\)|[^\n]+\(CalOES[^\n]*\)|[^\n]+\(CalJPIA[^\n]*\))', text, re.IGNORECASE)
    
    for match in matches:
        if '2022' in text:
            disaster_projects.append(match.strip())

# Get unique disaster project names
unique_disaster = list(set(disaster_projects))

# Find matching funding records
matches = []
for funding_item in funding_data:
    funding_name = funding_item['Project_Name']
    
    # Check if funding name matches any disaster project
    for disaster_proj in unique_disaster:
        # Exact match
        if funding_name == disaster_proj:
            matches.append(funding_item)
        # Partial match without suffix
        elif disaster_proj.startswith(funding_name):
            matches.append(funding_item)
        # Check for disaster keywords
        elif any(keyword in funding_name.lower() for keyword in ['fema', 'caloes', 'caljpia']):
            if '2022' in funding_name:
                matches.append(funding_item)

# Calculate total funding
total = sum(int(item['Amount']) for item in matches)

# Get unique matches
unique_matches = []
seen = set()
for item in matches:
    if item['Project_Name'] not in seen:
        unique_matches.append(item)
        seen.add(item['Project_Name'])

print("__RESULT__:")
result = {
    "disaster_projects_identified": len(unique_disaster),
    "funding_records_matched": len(unique_matches),
    "total_funding": total
}
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.execute_python:6': {'count': 0, 'file_exists': False, 'error': 'File not found: /tmp/tmphn4t1u8a.json'}, 'var_functions.query_db:12': [{'Funding_ID': '1', 'Project_Name': '2021 Annual Street Maintenance', 'Funding_Source': 'Public-Private Partnership (PPP)', 'Amount': '24000'}, {'Funding_ID': '2', 'Project_Name': '2022 Annual Street Maintenance', 'Funding_Source': 'Government Grant', 'Amount': '45000'}, {'Funding_ID': '3', 'Project_Name': '2022 Morning View Resurfacing & Storm Drain Improvements', 'Funding_Source': 'State Development Grant', 'Amount': '38000'}, {'Funding_ID': '4', 'Project_Name': 'Annual Street Maintenance', 'Funding_Source': 'Corporate Sponsorship', 'Amount': '23000'}, {'Funding_ID': '5', 'Project_Name': 'Birdview Avenue Improvements', 'Funding_Source': 'National Foundation Fund', 'Amount': '79000'}], 'var_functions.query_db:14': 'file_storage/functions.query_db:14.json', 'var_functions.query_db:16': 'file_storage/functions.query_db:16.json', 'var_functions.query_db:18': 'file_storage/functions.query_db:18.json', 'var_functions.execute_python:22': {'funding_type': 'str', 'civic_docs_type': 'str', 'funding_preview': 'file_storage/functions.query_db:18.json', 'civic_docs_preview': 'file_storage/functions.query_db:14.json'}, 'var_functions.execute_python:24': 'file_storage/functions.execute_python:24.json'}

exec(code, env_args)
