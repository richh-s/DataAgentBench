code = """import json
import re

# Read the civic documents result
with open('var_functions.query_db:2', 'r') as f:
    civic_docs_records = json.load(f)

print('Found ' + str(len(civic_docs_records)) + ' documents')

# Extract projects from the text documents
extracted_projects = []

for doc in civic_docs_records:
    text = doc.get('text', '')
    filename = doc.get('filename', '')
    
    # Check if document contains emergency/FEMA keywords
    lower_text = text.lower()
    is_fema = 'fema' in lower_text
    is_emergency = 'emergency' in lower_text
    
    if is_fema or is_emergency:
        # Regular expression to find project blocks
        project_patterns = re.findall(r'([A-Za-z][^\n]{5,100})\n\s*\(cid:190\) Updates?:', text)
        
        for project_name in project_patterns:
            # Clean up project name
            project_name = project_name.strip()
            
            # Skip if it is a category header
            skip_headers = ['Capital Improvement Projects', 'Disaster Recovery Projects', 'Public Works', 'Agenda Report', 'Public Works Commission']
            skip = False
            for header in skip_headers:
                if header in project_name:
                    skip = True
                    break
            if skip:
                continue
            
            # Determine status based on context
            status = 'not started'
            if 'Updates: Project is currently under construction' in text and project_name in text[:text.find('under construction') + 500]:
                status = 'construction'
            elif '(cid:190) Updates:' in text:
                project_pos = text.find(project_name)
                if project_pos > 0:
                    snippet = text[project_pos:project_pos + 500]
                    if 'design' in snippet.lower():
                        status = 'design'
                    elif 'complete' in snippet.lower() or 'completed' in snippet.lower():
                        status = 'completed'
            
            # Determine topic
            topic = []
            if is_fema:
                topic.append('FEMA')
            if is_emergency:
                topic.append('emergency')
            
            # Determine project type
            project_type = 'disaster' if is_fema or 'disaster' in lower_text else 'capital'
            
            extracted_projects.append({
                'Project_Name': project_name,
                'topic': ', '.join(topic),
                'type': project_type,
                'status': status,
                'filename': filename
            })

print('Extracted ' + str(len(extracted_projects)) + ' emergency/FEMA related projects')

# Convert to JSON string and print
result_json = json.dumps(extracted_projects, ensure_ascii=False)
print('__RESULT__:')
print(result_json)"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json'}

exec(code, env_args)
