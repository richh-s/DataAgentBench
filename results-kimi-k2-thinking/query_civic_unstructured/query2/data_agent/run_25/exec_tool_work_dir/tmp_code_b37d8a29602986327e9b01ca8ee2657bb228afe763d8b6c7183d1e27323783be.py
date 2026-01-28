code = """import json
import re

# Load data
civic_docs_path = locals()['var_functions.query_db:0']
with open(civic_docs_path, 'r') as f:
    civic_docs = json.load(f)

funding_path = locals()['var_functions.query_db:2']
with open(funding_path, 'r') as f:
    funding_data = json.load(f)

# Create funding dictionary
funding_dict = {}
for record in funding_data:
    proj_name = record['Project_Name'].strip()
    amount = int(record['Amount'])
    funding_dict[proj_name] = amount

# More comprehensive search for park projects completed in 2022
park_projects_completed = []

for doc in civic_docs:
    doc_text = doc.get('text', '')
    
    # Look for park-related text blocks
    park_blocks = []
    lines = doc_text.split(chr(10))
    
    current_block = []
    in_park_section = False
    
    for line in lines:
        if not line.strip():
            if current_block:
                park_blocks.append('\n'.join(current_block))
                current_block = []
                in_park_section = False
            continue
            
        line_lower = line.lower()
        
        # Start of a park project section
        if 'park' in line_lower and len(line.strip()) > 5:
            in_park_section = True
            
        if in_park_section:
            current_block.append(line)
    
    # Process each park block
    for block in park_blocks:
        if 'completed' in block.lower() and '2022' in block:
            # Extract project name (first line containing park)
            block_lines = block.split(chr(10))
            for line in block_lines:
                if 'park' in line.lower() and len(line.strip()) > 10:
                    if not any(x in line for x in ['Capital Improvement', 'status report', 'agenda report']):
                        if line.strip() not in park_projects_completed:
                            park_projects_completed.append(line.strip())
                        break

# Find all park-related funding
park_funding_matches = []
total_park_funding = 0

for project in park_projects_completed:
    if project in funding_dict:
        park_funding_matches.append({'project': project, 'amount': funding_dict[project]})
        total_park_funding += funding_dict[project]

# Also check for any project with 'park' in name completed in 2022
additional_projects = []
for funding_project, amount in funding_dict.items():
    if 'park' in funding_project.lower():
        # Check if this appears in any document with completed 2022
        for doc in civic_docs:
            doc_text = doc.get('text', '')
            if funding_project in doc_text:
                if 'completed' in doc_text.lower() and '2022' in doc_text:
                    additional_projects.append({'project': funding_project, 'amount': amount})
                    total_park_funding += amount
                    break

result = {
    'park_projects_completed': park_projects_completed,
    'park_funding_matches': park_funding_matches,
    'additional_projects': additional_projects,
    'total_park_funding': total_park_funding
}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.execute_python:5': {'civic_docs_count': 5, 'funding_records_count': 500}, 'var_functions.execute_python:14': {'park_projects': ['Bluffs Park Shade Structure', 'Permanent Skate Park', 'permanent skate park located on the Crummer/Case Court parcel adjacent', 'to Malibu Bluffs Park. The project would include parking and additional site'], 'all_completed_2022': [], 'funding_matches': [{'project': 'Bluffs Park Shade Structure', 'amount': 21000}, {'project': 'Permanent Skate Park', 'amount': 97000}], 'total_funding': 118000}}

exec(code, env_args)
