code = """import json, re

# Read the file path from the stored variable
civic_docs_file = str(var_functions.query_db:4)

# Since the variable contains the file path as a string, let's read it
with open(civic_docs_file.strip("'"), 'r') as f:
    civic_docs = json.load(f)

# Find all disaster projects mentioned in the documents
disaster_project_names = set()

for doc in civic_docs:
    text = doc.get('text', '')
    lines = text.split('\n')
    
    for i, line in enumerate(lines):
        line = line.strip()
        if not line or len(line) < 5:
            continue
        
        # Check if line contains disaster keywords
        if any(keyword in line.lower() for keyword in ['fema', 'caljpia', 'caloes', 'disaster', 'fire', 'emergency', 'woolsey']):
            # Look for project name patterns
            if line.endswith('Project') or re.match(r'^[A-Z].*Project$', line):
                # Check if 2022 appears in context
                context_start = max(0, i-5)
                context_end = min(len(lines), i+10)
                context = '\n'.join(lines[context_start:context_end])
                
                if '2022' in context:
                    # Clean up the project name
                    proj_name = line.strip()
                    if proj_name and len(proj_name) > 5:
                        disaster_project_names.add(proj_name)

# Also find projects with (FEMA Project) style suffixes that have 2022 context
for doc in civic_docs:
    text = doc.get('text', '')
    pattern = r'([A-Z][^\n(]*?)\s*\(([^)]*(?:FEMA|CalJPIA|CalOES)[^)]*Project)\)'
    matches = re.findall(pattern, text, re.IGNORECASE | re.MULTILINE)
    
    for match in matches:
        proj_name = match[0].strip()
        if proj_name and len(proj_name) > 5:
            # Find if 2022 is mentioned near this project
            try:
                pos = text.index(proj_name)
                context = text[max(0, pos-150):min(len(text), pos+150)]
                if '2022' in context:
                    disaster_project_names.add(proj_name)
            except:
                pass

# Convert to list for JSON serialization
disaster_list = list(disaster_project_names)

# Now query the funding database for these projects
# We'll do this in the next step, but first let's see what projects we found
print('__RESULT__:')
print(json.dumps({
    'disaster_projects_found': disaster_list,
    'count': len(disaster_list)
}))"""

env_args = {'var_functions.list_db:0': ['Funding'], 'var_functions.list_db:1': ['civic_docs'], 'var_functions.query_db:4': 'file_storage/functions.query_db:4.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json'}

exec(code, env_args)
