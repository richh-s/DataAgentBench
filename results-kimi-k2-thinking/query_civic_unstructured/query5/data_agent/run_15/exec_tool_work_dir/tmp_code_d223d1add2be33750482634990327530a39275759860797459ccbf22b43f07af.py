code = """import json
import re

# Load the MongoDB results file
file_path = var_functions.query_db:10
with open(file_path, 'r') as f:
    documents = json.load(f)

# Extract disaster-related projects that started in 2022
disaster_projects_2022 = []

for doc in documents:
    text = doc.get('text', '')
    filename = doc.get('filename', '')
    
    # Look for disasters projects - containing FEMA, CalOES, CalJPIA, or (FEMA Project) etc.
    if re.search(r'disaster|FEMA|CalOES|CalJPIA|Woolsey Fire', text, re.IGNORECASE):
        # Extract project names and start dates
        lines = text.split('\n')
        for line in lines:
            # Look for date patterns containing 2022
            if re.search(r'2022', line):
                # Also look for project context in nearby lines
                # Simple approach: If line has 2022 and disaster keywords in context
                if re.search(r'Project|Updates|Schedule', line, re.IGNORECASE):
                    if not re.search(r'2022-2023|FY 2022', line):  # Exclude fiscal year references
                        # Try to find project names (often all caps or with specific patterns)
                        project_lines = []
                        current_line_idx = lines.index(line)
                        # Look backward for project name
                        for i in range(current_line_idx - 5, current_line_idx):
                            if i >= 0:
                                prev_line = lines[i].strip()
                                if prev_line and not prev_line.startswith('(') and \
                                   len(prev_line) > 10 and not re.match(r'^\s*\d+\s*$', prev_line):
                                    project_lines.append(prev_line)
                                    break
                        
                        disaster_projects_2022.append({
                            'filename': filename,
                            'line': line.strip(),
                            'context': project_lines[0] if project_lines else ''
                        })

# Let's print what we found
found_projects = []
for item in disaster_projects_2022[:20]:  # Show first 20
    found_projects.append(f"File: {item['filename']}")
    if item['context']:
        found_projects.append(f"Project: {item['context']}")
    found_projects.append(f"Info: {item['line']}")
    found_projects.append("---")

print('__RESULT__:')
print(json.dumps('\n'.join(found_projects)))"""

env_args = {'var_functions.query_db:0': [], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.list_db:5': ['civic_docs'], 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json', 'var_functions.query_db:10': 'file_storage/functions.query_db:10.json'}

exec(code, env_args)
