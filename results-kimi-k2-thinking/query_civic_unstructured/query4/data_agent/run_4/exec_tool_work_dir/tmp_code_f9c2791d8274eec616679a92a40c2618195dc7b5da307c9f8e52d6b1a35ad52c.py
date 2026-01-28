code = """import json
import re

# Get the stored data using locals()
civic_docs_data = locals().get('var_functions.query_db:2', [])
funding_data = locals().get('var_functions.query_db:4', [])

print('Type of civic_docs_data:', type(civic_docs_data))
print('Type of funding_data:', type(funding_data))

# Load civic documents
civic_docs = []
if isinstance(civic_docs_data, str) and civic_docs_data.endswith('.json'):
    with open(civic_docs_data, 'r') as f:
        civic_docs = json.load(f)
elif isinstance(civic_docs_data, list):
    civic_docs = civic_docs_data

# Load funding data  
funding_records = []
if isinstance(funding_data, str) and funding_data.endswith('.json'):
    with open(funding_data, 'r') as f:
        funding_records = json.load(f)
elif isinstance(funding_data, list):
    funding_records = funding_data

print(f'Loaded {len(civic_docs)} civic documents')
print(f'Loaded {len(funding_records)} funding records')

# Create funding lookup by project name
funding_lookup = {}
for fund in funding_records:
    proj_name = fund.get('Project_Name', '')
    amount = int(fund.get('Amount', 0))
    funding_lookup[proj_name] = amount

print(f'Created funding lookup with {len(funding_lookup)} projects')

# Extract Spring 2022 projects from civic documents
spring_2022_projects = []

for doc in civic_docs:
    text = doc.get('text', '')
    
    # Look for project sections that mention Spring 2022
    # Find paragraphs or sections
    sections = text.split('\n\n')
    
    for section in sections:
        if 'Spring 2022' in section or '2022-Spring' in section:
            # Try to extract project name from this section
            lines = section.strip().split('\n')
            for line in lines:
                line = line.strip()
                # Project names are typically at the start of a section and capitalized
                if line and not line.startswith('(') and not line.startswith('To:') and \
                   not line.startswith('From:') and not line.startswith('Subject:') and \
                   len(line) > 10 and len(line) < 150:
                    # Check if it looks like a project name (contains project-related words)
                    project_indicators = ['Project', 'Improvements', 'Repairs', 'Replacement', 'Installation', 
                                        'Facility', 'System', 'Structure', 'Road', 'Park', 'Drainage']
                    if any(indicator in line for indicator in project_indicators):
                        spring_2022_projects.append(line)
                        break

# Remove duplicates
spring_2022_projects = list(set(spring_2022_projects))

print(f'Found {len(spring_2022_projects)} potential Spring 2022 projects')

# Match with funding data
total_funding = 0
matched_projects = []

for proj in spring_2022_projects:
    if proj in funding_lookup:
        amount = funding_lookup[proj]
        matched_projects.append({'project': proj, 'funding': amount})
        total_funding += amount

# Try to find more projects by searching the text directly for patterns
all_project_names = list(funding_lookup.keys())

for doc in civic_docs:
    text = doc.get('text', '')
    
    if 'Spring 2022' in text or '2022-Spring' in text:
        for fund_proj in all_project_names:
            # Check if project name appears in text near Spring 2022
            if fund_proj in text:
                # Simple proximity check - within 500 characters
                idx = text.find(fund_proj)
                spring_idx = text.find('Spring 2022')
                if spring_idx == -1:
                    spring_idx = text.find('2022-Spring')
                
                if abs(idx - spring_idx) < 500:
                    if fund_proj not in [p['project'] for p in matched_projects]:
                        amount = funding_lookup[fund_proj]
                        matched_projects.append({'project': fund_proj, 'funding': amount})
                        total_funding += amount

# Count unique projects (remove duplicates from matching)
unique_matched = {}
for proj in matched_projects:
    proj_name = proj['project']
    if proj_name not in unique_matched:
        unique_matched[proj_name] = proj['funding']

final_matched = [{'project': k, 'funding': v} for k, v in unique_matched.items()]
total_funding = sum(v for v in unique_matched.values())

result = {
    'total_spring_2022_projects': len(spring_2022_projects),
    'matched_with_funding': len(final_matched),
    'total_funding_amount': total_funding,
    'projects_with_funding': final_matched[:20]  # Limit output
}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:4': 'file_storage/functions.query_db:4.json'}

exec(code, env_args)
