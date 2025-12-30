code = """import json

# Load funding data
# Variable name for funding data file is var_function-call-3954074569123146275
with open(locals()['var_function-call-3954074569123146275'], 'r') as f:
    funding_list = json.load(f)

# Load civic docs data
# Variable name for civic docs file is var_function-call-8497791855940223179
with open(locals()['var_function-call-8497791855940223179'], 'r') as f:
    civic_docs = json.load(f)

# Filter high funding projects
# Amount is string in the file, convert to int/float
high_funding_projects = set()
for item in funding_list:
    try:
        amt = float(item['Amount'])
        if amt > 50000:
            high_funding_projects.add(item['Project_Name'])
    except ValueError:
        continue

# Identify projects in "Capital Improvement Projects (Design)" section
found_projects = set()

start_marker = "Capital Improvement Projects (Design)"
stop_markers = [
    "Capital Improvement Projects (Construction)",
    "Capital Improvement Projects (Not Started)",
    "Disaster Recovery Projects"
]

for doc in civic_docs:
    text = doc.get('text', "")
    if not text:
        continue
    
    # Locate the design section
    start_idx = text.find(start_marker)
    if start_idx == -1:
        continue
    
    # Text after the header
    content_after = text[start_idx + len(start_marker):]
    
    # Find the nearest stop marker
    end_idx = len(content_after)
    for marker in stop_markers:
        idx = content_after.find(marker)
        if idx != -1 and idx < end_idx:
            end_idx = idx
    
    section_text = content_after[:end_idx]
    
    # Check for project names in this section
    for proj_name in high_funding_projects:
        # Use exact string match (case-sensitive)
        # To avoid partial matches (e.g. "Project A" inside "Project A Phase 2"), 
        # normally we'd want boundary checks, but names are quite specific.
        # However, checking if it is a substring is the standard 'extraction' if no NER.
        if proj_name in section_text:
            found_projects.add(proj_name)

print("__RESULT__:")
print(len(found_projects))"""

env_args = {'var_function-call-3954074569123146275': 'file_storage/function-call-3954074569123146275.json', 'var_function-call-3954074569123143856': 'file_storage/function-call-3954074569123143856.json', 'var_function-call-8497791855940223179': 'file_storage/function-call-8497791855940223179.json'}

exec(code, env_args)
