code = """import json
import re

def analyze_documents():
    mongo_result = locals()['var_functions.query_db:0']
    
    if isinstance(mongo_result, str) and mongo_result.endswith('.json'):
        with open(mongo_result, 'r') as f:
            documents = json.load(f)
    else:
        documents = mongo_result
    
    projects = []
    
    for doc in documents:
        text = doc.get('text', '')
        filename = doc.get('filename', '')
        text_lower = text.lower()
        
        if 'fema' not in text_lower and 'caloes' not in text_lower and 'caljpia' not in text_lower and 'emergency' not in text_lower:
            continue
        
        lines = text.split('\n')
        for line in lines:
            line = line.strip()
            if len(line) < 10:
                continue
                
            line_lower = line.lower()
            is_disaster = '(fema' in line_lower or '(caloes' in line_lower or '(caljpia' in line_lower
            is_emergency = 'emergency' in line_lower and 'project' in line_lower
            is_warning = 'warning' in line_lower and ('siren' in line_lower or 'sign' in line_lower)
            
            if is_disaster or is_emergency or is_warning:
                status = 'unknown'
                if 'completed' in text_lower:
                    status = 'completed'
                elif 'design' in text_lower or 'planning' in text_lower:
                    status = 'design'
                elif 'not started' in text_lower:
                    status = 'not started'
                
                topic = 'emergency, fema'
                if 'warning' in line_lower:
                    topic = 'emergency warning'
                elif 'fire' in line_lower:
                    topic = 'emergency, fema, fire'
                
                projects.append({
                    'Project_Name': line,
                    'topic': topic,
                    'type': 'disaster',
                    'status': status,
                    'source_file': filename
                })
    
    unique = []
    seen = set()
    for proj in projects:
        if proj['Project_Name'] not in seen:
            unique.append(proj)
            seen.add(proj['Project_Name'])
    
    return unique

result = analyze_documents()
print('__RESULT__')
print(json.dumps(result))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json'}

exec(code, env_args)
