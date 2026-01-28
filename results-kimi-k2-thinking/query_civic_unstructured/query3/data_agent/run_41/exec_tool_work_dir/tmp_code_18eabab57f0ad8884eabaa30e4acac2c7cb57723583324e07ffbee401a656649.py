code = """import json
import re

# Load the MongoDB query result
mongo_result = locals()['var_functions.query_db:0']

# Parse the result
if isinstance(mongo_result, str) and mongo_result.endswith('.json'):
    with open(mongo_result, 'r') as f:
        documents = json.load(f)
else:
    documents = mongo_result

print(f"Number of documents found: {len(documents)}")

# Initialize projects list
projects = []

# Process each document
for doc in documents:
    text = doc.get('text', '')
    filename = doc.get('filename', '')
    lower_text = text.lower()
    
    # Look for disaster project patterns (FEMA, CalOES, CalJPIA)
    if 'fema' in lower_text or 'caloes' in lower_text or 'caljpia' in lower_text or 'emergency' in lower_text:
        # Find project name patterns
        lines = text.split('\n')
        for line in lines:
            line = line.strip()
            if len(line) < 10:
                continue
            
            lower_line = line.lower()
            # Check if this is likely a project name with disaster terms
            if ('(fema' in lower_line or '(caloes' in lower_line or '(caljpia' in lower_line or
                ('emergency' in lower_line and 'project' in lower_line) or
                ('warning' in lower_line and ('siren' in lower_line or 'sign' in lower_line))):
                
                project_name = line
                
                # Determine status
                status = 'unknown'
                if 'completed' in lower_text or 'complete construction' in lower_text or 'notice of completion' in lower_text:
                    status = 'completed'
                elif 'design' in lower_text or 'planning' in lower_text or 'rfp' in lower_text or 'rfq' in lower_text:
                    status = 'design'
                elif 'construction' in lower_text and 'completed' not in lower_text:
                    status = 'design'
                elif 'not started' in lower_text or 'identified' in lower_text:
                    status = 'not started'
                
                # Determine topic
                topic = 'emergency, fema'
                if 'warning' in lower_line:
                    topic = 'emergency warning'
                elif 'fire' in lower_line:
                    topic = 'emergency, fema, fire'
                
                projects.append({
                    'Project_Name': project_name,
                    'topic': topic,
                    'type': 'disaster',
                    'status': status,
                    'source_file': filename
                })

# Remove exact duplicates
unique_projects = []
seen_names = set()
for proj in projects:
    if proj['Project_Name'] not in seen_names:
        unique_projects.append(proj)
        seen_names.add(proj['Project_Name'])

print(f"Found {len(unique_projects)} unique emergency/FEMA projects")

result = json.dumps(unique_projects)
print('__RESULT__')
print(result)"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json'}

exec(code, env_args)
