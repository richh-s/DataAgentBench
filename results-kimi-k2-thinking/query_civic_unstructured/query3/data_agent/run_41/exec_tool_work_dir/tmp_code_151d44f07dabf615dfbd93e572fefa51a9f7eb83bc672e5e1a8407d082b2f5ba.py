code = """import json
import re

def extract_projects():
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
        lower_text = text.lower()
        
        if 'fema' in lower_text or 'caloes' in lower_text or 'caljpia' in lower_text or 'emergency' in lower_text:
            lines = text.split('\n')
            for line in lines:
                line = line.strip()
                if len(line) < 10:
                    continue
                    
                lower_line = line.lower()
                has_disaster = ('(fema' in lower_line) or ('(caloes' in lower_line) or ('(caljpia' in lower_line)
                has_emergency = ('emergency' in lower_line and 'project' in lower_line)
                has_warning = ('warning' in lower_line and ('siren' in lower_line or 'sign' in lower_line))
                
                if has_disaster or has_emergency or has_warning:
                    status = 'unknown'
                    if 'completed' in lower_text or 'complete construction' in lower_text:
                        status = 'completed'
                    elif 'design' in lower_text or 'planning' in lower_text or 'rfp' in lower_text:
                        status = 'design'
                    elif 'not started' in lower_text or 'identified' in lower_text:
                        status = 'not started'
                    
                    topic = 'emergency, fema'
                    if 'warning' in lower_line:
                        topic = 'emergency warning'
                    elif 'fire' in lower_line:
                        topic = 'emergency, fema, fire'
                    
                    projects.append({
                        'Project_Name': line,
                        'topic': topic,
                        'type': 'disaster',
                        'status': status,
                        'source_file': filename
                    })
    
    unique_projects = []
    seen_names = set()
    for proj in projects:
        if proj['Project_Name'] not in seen_names:
            unique_projects.append(proj)
            seen_names.add(proj['Project_Name'])
    
    return unique_projects

projects_list = extract_projects()
print('__RESULT__')
print(json.dumps(projects_list))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json'}

exec(code, env_args)
