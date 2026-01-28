code = """import json
import re

# Load data
civic_docs_path = locals()['var_function-call-7157939871696024413']
funding_data_path = locals()['var_function-call-17433077485285005998']

with open(civic_docs_path, 'r') as f:
    civic_docs = json.load(f)

with open(funding_data_path, 'r') as f:
    funding_data = json.load(f)

# Combine text
full_text = "\n".join([doc['text'] for doc in civic_docs])
lines = full_text.split('\n')

projects = []
current_project = None
current_block = []

bullet_pattern = re.compile(r'^\(cid:\d+\)')

for i, line in enumerate(lines):
    line = line.strip()
    if not line:
        continue
    
    is_header = False
    if not bullet_pattern.match(line) and "Page" not in line and "Agenda Item" not in line:
        if i + 1 < len(lines):
            next_line = lines[i+1].strip()
            if "(cid:190)" in next_line or "Updates:" in next_line or "Project Description:" in next_line:
                is_header = True
            elif next_line == "":
                 if i + 2 < len(lines):
                     next_next_line = lines[i+2].strip()
                     if "(cid:190)" in next_next_line or "Updates:" in next_next_line or "Project Description:" in next_next_line:
                         is_header = True

    if is_header:
        if current_project:
            projects.append({'name': current_project, 'text': "\n".join(current_block)})
        current_project = line
        current_block = []
    else:
        if current_project:
            current_block.append(line)

if current_project:
    projects.append({'name': current_project, 'text': "\n".join(current_block)})

completed_park_projects_2022 = []

for p in projects:
    name = p['name']
    text = p['text'].lower()
    
    if "park" in name.lower() or "park" in text:
        # Check for 2022 completion
        match = re.search(r'completed.*?([a-zA-Z]+)[\s,]+(202\d)', text)
        found_year = None
        if match and match.group(2) == '2022':
             found_year = '2022'
        
        if not found_year:
            match2 = re.search(r'complete construction:.*?([a-zA-Z]+)[\s,]+(202\d)', text)
            if match2 and match2.group(2) == '2022':
                found_year = '2022'
        
        if found_year == '2022':
            completed_park_projects_2022.append(name)

unique_extracted = list(set(completed_park_projects_2022))
final_total = 0
final_matched = []

for cp in unique_extracted:
    c_name = cp.strip().lower()
    project_fund = 0
    match_found = False
    for fund in funding_data:
        f_name = fund['Project_Name'].strip().lower()
        if f_name == c_name:
            project_fund += int(fund['Amount'])
            match_found = True
    
    if match_found:
        final_total += project_fund
        final_matched.append(cp)

print("__RESULT__:")
print(json.dumps({"total_funding": final_total, "projects": final_matched, "extracted": unique_extracted}))"""

env_args = {'var_function-call-7157939871696024413': 'file_storage/function-call-7157939871696024413.json', 'var_function-call-17433077485285005998': 'file_storage/function-call-17433077485285005998.json'}

exec(code, env_args)
