code = """import json
import re

civic_docs_var = var_functions_query_db_36
funding_var = var_functions_query_db_34

if isinstance(civic_docs_var, str):
    with open(civic_docs_var, 'r') as f:
        civic_docs = json.load(f)
else:
    civic_docs = civic_docs_var

if isinstance(funding_var, str):
    with open(funding_var, 'r') as f:
        funding_data = json.load(f)
else:
    funding_data = funding_var

print(f"Found {len(civic_docs)} documents with Spring 2022 dates")
print(f"Found {len(funding_data)} funding records")

spring_2022_projects = []

for doc in civic_docs:
    text = doc.get('text', '')
    filename = doc.get('filename', '')
    
    # Look for project names and Spring 2022 start dates
    lines = text.split('\n')
    
    i = 0
    while i < len(lines):
        line = lines[i].strip()
        
        # Skip empty lines and obvious non-project lines
        if not line or len(line) < 10 or line.startswith('Page ') or line.startswith('('):
            i += 1
            continue
        
        # Look for project indicators in current line
        project_indicators = ['project', 'improvements', 'repairs', 'replacement', 'facility', 'road', 'park', 'drain', 'bridge']
        if any(indicator in line.lower() for indicator in project_indicators):
            
            # Look ahead in next few lines for Spring 2022 dates
            context = '\n'.join(lines[i:i+8])
            
            spring_patterns = [
                r'Begin[^\n]*Spring[^\n]*2022',
                r'Start[^\n]*Spring[^\n]*2022', 
                r'2022[^\n]*Spring[^\n]*Begin',
                r'2022[^\n]*Spring[^\n]*Start',
                r'Begin[^\n]*(?:March|April|May)[^\n]*2022',
                r'Start[^\n]*(?:March|April|May)[^\n]*2022'
            ]
            
            for pattern in spring_patterns:
                if re.search(pattern, context, re.IGNORECASE):
                    # Clean up project name
                    clean_name = re.sub(r'^(cid:\d+\s*)+', '', line)
                    clean_name = re.sub(r'^[\-\*\•\d\.\s]+', '', clean_name)
                    clean_name = clean_name.strip()
                    
                    if clean_name and len(clean_name) > 10:
                        spring_2022_projects.append({
                            'name': clean_name,
                            'filename': filename
                        })
                        break
        
        i += 1

# Remove duplicates
unique_projects = {}
for proj in spring_2022_projects:
    name = proj['name']
    if name not in unique_projects:
        unique_projects[name] = proj

spring_2022_projects = list(unique_projects.values())
print(f"Found {len(spring_2022_projects)} unique Spring 2022 projects")

for i, proj in enumerate(spring_2022_projects[:15]):
    print(f"{i+1}. {proj['name']}")

print('__RESULT__:', json.dumps({
    'project_count': len(spring_2022_projects),
    'projects': spring_2022_projects
}))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.list_db:2': ['Funding'], 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.execute_python:24': {'civic_count': 5, 'funding_count': 500}, 'var_functions.query_db:30': 'file_storage/functions.query_db:30.json', 'var_functions.query_db:34': 'file_storage/functions.query_db:34.json', 'var_functions.query_db:36': 'file_storage/functions.query_db:36.json'}

exec(code, env_args)
