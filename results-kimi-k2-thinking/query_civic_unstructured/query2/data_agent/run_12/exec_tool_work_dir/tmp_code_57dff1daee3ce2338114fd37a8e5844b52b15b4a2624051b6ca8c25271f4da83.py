code = """import json, re

funding_data = var_functions.query_db_5
civic_docs_data = var_functions.query_db_2

print('Loaded {} funding records'.format(len(funding_data)))
print('Loaded {} civic documents'.format(len(civic_docs_data)))

# Extract park-related projects completed in 2022
park_projects_2022 = []

for doc in civic_docs_data:
    text = doc.get('text', '')
    
    # Look for park projects completed in 2022
    lines = text.split('
')
    
    for i in range(len(lines)):
        line = lines[i].strip()
        if not line or len(line) > 100 or line.startswith('(') or line.startswith('•'):
            continue
            
        # Check if this line contains a park project name
        if 'park' in line.lower():
            # Check surrounding context for completion status
            context_start = max(0, i-2)
            context_end = min(len(lines), i+8)
            context = ' '.join(lines[context_start:context_end]).lower()
            
            # Check if completed in 2022
            if 'completed' in context and '2022' in context:
                if '2022' in text:
                    park_projects_2022.append(line)
                    print('Found park project: {}'.format(line))  

print('Found {} park projects completed in 2022'.format(len(park_projects_2022)))

# Clean project names for matching
def clean_project_name(name):
    if not name:
        return ''
    # Remove common suffixes
    name = re.sub(r'(?i)\s+Project\s*$', '', name)
    name = re.sub(r'(?i)\s*-\s*Design\s*$', '', name)
    name = re.sub(r'(?i)\s*-\s*Construction\s*$', '', name)
    return name.strip()

# Get park project names
cleaned_park_names = [clean_project_name(p) for p in park_projects_2022]
print('Cleaned park project names: {}'.format(cleaned_park_names))

# Match with funding records and calculate total
total_funding = 0
matched_projects = []

for i, park_name in enumerate(cleaned_park_names):
    if not park_name:
        continue
        
    # Look for matching funding records
    for fund_record in funding_data:
        fund_project_name = fund_record.get('Project_Name', '')
        fund_amount = int(fund_record.get('Amount', 0))
        
        if not fund_project_name:
            continue
            
        # Clean funding project name
        clean_fund_name = clean_project_name(fund_project_name)
        
        # Check for matches (park name contains fund name or vice versa)
        if (park_name.lower() in clean_fund_name.lower() or 
            clean_fund_name.lower() in park_name.lower()):
            total_funding += fund_amount
            matched_projects.append({
                'park_project': park_projects_2022[i],
                'funding_project': fund_project_name,
                'amount': fund_amount
            })
            print('Matched: {} -> {} (${})'.format(park_projects_2022[i], fund_project_name, fund_amount))

print('Total funding for park projects completed in 2022: {}'.format(total_funding))

result = {
    'total_funding': total_funding,
    'matched_project_count': len(matched_projects),
    'details': matched_projects
}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.execute_python:36': {'total_funding': 0, 'park_records_found': 0}}

exec(code, env_args)
