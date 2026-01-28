code = """import json, re, os

# Load data from files
civic_docs_path = locals()['var_functions.query_db:16']
funding_path = locals()['var_functions.query_db:17']

with open(civic_docs_path) as f:
    civic_docs = json.load(f)
with open(funding_path) as f:
    funding_data = json.load(f)

print('Successfully loaded {} civic documents and {} funding records'.format(len(civic_docs), len(funding_data)))

# Find park projects completed in 2022
park_projects_2022 = []

# Process all documents
for doc in civic_docs:
    text = doc.get('text', '')
    doc_lines = text.split('\n')
    
    # Look for completion indicators with 2022
    for i, line in enumerate(doc_lines):
        line_lower = line.lower()
        
        # Check if this line indicates completion in 2022
        has_2022 = '2022' in line
        has_completion = 'completed' in line_lower or 'completion' in line_lower
        
        if has_2022 and has_completion:
            # Look for park project name in nearby lines
            project_name = None
            
            # Search backwards up to 5 lines
            for j in range(i-1, max(0, i-6), -1):
                prev_line = doc_lines[j].strip()
                if not prev_line or prev_line.startswith('('):
                    continue
                
                # Check if this looks like a project name
                if len(prev_line) > 5 and 'Updates:' not in prev_line and 'Project Schedule' not in prev_line:
                    project_name = prev_line
                    break
            
            # Also search forwards if not found backwards
            if not project_name:
                for j in range(i+1, min(len(doc_lines), i+6)):
                    next_line = doc_lines[j].strip()
                    if next_line and not next_line.startswith('(') and len(next_line) > 5:
                        project_name = next_line
                        break
            
            if project_name:
                # Clean up the project name
                clean_name = re.sub(r'^[•◦\s]+', '', project_name)
                clean_name = re.sub(r'^\w\s+', '', clean_name)  # Remove leading single char+space
                clean_name = clean_name.strip()
                
                # Check if it's park-related
                name_lower = clean_name.lower()
                if 'park' in name_lower or 'playground' in name_lower:
                    # Avoid duplicates
                    if clean_name not in park_projects_2022:
                        park_projects_2022.append(clean_name)

print('Found {} unique park-related projects completed in 2022'.format(len(park_projects_2022)))

# Calculate total funding by matching with funding data
total_funding = 0
funded_project_details = []

# Simplify function for name matching
def simplify_name(name):
    return re.sub(r'[^a-z0-9]', '', name.lower())

for park_name in park_projects_2022:
    park_simple = simplify_name(park_name)
    
    for fund_record in funding_data:
        fund_name = fund_record['Project_Name']
        fund_simple = simplify_name(fund_name)
        fund_amount = int(fund_record['Amount'])
        
        # Check for name match (one contains the other)
        if park_simple in fund_simple or fund_simple in park_simple:
            total_funding += fund_amount
            funded_project_details.append({
                'project_name': park_name,
                'funding_record': fund_name,
                'amount': fund_amount
            })
            break

print('Total funding for 2022 park projects: ${:,}'.format(total_funding))

# Prepare final result
result = {
    'total_funding_dollars': total_funding,
    'number_of_projects': len(park_projects_2022),
    'projects': park_projects_2022,
}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:3': 'file_storage/functions.query_db:3.json', 'var_functions.query_db:16': 'file_storage/functions.query_db:16.json', 'var_functions.query_db:17': 'file_storage/functions.query_db:17.json', 'var_functions.execute_python:56': {'test': 'success'}}

exec(code, env_args)
