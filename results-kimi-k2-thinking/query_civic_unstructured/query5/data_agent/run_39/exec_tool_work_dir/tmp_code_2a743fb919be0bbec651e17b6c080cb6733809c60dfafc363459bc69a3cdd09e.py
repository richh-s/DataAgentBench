code = """import json
import re

# Load funding data
funding_file = var_functions.query_db:2
with open(funding_file, 'r') as f:
    funding_data = json.load(f)

# Load civic docs
civic_file = var_functions.query_db:6
with open(civic_file, 'r') as f:
    civic_docs = json.load(f)

print('Loaded data:')
print(f'Funding records: {len(funding_data)}')
print(f'Civic documents: {len(civic_docs)}')

# Create a dictionary for funding lookup
funding_lookup = {}
for record in funding_data:
    project_name = record.get('Project_Name', '')
    funding_lookup[project_name] = {
        'Funding_ID': record.get('Funding_ID'),
        'Funding_Source': record.get('Funding_Source'),
        'Amount': int(record.get('Amount', 0))
    }

# Extract projects from civic_docs
disaster_projects_2022 = []

for doc in civic_docs:
    text = doc.get('text', '')
    
    # Find project sections in the text
    # Look for patterns like project names followed by project details
    project_patterns = r'([A-Z][A-Za-z0-9\s\(\)\-&/,]+?(?:Project|Improvements|Repairs|Replacement|Structure|System|Facility|Program))\s*\n\s*\(cid:\d+\)\s*([^\n]+)'
    
    # Find all projects mentioned
    project_matches = re.findall(r'([A-Z][A-Za-z0-9\s\(\)\-&/,]+?(?:Project|Improvements|Repairs|Replacement|Structure|System|Facility|Program))', text)
    
    for project_name in project_matches:
        project_name = project_name.strip()
        
        # Skip if it's a generic heading or if we already processed it
        if len(project_name) < 20 or 'Capital Improvement Projects' in project_name or 'Discussion' in project_name:
            continue
            
        # Check if this is a disaster-related project
        is_disaster = False
        if '(FEMA' in project_name or 'FEMA' in project_name:
            is_disaster = True
        if '(CalOES' in project_name or '(CalJPIA' in project_name:
            is_disaster = True
        if 'fire' in project_name.lower() or 'emergency' in project_name.lower():
            is_disaster = True
            
        if not is_disaster:
            continue
            
        # Look for start date in the text around this project
        # Find the position of this project in text
        pos = text.find(project_name)
        if pos == -1:
            continue
            
        # Search for date patterns indicating 2022
        nearby_text = text[pos:pos+500]
        
        # Look for start indicators
        has_2022 = False
        if '2022' in nearby_text:
            # Check if it's a start date
            if any(indicator in nearby_text.lower() for indicator in ['completed', 'completion']):
                has_2022 = True
            elif 'st:' in nearby_text.lower() or 'start' in nearby_text.lower():
                has_2022 = True
            
        if has_2022:
            # Look for funding info
            funding_info = funding_lookup.get(project_name, None)
            
            if funding_info:
                disaster_projects_2022.append({
                    'Project_Name': project_name,
                    'Amount': funding_info['Amount'],
                    'Funding_Source': funding_info['Funding_Source']
                })
            else:
                # Try variations without suffixes
                base_name = project_name.split('(')[0].strip()
                funding_info = funding_lookup.get(base_name, None)
                if funding_info:
                    disaster_projects_2022.append({
                        'Project_Name': project_name,
                        'Amount': funding_info['Amount'],
                        'Funding_Source': funding_info['Funding_Source']
                    })

# Calculate total funding
total_funding = sum(p['Amount'] for p in disaster_projects_2022)

print(f'Disaster projects from 2022 found: {len(disaster_projects_2022)}')
print(f'Total funding: ${total_funding:,}')

if disaster_projects_2022:
    print('\nProjects:')
    for p in disaster_projects_2022:
        print(f"- {p['Project_Name']}: ${p['Amount']:,}")

result = {
    'total_funding': total_funding,
    'project_count': len(disaster_projects_2022),
    'projects': disaster_projects_2022
}

print('\n__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['Funding'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json'}

exec(code, env_args)
