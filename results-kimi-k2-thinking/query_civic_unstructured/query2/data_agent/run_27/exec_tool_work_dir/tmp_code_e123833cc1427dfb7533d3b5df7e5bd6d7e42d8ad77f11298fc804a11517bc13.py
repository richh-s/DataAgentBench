code = """import json, re

# Load data from the stored file paths
civic_docs_path = locals()['var_functions.query_db:16']
funding_path = locals()['var_functions.query_db:17']

with open(civic_docs_path, 'r') as f:
    civic_docs = json.load(f)

with open(funding_path, 'r') as f:
    funding_records = json.load(f)

print('Loaded %d civic documents and %d funding records' % (len(civic_docs), len(funding_records)))

# Extract park projects completed in 2022 from civic documents
park_projects_2022 = []

for doc in civic_docs:
    text = doc['text']
    lines = text.split('\n')
    
    # Look for patterns indicating completion in 2022
    for i, line in enumerate(lines):
        line_lower = line.lower()
        
        # Check if this line mentions completion in 2022
        if '2022' in line and ('completed' in line_lower or 'completion' in line_lower):
            project_name = None
            
            # Look backwards for the project name
            for j in range(i-1, max(0, i-8), -1):
                prev_line = lines[j].strip()
                if prev_line and not prev_line.startswith('(') and len(prev_line) > 5:
                    # Clean project name
                    clean_name = prev_line.replace('•', '').replace('◦', '').strip()
                    # Remove common prefixes
                    clean_name = re.sub(r'^[A-Z]\.?\s+', '', clean_name)
                    if clean_name and not any(keyword in clean_name.lower() for keyword in ['update', 'schedule', 'project status']):
                        project_name = clean_name
                        break
            
            # Also search forwards if not found
            if not project_name:
                for j in range(i+1, min(len(lines), i+6)):
                    next_line = lines[j].strip()
                    if next_line and not next_line.startswith('(') and len(next_line) > 5:
                        clean_name = next_line.replace('•', '').replace('◦', '').strip()
                        clean_name = re.sub(r'^[A-Z]\.?\s+', '', clean_name)
                        if clean_name:
                            project_name = clean_name
                            break
            
            # Check if park-related
            if project_name and ('park' in project_name.lower() or 'playground' in project_name.lower()):
                # Remove duplicates
                if project_name not in park_projects_2022:
                    park_projects_2022.append(project_name)
                    print('Found park project completed in 2022: %s' % project_name)

print('\nFound %d unique park projects completed in 2022' % len(park_projects_2022))

# Match with funding data and calculate total funding
total_funding = 0
matched_funding = []

# Simplify function for name matching
def normalize_name(name):
    return re.sub(r'[^a-z0-9]', '', name.lower())

for park_name in park_projects_2022:
    park_normalized = normalize_name(park_name)
    
    for fund in funding_records:
        fund_name = fund['Project_Name']
        fund_normalized = normalize_name(fund_name)
        fund_amount = int(fund['Amount'])
        
        # Check if names match (one is subset of the other)
        if park_normalized in fund_normalized or fund_normalized in park_normalized:
            total_funding += fund_amount
            matched_funding.append({
                'park_project': park_name,
                'funding_record': fund_name,
                'amount': fund_amount
            })
            print('Matched: %s -> $%,d' % (park_name, fund_amount))
            break

print('\nTotal funding for park-related projects completed in 2022: $%,d' % total_funding)

# Return final result
result = {
    'total_funding_dollars': total_funding,
    'number_of_projects': len(park_projects_2022),
    'projects': park_projects_2022,
    'funding_matches': matched_funding
}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:3': 'file_storage/functions.query_db:3.json', 'var_functions.query_db:16': 'file_storage/functions.query_db:16.json', 'var_functions.query_db:17': 'file_storage/functions.query_db:17.json', 'var_functions.execute_python:56': {'test': 'success'}, 'var_functions.execute_python:66': {'status': 'success', 'docs_loaded': 5}}

exec(code, env_args)
