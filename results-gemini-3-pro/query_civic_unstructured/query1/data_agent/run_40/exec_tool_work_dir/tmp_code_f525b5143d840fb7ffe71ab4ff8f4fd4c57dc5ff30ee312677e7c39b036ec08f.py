code = """import json

# Load DB results
with open(locals()['var_function-call-15734796110705634843'], 'r') as f:
    funding_data = json.load(f)

funded_projects = set()
for row in funding_data:
    if float(row['Amount']) > 50000:
        funded_projects.add(row['Project_Name'].strip())

# Load Docs
with open(locals()['var_function-call-3653011467868570124'], 'r') as f:
    docs = json.load(f)

extracted_design_projects = set()

for doc in docs:
    text = doc['text']
    lines = text.splitlines()
    
    in_design_section = False
    buffer_line = None
    
    for line in lines:
        line = line.strip()
        if not line:
            continue
            
        if "Capital Improvement Projects (Design)" in line:
            in_design_section = True
            buffer_line = None
            continue
        
        if "Capital Improvement Projects (Construction)" in line or \
           "Capital Improvement Projects (Not Started)" in line or \
           "Disaster Recovery Projects" in line:
            in_design_section = False
            buffer_line = None
            continue
            
        if in_design_section:
            # Check for bullet
            if "(cid:190)" in line or "Updates:" in line or "Project Description:" in line:
                if buffer_line:
                    if "Page" not in buffer_line and "Agenda" not in buffer_line and "Subject:" not in buffer_line:
                        extracted_design_projects.add(buffer_line)
                buffer_line = None
            else:
                buffer_line = line

matches = []
unmatched = []
for proj in extracted_design_projects:
    if proj in funded_projects:
        matches.append(proj)
    else:
        unmatched.append(proj)

print("Matches:", len(matches))
print("Match List:", matches)
print("Unmatched List:", unmatched)

print("__RESULT__:")
print(json.dumps(len(matches)))"""

env_args = {'var_function-call-15734796110705634843': 'file_storage/function-call-15734796110705634843.json', 'var_function-call-15734796110705631480': 'file_storage/function-call-15734796110705631480.json', 'var_function-call-3653011467868570124': 'file_storage/function-call-3653011467868570124.json'}

exec(code, env_args)
