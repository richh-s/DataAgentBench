code = """import json
import re
from datetime import datetime

# Read the civic documents result
with open('var_functions.query_db:2', 'r') as f:
    civic_docs_records = json.load(f)

print('Found ' + str(len(civic_docs_records)) + ' documents')

# Extract projects from the text documents
extracted_projects = []

for doc in civic_docs_records:
    text = doc.get('text', '')
    filename = doc.get('filename', '')
    
    # Regular expression to find project blocks
    project_patterns = re.findall(r'([A-Za-z][^\n]{5,100})\n\s*\(cid:190\) Updates?:', text)
    
    for project_name in project_patterns:
        # Clean up project name
        project_name = project_name.strip()
        
        # Skip if it's a category header
        if 'Capital Improvement Projects' in project_name or 'Disaster Recovery Projects' in project_name or 'Public Works' in project_name or 'Agenda Report' in project_name:
            continue
        
        # Determine status based on context
        status = 'not started'
        if 'Updates: Project is currently under construction' in text:
            if project_name in text[:text.find('under construction') + 200]:
                status = 'construction'
        elif '(cid:190) Updates:' in text:
            # Find the position of this project
            project_pos = text.find(project_name)
            if project_pos > 0:
                # Look for status indicators after the project name
                snippet = text[project_pos:project_pos + 500]
                if 'design' in snippet.lower():
                    status = 'design'
                elif 'complete' in snippet.lower() or 'completed' in snippet.lower():
                    status = 'completed'
        
        # Determine if it's FEMA/emergency related
        lower_text = text.lower()
        is_fema = 'fema' in lower_text or 'FEMA' in text
        is_emergency = 'emergency' in lower_text
        
        if is_fema or is_emergency:
            topic = []
            if is_fema:
                topic.append('FEMA')
            if is_emergency:
                topic.append('emergency')
            
            # Determine project type
            project_type = 'disaster' if 'fema' in lower_text or 'disaster' in lower_text else 'capital'
            
            extracted_projects.append({
                'Project_Name': project_name,
                'topic': ', '.join(topic),
                'type': project_type,
                'status': status,
                'filename': filename
            })

print('Extracted ' + str(len(extracted_projects)) + ' emergency/FEMA related projects')

# Print first few for debugging
for i, proj in enumerate(extracted_projects[:5]):
    print('Project ' + str(i) + ': ' + proj['Project_Name'] + ', Type: ' + proj['type'] + ', Status: ' + proj['status'])

# Output results
result_str = json.dumps(extracted_projects)
print('__RESULT__:')
print(result_str)"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json'}

exec(code, env_args)
