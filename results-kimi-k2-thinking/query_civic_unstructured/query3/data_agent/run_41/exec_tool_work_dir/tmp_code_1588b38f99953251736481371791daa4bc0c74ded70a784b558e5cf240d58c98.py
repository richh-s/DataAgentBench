code = """import json, re, os

# Read the MongoDB documents from the stored result
mongo_path = 'var_functions.query_db:0'
if os.path.exists(mongo_path.replace('var_', '')):
    with open(mongo_path.replace('var_', ''), 'r') as f:
        docs = json.load(f)
else:
    # Try accessing via locals
    docs = locals()['var_functions.query_db:0']
    # If it's a file path string
    if isinstance(docs, str) and docs.endswith('.json'):
        with open(docs, 'r') as f:
            docs = json.load(f)

print('Documents:', len(docs))

projects = []
seen = set()

for doc in docs:
    t = doc.get('text', '').lower()
    if not any(x in t for x in ['fema', 'caloes', 'caljpia', 'emergency']):
        continue
    
    for line in doc.get('text', '').split('\n'):
        line = line.strip()
        if len(line) < 10 or line in seen:
            continue
        
        l = line.lower()
        is_disaster = any(p in l for p in ['(fema', '(caloes', '(caljpia'])
        is_warning = 'warning' in l and ('siren' in l or 'sign' in l)
        is_emergency = 'emergency' in l and 'project' in l
        
        if is_disaster or is_warning or is_emergency:
            seen.add(line)
            status = 'unknown'
            full_text = doc.get('text', '').lower()
            if 'completed' in full_text:
                status = 'completed'
            elif 'design' in full_text or 'planning' in full_text:
                status = 'design'
            elif 'not started' in full_text:
                status = 'not started'
            
            topic = 'emergency, fema'
            if is_warning:
                topic = 'emergency warning'
            
            projects.append({
                'Project_Name': line,
                'topic': topic,
                'type': 'disaster',
                'status': status
            })

print('Projects:', len(projects))
print('__RESULT__')
print(json.dumps(projects))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json'}

exec(code, env_args)
