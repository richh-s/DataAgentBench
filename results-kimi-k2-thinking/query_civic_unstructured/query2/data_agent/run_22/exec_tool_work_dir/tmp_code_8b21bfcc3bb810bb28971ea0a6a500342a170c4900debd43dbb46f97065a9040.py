code = """import json
import re

# Load data from files
civic_docs = json.load(open('var_functions.query_db_64'))
funding_data = json.load(open('var_functions.query_db_8'))

# Find park-related projects completed in 2022
park_projects = []

for doc in civic_docs:
    text = doc.get('text', '')
    lower_text = text.lower()
    
    # Check if text mentions park and 2022 completion
    if 'park' in lower_text and '2022' in lower_text and 'completed' in lower_text:
        # Extract park project names from text
        lines = text.split('\n')
        for line in lines:
            line_clean = line.strip()
            # Look for lines with "Park" that are likely project names
            if 'Park' in line_clean and len(line_clean) < 150:
                # Skip metadata lines
                skip_terms = ['updates:', 'schedule:', 'description:', 'page', 'agenda', 'item', 'recommended', 'discussion:', 'subject:']
                should_skip = any(term in line_clean.lower() for term in skip_terms)
                if not should_skip:
                    # Check if this park project was completed in 2022
                    # Look at nearby lines for completion status
                    line_index = lines.index(line)
                    nearby_text = ' '.join(lines[max(0, line_index-3):min(len(lines), line_index+4)])
                    if 'completed' in nearby_text.lower() and '2022' in nearby_text:
                        if line_clean not in park_projects:
                            park_projects.append(line_clean)

# Also check for Broad Beach Road Water Quality Repair which is park infrastructure
for doc in civic_docs:
    text = doc.get('text', '')
    lower_text = text.lower()
    if 'broad beach road water quality' in lower_text and 'completed' in lower_text and '2022' in lower_text:
        if 'Broad Beach Road Water Quality Repair' not in park_projects:
            park_projects.append('Broad Beach Road Water Quality Repair')

# Match park projects with funding records
total_funding = 0
matched_records = []

for project in park_projects:
    proj_lower = project.lower().strip()
    
    for fund in funding_data:
        fund_name = fund['Project_Name'].lower()
        
        # Match if project name equals fund name or fund name starts with project name
        if proj_lower == fund_name or fund_name.startswith(proj_lower):
            amount = int(fund['Amount'])
            total_funding += amount
            matched_records.append({
                'project': project,
                'funding_id': fund['Funding_ID'],
                'amount': amount,
                'source': fund['Funding_Source']
            })

# Calculate result
result = {
    'total_funding': total_funding,
    'num_projects': len(park_projects),
    'num_matches': len(matched_records),
    'projects': park_projects,
    'funding_details': matched_records
}

print('__RESULT__:')
print(json.dumps(result, indent=2))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json', 'var_functions.query_db:32': 'file_storage/functions.query_db:32.json', 'var_functions.query_db:36': 'file_storage/functions.query_db:36.json', 'var_functions.execute_python:56': [], 'var_functions.execute_python:60': {'has_civic_file': False, 'has_funding_file': False}, 'var_functions.query_db:64': 'file_storage/functions.query_db:64.json'}

exec(code, env_args)
