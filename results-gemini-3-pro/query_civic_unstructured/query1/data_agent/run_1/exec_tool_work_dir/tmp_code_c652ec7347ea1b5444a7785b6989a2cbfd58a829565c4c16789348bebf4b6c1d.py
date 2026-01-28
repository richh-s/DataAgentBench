code = """import json

# Load funding data
with open(locals()['var_function-call-4958646437851811265'], 'r') as f:
    funding_data = json.load(f)

high_funding_projects = set()
for record in funding_data:
    try:
        if int(record['Amount']) > 50000:
            high_funding_projects.add(record['Project_Name'].strip())
    except ValueError:
        continue

# Load civic docs
with open(locals()['var_function-call-11007850212329188700'], 'r') as f:
    civic_docs = json.load(f)

matched_projects = set()
all_extracted_names = []

for doc in civic_docs:
    text = doc.get('text', '')
    lines = text.split('\n')
    
    start_index = -1
    for i, line in enumerate(lines):
        if "Capital Improvement Projects (Design)" in line:
            start_index = i
            break
            
    if start_index == -1:
        continue
        
    end_index = len(lines)
    for i in range(start_index + 1, len(lines)):
        line = lines[i].strip()
        # Check for next section headers
        if "Capital Improvement Projects" in line and "(Design)" not in line:
            end_index = i
            break
        if "Disaster Recovery Projects" in line:
            end_index = i
            break
            
    section_lines = lines[start_index+1:end_index]
    
    # Extract project names
    for i in range(len(section_lines)):
        line = section_lines[i].strip()
        if not line:
            continue
            
        # Check if this line is a project name
        # We look ahead for the bullet point
        is_project = False
        
        # Look at the next non-empty line
        j = i + 1
        while j < len(section_lines):
            next_l = section_lines[j].strip()
            if next_l:
                if next_l.startswith('(cid:190)'):
                    is_project = True
                break
            j += 1
            
        if is_project:
            proj_name = line
            all_extracted_names.append(proj_name)
            if proj_name in high_funding_projects:
                matched_projects.add(proj_name)

print("__RESULT__:")
print(json.dumps({"count": len(matched_projects), "matched": list(matched_projects), "extracted_sample": all_extracted_names[:5]}))"""

env_args = {'var_function-call-4958646437851811265': 'file_storage/function-call-4958646437851811265.json', 'var_function-call-11007850212329188700': 'file_storage/function-call-11007850212329188700.json'}

exec(code, env_args)
