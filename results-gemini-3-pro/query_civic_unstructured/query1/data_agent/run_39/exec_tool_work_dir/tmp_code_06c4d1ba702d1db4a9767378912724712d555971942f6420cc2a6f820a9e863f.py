code = """import json

# Load SQL results
with open(locals()['var_function-call-12678318650997066316']) as f:
    funding_data = json.load(f)

# Filter funding > 50,000 and exclude potential noise
noise_terms = {
    "Discussion", "Recommended Action", "Subject", "Item", "Meeting date", "Date prepared", 
    "Approved by", "Prepared by", "To", "From", "Agenda Report", "Public Works Commission",
    "Updates", "Project Schedule", "Estimated Schedule", "Project Description",
    "Capital Improvement Projects", "Disaster Recovery Projects"
}

funded_projects = set()
for item in funding_data:
    try:
        amount = float(item['Amount'])
        name = item['Project_Name'].strip()
        if amount > 50000 and name not in noise_terms:
            funded_projects.add(name)
    except:
        continue

# Load Mongo results
with open(locals()['var_function-call-17761528732148593942']) as f:
    docs = json.load(f)

capital_design_projects = set()

# Markers to identify the section and its end
start_marker = "Capital Improvement Projects (Design)"
# Only stop at the start of the next specific project list sections
end_markers = [
    "Capital Improvement Projects (Construction)",
    "Capital Improvement Projects (Not Started)",
    "Disaster Recovery Projects"
]

for doc in docs:
    text = doc.get('text', '')
    
    start_idx = text.find(start_marker)
    if start_idx == -1:
        continue
        
    content_start = start_idx + len(start_marker)
    sub_text = text[content_start:]
    
    limit_idx = len(sub_text)
    for marker in end_markers:
        idx = sub_text.find(marker)
        if idx != -1 and idx < limit_idx:
            limit_idx = idx
            
    section_text = sub_text[:limit_idx]
    
    # Check for projects in this section
    for proj in funded_projects:
        if proj in section_text:
            capital_design_projects.add(proj)

print("__RESULT__:")
print(len(capital_design_projects))"""

env_args = {'var_function-call-12678318650997066316': 'file_storage/function-call-12678318650997066316.json', 'var_function-call-17761528732148593942': 'file_storage/function-call-17761528732148593942.json', 'var_function-call-1838807570342644039': 1}

exec(code, env_args)
