code = """import json
import re

# Load data
with open(locals()['var_function-call-18417564437237588666'], 'r') as f:
    funding_data = json.load(f)
with open(locals()['var_function-call-2011440110474584919'], 'r') as f:
    civic_docs = json.load(f)

funding_map = {item['Project_Name']: item for item in funding_data}
project_names = set(funding_map.keys())

keywords = ['park', 'road', 'FEMA', 'fire', 'emergency', 'drainage', 'storm drain', 'highway', 'bridge', 'playground', 'water treatment', 'guardrail']

def extract_topics(text):
    found = []
    text_lower = text.lower()
    for kw in keywords:
        if kw.lower() in text_lower:
            found.append(kw)
    return ', '.join(found)

extracted_projects = []

for doc in civic_docs:
    text = doc['text']
    lines = text.split('\n')
    
    current_status = None
    
    current_project_name = None
    current_project_lines = []
    current_project_status = None
    
    for line in lines:
        line = line.strip()
        if not line:
            continue
        
        # Determine section status
        if 'Capital Improvement Projects (Design)' in line:
            current_status = 'design'
        elif 'Capital Improvement Projects (Construction)' in line:
            current_status = 'construction_section'
        elif 'Capital Improvement Projects (Not Started)' in line:
            current_status = 'not started'
            
        # Check for project name
        is_new_project = False
        matched_name = None
        
        if line in project_names:
            is_new_project = True
            matched_name = line
        
        if is_new_project:
            if current_project_name:
                blob = '\n'.join(current_project_lines)
                topics = extract_topics(blob)
                
                p_status = current_project_status
                if p_status == 'construction_section':
                    if 'completed' in blob.lower() and 'construction was completed' in blob.lower():
                        p_status = 'completed'
                    else:
                        p_status = 'design'
                
                extracted_projects.append({
                    'Project_Name': current_project_name,
                    'text': blob,
                    'topics': topics,
                    'status': p_status
                })

            current_project_name = matched_name
            current_project_status = current_status
            current_project_lines = []
        else:
            if current_project_name:
                current_project_lines.append(line)

    if current_project_name:
        blob = '\n'.join(current_project_lines)
        topics = extract_topics(blob)
        p_status = current_project_status
        if p_status == 'construction_section':
            if 'completed' in blob.lower() and 'construction was completed' in blob.lower():
                p_status = 'completed'
            else:
                p_status = 'design'
        
        extracted_projects.append({
            'Project_Name': current_project_name,
            'text': blob,
            'topics': topics,
            'status': p_status
        })

results = []
for p in extracted_projects:
    name = p['Project_Name']
    topics = p['topics']
    
    is_relevant = False
    if 'emergency' in name.lower() or 'fema' in name.lower():
        is_relevant = True
    elif 'emergency' in topics.lower() or 'fema' in topics.lower():
        is_relevant = True
    
    if is_relevant:
        fund = funding_map.get(name, {})
        results.append({
            'Project_Name': name,
            'Funding_Source': fund.get('Funding_Source'),
            'Amount': fund.get('Amount'),
            'Status': p['status']
        })

print('__RESULT__:')
print(json.dumps(results))"""

env_args = {'var_function-call-718083360351244279': ['Funding'], 'var_function-call-18180175954049714507': ['civic_docs'], 'var_function-call-18417564437237588666': 'file_storage/function-call-18417564437237588666.json', 'var_function-call-15750785103731277678': 'file_storage/function-call-15750785103731277678.json', 'var_function-call-2011440110474584919': 'file_storage/function-call-2011440110474584919.json'}

exec(code, env_args)
