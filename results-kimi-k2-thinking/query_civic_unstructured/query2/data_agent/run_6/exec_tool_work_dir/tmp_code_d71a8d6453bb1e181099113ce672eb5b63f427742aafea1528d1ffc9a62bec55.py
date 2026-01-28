code = """import json, re
with open('file_storage/functions.query_db:2.json', 'r') as f:
    civic_docs = json.load(f)

# Simple extraction of completed projects in 2022
projects_2022 = []
park_projects_2022 = []

for doc in civic_docs:
    text = doc['text']
    
    # Look for park-related projects completed in 2022
    park_keywords = ['Park', 'park', 'playground', 'walkway']
    
    # Find lines with park keywords and 2022 completion
    lines = text.split('\n')
    
    for line in lines:
        line_lower = line.lower()
        
        # Check if this mentions 2022 completion
        has_2022 = '2022' in line
        completion_indicators = ['completed', 'completion', 'complete construction', 'construction was completed']
        indicates_completion = any(indicator in line_lower for indicator in completion_indicators)
        
        if has_2022 and indicates_completion:
            # Check if this is a park project by looking for park keywords
            is_park = any(keyword in line_lower for keyword in park_keywords)
            
            # Also check context in surrounding lines
            if is_park:
                # Extract project name (look backwards for project titles)
                project_name = []
                for j in range(max(0, lines.index(line)-5), lines.index(line)):
                    prev_line = lines[j].strip()
                    if prev_line and len(prev_line.split()) <= 8 and not any(x in prev_line.lower() for x in ['updates:', 'schedule:', 'project description:', 'completion', 'complete construction']):
                        project_name = [prev_line]
                        break
                
                if project_name:
                    park_projects_2022.append({
                        'project': project_name[0] if project_name else 'Unknown',
                        'details': line.strip()
                    })

print('__RESULT__:')
print(json.dumps({'park_projects_2022': park_projects_2022}))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.execute_python:6': ['var_functions.list_db:0', 'var_functions.query_db:2', '__builtins__', 'json'], 'var_functions.execute_python:8': {'path': 'file_storage/functions.query_db:2.json'}, 'var_functions.execute_python:10': 'file_storage/functions.execute_python:10.json', 'var_functions.execute_python:12': 'Loaded 5 documents'}

exec(code, env_args)
