code = """import json
import re

# Load data
funding_records = []
try:
    with open(locals()['var_function-call-6082162408351623791'], 'r') as f:
        funding_records = json.load(f)
except:
    funding_records = locals()['var_function-call-6082162408351623791']

civic_docs = []
try:
    with open(locals()['var_function-call-12699093529231824248'], 'r') as f:
        civic_docs = json.load(f)
except:
    civic_docs = locals()['var_function-call-12699093529231824248']

def get_base_name(name):
    # Escape backslashes for python string in the tool call
    # Regex to remove suffixes like (FEMA Project), (CalOES Project), etc.
    name = re.sub(r'\\s*\\((FEMA|CalJPIA|CalOES|FEMA/CalOES|CalOES/FEMA).*?\\)', '', name, flags=re.IGNORECASE)
    name = re.sub(r'\\s*\\(FEMA\\)', '', name, flags=re.IGNORECASE)
    return name.strip()

valid_project_names = set()
for r in funding_records:
    valid_project_names.add(r['Project_Name'])
    valid_project_names.add(get_base_name(r['Project_Name']))

project_status_map = {} 
current_status = "Unknown"
current_project = None

full_text_lines = []
for doc in civic_docs:
    lines = doc['text'].split('\\n') # Split by escaped newline char if passed as raw string, or just \n
    # The JSON text might have actual newlines.
    if len(lines) == 1: # Maybe it didn't split correctly
       lines = doc['text'].split('\n')
    for line in lines:
        line = line.strip()
        if not line: continue
        full_text_lines.append(line)

status_headers = {
    "Capital Improvement Projects (Design)": "design",
    "Capital Improvement Projects (Construction)": "construction",
    "Capital Improvement Projects (Not Started)": "not started",
    "Disaster Recovery Projects (Design)": "design",
    "Disaster Recovery Projects (Construction)": "construction",
    "Disaster Recovery Projects (Not Started)": "not started"
}

for line in full_text_lines:
    # Check header
    header_found = False
    for header, status in status_headers.items():
        if header.lower() in line.lower():
            current_status = status
            current_project = None
            header_found = True
            break
    if header_found: continue

    # Check project name
    # We check if the line is exactly a valid project name
    if line in valid_project_names:
        current_project = line
        if current_project not in project_status_map:
             project_status_map[current_project] = {'status': current_status, 'text': ''}
        continue
    
    if current_project:
        project_status_map[current_project]['text'] += " " + line

# Post-process statuses
for proj, data in project_status_map.items():
    txt = data['text'].lower()
    if data['status'] == 'construction':
        if 'completed' in txt and ('notice of completion' in txt or 'construction was completed' in txt):
             data['status'] = 'completed'

final_results = []
keywords = ['emergency', 'fema']

for record in funding_records:
    name = record['Project_Name']
    base = get_base_name(name)
    
    is_relevant = False
    
    # Check keywords in name
    for kw in keywords:
        if kw in name.lower():
            is_relevant = True
            break
    
    # Check keywords in text
    proj_data = project_status_map.get(name) or project_status_map.get(base)
    if proj_data:
        for kw in keywords:
            if kw in proj_data['text'].lower():
                is_relevant = True
                break
    
    if is_relevant:
        status = "Unknown"
        if proj_data:
            status = proj_data['status']
        else:
            # Maybe the name implies status? No.
            # If not in text, assume "not started" or "Unknown".
            # Given the report covers "active" projects, maybe others are inactive?
            # But let's stick to "Unknown" if not found.
            pass
            
        final_results.append({
            "Project_Name": name,
            "Funding_Source": record['Funding_Source'],
            "Amount": record['Amount'],
            "Status": status
        })

print("__RESULT__:")
print(json.dumps(final_results))"""

env_args = {'var_function-call-6082162408351623791': 'file_storage/function-call-6082162408351623791.json', 'var_function-call-6082162408351624496': 'file_storage/function-call-6082162408351624496.json', 'var_function-call-12699093529231824248': 'file_storage/function-call-12699093529231824248.json'}

exec(code, env_args)
