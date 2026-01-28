code = """import json
import re

# Load the data from storage
# Get the file paths from the stored variables
civic_docs_var = locals()['var_functions.query_db:2']
funding_var = locals()['var_functions.query_db:5']

# Load civic documents
civic_docs_file = civic_docs_var if isinstance(civic_docs_var, str) and civic_docs_var.endswith('.json') else None
civic_docs = []
if civic_docs_file:
    with open(civic_docs_file, 'r') as f:
        civic_docs = json.load(f)

# Load funding data
funding_file = funding_var if isinstance(funding_var, str) and funding_var.endswith('.json') else None
funding_data = []
if funding_file:
    with open(funding_file, 'r') as f:
        funding_data = json.load(f)

print(f"Loaded {len(civic_docs)} civic documents and {len(funding_data)} funding records")

# Extract park projects completed in 2022
park_projects = []

for doc in civic_docs:
    text = doc.get('text', '')
    lines = text.split('\n')
    
    for i, line in enumerate(lines):
        line = line.strip()
        if not line:
            continue
            
        # Skip headers and non-project lines
        skip_patterns = ['Public Works', 'Commission', 'Agenda', 'Page', 'Item', 'Updates', 'Schedule', 'RECOMMENDED ACTION']
        if any(pattern in line for pattern in skip_patterns) or len(line) < 10:
            continue
            
        # Check if line looks like a project name (contains project-related words)
        line_lower = line.lower()
        if any(word in line_lower for word in ['project', 'improvements', 'repairs', 'replacement', 'structure', 'walkway', 'shade', 'park']):
            
            # Look ahead for completion info mentioning 2022
            for j in range(i+1, min(i+12, len(lines))):
                next_line = lines[j].strip()
                next_line_lower = next_line.lower()
                
                # Check for completion in 2022
                if '2022' in next_line and ('complete' in next_line_lower or 'construction was completed' in next_line_lower):
                    
                    # Check context for park-related keywords
                    context_start = max(0, i-5)
                    context_end = min(len(lines), i+12)
                    context = ' '.join(lines[context_start:context_end]).lower()
                    
                    park_keywords = ['park', 'playground', 'shade structure', 'walkway', 'bluffs', 'legacy park', 'marie canyon', 'point dume']
                    is_park = any(keyword in context for keyword in park_keywords)
                    
                    if is_park:
                        project_name = line
                        # Clean up bullets
                        if project_name.startswith('(') and ')' in project_name:
                            project_name = project_name.split(')', 1)[1].strip()
                        
                        # Avoid duplicates
                        if not any(p['name'] == project_name for p in park_projects):
                            park_projects.append({
                                'name': project_name,
                                'completed': True,
                                'year': 2022
                            })
                        break

print(f"Found {len(park_projects)} park projects completed in 2022")
for proj in park_projects[:5]:
    print(f"  - {proj['name']}")

# Save results
result = json.dumps(park_projects)
print('__RESULT__:')
print(result)"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json'}

exec(code, env_args)
