code = """import json, re, os
import sys

# File paths from stored variables
funding_path = var_functions.query_db:41
civic_path = var_functions.query_db:40

# Load data from files
with open(funding_path) as f:
    funding_entries = json.load(f)

with open(civic_path) as f:
    civic_entries = json.load(f)

# Track projects that match criteria
matched_projects = {}

# Step 1: Find projects with 2022 and disaster keywords in funding data
for entry in funding_entries:
    project_name = entry.get('Project_Name', '')
    amount = int(entry.get('Amount', 0))
    
    # Check for disaster keywords and 2022 year
    has_disaster_keyword = any(kw in project_name.upper() for kw in ['FEMA', 'CALOES', 'CALJPIA'])
    has_2022 = '2022' in project_name
    
    if has_disaster_keyword and has_2022:
        if project_name not in matched_projects:
            matched_projects[project_name] = amount

# Step 2: Find additional projects from civic documents
for doc in civic_entries:
    text = doc.get('text', '')
    if '2022' not in text:
        continue
        
    # Look for FEMA/CalOES project patterns
    pattern = r'([A-Z][^\n(]*?)\s*\(((?:FEMA|CalOES|CalJPIA)[^)]*Project)\)'
    matches = re.findall(pattern, text, re.IGNORECASE | re.MULTILINE)
    
    for match in matches:
        clean_name = match[0].strip()
        if not clean_name or len(clean_name) < 5:
            continue
            
        # Find matching funding entry
        for fund_entry in funding_entries:
            fund_name = fund_entry.get('Project_Name', '')
            fund_amount = int(fund_entry.get('Amount', 0))
            
            if fund_name.startswith(clean_name) or clean_name in fund_name:
                if fund_name not in matched_projects:
                    matched_projects[fund_name] = fund_amount

# Calculate total and prepare output
total_funding = sum(matched_projects.values())
project_list = [{'name': k, 'amount': v} for k, v in matched_projects.items()]

output = {
    'total_funding': total_funding,
    'project_count': len(project_list),
    'projects': project_list
}

print('__RESULT__:')
print(json.dumps(output, indent=2))"""

env_args = {'var_functions.list_db:0': ['Funding'], 'var_functions.list_db:1': ['civic_docs'], 'var_functions.query_db:4': 'file_storage/functions.query_db:4.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.execute_python:24': {'test': 'hello'}, 'var_functions.query_db:26': 'file_storage/functions.query_db:26.json', 'var_functions.query_db:27': 'file_storage/functions.query_db:27.json', 'var_functions.query_db:30': 'file_storage/functions.query_db:30.json', 'var_functions.query_db:31': 'file_storage/functions.query_db:31.json', 'var_functions.query_db:40': 'file_storage/functions.query_db:40.json', 'var_functions.query_db:41': 'file_storage/functions.query_db:41.json'}

exec(code, env_args)
