code = """import json, re, os

# The data should be available in the locals as var_functions.query_db:0
data_key = 'var_functions.query_db:0'

# Try to access the data
civic_docs = None
if os.path.exists(data_key):
    with open(data_key, 'r') as f:
        civic_docs = json.load(f)
else:
    # If it's not a file path, it might be directly in locals
    try:
        civic_docs = locals()[data_key]
    except:
        # For debugging, let's see what's available
        available_vars = [k for k in locals().keys() if 'functions.query_db' in str(k)]
        print('DEBUG: Available variables containing query_db:', available_vars)
        # Let's just load an empty list for now
        civic_docs = []

# Process the documents
all_projects = []

if civic_docs:
    for doc in civic_docs:
        doc_text = doc.get('text', '')
        
        # Check for emergency or FEMA keywords
        if re.search(r'emergency|fema', doc_text, re.IGNORECASE):
            lines = doc_text.splitlines()
            
            for i, line in enumerate(lines):
                line = line.strip()
                if not line:
                    continue
                
                # Identify potential project names
                if line.isupper() and len(line) > 10:
                    is_project = True
                elif '(FEMA' in line:
                    is_project = True
                elif any(x in line for x in ['Project', 'Improvements', 'Repairs', 'Emergency', 'Warning']) and len(line) < 150:
                    is_project = True
                else:
                    is_project = False
                
                if is_project:
                    # Get context
                    start_i = max(0, i-5)
                    end_i = min(len(lines), i+25)
                    context = ' '.join(lines[start_i:end_i])
                    
                    # Extract status
                    status_lower = context.lower()
                    if 'design' in status_lower:
                        status = 'design'
                    elif 'construction' in status_lower and 'completed' not in status_lower:
                        status = 'construction'
                    elif 'complete' in status_lower:
                        status = 'completed'
                    else:
                        status = 'design'
                    
                    # Extract dates
                    dates = re.findall(r'\d{4}-(?:Spring|Summer|Fall|Winter|\d{1,2})', context, re.IGNORECASE)
                    st = dates[0] if dates else ''
                    et = dates[-1] if len(dates) > 1 else ''
                    
                    # Determine topic
                    if 'emergency' in doc_text.lower() and 'fema' in doc_text.lower():
                        topic = 'emergency, FEMA'
                    elif 'fema' in doc_text.lower():
                        topic = 'FEMA'
                    else:
                        topic = 'emergency'
                    
                    project_info = {
                        'Project_Name': line,
                        'topic': topic,
                        'type': 'disaster',
                        'status': status,
                        'st': st,
                        'et': et
                    }
                    
                    all_projects.append(project_info)

# Remove duplicates
unique_projects = {}
for p in all_projects:
    name = p['Project_Name']
    if name not in unique_projects:
        unique_projects[name] = p

final_projects = list(unique_projects.values())

print('__RESULT__:')
print(json.dumps(final_projects))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json'}

exec(code, env_args)
