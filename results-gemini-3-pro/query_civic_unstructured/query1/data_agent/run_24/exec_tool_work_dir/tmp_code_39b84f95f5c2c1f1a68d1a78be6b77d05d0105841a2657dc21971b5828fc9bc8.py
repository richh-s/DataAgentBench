code = """import json
import re

with open(locals()['var_function-call-2470903467818453572'], 'r') as f:
    funding_data = json.load(f)

high_funding_projects = set()
for item in funding_data:
    high_funding_projects.add(item['Project_Name'].strip())

with open(locals()['var_function-call-1752816955858049091'], 'r') as f:
    civic_docs = json.load(f)

capital_design_projects = set()

for doc in civic_docs:
    text = doc['text']
    
    start_match = re.search(r'Capital Improvement Projects\s*\(Design\)', text, re.IGNORECASE)
    if not start_match:
        continue
    
    start_index = start_match.end()
    
    end_match = re.search(r'Capital Improvement Projects\s*\((?:Construction|Not Started)\)|Disaster Recovery Projects', text[start_index:], re.IGNORECASE)
    
    if end_match:
        end_index = start_index + end_match.start()
        section_text = text[start_index:end_index]
    else:
        section_text = text[start_index:]
        
    lines = [line.strip() for line in section_text.split('\n') if line.strip()]
    
    for i in range(len(lines) - 1):
        current_line = lines[i]
        next_line = lines[i+1]
        
        # Check markers
        is_detail_start = False
        if next_line.startswith('(cid:'):
            is_detail_start = True
        if 'Updates:' in next_line:
            is_detail_start = True
        if 'Project Description:' in next_line:
            is_detail_start = True
        if 'Project Schedule:' in next_line:
            is_detail_start = True
            
        is_noise = False
        if current_line.startswith('Page '):
            is_noise = True
        if current_line.startswith('Agenda Item'):
            is_noise = True
        if current_line.startswith('(cid:'):
            is_noise = True
                   
        if is_detail_start and not is_noise:
            capital_design_projects.add(current_line.strip())

matched_projects = []
for p in capital_design_projects:
    if p in high_funding_projects:
        matched_projects.append(p)

result = {
    "extracted": list(capital_design_projects),
    "matched": matched_projects,
    "count": len(matched_projects)
}

print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_function-call-2470903467818453572': 'file_storage/function-call-2470903467818453572.json', 'var_function-call-1752816955858049091': 'file_storage/function-call-1752816955858049091.json'}

exec(code, env_args)
