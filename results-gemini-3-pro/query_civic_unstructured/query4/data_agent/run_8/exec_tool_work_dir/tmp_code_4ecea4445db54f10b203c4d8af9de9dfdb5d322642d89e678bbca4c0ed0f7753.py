code = """import json
import re

# Load the query result
with open(locals()['var_function-call-18089333164037500904'], 'r') as f:
    docs = json.load(f)

projects = []

for doc in docs:
    text = doc['text']
    lines = text.splitlines()
    
    current_project = None
    
    for i, line in enumerate(lines):
        stripped = line.strip()
        if not stripped:
            continue
            
        # Check if this line is a project name
        # Look ahead for (cid:190) which indicates a section start
        is_project_header = False
        j = i + 1
        while j < len(lines) and not lines[j].strip():
            j += 1
        
        if j < len(lines) and lines[j].strip().startswith('(cid:190)'):
            is_project_header = True
            
        if is_project_header:
            current_project = stripped
            
        if current_project:
            # Check for Start Date patterns in the current line
            # "Begin Construction", "Start Date", etc.
            # Using case-insensitive search
            if "Begin Construction" in line or "Start Date" in line or "Advertise" in line:
                # split by colon
                parts = line.split(':')
                if len(parts) > 1:
                    date_str = parts[-1].strip()
                    # extract the key
                    key = parts[0].strip()
                    # filter noisy characters from key
                    key = re.sub(r'[^\w\s]', '', key)
                    
                    projects.append({
                        'name': current_project,
                        'date_type': key,
                        'date': date_str,
                        'source_file': doc['filename']
                    })

print("__RESULT__:")
print(json.dumps(projects))"""

env_args = {'var_function-call-6715434972998628537': 'file_storage/function-call-6715434972998628537.json', 'var_function-call-18089333164037500904': 'file_storage/function-call-18089333164037500904.json'}

exec(code, env_args)
