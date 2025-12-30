code = """import json

funding_path = locals()['var_function-call-7838865705427955035']
civic_path = locals()['var_function-call-5237099237942450066']

with open(funding_path, 'r') as f:
    funding_data = json.load(f)

with open(civic_path, 'r') as f:
    civic_data = json.load(f)

funding_projects = set()
for row in funding_data:
    try:
        if float(row['Amount']) > 50000:
            funding_projects.add(row['Project_Name'].strip())
    except:
        pass

extracted_projects = set()

for doc in civic_data:
    text = doc.get('text', '')
    lines = text.splitlines()
    
    in_design = False
    buffer_line = None
    
    for line in lines:
        line = line.strip()
        if not line:
            continue
            
        if "Capital Improvement Projects (Design)" in line:
            in_design = True
            buffer_line = None
            continue
            
        if "Capital Improvement Projects (Construction)" in line:
            in_design = False
            continue
        if "Capital Improvement Projects (Not Started)" in line:
            in_design = False
            continue
        if "Disaster Recovery Projects" in line:
            in_design = False
            continue
            
        if in_design:
            if "(cid:190)" in line or "Updates:" in line or "Project Description:" in line:
                if buffer_line:
                    extracted_projects.add(buffer_line)
                    buffer_line = None
            else:
                if line.startswith("(cid:131)") or line.startswith("Page") or "Agenda Item" in line:
                    continue
                if line.startswith("Date prepared:") or line.startswith("Meeting date:"):
                    continue
                buffer_line = line

intersection = extracted_projects.intersection(funding_projects)

print("__RESULT__:")
print(json.dumps({
    "matches": len(intersection),
    "projects": list(intersection)
}))"""

env_args = {'var_function-call-13459136201759015403': ['Funding'], 'var_function-call-13459136201759017542': ['civic_docs'], 'var_function-call-7838865705427955035': 'file_storage/function-call-7838865705427955035.json', 'var_function-call-7838865705427954030': 'file_storage/function-call-7838865705427954030.json', 'var_function-call-5237099237942450066': 'file_storage/function-call-5237099237942450066.json'}

exec(code, env_args)
