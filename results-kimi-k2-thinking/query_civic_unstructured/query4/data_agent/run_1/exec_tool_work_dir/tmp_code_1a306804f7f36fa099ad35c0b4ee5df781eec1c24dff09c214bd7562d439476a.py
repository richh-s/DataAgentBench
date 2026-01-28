code = """import json
import re

# Get the file path from the storage variable
file_path = var_functions.query_db:5

# Read the full MongoDB result from the file
with open(file_path, 'r') as f:
    civic_docs = json.load(f)

print(f"Found {len(civic_docs)} documents")

# Let's extract project information by looking for patterns
projects = []

for doc in civic_docs:
    text = doc.get('text', '')
    lines = text.split('\n')
    
    # Look for project names and Spring 2022 dates
    project_name = None
    has_spring_2022 = False
    
    for i, line in enumerate(lines):
        line = line.strip()
        
        # Skip empty lines
        if not line:
            continue
            
        # Check for Spring 2022 patterns
        spring_patterns = ['2022-Spring', '2022-March', '2022-April', '2022-May', '2022-03', '2022-04', '2022-05']
        if any(pattern in line for pattern in spring_patterns):
            has_spring_2022 = True
            # Look for project name nearby (usually before the date)
            for j in range(max(0, i-5), i):
                prev_line = lines[j].strip()
                if prev_line and len(prev_line) > 3 and not prev_line.startswith('(') and not prev_line.startswith('cid'):
                    # Check if it looks like a project name (starts with capital, not a header)
                    if prev_line[0].isupper() and 'Agenda' not in prev_line and 'Commission' not in prev_line:
                        project_name = prev_line
                        break
        
        # Also check for project headings
        if line and line[0].isupper() and len(line) > 10 and 'Updates' not in line and 'Schedule' not in line:
            if 'Project' not in line or len(line) < 50:  # Avoid headers
                # This might be a project name
                project_name_candidate = line
    
    if has_spring_2022 and project_name:
        projects.append({
            'project_name': project_name,
            'doc_filename': doc.get('filename', '')
        })

print(f"Found {len(projects)} potential Spring 2022 projects")
for p in projects[:10]:
    print(f"  - {p['project_name']}")

# Let's also do a more comprehensive scan for any 2022 project mentions
all_2022_projects = []

for doc in civic_docs:
    text = doc.get('text', '')
    
    # Find mentions of 2022 and extract surrounding text
    matches = re.finditer(r'[^.\n]*2022[^.\n]*\s*[^.\n]*', text)
    for match in matches:
        context = match.group(0)
        # Check if this looks like a project description
        if any(keyword in context.lower() for keyword in ['project', 'construction', 'design', 'improvement']):
            # Extract potential project name from previous lines
            pos = match.start()
            before_text = text[max(0, pos-200):pos]
            lines_before = before_text.split('\n')
            for line in reversed(lines_before):
                line = line.strip()
                if line and len(line) > 5 and line[0].isupper():
                    all_2022_projects.append({
                        'project_name': line[:100],
                        'context': context[:200]
                    })
                    break

print(f"\nTotal 2022 project mentions found: {len(all_2022_projects)}")
print("__RESULT__:")
print(json.dumps({
    'spring_2022_projects': projects,
    'all_2022_projects': all_2022_projects[:20]  # First 20 for preview
}, indent=2))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': [], 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json'}

exec(code, env_args)
