code = """import json
import re

# Load data
# funding_records
try:
    with open(locals()['var_function-call-6082162408351623791'], 'r') as f:
        funding_records = json.load(f)
except:
    funding_records = locals()['var_function-call-6082162408351623791']

# civic_docs
try:
    with open(locals()['var_function-call-12699093529231824248'], 'r') as f:
        civic_docs = json.load(f)
except:
    civic_docs = locals()['var_function-call-12699093529231824248']

# Helper to get base name safely
def get_base_name(name):
    # Split by '(' and take the first part to remove suffixes like (FEMA Project)
    # This assumes legitimate names don't use parentheses, which seems true for this dataset.
    return name.split('(')[0].strip()

# Valid names set
valid_names = set()
for r in funding_records:
    valid_names.add(r['Project_Name'])
    valid_names.add(get_base_name(r['Project_Name']))

project_status_map = {}
current_status = "Unknown"
current_project = None

full_text_lines = []
for doc in civic_docs:
    lines = doc['text'].splitlines()
    for line in lines:
        line = line.strip()
        if not line: continue
        full_text_lines.append(line)

# Status headers
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
    found_header = False
    lower_line = line.lower()
    for header, status in status_headers.items():
        if header.lower() in lower_line:
            current_status = status
            current_project = None
            found_header = True
            break
    if found_header:
        continue

    # Check project name
    if line in valid_names:
        current_project = line
        if current_project not in project_status_map:
            project_status_map[current_project] = {'status': current_status, 'text': ''}
        continue

    if current_project:
        project_status_map[current_project]['text'] += " " + line

# Refine status "construction"
for proj, data in project_status_map.items():
    txt = data['text'].lower()
    if data['status'] == 'construction':
        if 'completed' in txt and ('notice of completion' in txt or 'construction was completed' in txt):
            data['status'] = 'completed'

# Filter results
final_results = []
keywords = ['emergency', 'fema']

for record in funding_records:
    name = record['Project_Name']
    base = get_base_name(name)
    
    is_relevant = False
    
    # Check name
    for kw in keywords:
        if kw in name.lower():
            is_relevant = True
            break
            
    # Check text
    proj_data = project_status_map.get(name) or project_status_map.get(base)
    
    if proj_data:
        # Check text for keywords
        txt = proj_data['text'].lower()
        for kw in keywords:
            if kw in txt:
                is_relevant = True
                break
    
    if is_relevant:
        status = "Unknown"
        if proj_data:
            status = proj_data['status']
        else:
            # If not in text, leave as Unknown
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
