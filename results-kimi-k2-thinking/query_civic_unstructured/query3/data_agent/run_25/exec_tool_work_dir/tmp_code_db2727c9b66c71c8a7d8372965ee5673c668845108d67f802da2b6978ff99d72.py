code = """import json, re
import os

# Load the data from the file path
data_file = 'var_functions.query_db:0'
if os.path.exists(data_file):
    with open(data_file, 'r') as f:
        civic_docs = json.load(f)
else:
    # Fallback - assume it's already loaded as a variable
    civic_docs = locals().get('var_functions.query_db:0', [])

# Ensure we have the data
if isinstance(civic_docs, str):
    # It's a file path string, not the actual data
    if os.path.exists(civic_docs):
        with open(civic_docs, 'r') as f:
            civic_docs = json.load(f)
    else:
        civic_docs = []

# Process documents to extract emergency/FEMA projects
all_projects = []

for doc in civic_docs:
    doc_text = doc.get('text', '')
    
    # Check for emergency or FEMA keywords (case insensitive)
    if re.search(r'emergency|fema', doc_text, re.IGNORECASE):
        lines = doc_text.splitlines()
        
        for i, line in enumerate(lines):
            line = line.strip()
            if not line:
                continue
            
            # Identify potential project names based on patterns
            is_project = False
            
            # Pattern 1: All caps line (likely a project title)
            if line.isupper() and len(line) > 10:
                is_project = True
            # Pattern 2: Contains FEMA/CalJPIA/CalOES designation
            elif '(FEMA' in line or '(CalJPIA' in line or '(CalOES' in line:
                is_project = True
            # Pattern 3: Common project-related terms
            elif any(term in line for term in ['Project', 'Improvements', 'Repairs', 'Emergency Warning', 'FEMA']) and len(line) < 150:
                is_project = True
            
            if is_project:
                # Get surrounding context for details
                start_i = max(0, i-5)
                end_i = min(len(lines), i+20)
                context = ' '.join(lines[start_i:end_i])
                
                # Determine status
                status_text = context.lower()
                if 'design' in status_text:
                    status = 'design'
                elif 'construction' in status_text and 'completed' not in status_text:
                    status = 'construction'
                elif 'complete' in status_text:
                    status = 'completed'
                elif 'not started' in status_text:
                    status = 'not started'
                else:
                    status = 'design'
                
                # Extract dates
                dates = re.findall(r'\d{4}-(?:Spring|Summer|Fall|Winter|\d{1,2})', context, re.IGNORECASE)
                st = dates[0] if dates else ''
                et = dates[-1] if len(dates) > 1 else ''
                
                # Determine type
                project_type = 'disaster' if ('(FEMA' in line or '(CalJPIA' in line or '(CalOES' in line) else 'disaster'
                
                # Determine topic
                doc_text_lower = doc_text.lower()
                if 'fema' in doc_text_lower and 'emergency' in doc_text_lower:
                    topic = 'emergency, FEMA'
                elif 'fema' in doc_text_lower:
                    topic = 'FEMA'
                elif 'emergency' in doc_text_lower:
                    topic = 'emergency'
                else:
                    topic = 'emergency'
                
                # Check if warning/siren related
                if 'warning' in line.lower() or 'siren' in line.lower():
                    topic = 'emergency warning'
                
                project_info = {
                    'Project_Name': line,
                    'topic': topic,
                    'type': project_type,
                    'status': status,
                    'st': st,
                    'et': et
                }
                
                all_projects.append(project_info)

# Remove duplicates based on project name
unique_projects = {}
for proj in all_projects:
    name = proj['Project_Name']
    if name not in unique_projects:
        unique_projects[name] = proj

final_projects = list(unique_projects.values())

print('__RESULT__:')
print(json.dumps(final_projects))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json'}

exec(code, env_args)
