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
    
    # Start
    start_match = re.search(r'Capital Improvement Projects\s*\(Design\)', text, re.IGNORECASE)
    if not start_match:
        continue
    start_idx = start_match.end()
    
    # End
    end_match = re.search(r'Capital Improvement Projects\s*\((?:Construction|Not Started)\)|Disaster Recovery Projects', text[start_idx:], re.IGNORECASE)
    if end_match:
        end_idx = start_idx + end_match.start()
        section = text[start_idx:end_idx]
    else:
        section = text[start_idx:]
        
    lines = [l.strip() for l in section.split('\n') if l.strip()]
    
    for i in range(len(lines) - 1):
        curr = lines[i]
        nxt = lines[i+1]
        
        # Check if next line is a bullet point or update
        # Bullet usually (cid:...)
        is_bullet = False
        if '(' in nxt and 'cid' in nxt:
            is_bullet = True
        if 'Updates:' in nxt:
            is_bullet = True
            
        # Check if current is not a noise
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

# Debug: check if we found matches. If 0, maybe names don't match exactly.
# Let's also output the extracted names to see.

result = {
    "count": len(matched),
    "matched": matched,
    "extracted_sample": list(capital_design_projects)[:10]
}

print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_function-call-2470903467818453572': 'file_storage/function-call-2470903467818453572.json', 'var_function-call-1752816955858049091': 'file_storage/function-call-1752816955858049091.json'}

exec(code, env_args)
