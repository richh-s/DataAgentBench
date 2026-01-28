code = """import json
import re

# Load the park documents from the stored result
result_key = 'var_functions.query_db:2'
print(f"Accessing data from: {result_key}")

# The result is either the actual data or a file path
park_docs_input = locals()[result_key]
print(f"Type of input: {type(park_docs_input)}")

# Handle both cases - if it's a string (file path) or direct data
if isinstance(park_docs_input, str) and '.json' in park_docs_input:
    with open(park_docs_input, 'r', encoding='utf-8') as f:
        park_docs = json.load(f)
else:
    park_docs = park_docs_input

print(f"Loaded {len(park_docs)} park-related documents")

# Create a comprehensive list to store all park projects completed in 2022
park_projects_2022 = []

# Process each document
for doc in park_docs:
    text = doc.get('text', '')
    filename = doc.get('filename', 'unknown')
    
    # Look for park projects completed in 2022 using various patterns
    patterns = [
        # Pattern 1: Project name with Park and completion info in 2022
        # Look for lines containing Park/
        # Then look ahead for 2022 and completion
        r'([A-Z][A-Za-z\s]*(?:Park|Playground)[A-Za-z\s]*)(?=(?:.|\n)*?2022)(?=(?:.|\n)*?(?:completed|Construction was completed|Notice of completion|Complete))',
        
        # Pattern 2: Look for the specific phrase and capture project name
        r'([A-Z][A-Za-z\s]*(?:Park|Playground)[A-Za-z\s]*?)\s*(?:.|\n)*?Construction was completed[,\s]*([A-Za-z]+)?\s*2022',
    ]
    
    for pattern in patterns:
        matches = re.findall(pattern, text, re.IGNORECASE | re.DOTALL)
        for match in matches:
            if isinstance(match, tuple):
                proj_name = match[0].strip()
            else:
                proj_name = match.strip()
            
            if proj_name and 10 < len(proj_name) < 200:  # Reasonable length
                # Verify this is actually completed in 2022
                proj_section = text[text.find(proj_name):text.find(proj_name)+400]
                if '2022' in proj_section and any(marker in proj_section.lower() for marker in ['completed', 'construction was completed', 'notice of completion']):
                    park_projects_2022.append({
                        'Project_Name': proj_name,
                        'status': 'completed',
                        'topic': 'park',
                        'et': '2022',
                        'type': 'capital',
                        'source_file': filename
                    })

    # Additional manual search for known patterns
    # Look for the specific completion statements
    completion_patterns = [
        (r'([A-Z][A-Za-z\s]*(?:Park|Playground)[A-Za-z\s]*?)\s*(?:.|\n){0,200}?Construction was completed[,\s]*([A-Za-z]+)?\s*2022', 'construction completed'),
        (r'([A-Z][A-Za-z\s]*(?:Park|Playground)[A-Za-z\s]*?)\s*(?:.|\n){0,200}?completed[,\s]*([A-Za-z]+)?\s*2022', 'completed'),
    ]
    
    for pattern, match_type in completion_patterns:
        matches = re.findall(pattern, text, re.IGNORECASE | re.DOTALL)
        for match in matches:
            if isinstance(match, tuple):
                proj_name = match[0].strip()
            else:
                proj_name = match.strip()
            
            if proj_name and 'Park' in proj_name and 10 < len(proj_name) < 200:
                park_projects_2022.append({
                    'Project_Name': proj_name,
                    'status': 'completed',
                    'topic': 'park',
                    'et': '2022',
                    'type': 'capital',
                    'source_file': filename,
                    'match_type': match_type
                })

# Remove duplicates based on Project_Name
unique_projects = {}
for proj in park_projects_2022:
    name = proj['Project_Name']
    if name not in unique_projects:
        unique_projects[name] = proj

final_park_projects = list(unique_projects.values())
print(f"Found {len(final_park_projects)} unique park projects completed in 2022")

for proj in final_park_projects:
    print(f"- {proj['Project_Name']} (from {proj['source_file']})")

# Create result to pass to next step
result = {
    'park_projects_2022': final_park_projects,
    'project_names': [p['Project_Name'] for p in final_park_projects],
    'count': len(final_park_projects)
}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json'}

exec(code, env_args)
