code = """import json

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
    
    # Locate section using simple find
    start_str = "Capital Improvement Projects (Design)"
    start_idx = text.find(start_str)
    if start_idx == -1:
        continue
    
    start_idx += len(start_str)
    
    # End section
    end_str_1 = "Capital Improvement Projects (Construction)"
    end_str_2 = "Disaster Recovery Projects"
    
    end_idx_1 = text.find(end_str_1, start_idx)
    end_idx_2 = text.find(end_str_2, start_idx)
    
    end_idx = -1
    if end_idx_1 != -1 and end_idx_2 != -1:
        end_idx = min(end_idx_1, end_idx_2)
    elif end_idx_1 != -1:
        end_idx = end_idx_1
    elif end_idx_2 != -1:
        end_idx = end_idx_2
        
    if end_idx != -1:
        section = text[start_idx:end_idx]
    else:
        section = text[start_idx:]
        
    lines = [l.strip() for l in section.split('\n') if l.strip()]
    
    for i in range(len(lines) - 1):
        curr = lines[i]
        nxt = lines[i+1]
        
        # Check markers
        is_bullet = False
        if '(' in nxt and 'cid' in nxt:
            is_bullet = True
        if 'Updates:' in nxt:
            is_bullet = True
            
        # Check noise
        is_noise = False
        if 'Page' in curr and 'of' in curr:
            is_noise = True
        if 'Agenda Item' in curr:
            is_noise = True
        if '(' in curr and 'cid' in curr:
            is_noise = True
            
        if is_bullet and not is_noise:
            capital_design_projects.add(curr)

matched = []
for p in capital_design_projects:
    if p in high_funding_projects:
        matched.append(p)

result = {
    "count": len(matched),
    "matched": matched,
    "extracted_sample": list(capital_design_projects)
}

print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_function-call-2470903467818453572': 'file_storage/function-call-2470903467818453572.json', 'var_function-call-1752816955858049091': 'file_storage/function-call-1752816955858049091.json'}

exec(code, env_args)
