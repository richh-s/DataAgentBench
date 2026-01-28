code = """import json
import re

# Open and read the file
with open('var_functions.query_db:2', 'r') as f:
    docs = json.load(f)

print('Documents found: ' + str(len(docs)))

projects = []

for doc in docs:
    text = doc.get('text', '')
    filename = doc.get('filename', '')
    
    # Check for FEMA/emergency keywords (case insensitive)
    if 'fema' in text.lower() or 'emergency' in text.lower():
        # Find project names using the pattern
        matches = re.findall(r'([A-Z][^\n]{10,80})\n\s*\(cid:190\)', text)
        
        for match in matches:
            proj_name = match.strip()
            # Skip section headers
            if 'Project' in proj_name and 'Projects' in proj_name:
                continue
            if 'Agenda' in proj_name:
                continue
            if 'Public Works' in proj_name:
                continue
                
            # Determine status
            status = 'not started'
            if 'under construction' in text.lower():
                status = 'construction'
            elif 'design' in text.lower():
                status = 'design'
            elif 'complete' in text.lower():
                status = 'completed'
            
            # Determine topic
            topics = []
            if 'fema' in text.lower():
                topics.append('FEMA')
            if 'emergency' in text.lower():
                topics.append('emergency')
                
            # Determine type
            proj_type = 'disaster' if 'fema' in text.lower() else 'capital'
            
            projects.append({
                'Project_Name': proj_name,
                'topic': ','.join(topics),
                'type': proj_type,
                'status': status,
                'filename': filename
            })

print('Projects extracted: ' + str(len(projects)))

# Convert to JSON and print
result = json.dumps(projects)
print('__RESULT__:')
print(result)"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json'}

exec(code, env_args)
