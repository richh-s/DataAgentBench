code = """import json
import re

# Get the file path from the stored variable
civic_docs_result = var_functions.query_db:4

# Load the data
civic_docs = []
with open(civic_docs_result) as f:
    civic_docs = json.load(f)

# Find disaster projects that started in 2022
disaster_project_names = set()

for doc in civic_docs:
    text = doc.get('text', '')
    
    # Method 1: Look for lines ending with Project that contain disaster keywords
    lines = text.split('\n')
    for i, line in enumerate(lines):
        line = line.strip()
        if not line:
            continue
        
        # Check if it's a project line and disaster-related
        if line.endswith('Project'):
            line_lower = line.lower()
            if any(k in line_lower for k in ['fema', 'caljpia', 'caloes', 'disaster', 'fire', 'emergency']):
                # Check context for 2022
                context_start = max(0, i-5)
                context_end = min(len(lines), i+10)
                context = ' '.join(lines[context_start:context_end])
                if '2022' in context:
                    disaster_project_names.add(line.strip())
    
    # Method 2: Look for patterns like "Project Name (FEMA Project)"
    pattern = r'([A-Z][^\n(]*?)\s*\(([^)]*(?:FEMA|CalJPIA|CalOES)[^)]*Project)\)'
    matches = re.findall(pattern, text, re.IGNORECASE | re.MULTILINE)
    
    for match in matches:
        proj_name = match[0].strip()
        if proj_name and len(proj_name) > 5:
            # Check if 2022 is mentioned in the document
            if '2022' in text:
                disaster_project_names.add(proj_name)

# Convert to sorted list
disaster_list = sorted(list(disaster_project_names))

print('__RESULT__:')
print(json.dumps({'projects': disaster_list, 'count': len(disaster_list)}))"""

env_args = {'var_functions.list_db:0': ['Funding'], 'var_functions.list_db:1': ['civic_docs'], 'var_functions.query_db:4': 'file_storage/functions.query_db:4.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json'}

exec(code, env_args)
