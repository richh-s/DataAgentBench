code = """import json
import re

# Load civic documents data
civic_docs_file = var_functions.query_db:2
if isinstance(civic_docs_file, str) and civic_docs_file.endswith('.json'):
    with open(civic_docs_file, 'r') as f:
        civic_docs = json.load(f)
else:
    civic_docs = var_functions.query_db:2

# Load funding data
funding_file = var_functions.query_db:5
if isinstance(funding_file, str) and funding_file.endswith('.json'):
    with open(funding_file, 'r') as f:
        funding_data = json.load(f)
else:
    funding_data = var_functions.query_db:5

print(f"Loaded {len(civic_docs)} civic documents")

# Extract project information from civic documents
park_projects_completed_2022 = []

for doc in civic_docs:
    text = doc.get('text', '')
    
    # Look for projects with completion in 2022
    # Pattern: project name on one line, then status/completion info follows
    
    lines = text.split('\n')
    
    current_project = None
    
    for i, line in enumerate(lines):
        line = line.strip()
        
        # Look for project names - typically not too short, not agenda headers
        if (line and 
            not line.startswith('Public Works') and
            not line.startswith('Commission') and
            not line.startswith('Agenda') and
            not line.startswith('Page') and
            not line.startswith('Item') and
            len(line) > 10 and
            len(line) < 200 and
            'Updates' not in line and
            'Schedule' not in line):
            
            # Check if it looks like a project name (has reasonable capitalization)
            # Skip if it's just common words
            skip_words = ['and', 'the', 'to', 'of', 'for', 'in', 'on', 'at', 'by', 'with']
            line_lower = line.lower()
            if any(w in line_lower for w in ['project', 'improvements', 'repairs', 'replacement', 'structure', 'walkway', 'shade']):
                current_project = line
                
                # Look ahead for status and completion info
                for j in range(i+1, min(i+15, len(lines))):
                    next_line = lines[j].strip()
                    
                    # Check for completion with 2022
                    if ('2022' in next_line and 
                        ('complete' in next_line.lower() or 
                         'construction was completed' in next_line.lower())):
                        
                        # Check if it's park-related
                        context_start = max(0, i-5)
                        context_end = min(len(lines), i+15)
                        context = ' '.join(lines[context_start:context_end]).lower()
                        
                        # Check for park keywords
                        park_keywords = ['park', 'playground', 'shade structure', 'walkway', 'bluffs', 'legacy park']
                        is_park = any(keyword in context for keyword in park_keywords)
                        
                        if is_park:
                            project_name = current_project
                            # Clean up the name
                            if project_name.startswith('('):
                                project_name = project_name.split(')', 1)[1].strip()
                            
                            # Check for duplicates
                            if not any(p['name'] == project_name for p in park_projects_completed_2022):
                                park_projects_completed_2022.append({
                                    'name': project_name,
                                    'completion_info': next_line
                                })
                        break

print(f"Found {len(park_projects_completed_2022)} park projects completed in 2022")
for proj in park_projects_completed_2022:
    print(f"  - {proj['name']}: {proj['completion_info'][:80]}...")

# Save the result
result = json.dumps(park_projects_completed_2022)
print('__RESULT__:')
print(result)"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json'}

exec(code, env_args)
