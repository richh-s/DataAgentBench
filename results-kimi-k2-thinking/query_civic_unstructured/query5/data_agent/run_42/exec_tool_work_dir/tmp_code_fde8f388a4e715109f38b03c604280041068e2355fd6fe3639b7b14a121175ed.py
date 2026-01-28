code = """import json, os, re
import sys
# Paths
funding_path = locals().get('var_functions.query_db:12')
civic_path = locals().get('var_functions.query_db:14')

# Load data
with open(funding_path) as f:
    funding_records = json.load(f)
with open(civic_path) as f:
    civic_docs = json.load(f)

# Extract disaster projects that started in 2022 from civic docs
disaster_projects_2022 = []

for doc in civic_docs:
    text = doc['text']
    lines = text.split('\n')
    i = 0
    while i < len(lines):
        line = lines[i].strip()
        if not line:
            i += 1
            continue
        
        # Detect project names (capitalized, not too long, contains keywords)
        project_keywords = ['Project', 'Improvements', 'Repairs', 'System', 'Facility', 'Study', 'Bridge', 'Road', 'Drain', 'Park']
        if any(keyword in line for keyword in project_keywords) and len(line) < 150 and line[0].isupper():
            project_name = line
            
            # Check next lines for disaster indicators and dates
            j = i + 1
            is_disaster = False
            start_date = None
            
            while j < min(i + 30, len(lines)):
                next_line = lines[j].strip().lower()
                
                # Check for disaster indicators
                if any(keyword in next_line for keyword in ['fema', 'caloes', 'caljpia', 'disaster', 'recovery', 'fire']):
                    is_disaster = True
                
                # Look for schedule/date info
                if 'schedule:' in next_line or 'complete design:' in next_line or 'begin construction:' in next_line:
                    # Extract date (look for 2022)
                    date_lines = lines[j:min(j+5, len(lines))]
                    for dl in date_lines:
                        if '2022' in dl:
                            start_date = '2022'
                            break
                
                # Stop if we hit another project-like line
                if j > i + 5 and any(keyword in next_line for keyword in project_keywords) and len(next_line) < 150 and next_line[0].isupper():
                    break
                
                j += 1
            
            # If disaster and starts in 2022, add it
            if is_disaster and start_date == '2022':
                disaster_projects_2022.append(project_name)
        
        i += 1

print(f'Found {len(disaster_projects_2022)} disaster projects starting in 2022:')
for name in disaster_projects_2022:
    print(f'  - {name}')

# Match with funding records
disaster_keywords = ['fema', 'caloes', 'caljpia', 'disaster', 'recovery', 'fire']
matched_funding = []

for project_name in disaster_projects_2022:
    # Find funding records that match this project
    for rec in funding_records:
        fund_name = rec['Project_Name'].lower()
        proj_name_lower = project_name.lower()
        
        # Check if they match (simplified)
        name_match = (
            proj_name_lower in fund_name or 
            fund_name in proj_name_lower or
            any(word in fund_name for word in proj_name_lower.split()[:3])
        )
        
        if name_match and any(keyword in fund_name for keyword in disaster_keywords):
            matched_funding.append({
                'Project': project_name,
                'Funding_Name': rec['Project_Name'],
                'Amount': int(rec['Amount'])
            })

print(f'\nFound {len(matched_funding)} matching funding records')
for mf in matched_funding:
    print(f"  - {mf['Project']} -> {mf['Funding_Name']}: ${mf['Amount']}")

# Sum funding
total_funding = sum(mf['Amount'] for mf in matched_funding)

print('__RESULT__:')
print(json.dumps({
    'disaster_projects_2022': disaster_projects_2022,
    'matching_funding': matched_funding,
    'total_funding': total_funding,
    'count': len(matched_funding)
}))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.execute_python:9': {'success': True, 'num_docs': 5}, 'var_functions.query_db:12': 'file_storage/functions.query_db:12.json', 'var_functions.query_db:14': 'file_storage/functions.query_db:14.json', 'var_functions.execute_python:16': {'funding_total': 500, 'civic_docs_total': 5, 'disaster_funding_count': 27}}

exec(code, env_args)
