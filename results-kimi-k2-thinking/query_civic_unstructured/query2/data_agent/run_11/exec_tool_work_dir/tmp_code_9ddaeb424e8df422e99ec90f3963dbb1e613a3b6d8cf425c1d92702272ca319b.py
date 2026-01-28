code = """# Load the data from file paths stored in variables
import json

# Access the stored file paths
civic_path = var_functions.query_db:60
funding_path = var_functions.query_db:48

# Load the data
with open(civic_path, 'r') as f:
    civic_docs = json.load(f)
with open(funding_path, 'r') as f:
    funding = json.load(f)

# Find park projects completed in 2022
park_projects = []

for doc in civic_docs:
    text = doc.get('text', '')
    lines = text.split('
')
    
    for i in range(len(lines)):
        line = lines[i].strip()
        
        # Look for park project names
        if 'Park' in line and len(line) > 5:
            # Skip headers and metadata
            if 'Subject' in line or 'Page' in line or 'Item' in line:
                continue
            if line.startswith('('):
                continue
            
            # Check following lines for completion in 2022
            next_section = ' '.join(lines[i:i+15])
            if 'completed' in next_section.lower() and '2022' in next_section:
                park_projects.append(line)

# Remove duplicates
unique_projects = list(set(park_projects))

# Find funding matches
total_funding = 0
matches = []

for project in unique_projects:
    project_lower = project.lower()
    for fund in funding:
        fund_name = fund.get('Project_Name', '')
        fund_amount = int(fund.get('Amount', 0))
        
        if project_lower in fund_name.lower():
            total_funding += fund_amount
            matches.append([project, fund_name, fund_amount])

# Print result
result = {
    'park_projects': unique_projects,
    'project_count': len(unique_projects),
    'total_funding': total_funding,
    'funding_matches': matches
}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.list_db:2': ['civic_docs'], 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.execute_python:12': {'civic_docs_count': 38, 'funding_records_count': 38, 'status': 'Data loaded successfully'}, 'var_functions.query_db:48': 'file_storage/functions.query_db:48.json', 'var_functions.query_db:60': 'file_storage/functions.query_db:60.json'}

exec(code, env_args)
