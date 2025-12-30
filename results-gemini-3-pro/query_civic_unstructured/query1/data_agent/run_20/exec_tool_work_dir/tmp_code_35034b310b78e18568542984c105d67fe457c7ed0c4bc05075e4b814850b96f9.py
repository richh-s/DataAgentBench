code = """import json

funding_file = locals()['var_function-call-4872762091954436572']
with open(funding_file, 'r') as f:
    funding_data = json.load(f)

high_funding_projects = set()
for item in funding_data:
    try:
        if float(item['Amount']) > 50000:
            high_funding_projects.add(item['Project_Name'].strip())
    except:
        pass

docs_file = locals()['var_function-call-4872762091954434845']
with open(docs_file, 'r') as f:
    civic_docs = json.load(f)

capital_design_projects = set()
target_header = "Capital Improvement Projects (Design)"
next_headers = [
    "Capital Improvement Projects (Construction)",
    "Capital Improvement Projects (Not Started)",
    "Disaster Recovery Projects"
]

for doc in civic_docs:
    text = doc.get('text', '')
    start_idx = text.find(target_header)
    if start_idx == -1:
        continue
    start_idx += len(target_header)
    
    end_idx = len(text)
    for nh in next_headers:
        idx = text.find(nh, start_idx)
        if idx != -1 and idx < end_idx:
            end_idx = idx
            
    section_text = text[start_idx:end_idx]
    lines = [l.strip() for l in section_text.split(chr(10))]
    
    for i in range(len(lines) - 1):
        line = lines[i]
        next_line = lines[i+1]
        
        if not line:
            continue
            
        is_start_of_block = False
        if "(cid:190)" in next_line:
            is_start_of_block = True
        elif "Updates:" in next_line or "Project Description:" in next_line or "Project Schedule:" in next_line or "Estimated Schedule:" in next_line:
            is_start_of_block = True
            
        if is_start_of_block:
            if "Page" in line and "of" in line:
                continue
            if "Agenda Item" in line:
                continue
            
            capital_design_projects.add(line)

result = capital_design_projects.intersection(high_funding_projects)
print("__RESULT__:")
print(json.dumps({"count": len(result), "projects": list(result)}))"""

env_args = {'var_function-call-4872762091954436572': 'file_storage/function-call-4872762091954436572.json', 'var_function-call-4872762091954434845': 'file_storage/function-call-4872762091954434845.json'}

exec(code, env_args)
