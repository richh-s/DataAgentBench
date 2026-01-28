code = """import json
import re

# Load data
with open('file_storage/functions.query_db:18.json', 'r') as f:
    funding_data = json.load(f)

with open('file_storage/functions.query_db:14.json', 'r') as f:
    civic_docs = json.load(f)

# Find disaster projects that started in 2022
disaster_names = set()

for doc in civic_docs:
    text = doc.get('text', '').lower()
    
    # Check if document has disaster keywords and 2022
    if any(k in text for k in ['fema', 'caloes', 'caljpia']) and '2022' in text:
        # Extract project names from this document
        full_text = doc.get('text', '')
        lines = full_text.split('\n')
        
        for line in lines:
            line = line.strip()
            if len(line) < 5:
                continue
            # Look for lines that might be project names
            if any(indicator in line.lower() for indicator in ['improvements', 'repairs', 'project', 'drainage', 'bridge', 'culvert']):
                if any(k in line.lower() for k in ['fema', 'caloes', 'caljpia']):
                    disaster_names.add(line.strip())

# Find all projects with FEMA/CalOES/CalJPIA suffixes
for doc in civic_docs:
    text = doc.get('text', '')
    pattern = r'([^\n]+\((?:FEMA|CalOES|CalJPIA)[^\n]*\))'
    matches = re.findall(pattern, text, re.IGNORECASE)
    for m in matches:
        if '2022' in text:
            disaster_names.add(m.strip())

# Match with funding data
total = 0
matched = []

# Create simplified lookup
simple_lookup = {}
for name in disaster_names:
    simple = re.sub(r'\s*\([^)]*\)$', '', name).strip()
    simple_lookup[simple] = name

for item in funding_data:
    fund_name = item['Project_Name']
    
    # Direct match
    if fund_name in disaster_names:
        total += int(item['Amount'])
        matched.append(item)
    # Simplified match
    elif fund_name in simple_lookup:
        total += int(item['Amount'])
        matched.append(item)
    # Disaster projects with 2022 in name
    elif any(k in fund_name.lower() for k in ['fema', 'caloes', 'caljpia']) and '2022' in fund_name:
        total += int(item['Amount'])
        matched.append(item)

# Remove duplicates
seen = set()
unique_matched = []
for item in matched:
    if item['Project_Name'] not in seen:
        seen.add(item['Project_Name'])
        unique_matched.append(item)

# Recalculate total
total = sum(int(item['Amount']) for item in unique_matched)

print('__RESULT__:')
print(json.dumps({
    'disaster_projects_count': len(disaster_names),
    'funding_records': len(unique_matched),
    'total_funding': total
}))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.execute_python:6': {'count': 0, 'file_exists': False, 'error': 'File not found: /tmp/tmphn4t1u8a.json'}, 'var_functions.query_db:12': [{'Funding_ID': '1', 'Project_Name': '2021 Annual Street Maintenance', 'Funding_Source': 'Public-Private Partnership (PPP)', 'Amount': '24000'}, {'Funding_ID': '2', 'Project_Name': '2022 Annual Street Maintenance', 'Funding_Source': 'Government Grant', 'Amount': '45000'}, {'Funding_ID': '3', 'Project_Name': '2022 Morning View Resurfacing & Storm Drain Improvements', 'Funding_Source': 'State Development Grant', 'Amount': '38000'}, {'Funding_ID': '4', 'Project_Name': 'Annual Street Maintenance', 'Funding_Source': 'Corporate Sponsorship', 'Amount': '23000'}, {'Funding_ID': '5', 'Project_Name': 'Birdview Avenue Improvements', 'Funding_Source': 'National Foundation Fund', 'Amount': '79000'}], 'var_functions.query_db:14': 'file_storage/functions.query_db:14.json', 'var_functions.query_db:16': 'file_storage/functions.query_db:16.json', 'var_functions.query_db:18': 'file_storage/functions.query_db:18.json', 'var_functions.execute_python:22': {'funding_type': 'str', 'civic_docs_type': 'str', 'funding_preview': 'file_storage/functions.query_db:18.json', 'civic_docs_preview': 'file_storage/functions.query_db:14.json'}, 'var_functions.execute_python:24': 'file_storage/functions.execute_python:24.json'}

exec(code, env_args)
