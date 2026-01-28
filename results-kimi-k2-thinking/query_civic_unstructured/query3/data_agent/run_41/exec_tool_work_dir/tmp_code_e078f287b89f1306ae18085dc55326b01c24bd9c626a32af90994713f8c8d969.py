code = """import json
import re

# Load MongoDB documents
mongo_result = locals()['var_functions.query_db:0']

if type(mongo_result) is str and mongo_result.endswith('.json'):
    with open(mongo_result, 'r') as f:
        docs = json.load(f)
else:
    docs = mongo_result

print('Found', len(docs), 'documents')

# Extract projects
project_list = []
seen = set()

for doc in docs:
    text = doc.get('text', '')
    filename = doc.get('filename', '')
    text_lower = text.lower()
    
    # Check if document contains emergency/fema terms
    has_terms = any(term in text_lower for term in ['fema', 'caloes', 'caljpia', 'emergency'])
    if not has_terms:
        continue
    
    lines = text.split('\n')
    for line in lines:
        line = line.strip()
        if len(line) < 10:
            continue
        
        line_lower = line.lower()
        is_disaster = any(x in line_lower for x in ['(fema', '(caloes', '(caljpia'])
        is_emergency = 'emergency' in line_lower and 'project' in line_lower
        is_warning = 'warning' in line_lower and any(x in line_lower for x in ['siren', 'sign'])
        
        if is_disaster or is_emergency or is_warning:
            if line in seen:
                continue
            seen.add(line)
            
            status = 'unknown'
            if 'completed' in text_lower or 'construction was completed' in text_lower:
                status = 'completed'
            elif 'design' in text_lower or 'planning' in text_lower or 'rfp' in text_lower:
                status = 'design'
            elif 'not started' in text_lower or 'identified but not begun' in text_lower:
                status = 'not started'
            
            topic = 'emergency, fema'
            if 'warning' in line_lower:
                topic = 'emergency warning'
            elif 'fire' in line_lower:
                topic = 'emergency, fema, fire'
            
            project_list.append({
                'Project_Name': line,
                'topic': topic,
                'type': 'disaster',
                'status': status,
                'source_file': filename
            })

print('Extracted', len(project_list), 'projects')
print('__RESULT__')
print(json.dumps(project_list))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json'}

exec(code, env_args)
